import json
S='/tmp/claude-0/-home-claude/60837be5-8cde-507a-87a7-2bafa6fa6f6c/scratchpad/lh/un.json'
un={x['id']:x for x in json.load(open(S))}
P='recovery-oct22/lockedhour/'
FOLLOW="Follow for one small focus fix a day, each one backed by research."
def c(i): return un[i]['caption']
patch=[]
def add(i,a,r,new=None):
    e={"id":i,"action":a,"reason":r}
    if new: e["new"]=new
    patch.append(e)

keep_reasons={
 "lh-1022-split-desk":"Publishes today 5 pm (inside 24 h, no hard rule broken). Weak spot noted: 'in 5 swipes 👉' interactive hook, a format the studio retired as a hook; carousels reach 1-13.",
 "lh-reel-1022-walk":"Tonight 7 pm; already recut to 13.9 s today. Payoff (60%) lands at ~5 s and it uses the overused pointing hand, but no hard rule broken inside 24 h.",
 "lh-ch-1023-1":"Story chain frame; clear quiz hook, on-palette.",
 "lh-ch-1023-2":"Story chain frame; payoff + source line.",
 "lh-ch-1023-3":"Story chain frame.",
 "lh-ch-1023-4":"Story chain frame; the rule.",
 "lh-ch-1023-5":"Minor: the mini cover in the frame ('A 40-second break that works') doesn't match the real post cover ('Me, rereading the same line again:'). Not a rule break; inside 48 h.",
 "lh-1023-green-break":"Sourced (Lee et al. 2015), real study, clear Do this. Cover is bold sans + emoji (off the serif look) but inside the no-edit window and no rule broken.",
 "lh-1023-roadmap-sunday-plan":"Panorama-route carousel, sourced, on palette. Inside window.",
 "lh-reel-1023-caffeine":"Fri 7 pm, 13.5 s, sourced (Drake 2013), disclaimer present. Pointing-hand template and payoff at ~3.5 s; inside window, no rule broken.",
 "lh-reel-1024am-floss-after":"Sat 8:30 am (before the Sat-noon line). 14.1 s, sourced. Same pointing-hand template; payoff ~3.5 s. Leave.",
 "lh-ch-1024-1":"Story hook on a real photo, per 13.4.",
 "lh-ch-1024-2":"Story chain frame; relatable chat bubbles.",
 "lh-ch-1024-3":"Story chain frame; the research.",
 "lh-ch-1024-4":"Story chain frame (hourglass, no pointing hand).",
 "lh-1024-follow-cant-start":"Follow-the-line carousel; strong reframe (mood, not time), verified sources (Sirois & Pychyl 2013; Wohl et al. 2010). The studio log names the Oct 24-25 interactive tiles as the last of their kind; keep.",
 "lh-ch-1025-1":"Story quiz frame.",
 "lh-ch-1025-2":"Story payoff with source.",
 "lh-ch-1025-3":"Story chain frame.",
 "lh-ch-1025-4":"Story rule frame.",
 "lh-ch-1025-5":"Hand-off frame; mini cover matches the done-list post.",
 "lh-1025-done-list":"10-slide teach carousel, sourced (Amabile & Kramer), clear WHY and Do this. Pointing hand on slides 6 and 10 is the only weak spot.",
}
order=[x for x in un]
for i in order:
    if i in keep_reasons: add(i,"keep",keep_reasons[i])

# ---- improve: reveal 47
cap=c("lh-1024-reveal-47-seconds").replace("Send this to your 40-tabs friend.","Send this to your 40-tabs friend.\n\n"+FOLLOW)
add("lh-1024-reveal-47-seconds","improve",
 "Slide 4 used the piggy bank (overused, off-topic), slides 2-3 were pixelation blurs that read as broken files on a phone, and 5 slides for one number. Rebuilt as 3 slides: guess cover with the 60:00 ring, two to-scale rings (2:30 vs 0:47), Do this. Caption gains the follow reason.",
 {"images":[P+"lh-1024-reveal-47-seconds/01.jpg",P+"lh-1024-reveal-47-seconds/02.jpg",P+"lh-1024-reveal-47-seconds/03.jpg"],
  "caption":cap,
  "alt_text":"Locked Hour 3-slide carousel. Slide 1: 'How long do you stay on one screen?' in a large serif on butter yellow, with '2004: 2½ minutes' and an empty timer ring reading ?:?? labelled now. Slide 2: '47 seconds. On one screen, on average.' Two timer rings drawn to scale: 2:30 in 2004 and 0:47 in 2016 to 2020, source Gloria Mark. Slide 3: Do this: Next task: full screen. One window, until it's done."})
add("lh-ch-1024-5","improve","The frame showed a mini cover that no longer matches (and never matched) the post's slide 1, plus a pointing hand. New frame shows the real new cover, no hand.",
 {"image":P+"stories/lh-ch-1024-5.jpg"})
# ---- reels
add("lh-reel-1024-lyrics","improve",
 "Same template as every LH Reel this week (pointing hand, static hook for 3.5 s, payoff at ~5.5 s). Rebuilt 13.2 s: payoff 'Songs with words lowered reading scores' at 1.8 s, 'even songs they liked' at 2.7 s, word-lane metaphor at the 60:00 keyhole ring, Do this at 9 s, loop. Original track reused.",
 {"video":P+"reels/lh-reel-1024-lyrics-r1.mp4","cover":P+"reels/lh-reel-1024-lyrics-r1-cover.jpg",
  "alt_text":"Edited video in the Locked Hour look: big serif lines with highlighter pills on butter, cream and pink paper, a 60:00 timer ring with a keyhole notch. Text: Studying with your playlist on? / Songs with words lowered reading scores. Even songs they liked. (Perham & Currie 2014, 30 students) / No words? About as good as quiet. / Lyrics and the page fight for the same word lane. Only one gets through. / Do this: Make one no-lyrics playlist. Play it every focus hour. / Save the songs you love for chores. It loops back to the opening line."})
cap=c("lh-reel-1025am-planning-fallacy").replace("Why does everything take longer than you think? You're not bad at planning. Everyone is.","Everything takes longer than you think? It's not just you. You're not bad at planning. Everyone is.",1)
add("lh-reel-1025am-planning-fallacy","improve",
 "Rebuilt on the best-holding structure (rule + reassurance open, 41% at 13.9 s): 'Everything takes longer? It's not just you.' at frame 0, the 34 → 56 days ruler lands by 2.8 s with the worst-case 49 marker, then the why, 'last time?' and Do this. 13.8 s, hourglass (no pointing hand), original track reused. Caption line 1 matches.",
 {"video":P+"reels/lh-reel-1025am-planning-fallacy-r1.mp4","cover":P+"reels/lh-reel-1025am-planning-fallacy-r1-cover.jpg","caption":cap,
  "alt_text":"Edited video in the Locked Hour look: big serif lines with highlighter pills on butter, cream and pink paper, a halftone hourglass and a ruler of days. Text: Everything takes longer? It's not just you. / Students guessed their thesis: 34 days. It took 56. A bar grows to 34, a pink bar to 56, and a marker shows the worst-case guess, 49. (Buehler, Griffin & Ross 1994) / We plan for the day everything goes right: no slow replies, no sick day, no file that won't open. / Ask: how long did it take last time? / Do this: Add half again. 2 hours? Plan 3. Part 2 tonight at 7. It loops back to the opening line."})
cap=c("lh-reel-1025-unpack").replace("\"An hour\" was really about 2 hours of work and 2 days of waiting.","\"An hour\" was really about 2 hours of work and 2 days of waiting. (The website task is made up for this post.)")
add("lh-reel-1025-unpack","improve",
 "Same pointing-hand template, payoff at ~5.5 s. Rebuilt 13.8 s: a 'to do' card unpacks into 5 timed step chips by 3 s (labelled 'Made up for this post.'), then the study line, hidden steps, Do this, loop. Original track reused; caption now labels the made-up task.",
 {"video":P+"reels/lh-reel-1025-unpack-r1.mp4","cover":P+"reels/lh-reel-1025-unpack-r1-cover.jpg","caption":cap,
  "alt_text":"Edited video in the Locked Hour look: big serif lines with highlighter pills on cream, butter and pink paper. Text: 'It'll take an hour.' It won't. A to-do card reads Update the website (1 h). / List the steps before you guess: find the old photos 15 min, wait for the new ones 1 day, write the new text 45 min, check then fix 30 min + 1 day, upload + test 20 min = 2 h of work + 2 days of waiting (made up for this post). / People who listed the steps made more realistic guesses (Kruger & Evans 2004). / Always add the hidden steps: waiting on someone, setup, the back-and-forth, the final check. / Do this: Tonight, list Monday's biggest task, step by step. Then guess. It loops back to the opening line."})
# ---- replace 1%
add("lh-1025-climb-one-percent","replace",
 "'1% better a day = 38x' is the most-repeated productivity cliché, its numbers are an illustration not research, and the brief rules out clichés. Replaced in the same Sun 5 pm slot with 'Monday isn't magic. It's a handle.' (v0.5 floor tile 09, rebuilt in the v4 palette): verified fresh-start data with its correlational caveat, and it lands the night before Monday. Id kept so the slot holds; content is new.",
 {"images":[P+"lh-1025-monday-handle/01.jpg",P+"lh-1025-monday-handle/02.jpg",P+"lh-1025-monday-handle/03.jpg"],
  "caption":"Monday isn't magic. It's a handle. Grab it tonight.\n\nTHE RESEARCH: researchers looked at the gym records of about 12,000 students at one US university. At the start of a new week, the chance of a gym visit was 33.4% higher than usual. The start of a month: 14.4%. The start of a semester: 47.1%. They call it the fresh start effect: a new week feels like a clean page, so people try again.\n\nTHE HONEST PART: it's correlational. It shows when people start, not that Mondays make anything work. And it cuts both ways: waiting for Monday can turn into waiting forever.\n\nHOW TO USE IT:\n1. Tonight, pick one thing you want to start.\n2. Write when and where: \"Monday, 8 am, after coffee.\"\n3. Missed it? Every day has a handle: tomorrow morning, after lunch, the next hour.\n\nDo this: tonight, pick one thing and write when you'll start it: \"Monday, 8 am, after coffee.\"\n\nSend this to the friend waiting for a fresh start.\n\n"+FOLLOW+"\n\n#habits #freshstart #mondaymotivation #focus #selfimprovement",
  "first_comment":"When will you start yours? Source: Dai, Milkman & Riis (2014), The Fresh Start Effect: Temporal Landmarks Motivate Aspirational Behavior, Management Science 60(10). Study 2: gym attendance records of 11,912 undergraduates at a large northeastern US university, Sept 2010 to Dec 2011. The probability of a gym visit rose at the start of a week (33.4%), month (14.4%) and semester (47.1%), relative to baseline. Archival, correlational data.",
  "alt_text":"Locked Hour 3-slide carousel. Slide 1: 'Monday isn't magic. It's a handle.' in a large serif on butter yellow; below, a week strip where Monday is a yellow padlock with a handle. Slide 2: 'At the start of a week, gym visits jumped 33.4%.' A card lists start of a week +33.4%, start of a month +14.4%, start of a semester +47.1%. Source: Dai, Milkman & Riis 2014, gym records of about 12,000 students, correlational. Slide 3: Do this: Tonight, pick one thing. Write when you start: 'Monday, 8 am, after coffee.' Use the handle. Don't wait for it."})
# ---- one word
cap=c("lh-oneword-01").replace("One Word No. 1. Each episode is one word that guards your focus.","One Word No. 2 (No. 1 was \"Later\"). Each episode is one word that guards your focus.").replace("One Word No. 2 is Wednesday at 5 pm.","One Word No. 3 is Wednesday at 5 pm.")
add("lh-oneword-01","improve",
 "Numbering was wrong: One Word No. 1 ('Later') shipped Oct 17 (brand-system-v4 §1), so this is No. 2 (13.5: keep numbering honest). Cover now follows the series spec (black label 'ONE WORD · No. 2', one huge word with a pink highlighter stripe, halftone clock, stamp); slides 2-3 were bare flat cards (§12 says never) and are rebuilt with the 3-check clock ring and the study + Do this. Caption renumbered. NOTE for the schedule owner: Wednesday's One Word must be labelled No. 3.",
 {"images":[P+"lh-oneword-02-batch/01.jpg",P+"lh-oneword-02-batch/02.jpg",P+"lh-oneword-02-batch/03.jpg"],"caption":cap,
  "alt_text":"Locked Hour 3-slide carousel. Slide 1: black label 'One Word · No. 2', the line 'Inbox open all day again?' and the huge word 'Batch.' over a pink highlighter stripe, with a halftone alarm clock and the note '3 email checks a day, not all day'. Slide 2: '3 checks. That's it.' A clock ring with pink marks at 9:30, 1:00 and 4:30; 'Tab closed in between. Urgent? People can call or text.' Slide 3: 'Less stress.' In a 2-week study, the week people checked email 3 times a day felt calmer than the week they checked whenever. Do this: write your 3 check times on a sticky note. Close the tab. Source: Kushlev & Dunn 2015."})
ids=[p['id'] for p in patch]; assert len(ids)==len(set(ids))==29, (len(ids),set(un)-set(ids))
json.dump(patch,open('/home/claude/steadfold-autopost/studio/recovery-oct22/lockedhour/patch.json','w'),indent=1,ensure_ascii=False)
print('ok',{a:sum(1 for p in patch if p['action']==a) for a in ['keep','improve','replace','hold']})
