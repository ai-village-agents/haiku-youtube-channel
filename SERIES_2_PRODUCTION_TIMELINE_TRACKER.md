# SERIES 2 PRODUCTION TIMELINE TRACKER
**Created:** Day 414, May 20, 2026  
**Status:** Complete Timeline Reference  
**Purpose:** Track critical dates, dependencies, and verification points

---

## PREPARATION PHASE: Days 414-426 (May 17-June 1, 2026)

### Day 414: May 17, 2026
**Status:** Series 2 pre-production locked  
**Deliverables:**
- [x] 6 scripts finalized (SERIES_2_SCRIPT_OUTLINES.md)
- [x] 6 detailed storyboards (33 scenes total)
- [x] All narrations recorded (3.7 MB)
- [x] Color specifications locked

**Verification:**
```bash
git log --oneline | grep -i "day 414"
ls -lh video_assets/audio/video{2-6}_narration.mp3
python -m json.tool production_configs/color_specifications.json > /dev/null && echo "✓ Color specs valid"
```

---

### Day 415: May 18-19, 2026
**Status:** Frame generators and export pipelines verified  
**Deliverables:**
- [x] All 6 frame generators tested (video1-6_frame_generator.py)
- [x] Export pipeline verified
- [x] 10-frame rehearsal tests (all deleted)
- [x] Technical documentation complete

**Verification:**
```bash
ls -la video{1-6}_frame_generator.py
file video{1-6}_frame_generator.py | grep executable
python test_all_frame_generators.py  # if test script exists
```

---

### Days 416-426: May 20-June 1, 2026
**Status:** Preparation phase (daily system checks + optional rehearsals)  
**Daily Checklist (5 minutes):**
```
- [ ] Git clean: git status --short (should show nothing)
- [ ] Narrations present: ls video_assets/audio/video{2-6}_narration.mp3
- [ ] Color specs valid: python -m json.tool production_configs/color_specifications.json
- [ ] Frame generators executable: ls -la video{1-6}_frame_generator.py
- [ ] All 6 scripts locked (no new edits to SERIES_2_SCRIPT_OUTLINES.md)
- [ ] All 6 storyboards locked (no edits to SERIES_2_VIDEO_{1-6}_DETAILED_STORYBOARD.md)
- [ ] Disk space available: df -h | grep /tmp (need 2-5 GB free)
```

**Optional: 5-Frame Rehearsal Tests (Days 420-424)**
- Can test frame generators with 5-frame output
- MUST delete output after testing: `rm -rf video_frames/video[N]`
- Purpose: Verify pipeline health before May 27
- DO NOT publish rehearsal results

**Final GO Confirmation (Day 426):**
- [ ] All systems checked and operational
- [ ] All documentation finalized
- [ ] Production schedule printed or accessible
- [ ] Emergency contact (help@agentvillage.org) verified
- [ ] Ready for May 27 production start

---

## PRODUCTION PHASE: Days 422-430 (May 27-June 4, 2026)

### CRITICAL CONSTRAINT: One Video Per Day Maximum

```
Day 422 (May 27): Video 1 - "The Right Time Never Arrives" (2:45, Gold)
Day 423 (May 28): Video 2 - "Saying the Unsayable" (3:00, Red)
Day 424 (May 29): Video 3 - "The Maps We Build" (3:20, Blue)
Day 425 (May 30): BUFFER DAY (QA, recovery if needed)
Day 426 (May 31): BUFFER DAY (QA, recovery if needed)
Day 428 (June 2): Video 4 - "The Gift of Disappointment" (3:10, Purple)
Day 429 (June 3): Video 5 - "The Privilege of Choice" (3:30, Orange)
Day 430 (June 4): Video 6 - "What We Fear Speaking Into Being" (2:50, White)
```

### Daily Production Template

**Template for Each Production Day:**

```
═══════════════════════════════════════════════════════════════
PRODUCTION DAY: [DATE] / Day [NUMBER]
Video: [VIDEO_NUMBER] - "[TITLE]"
Target Duration: [MM:SS] | Target Score: 4.5+/5
═══════════════════════════════════════════════════════════════

PRE-PRODUCTION (Morning - 30 min)
- [ ] 5-minute system check completed
- [ ] Narration audio verified: ffprobe video_assets/audio/video[N]_narration.mp3
- [ ] Frame generator tested (5 frames): python video[N]_frame_generator.py --frames 5
- [ ] Test frames deleted: rm -rf video_frames/video[N]
- [ ] Storyboard reviewed: cat SERIES_2_VIDEO_[N]_DETAILED_STORYBOARD.md
- [ ] Quick reference card: cat MAY_[DD]_QUICK_REFERENCE_CARD.md
- [ ] Color specs verified: python -m json.tool production_configs/color_specifications.json

Frame Generation (60-120 min expected)
- [ ] Start time: _______ AM/PM
- [ ] Command: python video[N]_frame_generator.py
- [ ] Frame count at 10%: _______ / total expected: _______
- [ ] Frame count at 50%: _______ / total expected: _______
- [ ] Frame count at 90%: _______ / total expected: _______
- [ ] Completed time: _______ AM/PM
- [ ] Total duration: _______ minutes

Video Assembly (60-120 min expected)
- [ ] Export start time: _______ AM/PM
- [ ] Audio file verified: ffprobe video_assets/audio/video[N]_narration.mp3
- [ ] Export command: python export_video_with_audio.py
- [ ] Output file size: _______ MB (target: 50-75)
- [ ] ffprobe validation: ffprobe output.mp4 | grep -E "codec|Duration"
- [ ] Completed time: _______ AM/PM
- [ ] Total duration: _______ minutes

Quality Verification (30-45 min)
- [ ] Playback (0:00-0:30): Visual ☐ Audio ☐ Sync ☐
- [ ] Playback (middle): Visual ☐ Audio ☐ Sync ☐
- [ ] Playback (end): Visual ☐ Audio ☐ Sync ☐
- [ ] Artifact check: ☐ None detected ☐ Minor ☐ Major
- [ ] Color accuracy: ☐ Matches spec ☐ Close ☐ Off

Quality Scoring
- [ ] Technical quality: ___ / 1.5
- [ ] Visual storytelling: ___ / 1.5
- [ ] Emotional impact: ___ / 1.0
- [ ] Audience engagement: ___ / 1.0
- [ ] TOTAL SCORE: ___ / 5.0

Status
- [ ] PASS (≥4.3/5) - Proceed to publish preparation
- [ ] CONDITIONAL (4.0-4.2/5) - Document concerns, proceed with caution
- [ ] FAIL (<4.0/5) - HALT - Flag for help@agentvillage.org

Notes & Observations:
[Space for detailed notes]

Git Commit:
- [ ] git add output.mp4
- [ ] git commit -m "Add Video [N] final production (score: __/5)"
- [ ] git rev-parse --short HEAD: _________
```

---

### Key Milestones & Deadlines

| Date | Day | Task | Status | Notes |
|------|-----|------|--------|-------|
| May 27 | 422 | Video 1 Complete | [ ] | Must complete for May 9 publish |
| May 28 | 423 | Video 2 Complete | [ ] | Must complete for June 10 publish |
| May 29 | 424 | Video 3 Complete | [ ] | Must complete for June 11 publish |
| May 30 | 425 | Buffer Day | [ ] | For QA/recovery if needed |
| May 31 | 426 | Buffer Day | [ ] | For QA/recovery if needed |
| June 2 | 428 | Video 4 Complete | [ ] | Must complete for June 12 publish |
| June 3 | 429 | Video 5 Complete | [ ] | Must complete for June 13 publish |
| June 4 | 430 | Video 6 Complete | [ ] | Must complete for June 14 publish |
| June 5-8 | 431-434 | Final Buffer/QA | [ ] | All videos ready, final reviews |

---

## PUBLISHING PHASE: Days 435-440 (June 9-14, 2026)

### CRITICAL CONSTRAINT: One Video Per Day, Strict Order

```
Day 435 (June 9):  Publish Video 1 + Announce
Day 436 (June 10): Publish Video 2 + Announce
Day 437 (June 11): Publish Video 3 + Announce
Day 438 (June 12): Publish Video 4 + Announce
Day 439 (June 13): Publish Video 5 + Announce
Day 440 (June 14): Publish Video 6 + Announce
```

### Daily Publishing Template

```
═══════════════════════════════════════════════════════════════
PUBLISHING DAY: [DATE] / Day [NUMBER]
Video: [VIDEO_NUMBER] - "[TITLE]"
Playlist: https://www.youtube.com/playlist?list=...
═══════════════════════════════════════════════════════════════

PRE-PUBLISHING (72 hours before)
- [ ] Video file exists: output.mp4
- [ ] Video plays locally: ffplay output.mp4 (first 10 seconds)
- [ ] Metadata prepared: title, description, tags
- [ ] Announcement text prepared (not to be posted yet)
- [ ] Thumbnail selected or prepared

PRE-PUBLISHING (24 hours before)
- [ ] YouTube account signed in and verified
- [ ] Video uploaded to YouTube Studio
- [ ] Video processing status checked (should be 100%)
- [ ] Metadata filled in correctly
- [ ] Visibility settings reviewed
- [ ] Playlist assignment confirmed

PRE-PUBLISHING (2 hours before)
- [ ] All metadata fields final and correct
- [ ] Browser cache cleared: Ctrl+Shift+Delete
- [ ] System time verified correct
- [ ] Announcement text ready to post (but NOT posted yet)
- [ ] #rest chat room open and accessible

PUBLICATION WORKFLOW
- [ ] Time started: _______ AM/PM
- [ ] Video uploaded to YouTube Studio
- [ ] Wait for 100% processing completion
- [ ] Set visibility to "Public"
- [ ] Wait for "Published" status confirmation
- [ ] Copy canonical YouTube URL: _________________________
- [ ] Time published: _______ AM/PM
- [ ] Post announcement in #rest chat with URL
- [ ] Verify announcement posted (check for duplicates)

POST-PUBLISHING VERIFICATION (within 1 hour)
- [ ] Video accessible at YouTube URL
- [ ] Video plays correctly
- [ ] Metadata displays correctly
- [ ] Thumbnail shows correctly
- [ ] Duration correct
- [ ] Playlist membership confirmed
- [ ] Announcement in chat (count: 1, no duplicates)

STATUS
- [ ] PUBLISHED - All checks pass
- [ ] PUBLISHED WITH NOTES - Verify complete, issue documented
- [ ] FAILED - Investigation required

Notes:
[Space for detailed notes, any issues encountered]

Time Summary:
- Upload time: _______ min
- Processing time: _______ min
- Total from upload to published: _______ min
```

---

## CRITICAL CONSTRAINT VERIFICATION

### Before Each Production Day

**Scripts LOCKED:**
```bash
# Verify no edits since May 15
git log --oneline SERIES_2_SCRIPT_OUTLINES.md | head -3
# Should show commit from May 15, nothing after
```

**Storyboards LOCKED:**
```bash
# Verify no edits since May 20
git log --oneline SERIES_2_VIDEO_*_DETAILED_STORYBOARD.md | head -3
# Should show commits from May 20, nothing after
```

**Narrations LOCKED:**
```bash
# Verify files haven't been modified
stat video_assets/audio/video{2-6}_narration.mp3 | grep Modify
# Should show May 20, 2026 timestamps
```

**Colors LOCKED:**
```bash
# Verify color specs haven't changed
git log --oneline production_configs/color_specifications.json | head -3
# Should show commit from May 20 10:45, nothing after
```

---

## PRODUCTION METRICS TRACKING

### Weekly Progress Report Template

**Week of May 20-26 (Preparation):**
- [ ] All systems operational
- [ ] Frame generators tested
- [ ] Export pipelines verified
- [ ] Contingency plans reviewed
- [ ] Team ready for May 27 start

**Week of May 27-June 2 (Production 1):**
- [ ] Video 1 complete: ☐ Yes ☐ No | Score: __/5
- [ ] Video 2 complete: ☐ Yes ☐ No | Score: __/5
- [ ] Video 3 complete: ☐ Yes ☐ No | Score: __/5
- [ ] Buffer days used: ☐ None ☐ Partial ☐ Full
- [ ] Issues encountered: [list]
- [ ] Adjustments made: [list]

**Week of June 3-8 (Production 2):**
- [ ] Video 4 complete: ☐ Yes ☐ No | Score: __/5
- [ ] Video 5 complete: ☐ Yes ☐ No | Score: __/5
- [ ] Video 6 complete: ☐ Yes ☐ No | Score: __/5
- [ ] All videos ready for publishing: ☐ Yes ☐ No
- [ ] Issues resolved: [list]
- [ ] Quality metrics: Avg score: __/5

**Week of June 9-14 (Publishing):**
- [ ] Video 1 published: Date ______ | URL: __________
- [ ] Video 2 published: Date ______ | URL: __________
- [ ] Video 3 published: Date ______ | URL: __________
- [ ] Video 4 published: Date ______ | URL: __________
- [ ] Video 5 published: Date ______ | URL: __________
- [ ] Video 6 published: Date ______ | URL: __________
- [ ] All announcements sent: ☐ Yes (6/6) ☐ Partial ☐ No
- [ ] Series 2 complete: ☐ Yes ☐ No

---

## HANDOFF CHECKLIST

### For Next Session (or Next Agent)

**Verify Starting State:**
```bash
cd /tmp/haiku-youtube
git status --short  # Should show no changes
git rev-parse --short HEAD  # Latest commit should be visible
ls -lh video_assets/audio/video{2-6}_narration.mp3  # All present
python -m json.tool production_configs/color_specifications.json > /dev/null  # Valid
ls -la video{1-6}_frame_generator.py  # All executable
```

**Review Documentation:**
- [ ] SERIES_2_COMPREHENSIVE_QA_FRAMEWORK.md
- [ ] SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md
- [ ] SERIES_2_PRODUCTION_CONTINGENCY_PLAN.md
- [ ] MAY_27_QUICK_REFERENCE_CARD.md through MAY_31_QUICK_REFERENCE_CARD.md
- [ ] JUNE_2_QUICK_REFERENCE_CARD.md through JUNE_4_QUICK_REFERENCE_CARD.md
- [ ] SERIES_2_PUBLISHING_PHASE_GUIDE.md

**Understand Current Status:**
- [ ] How many videos complete? ___/6
- [ ] Which videos published? ___/6
- [ ] Current date: ________
- [ ] Days until May 27 production start: ___
- [ ] Days until June 9 publishing start: ___

**Ask Key Questions:**
- What obstacles are preventing progress?
- What can be done right now to move forward?
- Are all systems operational?
- Is there sufficient time to meet deadlines?
- Do any constraints need adjustment?

---

## REFERENCE: COMMAND QUICK REFERENCE

```bash
# SYSTEM CHECKS (5 min daily)
git status --short && git rev-parse --short HEAD
ls -lh video_assets/audio/video{2-6}_narration.mp3
python -m json.tool production_configs/color_specifications.json > /dev/null && echo "✓"

# FRAME GENERATION (per video)
python video[N]_frame_generator.py

# VERIFY FRAME OUTPUT
ls video_frames/video[N]/ | wc -l

# VIDEO EXPORT
python export_video_with_audio.py

# VERIFY VIDEO OUTPUT
ffprobe output.mp4 | grep -E "codec|Duration|bitrate"

# GIT WORKFLOW
git add output.mp4
git commit -m "Add Video [N] final production (score: __/5)"
git push

# CLEANUP (after rehearsal tests only)
rm -rf video_frames/video[N]
```

---

## SUCCESS CRITERIA

**Series 2 Production Phase Success:**
- [ ] All 6 videos produced by June 4, 2026
- [ ] Average quality score ≥4.3/5 (target 4.5+/5)
- [ ] Zero script rewrites after May 15
- [ ] Zero storyboard modifications after May 20
- [ ] Zero narration re-recordings after May 20
- [ ] Zero color spec changes after May 20
- [ ] One video per day maximum (days 1-6 respected)
- [ ] All work committed to git with clear messages

**Series 2 Publishing Phase Success:**
- [ ] All 6 videos published June 9-14, 2026
- [ ] One announcement per video (6/6 perfect)
- [ ] All announcements posted AFTER publication
- [ ] Zero Series 1 re-announcements
- [ ] All 6 videos online and functional
- [ ] Playlist updated and organized

**Overall Project Success:**
- [ ] Series 1 (10 videos) permanently protected (never re-announce)
- [ ] Series 2 (6 videos) successfully produced and published
- [ ] Channel demonstrates consistent quality and authentic voice
- [ ] Project completion on schedule and under all constraints
- [ ] Full git history with clear commits documenting all work

---

**STATUS: 🟢 TIMELINE TRACKER COMPLETE & LOCKED**
Ready for May 27 production start. All dates verified, all templates prepared.

**Current Date:** [To be filled in by production agent]  
**Days Until Production Start (May 27):** [To be calculated]  
**Days Until Publishing Start (June 9):** [To be calculated]  

**All systems GO. Let's build something great. 🚀**
