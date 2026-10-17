"""Turn a footage frame into a painted storybook plate + a cut-out subject layer for parallax.

paint(src_jpg, out_dir, name, rect) -> out_dir/name-bg.png (subject removed, inpainted, painted),
                                       out_dir/name-fg.png (painted subject with soft alpha), name-full.png
rect = (x, y, w, h) around the subject, in the source frame's pixels (GrabCut seed).
"""
import sys
import cv2
import numpy as np


def painterly(img):
    x = cv2.bilateralFilter(img, 7, 50, 50)
    x = cv2.edgePreservingFilter(x, flags=1, sigma_s=60, sigma_r=0.45)
    x = cv2.stylization(x, sigma_s=60, sigma_r=0.5)
    # flatten toward gouache: soft colour quantisation (k-means on a small copy, then map)
    sm = cv2.resize(x, None, fx=0.25, fy=0.25).reshape(-1, 3).astype(np.float32)
    _, lab, cent = cv2.kmeans(sm, 14, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0), 2, cv2.KMEANS_PP_CENTERS)
    d = ((x.reshape(-1, 1, 3).astype(np.float32) - cent[None]) ** 2).sum(2)
    q = cent[d.argmin(1)].reshape(x.shape)
    x = (0.35 * q + 0.65 * x.astype(np.float32)).astype(np.uint8)
    # warm storybook grade
    f = x.astype(np.float32) / 255
    f = np.clip(0.12 + 0.9 * f, 0, 1)
    f[..., 2] = np.clip(f[..., 2] * 1.06 + 0.02, 0, 1)
    f[..., 0] = np.clip(f[..., 0] * 0.93, 0, 1)
    hsv = cv2.cvtColor((f * 255).astype(np.uint8), cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[..., 1] = np.clip(hsv[..., 1] * 1.32, 0, 255)
    x = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
    # ink only on strong edges
    g = cv2.cvtColor(cv2.GaussianBlur(img, (0, 0), 3.0), cv2.COLOR_BGR2GRAY)
    e = cv2.Canny(g, 22, 60)
    e = cv2.dilate(e, np.ones((3, 3), np.uint8))
    e = cv2.GaussianBlur(e, (0, 0), 1.1).astype(np.float32) / 255
    ink = np.array([55, 38, 42], np.float32)
    out = x.astype(np.float32) * (1 - 0.7 * e[..., None]) + ink * 0.7 * e[..., None]
    return np.clip(out, 0, 255).astype(np.uint8)


def paint(src, out_dir, name, rect):
    img = cv2.imread(src)
    mask = np.zeros(img.shape[:2], np.uint8)
    bgd, fgd = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
    cv2.grabCut(img, mask, tuple(rect), bgd, fgd, 6, cv2.GC_INIT_WITH_RECT)
    m = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    # keep the biggest blob
    n, lab, stats, _ = cv2.connectedComponentsWithStats(m)
    if n > 1:
        k = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
        m = np.where(lab == k, 255, 0).astype(np.uint8)
    painted = painterly(img)
    hole = cv2.dilate(m, np.ones((31, 31), np.uint8))
    small = cv2.resize(img, None, fx=0.5, fy=0.5)
    bg = cv2.inpaint(small, cv2.resize(hole, None, fx=0.5, fy=0.5), 9, cv2.INPAINT_TELEA)
    bg = cv2.resize(bg, (img.shape[1], img.shape[0]))
    bg = painterly(cv2.GaussianBlur(bg, (0, 0), 3))
    alpha = cv2.GaussianBlur(m, (0, 0), 3)
    fg = np.dstack([painted, alpha])
    cv2.imwrite(f"{out_dir}/{name}-bg.png", bg)
    cv2.imwrite(f"{out_dir}/{name}-fg.png", fg)
    cv2.imwrite(f"{out_dir}/{name}-full.jpg", painted, [cv2.IMWRITE_JPEG_QUALITY, 92])
    cv2.imwrite(f"{out_dir}/{name}-mask.png", m)


if __name__ == "__main__":
    paint(sys.argv[1], sys.argv[2], sys.argv[3], [int(v) for v in sys.argv[4].split(",")])
