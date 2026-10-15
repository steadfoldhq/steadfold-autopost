# Steadfold studio: the full engine, packed in this repo

`steadfold-studio.tgz` (about 34 MB) holds the whole current engine. It lives here because the Learning Lab project is full. The standard it serves is `docs/brand-system-v4.md`, and the approved look is `docs/grids-FINAL.png`.

**Inside** (paths are relative to `/home/claude`, because every script uses absolute paths there):
- **`content/design/`**:
  - `render.py`, `engine/` (templates, themes, covers, feed, episode, interactive) and `post.schema.json`;
  - `selftest.py`, `grid_preview.py`, fixtures and marks;
  - `assets/cutouts/` (clean glove mattes);
  - every sample build script with its input prep files (`samples-v3`, `samples-v4`, `samples-v5`: `build_final.py`, `build_mix.py`, `matte.py`, `recolor.py` and the others);
  - the interactive and episode demo builds (`demos-interactive/`, `demos-episode/`).
- **`content/video/src/`**: the Reel engines `slowpan.py` + `slowpan_bg.py`, `vlab.py`, `music2.py`, `covers_v3.py` and `lf_silhouette_letters.py`, plus `REEL-BRIEF.md`.
- **`content/oct16-21/`**: the Oct 16–21 build.
  - `reels_lib.py`: 2× text layers, 2× kinetic renderer and dedicated covers with safe-zone QA.
  - `reels.py`, `build_feed.py`, `ff_math.py` and `items.py`.
  - `style_selftest.py`.
  - `make_bundle.py`, which rebuilds this file.
- **`content/week03-global/fullyfunded/`**: the reference global build.
- **`steadfold-library/current/guides/`**: CONTENT-STANDARD-v3, PAYOFF-FIRST, COPY-STANDARD and `copy-lint.py`.

**Left out:**
- `build/` folders and rendered outputs (slides, sheets, MP4s), which the scripts regenerate;
- the photo library and the Caveat, Fraunces, Instrument and other OFL fonts, which are already in this repo under `assets/inbox/` and `assets/fonts/`.

## Setup (about 2 minutes)
```bash
# 0. Clone this repo to /home/claude/steadfold-autopost first (add_repo steadfoldhq/steadfold-autopost, then git clone).
cd /home/claude
tar -xzf steadfold-autopost/studio/steadfold-studio.tgz -C /home/claude

# 1. Fonts. Inter, Inter Display, Lora and Poppins are in the bundle; add the OFL fonts from the repo.
cp -n steadfold-autopost/assets/fonts/* content/design/assets/fonts/
cp -n steadfold-autopost/assets/inbox/InstrumentSerif-* content/design/assets/fonts/

# 2. Photo library (Canva AI photos, full resolution) into the paths the scripts read
mkdir -p content/design/samples-v3/assets content/design/samples-v4/assets
cp -n steadfold-autopost/assets/inbox/*.png steadfold-autopost/assets/inbox/*.jpg content/design/samples-v3/assets/
cp -n steadfold-autopost/assets/inbox/g-glove*.png content/design/samples-v4/assets/

# 3. Chromium for Playwright is preinstalled at /opt/pw-browsers/chromium. Never run "playwright install".
export PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1
#    render.py/selftest.py drive Chromium from Node: the Node playwright package must be in `npm root -g`
#    (preinstalled at /home/claude/.npm-global/lib/node_modules/playwright, v1.56.0). On a fresh machine:
npm ls -g playwright >/dev/null 2>&1 || npm i -g playwright@1.56.0
python3 -c "import playwright, cv2, numpy, PIL, scipy, jsonschema" || pip install playwright opencv-python-headless numpy pillow scipy jsonschema

# 4. Self-tests
python3 content/design/selftest.py                # QA gate catches its known failures
python3 content/oct16-21/style_selftest.py        # one sample of EVERY style -> content/oct16-21/build/style-selftest/contact-sheet.png
```
If a script asks for a font file by an exact name (for example `Inter-Bold.ttf`) and that name is missing, copy or rename the closest weight to that name.

`style_selftest.py` renders one sample of each style, all at 2× and then Lanczos:
- **Feed tiles:** Look B cover, put-a-finger-down glove, soft countdown, Ep.01 B/W photo, one-word photo, "Instead of… Say…" reframe, emoji meme, sticky-note list and awards.
- **render.py templates:** original template, panorama, follow-the-line, awards, swipe-to-reveal and episode.
- **Video:** slow-pan photo, calm text, kinetic, and a dedicated Reel cover.

It exits with code 1 if anything fails.

## Proof of a clean extract (Oct 15, 2026): PASS
**What was tested:**
- The bundle was extracted into an empty temporary directory, together with a copy of this repo's `assets/` and `studio/` only.
- Steps 1–2 were run there.
- In a private mount namespace (`unshare -m`), the extracted `content/`, `steadfold-library/` and repo copy were bind-mounted over the live ones. The live engine tree and outputs were invisible, so only the bundle and the repo assets could be used.
- Machine tooling stayed visible: Chromium in `/opt` and Node playwright in `~/.npm-global`.

**Results:**
- `selftest.py`: every expected QA failure was caught.
- `style_selftest.py`: **3/3 style groups, 21 samples, 0 failures.** The sheet is `studio/clean-extract-selftest.jpg`.

**Limit:** a fully empty `/home/claude` was also tried. Everything except the Node renderer ran. `npm i -g playwright` could not reach the npm registry from this sandbox, so step 3's npm line is the one dependency the bundle doesn't carry.

## Rebuild the bundle after engine changes
```bash
python3 /home/claude/content/oct16-21/make_bundle.py   # writes studio/steadfold-studio.tgz; keep it under 40 MB
```

## Not included on purpose
- **samples-v4 glam and derived glove photos** (`glove1-5.png`, `d-glove1-2.png`): retired after v4. Use `assets/cutouts/glove-pink-*.png` with `build_final.tint_glove()`.
- **The folded-letter look** (`build_original.py fold_layer`): retired in brand-system v4. The script is kept only for reference.
