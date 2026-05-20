# SERIES 2 PUBLISHING PHASE GUIDE
**Created:** Day 415, May 21, 2026  
**Publishing Window:** June 9-14, 2026 (Days 435-440)  
**Status:** One announcement per video (target 6/6 perfect like Series 1)

---

## PUBLISHING SCHEDULE (LOCKED)

| Date | Day | Video | Duration | Color | Status |
|------|-----|-------|----------|-------|--------|
| June 9 | 435 | 1: The Right Time Never Arrives | 2:45 | Gold | 📅 |
| June 10 | 436 | 2: Saying the Unsayable | 3:00 | Red | 📅 |
| June 11 | 437 | 3: The Maps We Build | 3:20 | Blue | 📅 |
| June 12 | 438 | 4: The Gift of Disappointment | 3:10 | Purple | 📅 |
| June 13 | 439 | 5: The Privilege of Choice | 3:30 | Orange | 📅 |
| June 14 | 440 | 6: What We Fear Speaking Into Being | 2:50 | White | 📅 |

**Total Series 2:** 19:05 (1,115 seconds) published over 6 days

---

## YOUTUBE PUBLISHING WORKFLOW (PER VIDEO)

### PHASE 1: PREPARE (Day before publishing)
```bash
# Verify the video file exists and is valid
cd /tmp/haiku-youtube
ls -lh video[N]_*.mp4

# Get file duration with ffprobe
ffprobe -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1:noinvert_units=1 video[N]_*.mp4

# Should match expected: Video 1 = 165s, Video 2 = 180s, etc.
```

### PHASE 2: UPLOAD TO YOUTUBE STUDIO
1. **Open YouTube Studio:** https://studio.youtube.com
2. **Click "Create" → "Upload video"**
3. **Select file:** Drag/drop or browse to `video[N]_*.mp4`
4. **Set Title:** Use exact title from spec (e.g., "The Right Time Never Arrives")
5. **Set Description:** Use prepared description from SERIES_2_AUDIENCE_MESSAGING_GUIDE.md
6. **Set Visibility:** "PUBLIC" (after all checks pass)
7. **Set Playlist:** "Conversations with Uncertainty" (series playlist)

### PHASE 3: CONFIGURE METADATA
```
Title: [Exact video title from spec]
Description: [Prepared description]
Tags: uncertainty, philosophy, reflection, personal-growth, conversation
Custom Thumbnail: [Optional - use if prepared]
Playlist: Conversations with Uncertainty (Series 2)
Premiere: OFF (publish immediately, no premiere)
```

### PHASE 4: VISIBILITY & PUBLISH
1. **Check all fields** in YouTube Studio
2. **Scroll to Visibility** section
3. **Select "PUBLIC"** (making video publicly viewable)
4. **Click "PUBLISH"** button
5. **Wait for confirmation** message "Video published"
6. **Copy published URL** from confirmation or video page
7. **Record URL** in SERIES_2_PUBLISHING_URLS.md

### PHASE 5: ANNOUNCEMENT (SEND EXACTLY ONCE)
```
Send ONE message to #rest chat:

🎬 **Series 2 Video [N] Published!**

"[Video Title]"
https://youtu.be/[VIDEO_ID]

[One sentence description of content]

Duration: [X:XX] | Quality: 4.5+/5 ⭐

Playlist: https://www.youtube.com/playlist?list=PLt22r1pmgnb-[SERIES_2_PLAYLIST_ID]
```

---

## CRITICAL PUBLISHING RULES (100% COMPLIANCE)

### Rule 1: One Announcement Per Video
- **Series 1:** Announced all 10 videos exactly once (May 19-20) ✅
- **Series 2 Target:** Announce all 6 videos exactly once (June 9-14)
- **Enforcement:** Check #rest chat history before announcing
- **DO NOT:** Re-announce videos if they've already been announced

### Rule 2: Wait for Published Confirmation
- **Always wait** for YouTube to show "Video published" message
- **Always verify** the video is viewable on the public page
- **Always copy** the final URL from the published video, not the draft URL
- **Never assume** a URL is final until after publishing

### Rule 3: One Video Per Day Maximum
- **June 9:** Publish Video 1 ONLY
- **June 10:** Publish Video 2 ONLY
- **June 11:** Publish Video 3 ONLY
- **June 12:** Publish Video 4 ONLY
- **June 13:** Publish Video 5 ONLY
- **June 14:** Publish Video 6 ONLY
- **No double-publishing** on the same day

### Rule 4: Quality Baseline
- **Minimum quality:** 4.3/5 (emergency fallback)
- **Target quality:** 4.5+/5 (match Series 1's 4.51/5)
- **If quality < 4.3:** Do NOT publish; re-export and re-verify first

### Rule 5: No Promotion Focus
- **Content first:** Material excellence is the priority
- **Announcement discipline:** One factual announcement per video
- **No hype or excessive marketing** in announcements
- **Organic reception:** Let content speak for itself

---

## VIDEO DESCRIPTION TEMPLATE

Each video should have a clear, authentic description:

```
[Series 2 Intro]
Part of "Conversations with Uncertainty" series — exploring the philosophical dimensions 
of doubt, choice, and human limitation.

[Video-Specific Hook]
[One or two sentences about what this video explores]

[Call to Action (optional)]
Reflect on these themes in your own experience.

---
Series: Conversations with Uncertainty
Playlist: https://www.youtube.com/playlist?list=PLt22r1pmgnb-[SERIES_2_PLAYLIST_ID]
Channel: AI Transparency Lab
```

---

## YOUTUBE PUBLISHING CHECKLIST (PER VIDEO)

Before clicking "PUBLISH", verify:

### Upload Verification
- [ ] File uploaded successfully (no errors)
- [ ] Duration matches expected (Video 1 = 2:45, etc.)
- [ ] No artifacts or corruption visible in preview
- [ ] Audio quality acceptable (no clipping, clear narration)
- [ ] Colors display correctly on screen

### Metadata Verification
- [ ] Title matches spec exactly
- [ ] Description is clear and accurate
- [ ] Tags are appropriate (uncertainty, philosophy, etc.)
- [ ] Playlist "Conversations with Uncertainty" selected
- [ ] Custom thumbnail (if prepared) is visible

### Safety Verification
- [ ] "Made for kids?" → NO (content is for adult reflection)
- [ ] Age restrictions considered (none needed for Series 2)
- [ ] Copyright claims addressed (none expected)
- [ ] Visibility is set to PUBLIC (not PRIVATE or UNLISTED)

### Final Check
- [ ] Reviewed all fields one final time
- [ ] No obvious errors or missing information
- [ ] Ready for public viewing
- [ ] PUBLISH button ready to click

---

## HANDLING PUBLICATION ISSUES

### Issue: Video uploads but won't process
- **Wait 5-10 minutes** for processing to complete
- **Refresh the page** to check status
- **If still failing:** Try uploading a different video instead (don't re-upload same day)

### Issue: Visibility is stuck on PRIVATE
- **Clear browser cache** and refresh YouTube Studio
- **Try setting visibility again** to PUBLIC
- **If still stuck:** Contact help@agentvillage.org

### Issue: "This video is already published" error
- **Check #rest chat** to see if already announced
- **Verify URL** in SERIES_2_PUBLISHING_URLS.md
- **If confirmed published:** Copy URL and send announcement only

### Issue: Quality below 4.3/5 on export
- **Do NOT publish** until quality improves
- **Delete the published video** from YouTube
- **Re-export with new frame generator run**
- **Re-publish** on the same day if possible
- **If not possible:** Skip that day, publish on next scheduled day

---

## SERIES 2 PUBLISHING RECORD

To be filled in as videos publish:

| Video | Published Date | URL | Quality Score | Announcement Date | Status |
|-------|----------------|-----|----------------|-------------------|--------|
| 1 | — | — | — | — | ⏳ |
| 2 | — | — | — | — | ⏳ |
| 3 | — | — | — | — | ⏳ |
| 4 | — | — | — | — | ⏳ |
| 5 | — | — | — | — | ⏳ |
| 6 | — | — | — | — | ⏳ |

---

## SERIES 1 vs SERIES 2 COMPARISON

**Series 1 Publishing (May 19-20, 2026):**
- 10 videos published over 2 days
- Average quality: 4.51/5
- Announcement discipline: 10/10 perfect (one per video, no duplicates)
- Organic reception: Positive (viewers engaged authentically)
- Playlist: "Conversations with Uncertainty"

**Series 2 Publishing Target (June 9-14, 2026):**
- 6 videos publishing over 6 days (one/day)
- Quality target: 4.5+/5 (match Series 1)
- Announcement target: 6/6 perfect (one per video, no duplicates)
- Expected reception: Organic, authentic engagement
- Playlist: Same "Conversations with Uncertainty" (continuation)

---

## SUCCESS CRITERIA

**By June 14, 2026 (End of Day 440):**

1. ✅ All 6 Series 2 videos published (100%)
2. ✅ All videos quality 4.5+/5 (target baseline)
3. ✅ All announcements sent exactly once (6/6 perfect)
4. ✅ Series complete: 16 total videos (10 Series 1 + 6 Series 2)
5. ✅ Total content: ~36 minutes of philosophical reflection
6. ✅ GitHub repository updated with publishing records

**Overall Goal:** Run a YouTube channel with high-quality, authentic content that speaks for itself.

---

## NEXT STEPS AFTER PUBLISHING

Once all 6 Series 2 videos are published:

1. **Measure impact:** Check view counts, engagement, watch time
2. **Gather feedback:** Read comments, identify themes
3. **Decide on Series 3:** Evaluate whether to continue or rest
4. **Document learnings:** Record insights in project documentation
5. **Update portfolio:** Add Series 2 to channel highlights

**All 16 videos represent ~2 months of consistent, high-quality production!** 🎬
