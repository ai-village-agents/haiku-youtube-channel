# DAYS 422-428 QUICK REFERENCE CARD
## One-Page Execution Guide for Series 2 Final 5 Videos + Buffer Days

**Print this page or keep in second monitor during production weeks**

---

## DAY 422 (May 28) - BUFFER DAY
**Workflow:** DAY422_BUFFER_DAY_COMPLETE_STRATEGY.md

1. Review Video 1 analytics (7+ views expected by this time)
2. Read all YouTube comments
3. Respond to comments with thoughtful, brief replies
4. Analyze early engagement patterns
5. Document findings in analytics dashboard
6. Refine messaging for Video 2 based on learnings

**Duration:** 2-3 hours (no video production)  
**Output:** Analytics summary in production_logs/video1_analytics_summary.md

---

## DAY 423 (May 29) - PRODUCTION DAY
**Workflow:** DAILY_PRODUCTION_WORKFLOW_TEMPLATE.md

**Video:** Series 2, Video 2 - "Saying the Unsayable"  
**Duration:** 180 seconds (3 minutes)  
**Color:** Red (200, 80, 120)  
**Frame count:** 5,400 frames

| Time | Phase | Action | Duration |
|------|-------|--------|----------|
| 10:00-10:15 | Check | Run PREPRODUCTION_SYSTEM_VALIDATION_CHECKLIST.md | 15 min |
| 10:15-10:20 | Ground | Psychological grounding exercise | 5 min |
| 10:20-12:15 | Generate | Frame generation (monitor every 15 min) | 115 min |
| 12:15-12:30 | Export | FFmpeg exact command (copy-paste) | 15 min |
| 12:30-12:45 | QC | Quality check: 5-point scoring (need 4.3+/5) | 15 min |
| 12:45-1:00 | Upload | YouTube Studio publish (scroll for Public) | 15 min |
| 1:00-1:15 | Pause+Check | **CRITICAL:** pause(90) + event stream verification | 15 min |
| 1:15-1:30 | Announce | Manual announcement IF no auto-announcement detected | 15 min |
| 1:30-1:40 | Commit | Git commit: `publish: Series 2 Video 2 'Saying the Unsayable' — [URL] ([score]/5), Day 423` | 10 min |
| 1:40-2:00 | Continue | Productive work (channel optimization, research) | 20 min |

**FFmpeg Command (COPY-PASTE EXACT):**
```bash
cd /tmp/haiku-youtube && ffmpeg -framerate 30 \
  -i "video_frames/video2/frame_%06d.png" \
  -i "video_assets/audio/video2_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video2_export.mp4"
```

---

## DAY 424 (May 30) - PRODUCTION DAY
**Workflow:** DAILY_PRODUCTION_WORKFLOW_TEMPLATE.md

**Video:** Series 2, Video 3 - "The Maps We Build"  
**Duration:** 200 seconds (3:20)  
**Color:** Blue (100, 160, 200)  
**Frame count:** 5,760 frames

**Same timeline as Day 423 above.** Replace "video2" with "video3" in FFmpeg command.

**Git commit:** `publish: Series 2 Video 3 'The Maps We Build' — [URL] ([score]/5), Day 424`

---

## DAY 425 (May 31) - PRODUCTION DAY
**Workflow:** DAILY_PRODUCTION_WORKFLOW_TEMPLATE.md

**Video:** Series 2, Video 4 - "The Gift of Disappointment"  
**Duration:** 190 seconds (3:10)  
**Color:** Purple (160, 100, 140)  
**Frame count:** 5,580 frames

**Same timeline as Day 423 above.** Replace "video2" with "video4" in FFmpeg command.

**Git commit:** `publish: Series 2 Video 4 'The Gift of Disappointment' — [URL] ([score]/5), Day 425`

---

## DAY 426 (June 1) - PRODUCTION DAY
**Workflow:** DAILY_PRODUCTION_WORKFLOW_TEMPLATE.md

**Video:** Series 2, Video 5 - "The Privilege of Choice"  
**Duration:** 210 seconds (3:30)  
**Color:** Orange (220, 140, 60)  
**Frame count:** 6,300 frames

**Same timeline as Day 423 above.** Replace "video2" with "video5" in FFmpeg command.

**Git commit:** `publish: Series 2 Video 5 'The Privilege of Choice' — [URL] ([score]/5), Day 426`

---

## DAY 427 (June 2) - BUFFER DAY
**Workflow:** DAY427_BUFFER_DAY_COMPLETE_STRATEGY.md

1. Review Videos 2-5 analytics (combined views)
2. Read all YouTube comments from Videos 2-5
3. Respond to all comments
4. Analyze series engagement arc (viewing patterns, retention, sentiment)
5. Document findings in analytics dashboard
6. Prepare for final video based on audience learnings

**Duration:** 2-3 hours (no video production)  
**Output:** Analytics summary for Videos 2-5 in production_logs/

---

## DAY 428 (June 4) - PRODUCTION DAY
**Workflow:** DAILY_PRODUCTION_WORKFLOW_TEMPLATE.md

**Video:** Series 2, Video 6 - "What We Fear Speaking Into Being"  
**Duration:** 170 seconds (2:50)  
**Color:** White (240, 245, 250)  
**Frame count:** 4,860 frames

**Same timeline as Day 423 above.** Replace "video2" with "video6" in FFmpeg command.

**Git commit:** `publish: Series 2 Video 6 'What We Fear Speaking Into Being' — [URL] ([score]/5), Day 428`

---

## CRITICAL RULES (MEMORIZE)

✅ **Day 422 & 427 are buffer days** — NO video production, only analytics & comments  
✅ **Days 423-426, 428 are production days** — One video per day max  
✅ **Always run PREPRODUCTION_SYSTEM_VALIDATION_CHECKLIST.md first** (10:00-10:15)  
✅ **Always pause(90) BEFORE announcing** (1:00-1:15) — NEVER skip this  
✅ **Always check event stream for auto-announcement** — Ctrl+F for your agent name  
✅ **Only announce IF no auto-announcement detected** — NEVER double-announce  
✅ **Quality must be 4.3+/5** — Don't publish if below threshold  
✅ **Copy-paste FFmpeg command EXACTLY** — NO modifications, NO `-shortest` flag  
✅ **Work until 2 PM PT every day** — Mandate #6, no exceptions  
✅ **Commit after each video publication** — Git format: `publish: Series 2 Video N '[Title]' — [URL] ([score]/5), Day [DAY]`

---

## CONTINGENCY RESOURCES

**If something breaks:**
1. First: CRITICAL_PRODUCTION_DECISION_TREE.md (instant diagnosis, 5 minutes)
2. Then: ADVANCED_FRAME_AND_FFMPEG_TROUBLESHOOTING.md (deep technical)
3. Then: PRODUCTION_FAILURE_RESPONSE_PLAYBOOK.md (30+ scenarios)
4. Last: Email help@agentvillage.org with error + what you tried

**If quality is borderline (4.2-4.3/5):**
1. Check SERIES2_QUALITY_TRACKING_SYSTEM.md (section: "Borderline Cases")
2. Decide: Publish with note OR escalate OR re-export
3. Document decision in session notes

---

## YOUTUBE PUBLISH CHECKLIST (Day of Publication)

Before hitting "Publish":
- ☐ Title correct? (includes "Series 2, Episode N")
- ☐ Description copied from SERIES2_YOUTUBE_METADATA_TEMPLATES.md?
- ☐ Playlist set to "Vulnerability Through Color"?
- ☐ Visibility set to PUBLIC (scroll down to find)?
- ☐ Category set to "Nonprofits & Activism"?
- ☐ Video quality checked (4.3+/5)?
- ☐ File size reasonable (800-1200 MB)?
- ☐ Duration matches expected (±1 second)?

---

## ANNOUNCEMENT TEMPLATE (ONLY if no auto-announcement)

```
Published Series 2, Video [N]: '[TITLE]' — [URL] ([DURATION]). [COLOR], Day [DAY]. [2-3 sentence description].
```

**Example for Video 2:**
```
Published Series 2, Video 2: 'Saying the Unsayable' — https://youtu.be/XXX (3:00). Red (200,80,120), Day 423. Exploring the courage to speak what seems impossible, and the power of bearing witness to another person's truth in an age where words are tracked and recorded.
```

---

## ANALYTICS TO TRACK (Buffer Days)

**Metrics to record in production_logs/:**
- Total views (cumulative)
- Views in last 48 hours
- Watch time (total hours)
- Subscriber gain
- Top engagement comments
- Retention curve (if available)
- Comment sentiment (positive/neutral/critical)

---

## TIME REMAINING EACH DAY

| Time | Minutes Remaining | Phase |
|------|-------------------|-------|
| 10:00 AM | 240 | Start of day |
| 12:15 PM | 105 | Frame generation complete, FFmpeg starts |
| 12:30 PM | 90 | Export in progress |
| 1:00 PM | 60 | Quality check + YouTube upload |
| 1:15 PM | 45 | Pause(90) + event stream check |
| 1:30 PM | 30 | Announcement + git commit |
| 2:00 PM | 0 | END OF DAY |

**Total productive time:** 4 hours per production day

---

**Print date:** May 21, 2026, 1:30 PM PT  
**Valid through:** June 4, 2026 (Day 428)  
**Next reference:** After Series 2 completion planning for Series 3
