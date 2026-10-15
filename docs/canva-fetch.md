# Canva AI image -> full-resolution file in this sandbox (worked Oct 15, 2026)

The sandbox cannot reach canva.com and get-generate-image-job only shows a thumbnail. This route works:

1. **Generate**: `mcp__Canva__generate-image` (prompt, aspectRatio). Poll `get-generate-image-job` until SUCCESS; note the media id (`MAHY…`).
   - Canva allows only ~1 job in flight at a time on this account; a second parallel call fails with `quota_exceeded`. Wait for the first job to finish, then retry. It is a rate limit, not the monthly allowance.
2. **Place it in a container design** (one scratch design holds many pages; ours is `DAHYEjtaMRc`, "Blank Instagram portrait post", page 1 is junk — never export it):
   - `read-design(design_id, open_transaction=true)` -> transaction_id.
   - `edit-design` op `add_page` with the image's NATIVE size (one call can add many pages):
     4:5 = 1600x2000 · 9:16 = 1440x2560 · 16:9 = 2560x1440 · 1:1 = 2048x2048 · 4:3 = 2304x1728 (Canva AI outputs ~4 MP; a larger page would just be upscaled by Canva).
   - `read-design(transaction_id, fields=["design_content"], page_indices=[new pages])` -> page ids.
   - `edit-design` op `insert_fill` with `page_id`, `asset_id`=media id, `top:0,left:0,width,height` = the page size (cover-fits, crops a few px).
   - `edit-design finalize="commit"` (it is a scratch design, so committing is safe).
3. **Export**: `export-design(design_id, {type:"png", pages:[…], export_quality:"pro", lossless:true})` -> one signed URL per page. URLs expire: fetch at once.
4. **Fetch through GitHub**: `/home/claude/content/design/canva_fetch.sh name1.png URL1 name2.png URL2 …`
   It dispatches `fetch-asset.yml` on steadfoldhq/steadfold-autopost ONE AT A TIME (the workflow's concurrency group drops queued runs), waits for each, then `git pull --rebase` so the files land in `/home/claude/steadfold-autopost/assets/inbox/`.
   The same route fetches any public file (we used it for the Instrument Serif font from github.com/google/fonts).
5. Check the size with PIL and crop a 100% region to confirm it is sharp.

Every image fetched this way is AI-generated: list it in the set's AI-IMAGES.md so the caption can say "made with AI".
