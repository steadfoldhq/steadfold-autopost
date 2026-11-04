"""Manifest entries for Day 14 (C) and Reel B, Nov 4 2026 (loaded by nov04_hourback_manifest.py; not run on its own)."""
import re


def entries(h):
    dur, reply, run_at, PICKER, FOLLOW = h["dur"], h["reply"], h["run_at"], h["PICKER"], h["FOLLOW"]
    out = []

    # -------------------------------------------------------------- C: AI, for real · Day 14 (Mon Nov 9, 17:45)
    pc, rc = reply("missed")
    TEXT = rc.strip().split("\n\n")[0].strip()
    assert TEXT.startswith("Hey Jordan") and len(TEXT.split()) == 48
    out.append(dict(
        id="hb-day14-missed-30th", account="hourback", publish_at="2026-11-09T17:45:00-05:00",
        images=["studio-nov04/hourback/hb-day14-missed-30th/01.jpg", "studio-nov04/hourback/hb-day14-missed-30th/02.jpg"],
        caption=("Slept through a friend's 30th and don't know what to text? Tell AI what happened and what you'll do, and ask "
                 "for a short apology that owns it.\n\n"
                 "AI, for real · Day 14. One real test of what AI can do, with the output shown.\n\n"
                 "WHY IT WORKS: when you feel bad, the text gets long: three excuses and no plan. Telling AI to own it, skip "
                 "the long excuses and offer one clear next step keeps the apology short and about them. Notice it ended on a "
                 "question your friend can answer: \"What night works for you?\"\n\n"
                 f"THE REAL TEST (names made up for this post), Claude (Anthropic), Nov 4, 2026:\nPrompt: \"{pc.strip()}\"\n"
                 "Slide 2 shows what we told it and its text, word for word.\n\n"
                 "THE CATCH: AI is bad at counting its own words. Under the text it wrote \"(55 words)\". The text is 48 words. "
                 "Harmless here, but don't trust a number AI gives about its own answer. And only send it if it sounds like "
                 "you: change \"my treat\" or any line you wouldn't say out loud.\n\n"
                 "PRIVACY TIP: a first name is enough. You don't need to paste your chats with your friend, their number, or "
                 "more about your health than you want to share.\n\n"
                 "Do this: in ChatGPT, Claude or Gemini, say what happened and what you'll do next. Then ask: \"Write a short "
                 "apology text. Own it, no long excuses. Under 60 words.\"\n\n"
                 "Send this to whoever still owes someone a sorry text.\n\n"
                 f"{FOLLOW}\n\n#ai #learnai #claude #friendship #apology\n\n"
                 "AI, for real · Day 15 lands Wed Nov 11 at 5:45 pm."),
        first_comment=(f"Made-up friendship, real output: run in Claude (Anthropic), model claude-opus-5-5, in a fresh, isolated "
                       f"session (Claude Code CLI print mode in an empty folder, no tools, no earlier chat, no Project or settings "
                       f"context loaded), {run_at('missed')[:10]} {run_at('missed')[11:16]} UTC. Jordan and the dinner are made up "
                       "for this post. Slide 2 shows Claude's text word for word; its after-note '(55 words)' is left off the slide "
                       "and discussed in the caption (we counted 48). Full prompt and reply in our public repo steadfold-autopost: "
                       "studio/editorial/hb-nov04-run-missed.txt. Results vary between apps and runs. Fact check (Nov 4 2026): the "
                       "only claims in this post are the run itself and its word count, checked against the saved transcript."),
        alt_text=("Hourback 2-slide carousel. Slide 1: 'AI, for real · Day 14' badge, 'Slept through their 30th. Now what?' in a "
                  "large serif with a periwinkle highlight, a drawn phone showing an orange '30' balloon with a 'zzz' beside it, "
                  "and the handwritten note 'new one every Mon · Wed · Fri'. Slide 2: 'Tell AI what happened and what you'll do. "
                  "It wrote this text:' above a white card headed 'Text to Jordan' with one purple message bubble: '"
                  + TEXT + "' Below it, a yellow note: 'what we told it (made up for this post): missed Jordan's 30th birthday dinner on Saturday · had a migraine, fell asleep · didn't text until Sunday morning'. Handwritten: 'Claude's real text, word for word · names and story made up for this post'."),
        beats=["[slide 1] AI, FOR REAL · DAY 14 | Slept through their 30th. Now what? | (phone) 30 · z z z | new one every Mon · Wed · Fri | (stamp) HOURBACK · YOUR EVENINGS BACK",
               f"[slide 2] 2/2 | Tell AI what happened and what you'll do. | It wrote this text: | TEXT TO | Jordan | {TEXT} | (yellow note) what we told it (made up for this post): · missed Jordan's 30th birthday dinner on Saturday · had a migraine, fell asleep · didn't text until Sunday morning | Claude's real text, word for word · names and story made up for this post"],
        hook_options=["Slept through their 30th. Now what?", "Missed their 30th. What do you text?", "Missed a friend's 30th? Say sorry tonight."],
        hook_picker=PICKER + "Verdict C: #3 'Slept through their 30th. Now what?' (specific, relatable guilt, clear; #1 generic, #2 reads like an ad giving orders). Adopted (listed first).",
        style=("Series layout 'AI, for real', SAME as Day 13 (Look B big-headline pills cover, kicker badge, one drawn object "
               "bottom-left, 'new one every Mon · Wed · Fri', stamp; slide 2 = the indigo white-card slide with the real output). "
               "Loud cover; series number and '30th' on the cover."),
        send_test=False,
        sources=[f"studio/editorial/hb-nov04-run-missed.txt (fresh, isolated verbatim Claude run via claude -p, {run_at('missed')})"],
        notes=("Fulfils Day 13's caption promise ('Day 14 lands Mon Nov 9 at 5:45 pm'); caption's last line promises Day 15 on "
               "Wed Nov 11 at 5:45 pm: the next studio run must build it. Builder: studio/editorial/nov04_hourback_feed.py (copy of "
               "nov03_hourback_feed.py; run: nov04_hourback_run.py missed). Topic check: no apology/missed-event piece in 14 days "
               "(the Oct 28 'kind-firm no' was a refusal, not an apology). Transcript scanned: no real personal name or employer. "
               "The run's own '(55 words)' is wrong (48 words, counted in code with an assert): used as the CATCH, not hidden. "
               "Self-review (QG-1): both slides checked at full size against Day 13 side by side; save line moved up to sit under "
               "the card. Not yet seen by an independent reviewer (QG-5). CD GATE FIXES (Nov 4): slide-2 save line now 'names and story made up "
               "for this post'; a yellow 'what we told it (made up for this post)' note under the text card shows the migraine came "
               "from our prompt, not from the AI."),
    ))

    # -------------------------------------------------------------- B: 31 years, a 2-minute retirement speech (Mon Nov 9, 19:00)
    pb, rb = reply("retire")
    body = rb.split("\n---\n")[0]
    P = [p.strip() for p in body.split("\n\n") if p.strip()][1:]
    opening = " ".join(P[0:3])
    reg_q = P[3].split(" Your favorite authors.")[0]
    joke = P[4]
    story_q = P[5].split(" Some of those kids")[0]
    jar_q = P[6].split(" It was a small thing.")[0]
    toast = P[-1]
    open3 = P[2].split(" And she always knew")[0] + " …"
    words = len(body.replace("**Speech for Linda**", "").split())
    assert words == 236, words
    out.append(dict(
        id="hb-reel-1109-retirement-speech", account="hourback", publish_at="2026-11-09T19:00:00-05:00",
        video="studio-nov04/hourback/hb-reel-1109-retirement-speech.mp4",
        cover="studio-nov04/hourback/hb-reel-1109-retirement-speech-cover.jpg",
        caption=("31 years at the same desk, and you get 2 minutes to say goodbye? Give AI 3 true things about the person and ask "
                 "for a 2-minute speech you can read out loud.\n\n"
                 "WHY IT WORKS: a speech lands on small true details, not big words. AI can only use what you give it, so 3 "
                 "real things (a habit, a job they did for years, a small kindness) become the stories in the speech. Asking "
                 "for short sentences makes it easy to read out loud.\n\n"
                 f"THE REAL TEST: we made up a coworker and asked Claude (Anthropic) on Nov 4, 2026: \"{pb.strip()}\"\n"
                 f"It turned the candy jar into this, word for word: \"{jar_q}\"\n"
                 f"And it ended: \"{toast}\"\n\n"
                 "HOW (10 minutes):\n1. Open ChatGPT, Claude or Gemini.\n2. Say who it's for, how long they've been there, and "
                 "3 true things about them.\n3. Ask for a 2-minute speech (about 250 words) in short sentences, with one light "
                 "joke and a line everyone can raise a glass to.\n4. Read it out loud once with a timer and cut anything that "
                 "isn't true.\n\n"
                 "THE CATCH: AI fills gaps with things that sound true. It wrote that Linda knew regulars' \"kids' names\" and "
                 "that kids from story time \"now bring their own kids\". We never said either. Cut or fix every line like that "
                 "before you stand up.\n\n"
                 "PRIVACY TIP: a first name and the 3 stories are enough. Leave out last names, health news and anything "
                 "they told you in confidence.\n\n"
                 "Names and the library made up for this post.\n\n"
                 "Do this: Tell AI 3 stories. Ask for 2 minutes.\n\n"
                 "Send this to whoever's giving the speech at the next send-off.\n\n"
                 f"{FOLLOW}\n\n#ai #learnai #claude #retirement #speechwriting"),
        first_comment=(f"How we made this: one real run in Claude (Anthropic), model claude-opus-5-5, in a fresh, isolated session "
                       f"(Claude Code CLI print mode in an empty folder, no tools, no earlier chat, no Project or settings context "
                       f"loaded), {run_at('retire')[:10]} {run_at('retire')[11:16]} UTC. Linda, the library and the 3 facts are made "
                       "up for this post. On screen: the opening (shortened: its line 'And she always knew whose face it was.' is cut, marked …), the regulars and story-time passages (shortened, "
                       "marked …), the joke and the closing toast (word for word), the candy-jar passage (shortened, marked …). The "
                       f"speech is {words} words (counted in code); Claude's own note said 'About 240 words, roughly two minutes at a "
                       "relaxed pace'. Full prompt and reply in our public repo steadfold-autopost: "
                       "studio/editorial/hb-nov04-run-retire.txt. Results vary between apps and runs. Fact check (Nov 4 2026): the "
                       "only claims are the run itself, checked against the saved transcript; no outside statistic or feature claim."),
        alt_text=("Illustrated Hourback Reel in periwinkle and cream: a send-off table with a microphone on a stand, a stopwatch "
                  "counting down from 2:00, and a jar of lemon candies labelled 'rough-day candies'. Words: '31 years. You get 2 "
                  f"minutes.' A speech page headed 'Speech for Linda, shortened' already shows its opening: '{P[0]} {P[1]} {open3}' Then "
                  "'try this. Tell AI 3 true stories. It writes the speech. Claude's real speech, shortened:' A yellow note, 'what "
                  "we told it (made up for this post): Linda: 31 years at the library front desk, knew every regular's name, 20 "
                  "years of Saturday story time, lemon candies for anyone's rough day', flies into the page. Passages land one by "
                  f"one: '{reg_q} …', then the joke, highlighted: '{joke}', then '{story_q} …'. Then 'it turns facts into moments. "
                  f"A jar of candies becomes the best line.' with 'And then there's the jar.' and, highlighted, "
                  f"'{jar_q.split('jar. ', 1)[1]} …' while the jar glows. Then 'Do "
                  f"this: Tell AI 3 stories. Ask for 2 minutes. In ChatGPT, Claude or Gemini. Read it out loud once.' with its last "
                  f"line: '{toast}' and a tick. Ends: 'Follow to learn one real AI trick a day.' Names made up for this post."),
        beats=[
            f"[0.0 s] 31 years. You get 2 minutes. | (chip, top) Real Claude reply · Linda and the library made up for this post | (stopwatch) 2:00 counting down | (jar) rough-day candies | (page header) Speech for Linda, shortened | (page) {P[0]} · {P[1]} · {open3} | (stamp) HOURBACK · YOUR EVENINGS BACK",
            "[2.0 s] try this | Tell AI 3 true stories. It writes the speech. | (from 4.3 s) Claude's real speech, shortened: | (sticky, 2.0-4.3 s, 52 px) what we told it (made up for this post): · Linda: 31 years at the library front desk · knew every regular's name · 20 years of Saturday story time · lemon candies for anyone's rough day",
            f"[4.3 s] Speech for Linda, shortened · {reg_q} … → [5.35 s] {joke} (highlighted) · ← the joke → [6.4 s] {story_q} …",
            f"[7.4 s] it turns facts into moments | A jar of candies becomes the best line. | (page) Its jar story, word for word · And then there's the jar. · {jar_q.split('jar. ', 1)[1]} … (highlighted)",
            f"[10.4 s] Do this: | Tell AI 3 stories. Ask for 2 minutes. | In ChatGPT, Claude or Gemini. Read it out loud once. | (page) Speech for Linda, word for word · its last line: · {toast}",
            "[11.8 s to end, 2.6 s] Follow to learn one real AI trick a day.",
        ],
        hook_options=["31 years. You get 2 minutes.", "Retirement speech tomorrow. 2 minutes.", "Coworker retires tomorrow. Speech: 2 minutes."],
        hook_picker=PICKER + ("Verdict B: #2 '31 years. You get 2 minutes.' (contrast creates tension; weakness: never says 'speech' or "
                              "'tomorrow', so the visual must establish it; #1 the clearest fallback). Adopted, listed first; frame 0 "
                              "carries 'Speech for Linda' on the page header, a mic and a 2:00 stopwatch so the speech is clear without the words."),
        duration_s=dur("studio-nov04/hourback/hb-reel-1109-retirement-speech.mp4"),
        style=("Body: drawn occasion scene (deadline + number + the REAL output in frame 0), new composition: a send-off table "
               "with a mic on a stand, a stopwatch that really counts down from 2:00, a jar of lemon candies that glows on the jar "
               "beat, and the speech page already showing Claude's opening at 0.00 s. Dedicated cover: original simple template "
               "'big number' (style 8, QUIET): a giant 2:00 + the hook + Claude's closing line. Grid: after Mon 5:45 pm Day 14 "
               "(Look B, loud). 9-tile window Nov 4 Day 12 -> Nov 9: Look B, reframe, one giant word, sticky note, follow the "
               "line, reframe, big number = 6 styles (if D1 keeps its giant-word cover)."),
        send_test=False,
        sources=[f"studio/editorial/hb-nov04-run-retire.txt (fresh, isolated verbatim Claude run via claude -p, {run_at('retire')})"],
        notes=("Standalone, no Part 2, no callback, no on-screen send line. No trial flag. Different occasion family from A (work "
               "send-off vs family birthday). Desk grade: >=5 s and >=30% on >=40. Numbers on frame 0 ('31', '2', stopwatch 2:00) "
               "and in caption line 1. Real output visible from 0.00 s (opening 3 paragraphs, 50 px Caveat). Payoff words at 2.0 s; "
               "first passage at 4.3 s. Follow pill 2.6 s. Music hb-x-ta-da-funk (existing HB track), -13.8 LUFS, 2.0 MB, 14.4 s. "
               "Builder: studio/editorial/nov04_hourback.py retire (scenes nov04_hourback_ab.py; cover nov04_hourback_covers.py; run "
               "nov04_hourback_run.py retire). Transcript scanned: no real personal name or employer. Topic check: wedding toast "
               "(Nov 1) and cue card (Nov 2) are speeches too: this is the 3rd speech-adjacent HB piece in 9 days (doubt), but a "
               "different occasion (work retirement) and a listed idea in the brief. CATCH names two real gap-fills in the reply "
               "(kids' names; kids bringing their own kids). Self-review (QG-1) fixes: ruled lines didn't match the text rows "
               "(removed); 'rough-day candies' sat behind the card, then on the stopwatch (moved above the jar); follow pill hid "
               "the mic and label (scene lowered 35-55 px); payoff and Do-this wording aligned ('Tell AI 3 true stories' / 'Tell "
               "AI 3 stories'); cover label 'AI's last line' -> 'Claude's real last line, word for word'. Not yet seen by an "
               "independent reviewer (QG-5). CD GATE FIXES (Nov 4, coordinator): made-up-facts sticky held 2.0 s at 52 px above the page, subtitle "
               "hidden while it shows; chip moved from ~84% to the top band (y 228); frame-0 opening now cuts the odd-out-loud line 'And "
               "she always knew whose face it was.' (real, but it needs the next paragraph for context): header 'Speech for Linda, "
               "shortened', the cut marked …, text up to 54 px. Beat 2 3.4 -> 3.0 s, Do this 4.2 -> 4.0 s. Strip re-checked."),
    ))
    return out
