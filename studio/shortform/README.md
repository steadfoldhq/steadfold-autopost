# Short-form studio engine (TikTok / YouTube Shorts)

9:16 voiced videos with TikTok-style word-by-word captions. No music baked in: a licensed sound is added in-app.

1. Write the scripts into tools/tts-spec-*.json (voice ids from media/voice/shortform/_voices.json).
2. Run the **Eleven TTS** workflow (.github/workflows/tts.yml) with that spec. It writes `<name>.mp3` plus `<name>.json` (character timings) into media/voice/shortform/.
3. `python3 studio/shortform/<pilot>.py` renders to /home/claude/shortform/out. Edit `V`/`OUT` in common.py if needed.
   - Long silences are trimmed to 0.42 s. `pauses={word_index: seconds}` inserts a beat.
   - Audio is loudness-normalized to -15 LUFS.
4. `python3 studio/shortform/sheet.py <module> 0,4,8` writes a preview contact sheet.

Pilots of Oct 16 2026: FF-S1 Guess the Gap, FF-S2 POV First Year Freelancing, LH-S1 Brain vs Me, LH-S2 Fake Productivity Tier List, HB-S1 Typed vs Sent, HB-S2 214 Unread. The MP4s are not in this public repo. They are sent to Dharma for approval.
