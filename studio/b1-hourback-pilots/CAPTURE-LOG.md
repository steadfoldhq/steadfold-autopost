# Hourback capture log: real AI runs for the Oct 19-21 pilots (agent B1)

Run date: Fri Oct 16, 2026. Each run: a fresh AI chat-assistant session (Claude, Anthropic; a new subagent with no other context) given the input file verbatim. Outputs are saved verbatim in `<run>.out.txt`. All inputs are made up for these posts: no real people, buildings, brands or chats.

| Run | Input (made up) | Used in | What the AI did | Our check |
|---|---|---|---|---|
| r1 | 255-word building email | hb-reel-1019am-just-the-asks | 3 asks + 1 conditional, each quoted | Every quote matches the email word for word. On screen: our 3-line summary (labelled) + one verbatim quote as the check |
| r2 | Over-apologetic email (4 sorries) | hb-reel-1019-one-sorry | Kept one "Sorry", kept the Friday promise | Sorry count 4 -> 1; meaning kept |
| r3 | Neighbour driveway text | hb-reel-1020am-driveway-text | 31-word calm reply | Word count 31 (<40); owns it; no grovel |
| r4 | 3 made-up blenders | hb-reel-1020-three-tabs | Picked A, table with price/power/warranty/noise | Figures in the table match the input specs |
| r5 | Made-up "Dewbrook Skin" brand email | hb-reel-1021am-brand-email | 7 red flags with quotes | Quotes match; advice: never share login, never pay |
| r6 | 63-message group chat | hb-reel-1021-group-costume | 3 themes, picked "weather" with who wears what | Weather line uses only items people named. Options 2 and 3 (smurfs, haunted house) were weaker; the AI itself flagged that Mila had said no to smurfs. Not shown. On screen the weather pick is shown as a table (labelled "as a table") |
| r7 | 47-message group chat | hb-1019-single-group-chat | "Saturday at 2pm at Rosa's, for 4 people, and Noor books" + flagged Noor's last "wait" | Matches the chat |
| r8 | $96 bill, $24 drinks, Ana didn't drink | hb-1021-ai-said-what-bill | 18 / 26 / 26 / 26 | 18+26+26+26 = 96 (checked in code) |
| r9 | 16-line card statement (made-up merchants) | hb-1021-single-subscriptions | 5 repeat charges, $78.47 a month; flagged the transit card and the FITLY annual->monthly line for a second look | 12.99+2.99+9.99+45.00+7.50 = 78.47 (checked in code) |

hb-1020-single-stopped-doing lists only things we ran this week (r1, r2, r4, r7).
