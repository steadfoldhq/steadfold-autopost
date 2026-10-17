# Etsy auto-lister: one-time setup (about 10–15 minutes)

You do this once. After that, say **"list approved"** and every approved listing goes live on Etsy with no browser prompts.

SteadfoldHQ and LittlefoldHQ are two Etsy accounts, because Etsy allows one shop per account. A seller app can only reach its own shop, so you make **one app in each account**. Steps 1 and 3 are done twice, once per shop.

## 1. Register the Etsy app (3 min per shop)

1. Sign in to Etsy as the **SteadfoldHQ** owner. Open https://www.etsy.com/developers, click **Create a seller app**, then **Get started**.
2. Fill in the form:
   - **App name:** `Steadfold Lister`
   - **Why you want to use the API:** `Create and publish listings for my own digital products in my own shop from my own GitHub automation, and read my shop's listings to avoid duplicates. No buyer or order data.`
   - If Etsy asks anything else: Website `https://github.com/steadfoldhq/steadfold-autopost` · Users: only me · Commercial: no.
3. Click **Read Terms and Create App**. Etsy says seller apps are usually approved within minutes. If it shows "pending", wait for the email.
4. Go to https://www.etsy.com/developers/your-apps, open the app, and set the **Callback URL** to exactly the line below, with no slash at the end:
   `https://github.com/steadfoldhq/steadfold-autopost`
5. Keep the page open. You need the **Keystring** and **Shared secret** in step 2.
6. Sign out of Etsy, sign in as the **LittlefoldHQ** owner, and repeat steps 1–5 with app name `Littlefold Lister`.

## 2. Paste the keys into GitHub (2 min, you do this yourself)

Go to GitHub → **steadfoldhq/steadfold-autopost** → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**. Add 4 secrets, one at a time:

| Name | Value |
|---|---|
| `ETSY_KEYSTRING` | SteadfoldHQ app **Keystring** |
| `ETSY_SHARED_SECRET` | SteadfoldHQ app **Shared secret** |
| `ETSY_KEYSTRING_LITTLEFOLD` | LittlefoldHQ app **Keystring** |
| `ETSY_SHARED_SECRET_LITTLEFOLD` | LittlefoldHQ app **Shared secret** |

Paste them only there, never into a chat.

## 3. Connect each shop (2 min per shop)

1. GitHub → **Actions** → **Etsy auth** → **Run workflow**. Set mode **start**, shop **STEADFOLD**, then click **Run workflow**.
2. Open the finished run and click the **Etsy link** in its Summary. Check that Etsy shows SteadfoldHQ, then click **Allow access**.
3. Etsy opens the GitHub repo page. Copy the **whole address** from the browser bar (it contains `?code=`).
4. Right away, go to **Actions** → **Etsy auth** → **Run workflow**. Set mode **finish**, shop **STEADFOLD**, paste the address into **code**, then run it. A green tick means the shop is connected, and the Summary shows the shop name and currency.
5. Sign out of Etsy, sign in as **LittlefoldHQ**, and repeat steps 1–4 with shop **LITTLEFOLD**.

The code works only once. If finish fails, start again from step 1.

## 4. Go

Say **"list approved"** in the Learning Lab chat. An agent then starts the **Etsy list** workflow, which lists the 12 approved items. You can also start it yourself: **Actions** → **Etsy list** → spec `all`, mode `list`.

- **Optional, read-only:** run it first with mode `check`. It shows each listing's currency, category and duplicate check, and creates nothing.
- **Fees:** Etsy charges its normal US$0.20 per listing to the shop's bill (12 listings = US$2.40).

**By hand afterwards** (Etsy's API can't create sales): the CALMLAUNCH sale (25% off both Calm planners, ends 30 Nov 2026) and the RIVERBANKLAUNCH sale (30% off Riverbank Routines, ends 30 Nov 2026). The run's Summary lists them again.

---

Good to know:
- You don't need GitHub Pages. Nothing goes through Etsy review beyond the seller-app approval in step 1.
- The connection lasts 90 days and renews every time the lister runs. After 90 days with no listing runs, repeat step 3.
- If a shop's Etsy name isn't exactly `SteadfoldHQ` / `LittlefoldHQ`, the lister refuses to list, to protect against the wrong account. Fix: Settings → Secrets and variables → Actions → **Variables** → add `ETSY_SHOP_NAME_STEADFOLD` or `ETSY_SHOP_NAME_LITTLEFOLD` with the real name.
