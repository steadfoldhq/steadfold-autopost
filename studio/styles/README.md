# Style menu (Oct 16, 2026)

One Locked Hour script in 8 visual languages, each cut to a new impact track. The "Try this" turn lands on the track's measured drop (tools/music-library.json).

| # | File | Look | Track |
|---|---|---|---|
| 1 | style1_storybook.py | Storybook pages, painted plates in parallax, 3D page turns | lh-x-phone-down |
| 2 | style2_footage_doodles.py | Bright footage + hand-drawn doodles tracked to the action | lh-x-lock-in |
| 3 | style3_paper_cutout.py | Torn-paper stop-motion on twos, paper rip on the drop | hb-x-ta-da-funk |
| 4 | style4_liquid_type.py | Gooey colour blobs behind poster-scale kinetic type | lh-x-tick-boom |
| 5 | style5_phone_ui.py | Phone UI, notifications pile up then explode | hb-x-smart-bounce |
| 6 | style6_desk_drop.py | 3D-ish desk, props drop on the beat with bounce and shadow | ff-x-big-reveal |
| 7 | style7_scrapbook.py | Scrapbook: footage polaroids, tape, die-cut stickers, travelling camera | lf-x-sunny-bounce |
| 8 | style8_character.py | Original character "Lockie" acts it out | lf-x-tiny-parade |

```bash
cd studio/styles
export STYLE_OUT=/path/to/out          # MP4s + QA sheets land here (frames are deleted after each encode)
python3 preview.py style5_phone_ui 0,3.9,5.8,9.6   # a few frames tiled, before a full render
python3 style5_phone_ui.py                          # full render -> $STYLE_OUT/Style-5-phone-ui.mp4
python3 style5_phone_ui.py remix                    # new sound only, same picture
python3 sampler.py $STYLE_OUT/Music-Sampler.mp4     # 12 tracks x 5 s around each drop
python3 contact.py $STYLE_OUT/contact.jpg           # 2 x 4 sheet (hook + fix per style)
```

- **common.py**: beat-grid timeline, voice placement, audio mix (ducking, SFX, top-end taming, −14 LUFS master), render through studio/motion/kit.py, QA, and the point tracker. Block lengths are the reading minimum (0.4 s/word + 0.6 s) rounded up to half beats. The voice is the one Laura take in media/voice/stylemenu (it is not regenerated).
- **Footage** comes from assets/inbox: sm-scroll-3851938, px-5991819, px-5935128, px-20736942 and px-7592151 (Pexels). The crops are cached in $STYLE_OUT/_cache/s2_*.
- **Styles 1 and 8 are fallback builds.** Canva image generation was out of credits on Oct 16, so style 1 paints footage frames (tools/paint.py) and style 8 draws Lockie as shaded SVG. Swap in generated plates or frames when credits return.
