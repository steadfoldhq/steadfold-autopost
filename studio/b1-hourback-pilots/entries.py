#!/usr/bin/env python3
"""Hourback pilot entries Oct 19-21 (agent B1). `python3 entries.py` writes entries.json + hourback-captions-lint.txt."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
T = lambda d, hm: f"2026-10-{d}T{hm}:00-04:00"  # noqa: E731
EX = "The reply is from a real AI run."

E = []


def reel(pid, d, hm, caption, fc):
    E.append(dict(id=pid, account="hourback", publish_at=T(d, hm), caption=caption, first_comment=fc,
                  video=f"reels/{pid}.mp4", cover=f"reels/{pid}-cover.jpg"))


def feed(pid, d, hm, caption, fc, alt, n=1):
    E.append(dict(id=pid, account="hourback", publish_at=T(d, hm), caption=caption, first_comment=fc, alt_text=alt,
                  images=[f"{pid}/{i:02d}.jpg" for i in range(1, n + 1)]))


def story(pid, d, hm, note):
    E.append(dict(id=pid, account="hourback", publish_at=T(d, hm), story=True, image=f"stories/{pid}.jpg", caption=note))


# ------------------------------------------------------------------ Mon Oct 19
reel("hb-reel-1019am-just-the-asks", 19, "08:45",
     "POV: it's 8:47 am, there's a 255-word building email, and you just want to know what they need from you.\n\n"
     "AI pulled out 3 asks: car out of the lot by 7 am Tuesday, a name tag on the bike by Friday, and a reply about the party "
     "only if you want to help. It quoted the line for each one, and we checked all 3 against the email.\n\n"
     "Full prompt below:\n"
     "Here's an email. What is it asking me to do, and by when? One line per ask. Quote the sentence each ask comes from.\n\n"
     f"Example made up for this post. {EX}\n\n"
     "Tip: remove names and addresses before you paste.\n\n"
     "#lifeadmin #aitips #emailtips #adulting #inbox",
     "Longest email you got this week? Guess the word count.")
feed("hb-1019-single-group-chat", 19, "17:45",
     "Your group chat: 47 messages about brunch. Still no plan.\n\n"
     "We pasted the whole chat into AI and asked for the plan in one line. It said: \"Saturday at 2pm at Rosa's, for 4 people, "
     "and Noor books.\" It also noticed Noor's last message was \"wait\", so it said to confirm. Fair.\n\n"
     "Full prompt below:\n"
     "Here's our group chat. Give me the plan in one line: day, time, place and who books.\n\n"
     f"Chat made up for this post. {EX}\n\n"
     "Tip: ask before you paste friends' messages, and remove phone numbers.\n\n"
     "Send this to the group chat that needs it.\n\n"
     "#groupchat #brunch #aitips #lifeadmin #friends",
     "How many messages does your group chat need to pick a time?",
     "Hourback single tile on indigo. Kicker \"Group chat vs AI\". Big headline \"47 messages. Still no plan.\" with \"47\" "
     "on a yellow pill and \"plan.\" on an orange pill. Below, a white chat bubble labelled \"Real AI reply\": \"Saturday at 2pm "
     "at Rosa's, for 4 people, and Noor books.\" Round Hourback stamp top right.")
reel("hb-reel-1019-one-sorry", 19, "19:00",
     "Things I stopped doing: saying sorry 4 times in one email.\n\n"
     "My draft had 4 sorries. I asked AI to keep my words and apologise once at most. It kept the Friday promise, kept one "
     "sorry and cut the rest.\n\n"
     "Full prompt below:\n"
     "Rewrite this so it's warm but apologises once at most. Keep my words where you can. Keep it short.\n\n"
     f"Example made up for this post. The rewrite is from a real AI run.\n\n"
     "Tip: remove personal details before you paste.\n\n"
     "#emailtips #lifeadmin #aitips #workemail #adulting",
     "Be honest: how many sorries are in your last email?")
for k, (hm, note) in enumerate([("08:15", "Morning question: unread emails A/B/C"),
                                ("12:15", "Behind the scenes: the 255-word email run, all 3 quotes matched"),
                                ("18:00", "New post share: hb-1019-single-group-chat"),
                                ("21:00", "This or that: 47 messages vs one person books")], 1):
    story(f"hb-st-1019-{k}", 19, hm, note)

# ------------------------------------------------------------------ Tue Oct 20
reel("hb-reel-1020am-driveway-text", 20, "08:45",
     "POV: it's 7:52 am and the neighbour texts about a car in their driveway. It was your guest. You didn't know.\n\n"
     "Draft 1 was 2 sorries and a lot of capitals. I asked AI for a calm reply under 40 words that owns it without grovelling. It wrote "
     "31 words, said sorry once and promised it won't happen again.\n\n"
     "Full prompt below:\n"
     "Help me reply to this text from my neighbour. I didn't know: my guest parked there last night and has gone now. I want to "
     "be friendly, own it and not grovel. Under 40 words.\n\n"
     f"Example made up for this post. {EX}\n\n"
     "Tip: remove names and addresses before you paste.\n\n"
     "#neighbours #lifeadmin #aitips #adulting #texting",
     "Neighbour texts: reply right away or wait till lunch?")
feed("hb-1020-single-stopped-doing", 20, "17:45",
     "Things I stopped doing since AI reads the boring bits for me.\n\n"
     "Still checking every quote though. Each one is a real run we did this week on made-up examples, and here are the "
     "prompts:\n\n"
     "1. Long emails: \"Here's an email. What is it asking me to do, and by when? One line per ask. Quote the sentence each ask "
     "comes from.\"\n"
     "2. Sorry-heavy drafts: \"Rewrite this so it's warm but apologises once at most. Keep my words where you can.\"\n"
     "3. 3 tabs at 11 pm: \"Which of these should I get? Answer in one line first, then a short comparison table.\"\n"
     "4. The 47-message group chat: \"Here's our group chat. Give me the plan in one line: day, time, place and who books.\"\n\n"
     "Check every answer against the original before you act on it.\n\n"
     "Tip: remove names, numbers and addresses before you paste.\n\n"
     "#lifeadmin #aitips #adulting #inbox #groupchat",
     "What would be on your list?",
     "Hourback sticky-note list on yellow. A lined paper note with tape and a red margin line, titled \"I stopped doing:\" in "
     "handwriting, with ticks: reading long emails, 4 sorries per email, 3 tabs at 11 pm, scrolling 47 messages. Below the "
     "note, in indigo handwriting: \"still checking every quote\".")
reel("hb-reel-1020-three-tabs", 20, "19:00",
     "POV: it's 11:02 pm, there are 3 tabs open, 3 blenders, and every one says \"best seller\".\n\n"
     "I pasted the specs, said smoothies for 2 most mornings and soup sometimes, and asked for one pick. AI chose Blender A: "
     "\"the best balance of price, power, and quietness\". It also pointed out that the glass jar handles hot soup well. Tabs "
     "closed.\n\n"
     "Full prompt below:\n"
     "I [how you'll use it]. Which of these should I get? Answer in one line first, then a short comparison table. "
     "[paste the specs]\n\n"
     f"Specs made up for this post. {EX} Check the specs on the shop page before you buy: AI only knows what you paste.\n\n"
     "Tip: paste the specs, never your card details.\n\n"
     "#shoppingtips #aitips #kitchen #lifeadmin #smartshopping",
     "What's open in your tabs right now? Be honest.")
for k, (hm, note) in enumerate([("08:15", "Be honest: sorries in your last email"),
                                ("12:15", "Behind the scenes: 31 words, under 40 (driveway reply run)"),
                                ("18:00", "New post share: hb-1020-single-stopped-doing"),
                                ("21:00", "Your turn: one thing you'd stop doing")], 1):
    story(f"hb-st-1020-{k}", 20, hm, note)

# ------------------------------------------------------------------ Wed Oct 21
reel("hb-reel-1021am-brand-email", 21, "08:45",
     "POV: you post online and a brand offers you $2,000 for one Reel. \"Reply within 24 hours.\"\n\n"
     "We asked AI if it was legit. First line: \"No, this looks like a scam.\" It listed 7 red flags, each with a quote. The big 4: it asks for your "
     "Instagram login, a $49 \"refundable\" fee, an app download from a link and a 24-hour rush. A real offer has a named contact, a brief "
     "and a written agreement, and it never asks for your password or your money.\n\n"
     "Full prompt below:\n"
     "Is this brand email legit? List the red flags, one line each, and quote the line each comes from. Then say in 2 lines what "
     "a real offer usually includes.\n\n"
     f"Email and brand made up for this post. {EX} Don't click anything, report and block the sender, and if you already typed a password "
     "somewhere, change it and turn on two-factor login.\n\n"
     "Tip: never paste passwords or login codes into any chat.\n\n"
     "#creatortips #scamawareness #smallcreator #aitips #branddeals",
     "Creators: what's the strangest brand email you've had?")
feed("hb-1021-ai-said-what-bill", 21, "13:00",
     "AI said what? We asked it to split a $96 dinner for 4. Ana didn't drink.\n\n"
     "Food for all 4, drinks only for the 3 who drank. It answered: Ana $18, everyone else $26. We checked: "
     "18 + 26 + 26 + 26 = 96. It passed this time.\n\n"
     "The line that keeps it honest: \"Show the math and check that it adds up.\" Then check it yourself.\n\n"
     "Full prompt below:\n"
     "Dinner for [number] came to [total], and [drinks] of that was drinks. [Name] didn't drink. Split it fairly: food equally "
     "between everyone, drinks only between the people who drank. Show the math and check that it adds up to [total].\n\n"
     f"Example made up for this post. {EX} Any currency, same math.\n\n"
     "Tip: first names are enough.\n\n"
     "#billsplit #aitips #dinnerwithfriends #lifeadmin #moneytips",
     "Fair split, or everyone pays the same? Pick one.",
     "Hourback carousel, 3 slides on cream. Slide 1: kicker \"AI said what?\", big serif headline \"$96 dinner. Ana didn't drink.\" "
     "with \"$96\" on a yellow pill and \"drink.\" on an indigo pill, and a yellow chat bubble \"Split it fairly. Food: all 4. Drinks "
     "($24): only the 3 who drank.\" Slide 2: \"What it said\", a white bubble labelled \"The AI's math, condensed\": food $72 divided by 4 is $18 each, drinks $24 divided by 3 is $8 each, "
     "Ana $18, the other 3 $26 each. Slide 3: \"It passed.\" with the check 18 + 26 + 26 + 26 = 96 and the fix line \"Show the "
     "math and check that it adds up.\"", n=3)
feed("hb-1021-single-subscriptions", 21, "17:45",
     "5 subscriptions hiding in one card statement.\n\n"
     "We gave AI a statement (made up for this post) and asked which charges look like subscriptions. It found streaming, cloud "
     "storage, a fitness app, the phone plan and a news subscription: $78.47 a month in this example. It quoted each line, and "
     "we added them up: 12.99 + 2.99 + 9.99 + 45.00 + 7.50 = 78.47. It also flagged 2 lines for a second look, including an "
     "\"annual->monthly\" charge.\n\n"
     "Full prompt below:\n"
     "Here's last month's card statement. Which charges look like subscriptions or repeat charges? List them with the amount "
     "and quote the line each comes from. Then give the monthly total of those.\n\n"
     f"Statement made up for this post. {EX}\n\n"
     "Tip: delete card numbers, names and addresses before you paste. The date, merchant and amount columns are enough.\n\n"
     "#subscriptions #lifeadmin #aitips #budgeting #moneytips",
     "Which subscription do you always forget you have?",
     "Hourback emoji meme on indigo. Top text: \"Me, finally reading my whole card statement:\". A big receipt emoji and "
     "eyes emoji. Handwritten yellow line below: \"AI: 5 subscriptions. $78.47 a month.\" Small label \"Example made up\".")
reel("hb-reel-1021-group-costume", 21, "19:00",
     "6 friends. 1 group costume. 63 messages. AI: one line.\n\n"
     "We pasted the whole chat and asked for 3 themes using what people already own. Its pick: weather. Priya is rain in her "
     "yellow raincoat, Theo a cloud in the white sheet, Mila the sun, Kai lightning, Sam fog, and Jonah gets the fog machine. "
     "Jonah still wants pirates.\n\n"
     "Full prompt below:\n"
     "Here's our group chat. Suggest 3 group-costume themes that use what people said they already own. One line each, with who "
     "wears what.\n\n"
     f"Chat made up for this post. {EX} Its 2 backup ideas were weaker, so read it before you send it.\n\n"
     "Tip: ask before you paste friends' messages.\n\n"
     "#halloweencostume #groupcostume #halloween #groupchat #aitips",
     "Tag the friend who sends 20 of the 63 messages.")
for k, (hm, note) in enumerate([("08:15", "Morning question: too-good brand email A/B/C"),
                                ("13:15", "New post share: hb-1021-ai-said-what-bill"),
                                ("16:30", "Behind the scenes: statement run, 78.47 matches; new post at 5:45 pm"),
                                ("18:30", "Tonight's Reel teaser: weather costume, who are you?")], 1):
    story(f"hb-st-1021-{k}", 21, hm, note)

if __name__ == "__main__":
    E.sort(key=lambda p: p["publish_at"])
    (HERE / "entries.json").write_text(json.dumps(E, indent=1, ensure_ascii=False))
    lines = []
    for p in E:
        if p.get("story"):
            continue
        lines += [f"== {p['id']}", "CAPTION", "<<<", p["caption"], ">>>", "FIRST COMMENT", "<<<", p["first_comment"], ">>>"]
        if p.get("alt_text"):
            lines += ["ALT TEXT", "<<<", p["alt_text"], ">>>"]
    (HERE / "hourback-captions-lint.txt").write_text("\n".join(lines) + "\n")
    print(len(E), "entries")
