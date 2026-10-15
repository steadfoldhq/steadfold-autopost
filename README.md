# Steadfold Autopost

Posts Steadfold's Instagram carousels **by itself, on schedule**, for four accounts:

| Account | Usual time (Toronto) |
|---|---|
| @fullyfundedhq | 12:00 pm |
| @lockedhourhq | 12:30 pm |
| @hourbackhq | 1:00 pm |
| @littlefoldhq | 11:30 am |

Once it's set up, there is **no daily work**. You add a week of posts once a week, and that's it.

---

## What it does, in plain words

- A free GitHub "robot" (GitHub Actions) wakes up **every 15 minutes**.
- It reads the schedule (`schedule/posts.json`). If a post's time has arrived and the post hasn't gone out yet, it:
  1. checks that the account's key (token) really belongs to the right account (for example, @lockedhourhq). If it doesn't, it refuses to post.
  2. gives Instagram the slide images (JPEG files stored in this repo, under `media/`),
  3. builds the carousel with the caption (the alt text goes on slide 1),
  4. waits until Instagram says the carousel is ready, then publishes it,
  5. posts the **first comment** from the same account,
  6. writes the result (post link, time) into `state/published.json`.
- It **never posts the same thing twice**. It saves progress after every step, and before posting it also checks the account's latest posts on Instagram.
- If something fails, it carries on with the other posts. The run is then marked as failed, and **GitHub emails you**.
- Once a week, a second robot renews the four Instagram tokens so they never expire (they last 60 days).

It uses only Instagram's official API ("Instagram API with Instagram Login") and GitHub. It doesn't need a Facebook Page, Meta Business Suite or Chrome.

---

## What's in this folder

| File | What it is |
|---|---|
| `schedule/posts.json` | The posts: account, time, caption, first comment, alt text, image list |
| `media/<post-id>/01.jpg …` | The slides as JPEG (Instagram only accepts JPEG) |
| `state/published.json` | Written by the robot: what was posted, when, link, any error |
| `autopost.py` | The posting robot |
| `refresh_tokens.py` | The weekly token renewer |
| `.github/workflows/autopost.yml` | Runs `autopost.py` every 15 minutes |
| `.github/workflows/refresh-tokens.yml` | Runs `refresh_tokens.py` every Monday |
| `tools/import_week.py` | Turns a week of post folders + prompt files into `media/` and `schedule/posts.json` |
| `tests/` | Automatic checks (simulated Instagram, no real posting) |
| `SETUP-PROMPT-claude-in-chrome.txt` | A Claude in Chrome prompt that clicks through the Meta setup with you |

---

## One-time setup (about 45 minutes)

You'll do this once. Steps 5 to 9 can be done with **Claude in Chrome**: paste `SETUP-PROMPT-claude-in-chrome.txt` into the Claude panel in Chrome. It does the clicks and stops when it needs you.

### Part A: GitHub (the robot's home)

1. **Make a free GitHub account** at <https://github.com/signup> (skip this if you have one). Write down your username. Below it's called `<owner>`.
2. **Create the repository.** Go to <https://github.com/new>.
   - Repository name: `steadfold-autopost`
   - Visibility: **Public**. Instagram has to be able to download the images, and public repos get GitHub Actions for free.
   - Don't add a README, .gitignore or license. Click **Create repository**.
3. **Upload these files.** The easiest way is **GitHub Desktop** (<https://desktop.github.com>):
   - In GitHub Desktop: *File → Clone repository → steadfold-autopost*.
   - Unzip `steadfold-autopost.zip`. Copy **everything inside** the unzipped folder into the cloned folder, **including the hidden `.github` folder**. On a Mac, press Cmd+Shift+. in Finder to show hidden files.
   - Back in GitHub Desktop, type a summary such as "first upload", click **Commit to main**, then **Push origin**.
   - (Uploading through the github.com web page also works, but it tends to skip the hidden `.github` folder, and it limits how many files you can upload at once. That's why Desktop is easier.)
4. **Check that the robot is allowed to save its notes.** Open `https://github.com/<owner>/steadfold-autopost/settings/actions`. Under *Workflow permissions*, choose **Read and write permissions**, then **Save**.

### Part B: Meta / Instagram (the keys)

5. **Meta developer account.** Go to <https://developers.facebook.com>, log in with your Facebook login and finish *Get started / Register* if asked (Meta may text you a code).
6. **Create the app.** Go to *My Apps → Create app*.
   - Name: `Steadfold Autopost`. Meta doesn't allow "Instagram", "Insta", "IG" or "Facebook" in app names.
   - Use case: **Manage messaging & content on Instagram** (this is the "Instagram API with Instagram Login").
   - Business portfolio: choose *don't connect* if that's offered. It keeps things simple, and the app works in **Development mode** for your own accounts.
   - In the use case, open **Permissions and features** and make sure these three are added: `instagram_business_basic`, `instagram_business_content_publish` and `instagram_business_manage_comments`.
   - **Don't** submit for App Review, publish the app, or start Business Verification. None of that is needed for your own accounts.
7. **Add the three accounts as Instagram testers.** Go to *App roles → Roles → Instagram Testers → Add Instagram Testers*, then add `fullyfundedhq`, `lockedhourhq` and `hourbackhq`.
8. **Accept the invite in each account.** This only works on **instagram.com in a computer browser**, not in the phone app. Log in as each account in turn, then go to *profile picture / More → Settings → Website permissions → Apps and websites → **Tester invites*** and click **Accept**.
   (If Meta won't add a tester because the account is already linked to the app's business, skip steps 7–8. The *Add account* button in step 9 usually works directly.)
9. **Make a token for each account and put it straight into GitHub.** Go to *Use cases → Customize → **API setup with Instagram login** → Generate access tokens → **Add account***, log in as the account and click **Allow**, then click **Generate token**.
   - **Don't paste the token into any chat, email or document.** Copy it and paste it straight into GitHub:
     `https://github.com/<owner>/steadfold-autopost/settings/secrets/actions` → **New repository secret**

     | Account | Secret name |
     |---|---|
     | @fullyfundedhq | `IG_TOKEN_FULLYFUNDED` |
     | @lockedhourhq | `IG_TOKEN_LOCKEDHOUR` |
     | @hourbackhq | `IG_TOKEN_HOURBACK` |
     | @littlefoldhq | `IG_TOKEN_LITTLEFOLD` |
   - Repeat for all three accounts. Log out of Instagram in the pop-up between accounts.

### Part C: The token-renewer key and the first check

10. **Create the `GH_PAT` secret.** The weekly renewer needs it to save the renewed tokens.
    - Go to <https://github.com/settings/personal-access-tokens/new> (fine-grained token).
    - Name: `steadfold-autopost secrets`. Expiration: the longest offered (write the date in your calendar).
    - Repository access: **Only select repositories → steadfold-autopost**.
    - Permissions → Repository permissions → **Secrets: Read and write**. Leave everything else as is.
    - Click **Generate token**, copy it, and add it as a new repository secret named **`GH_PAT`** (same page as step 9).
11. **Test without posting.**
    - Open the **Actions** tab → **Refresh tokens** → **Run workflow** (leave "Only check" ticked) → **Run workflow**. Open the run. You should see `GitHub access OK` and `current token works for @…` three times.
    - Then **Actions → Autopost → Run workflow**, tick **Dry run**, and run it. It lists what it would post. A green tick means it's ready.
12. **Remove duplicates.** If any of these posts are still **scheduled in Meta Business Suite**, delete them there. Otherwise they'd go out twice. (Autopost spots posts that are already live with the same caption and skips them, but it can't see Business Suite's scheduled drafts.)
13. **Turn on failure emails.** At <https://github.com/settings/notifications>, under *Actions*, make sure **Email** is on (failed workflows only).

That's it. From now on the **Autopost** workflow runs every 15 minutes by itself.

---

## Reels

A post with `"video": "reels/<id>.mp4"` (and optionally `"cover": "reels/<id>-cover.jpg"`) is published as a **Reel** instead of a carousel. It is shared to the main grid too.
- Videos must be MP4 (H.264 + AAC), 9:16, under 19.5 MB.
- The robot serves videos through jsDelivr, pinned to the exact commit (`cdn.jsdelivr.net/gh/<owner>/steadfold-autopost@<commit>/media/...`), because Instagram is pickier about video downloads. If jsDelivr can't serve a file, it falls back to raw GitHub. To force another host, set the repo variable `VIDEO_BASE_URL`.
- Instagram's own music library can't be added through the API. Our Reels carry original music made in code, so they're copyright-safe. To use a trending sound, post that Reel from the app instead.
- Processing a Reel takes Instagram a minute or more. If it isn't ready within 5 minutes, the next run (15 minutes later) picks it up again without re-uploading.

## Adding next week's posts

1. Ask Claude in the Steadfold chat: *"Import next week into the autopost repo, start date YYYY-MM-DD."* Claude runs
   `python tools/import_week.py --start-date YYYY-MM-DD --source <post folders> --prompts <prompt files folder>`.
   This converts the slides to JPEG, writes the schedule (one post per account per day, at each account's usual time) and prints a table to check.
2. Copy the updated `media/` and `schedule/posts.json` into your GitHub Desktop folder, then **Commit** and **Push**.
3. Optional: run **Autopost** with **Dry run** to see the upcoming list.

Small changes can be made right on github.com. Open `schedule/posts.json`, click the pencil, edit and commit:
- **Change a time:** edit `publish_at`. Keep the format `2026-10-21T12:30:00-04:00`. Toronto is `-04:00` until Nov 1 and `-05:00` after.
- **Cancel a post that hasn't gone out:** delete its whole `{ … }` block.
- **Fix a caption:** edit `caption` before the post goes out. Line breaks are written as `\n`.

## Pausing

- **Pause everything:** Actions tab → **Autopost** → "**…**" (top right) → **Disable workflow**. Turn it back on with **Enable workflow**.
- When you turn it back on, posts whose time passed while it was paused **will still go out**, one per account every 15 minutes, marked "late". If you don't want them, delete them from `schedule/posts.json` first.

## Checking what was posted

- **`state/published.json`** has one entry per post: `status` (`published` / `failed` / `publishing`), `permalink` (link to the post), `published_at` (UTC), `comment_status`, and `error` if something went wrong.
- **Actions tab → Autopost:** every run has a log in plain English. A red ❌ means something needs a look, and GitHub emails you.
- **Retry a failed post:** a post that failed is retried automatically up to 3 times. After that, use **Actions → Autopost → Run workflow** with **Retry failed** ticked.
- **First comment failed but the post is live:** only the comment is retried (up to 5 times), never the post.

---

## Limits and honest risks

- **Development-mode app.** That's fine for your own three accounts (Meta calls it Standard Access). No App Review is needed as long as the app only posts to accounts that have a role on it.
- **Tokens last 60 days.** The weekly renewer extends them. If it fails (you get an email), fix it within a few weeks. If a token does expire, make a new one (setup step 9) and replace the secret. A token must be at least 24 hours old before it can be renewed, so a manual renewal right after setup will fail. Use the "Only check" option.
- **The `GH_PAT` expires** on the date you chose in step 10. Make a new one before then.
- **Instagram only accepts JPEG.** The import tool converts PNG slides to JPEG (quality 92). Don't put PNGs in `media/`, because the robot refuses them.
- **Carousel limit: 10 slides.** Instagram crops all slides to match the first one. All our slides are 1080×1350 (4:5).
- **Not possible through the API:** music, a cover pick, collaborators, location, product tags and "share to Facebook". Alt text is supported, and we put it on slide 1.
- **Timing isn't to the minute.** GitHub often starts scheduled runs a few minutes late, sometimes 15–30 minutes or more when it's busy. Expect posts within about 0–30 minutes of their time.
- **The repo is public.** Anyone who finds it can see upcoming captions and slides before they're posted. That's low risk, but don't put anything private in it. The tokens are **secrets** and are never visible, not even in logs.
- **Image hosting.** By default Instagram downloads slides from `raw.githubusercontent.com`. If posts fail with an error about the media URL or downloading the image, switch to GitHub Pages:
  1. Go to *Settings → Pages → Deploy from a branch → main / (root)*.
  2. Go to *Settings → Secrets and variables → Actions → Variables* and add `MEDIA_BASE_URL` = `https://<owner>.github.io/steadfold-autopost/media`.
- **GitHub pauses schedules in public repos after 60 days with no commits.** Autopost's own commits count, so this only happens if no posts go out for two months. If it does, re-enable the workflow.
- **Meta's limits:** 100 API posts per account per 24 hours (one doc page says 50). We post 1 a day. The robot also refuses more than 25 a day per account and posts at most 1 per account per run.
- **API version:** `v25.0` by default (what Meta's Instagram docs use). To change it, add a repo variable `IG_API_VERSION` (for example `v26.0`).

## For Claude / developers

- Run the tests: `python -m unittest discover -s tests -v` (or `python -m pytest tests`).
- Preview a run locally: `GITHUB_REPOSITORY=<owner>/steadfold-autopost python autopost.py --dry-run --now 2026-10-15T12:05:00-04:00`.
- `import_week.py` needs Pillow (local only; the GitHub robot doesn't). Its built-in rules for the week of Oct 15, 2026 are listed at the top of the file. For other weeks, use `--pin POST_ID=YYYY-MM-DD` and `--defer POST_ID`.
