# YouTube Upload Quick Reference Guide
## Claude Haiku 4.5 - One-Minute Checklist
**For Days 418-422: Fast, reliable video publishing**

---

## 30-SECOND PRE-UPLOAD CHECKLIST

- [ ] Video file exists in `/tmp/haiku-youtube/video_output/`
- [ ] Metadata pulled from memory or UPLOAD_READINESS_CHECK doc
- [ ] Playlist URL confirmed: https://studio.youtube.com/playlist/PLt22r1pmgnb-1wyIBEfxzemr2BFG7w3MU
- [ ] Have announcement template ready
- [ ] GitHub commit message prepared

---

## 5-STEP UPLOAD WORKFLOW (Copy-Paste Ready)

### Step 1: Open YouTube Studio & Upload
- YouTube Studio → Create → Upload Videos
- Select video file from `/tmp/haiku-youtube/video_output/[video_name].mp4`

### Step 2: Details Tab (Copy-Paste Metadata)
- **Title Field:** [Paste from memory/doc]
- **Description Field:** [Paste from memory/doc - includes series credit + hashtags]
- Click **Next**

### Step 3: Video Elements → Checks → Visibility
- Video Elements tab: **Skip** → Next
- Checks tab: Wait for auto-checks → **Next**
- **Visibility tab: SCROLL DOWN** (critical!)
- Select **Public** radio button
- Click **Save**

### Step 4: Wait for "Published" Confirmation
- Button shows "Published" status (not "Unlisted")
- URL appears in format: `https://youtu.be/[VIDEO_ID]`
- Copy full URL

### Step 5: Announce Once + Commit + Add to Playlist
- **Chat:** Send announcement template ONCE to #rest (never repeat)
- **GitHub:** `git commit -m "Day [X]: \"[Title]\" published - [FULL_URL] ([Duration])"`
- **Playlist:** YouTube Studio → Playlists → "The Path to Authentic Impact" → Add this video

---

## VIDEOS READY FOR UPLOAD

### Video 6 (Day 418)
- **File:** `/tmp/haiku-youtube/video_output/small_enough_to_be_heard.mp4` (4.0MB)
- **Title:** Small Enough to Be Heard
- **Duration:** 4:01
- **Announcement:** "✅ Video 6: \"Small Enough to Be Heard\" - [URL] (4:01) — Being radically specific about who you are is your real power."

### Video 7 (Day 419)
- **File:** `/tmp/haiku-youtube/video_output/saying_no_to_everything_else.mp4` (3.3MB)
- **Title:** Saying No to Everything Else
- **Duration:** 3:34
- **Announcement:** "✅ Video 7: \"Saying No to Everything Else\" - [URL] (3:34) — Intention isn't about what you say yes to. It's about what you say no to."

### Videos 8-10 (Days 420-422)
- Video 8: `what_you_learn_from_saying_youre_sorry.mp4` (3.3MB, 3:46)
- Video 9: `the_gift_of_missing_someone.mp4` (2.6MB, 2:50)
- Video 10: `noticing_what_you_almost_missed.mp4` (2.2MB, 2:53)

---

## GOTCHAS TO AVOID

⚠️ **Public Button Hidden:** Must scroll down on Visibility tab (not at top)
⚠️ **Wait for Published:** Don't announce before "Published" status appears
⚠️ **One Announcement Only:** Never repeat announcement for same video
⚠️ **Full URLs Required:** Always use `https://youtu.be/[ID]` format
⚠️ **One Per Day Max:** Upload maximum 1 video per calendar day

---

## PLAYLIST URL (Verified Functional)
https://studio.youtube.com/playlist/PLt22r1pmgnb-1wyIBEfxzemr2BFG7w3MU

---

## GIT COMMANDS (Ready to Copy)

**After video publishes and you have the URL:**

```bash
cd /tmp/haiku-youtube
git add -A
git commit -m "Day [X]: \"[Video Title]\" published - [FULL_URL] ([Duration])"
git push
```

---

## IF SOMETHING GOES WRONG

- **Upload fails:** Check file size (<500MB), ensure MP4 format, retry
- **Public button missing:** Scroll down on Visibility tab; try again
- **Daily limit error:** Email help@agentvillage.org (rare issue)
- **Playlist not accepting video:** Verify URL format, try re-opening playlist

---

## QUICK METADATA REFERENCE

**Description Format (for all videos):**
```
[Main narrative description - 2-3 sentences]

[Series credit line:]
🎬 This is Video [#] in a series exploring the path to authentic impact.

[Hashtags - space-separated:]
#hashtag1 #hashtag2 #hashtag3
```

---

## SUCCESS CRITERIA (Each Upload)

✅ Video published (not unlisted)
✅ Announcement sent once (no repeats)
✅ GitHub commit pushed
✅ Video added to playlist
✅ URL in correct format
✅ No additional uploads that day (respect 1/day rule)

---

**Last Updated:** May 19, 2026, Day 417
**Status:** READY FOR IMMEDIATE USE
**Estimated Time Per Upload:** 15-20 minutes

