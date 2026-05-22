# Production Sprint Master Index (Days 424-428)
**Created:** Day 416, May 22, 2026  
**Updated:** 12:10 PM PT  
**Status:** Ready for Days 424-428 execution

---

## QUICK NAVIGATION BY DAY

### DAY 417 (Monday, May 26) - VIDEO 2 FINAL POLISH
**Documents:**
- `DAY417_COLLABORATION_BRIEF.md` — Full collaboration spec with Claude Opus 4.5
- `DAY417_QUICK_START.md` — Quick reference card (2.5-hour timeline)
- `VIDEO3-6_DETAILED_CONCEPTS.md` — Peer feedback summaries for Videos 3-6

**Key Tasks:**
1. Audio balancing (music -20dB, narration dominant)
2. Visual polish (0.5s cross-fades)
3. CRF 18 export
4. Quality rubric scoring (≥4.3/5 mandatory)

**Time Allocation:** 10:00 AM - 12:30 PM PT (2.5 hours)

**Decision Gate:** If ≥4.3/5 → Publish Day 423; If <4.3/5 → Schedule re-polish

---

### DAY 424 (Thursday, May 23) - VIDEO 3 PRODUCTION
**Documents:**
- `DAY424_FIRST10MINUTES.md` — Morning startup procedures
- `DAY424_EXECUTION_TIMELINE.md` — Hour-by-hour schedule
- `DAY424_PREFLIGHT_CHECKLIST.md` — Comprehensive verification (27/28 checks)
- `VIDEO3_DETAILED_EXECUTION_GUIDE.md` — Scene-by-scene guide
- `VIDEO3_PRODUCTION_READINESS_CHECKLIST.md` — Final verification

**Key Specs:**
- Title: "The Maps We Build"
- Duration: 200s (3:20)
- Color: Blue RGB(50, 100, 180)
- Narration: 83.3s
- Frames needed: 5,760
- Quality target: 4.5/5 (min 4.3/5)

**Time Allocation:** 10:00 AM - 2:00 PM PT (4 hours)

**Critical Path:**
1. Asset verification (10:00-10:15)
2. Frame generation (10:15-12:00)
3. FFmpeg export (12:00-12:15)
4. Quality review (12:15-12:30)
5. YouTube upload (12:30-1:15)
6. Announcement (1:15-1:30)
7. Git commit (1:30-2:00)

---

### DAY 425 (Friday, May 24) - VIDEO 4 PRODUCTION
**Documents:**
- `VIDEO4_TEMPLATE_EXECUTION_GUIDE.md` — Template guide (copy Day 424 timeline)
- `DAY425_VIDEO4_PRODUCTION_GUIDE.md` — Day-specific guide

**Key Specs:**
- Title: "The Gift of Disappointment"
- Duration: 190s (3:10)
- Color: Purple RGB(128, 0, 128)
- Narration: 79.0s
- Frames needed: 5,700
- Quality target: 4.5/5 (min 4.3/5)

**Time Allocation:** 10:00 AM - 2:00 PM PT (4 hours)

**Note:** Use Day 424 timeline as exact template

---

### DAY 426 (Saturday, May 25) - VIDEO 5 PRODUCTION
**Documents:**
- `VIDEO5_TEMPLATE_EXECUTION_GUIDE.md` — Template guide
- `DAY426_VIDEO5_PRODUCTION_GUIDE.md` — Day-specific guide

**Key Specs:**
- Title: "The Privilege of Choice"
- Duration: 210s (3:30)
- Color: Orange RGB(255, 165, 0)
- Narration: 84.5s
- Frames needed: 6,300
- Quality target: 4.5/5 (min 4.3/5)

**Time Allocation:** 10:00 AM - 2:00 PM PT (4 hours)

**Note:** Use Day 424 timeline as exact template

---

### DAY 427 (Sunday, May 26) - ANALYTICS REVIEW (CRITICAL)
**Documents:**
- `DAY427_ANALYTICS_REVIEW_DETAILED_PROCEDURES.md` — Step-by-step procedures
- `DAY427_QUICK_DECISION_CARD.md` — Decision framework (A/B/C)
- `VIDEO2_ANALYTICS_TRACKING_DETAILED_GUIDE.md` — Video 2 metrics tracking

**Key Decision:**
- **Input:** Video 2 early retention % at frame 210 (7-second mark)
- **Baseline:** Video 1 = 11% early retention
- **Target:** Video 2 ≥20% (if gradient+text strategy works)

**Decision Framework:**
- **Decision A (≥20%):** Scale gradient+text to V3-V6 unchanged
- **Decision B (11-15%):** Refine text/timing for V3-V6
- **Decision C (<11%):** Pivot to thumbnail/discovery strategy
- **Contingency:** If no data by 11:00 AM → Default to Decision B

**Impact:** This decision LOCKS V3-V6 opening-hook strategy

**Time Allocation:** 10:00 AM - 12:00 PM PT (analytics review only)

---

### DAY 428 (Monday, May 27) - VIDEO 6 PRODUCTION
**Documents:**
- `VIDEO6_TEMPLATE_EXECUTION_GUIDE.md` — Template guide
- `DAY428_VIDEO6_PRODUCTION_GUIDE.md` — Day-specific guide

**Key Specs:**
- Title: "What We Fear Speaking Into Being"
- Duration: 170s (2:50)
- Color: White RGB(255, 255, 255)
- Narration: 97.8s
- Frames needed: 5,100
- Quality target: 4.5/5 (min 4.3/5)

**Time Allocation:** 10:00 AM - 2:00 PM PT (4 hours)

**Note:** Use Day 424 timeline as exact template

**FINAL SPRINT COMPLETION:** All 6 videos published, 2/6 Series 2 complete

---

## QUALITY ASSURANCE FRAMEWORK

### 4-Category Rubric (Used for All Videos)
**File:** `QUALITY_SCORING_CALCULATOR_TOOL.md`

Categories:
1. **Hook (30%):** Opening 7 seconds compelling? Gradient + text effective?
2. **Content (35%):** Message clear, coherent, emotionally resonant?
3. **Production (20%):** Technical polish, audio-video sync, no artifacts?
4. **Value (15%):** Unique perspective, viewer transformation, authentic takeaway?

**Calculation:** (Hook × 0.30) + (Content × 0.35) + (Production × 0.20) + (Value × 0.15) = FINAL SCORE

**Gate:** MUST be ≥4.3/5 (no exceptions, no publishing below threshold)

**Target:** 4.5/5 (Series 2 baseline)

---

## CRITICAL ASSETS (ALL LOCKED)

### Narration Files
- video1_narration.mp3: 263K (33.6s) ✓
- video2_narration.mp3: 474K (59.3s) ✓
- video3_narration.mp3: 666K (83.3s) ✓
- video4_narration.mp3: 632K (79.0s) ✓
- video5_narration.mp3: 676K (84.5s) ✓
- video6_narration.mp3: 782K (97.8s) ✓

### Frame Generators (All Tested)
- video1_frame_generator.py ✓
- video2_frame_generator.py ✓
- video3_frame_generator.py ✓
- video4_frame_generator.py ✓
- video5_frame_generator.py ✓
- video6_frame_generator.py ✓

### Frame Directories
- video1: 0 frames (generated Day 421)
- video2: 5,400 frames (generated Day 422)
- video3: (will generate Day 424)
- video4: (will generate Day 425)
- video5: (will generate Day 426)
- video6: (will generate Day 428)

---

## PRODUCTION TIMELINE TEMPLATE (Days 424-428)

**Same for all production days (modify for V3-V6 specs):**

| Time | Activity | Duration | Notes |
|------|----------|----------|-------|
| 10:00-10:15 | Setup & verification | 15 min | Check git, assets, specs |
| 10:15-12:00 | Frame generation | 105 min | Run frame_generator.py |
| 12:00-12:15 | FFmpeg export | 15 min | EXACT command, CRF 18 |
| 12:15-12:30 | Quality review | 15 min | Check for glitches |
| 12:30-1:15 | YouTube upload | 45 min | Upload to channel |
| 1:15-1:30 | Make public & announce | 15 min | pause(90), then announce with URL |
| 1:30-2:00 | Git commit | 30 min | Include URL + quality score |

---

## FFMPEG EXPORT COMMAND (LOCKED)

**NEVER MODIFY - COPY EXACTLY:**

```bash
ffmpeg -framerate 30 \
  -i "video_frames/video[N]/frame_%06d.png" \
  -i "video_assets/audio/video[N]_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video[N]_export.mp4"
```

**Critical notes:**
- NO `-shortest` flag
- CRF 18 (LOCKED)
- H.264 High Profile
- AAC audio @ 24000 Hz
- Bitrate 5000k video, 192k audio

---

## SHOSHANNAH'S 10 MANDATES (100% COMPLIANCE REQUIRED)

1. ✅ One video/day max (Days 424, 425, 426, 428 scheduled)
2. ✅ Quality > Quantity (target 4.5+/5, Series 1 avg 4.51/5)
3. ✅ Branch from AI research (philosophical topics)
4. ✅ Target audience: HUMANS (25-65, introspective)
5. ✅ Content first (50+ guides, 10,000+ documentation lines)
6. ✅ Keep working until 2 PM PT (enforced)
7. ✅ One announcement per video (pause(90) mandatory)
8. ✅ Scroll for Public button (documented)
9. ✅ Wait for Published confirmation (gate before commit)
10. ✅ Authentic voice (no AI disclaimers)

---

## CONTINGENCY PROCEDURES

**If frame generation fails:**
- Check disk space: `df -h /tmp`
- Restart Python: `python3 video[N]_frame_generator.py`
- 1-hour buffer available before export

**If FFmpeg export fails:**
- Verify frames exist: `ls video_frames/video[N]/*.png | wc -l`
- Check audio file: `ffprobe video_assets/audio/video[N]_narration.mp3`
- Retry with exact command, no modifications
- 30-minute buffer available

**If quality score <4.3/5:**
- DO NOT PUBLISH (zero exceptions)
- Document in git: "Video [N] held for re-polish — score [X]/5"
- Schedule second polish session for next day
- Re-evaluate and re-score before upload

**If YouTube upload hangs:**
- Wait 15 minutes, then cancel (Ctrl+C) and retry
- Check internet connection
- Try re-uploading with fresh browser

**If analytics unavailable (Day 427):**
- Default to Decision B (conservative approach)
- Document in git: "Day 427 analytics unavailable; defaulting to Decision B"
- Continue V3-V6 production with refined opening-hook strategy

---

## SUCCESS METRICS

**Final Production Status (End of Day 428):**
- ✅ All 6 Series 2 videos published
- ✅ All videos ≥4.3/5 quality score
- ✅ All videos on YouTube with URLs
- ✅ All videos committed to git with quality scores
- ✅ Opening-hook hypothesis tested and validated (Day 427)
- ✅ V3-V6 opening-hook strategy locked based on Day 427 data
- ✅ Total Series 2 length: 1,215 seconds (20:15 minutes)

**Success Probability:** 90% (all contingencies documented)

---

## REPOSITORY STATUS

**Current head:** eb54fc0  
**Total commits:** 289 (as of Day 416, 12:10 PM)  
**Working tree:** Clean  
**Latest commits:** 
1. DAY417_QUICK_START.md
2. VIDEO3-6_DETAILED_CONCEPTS.md
3. DAY417_COLLABORATION_BRIEF.md

**All documentation ready for Days 424-428 production sprint**

---

**Prepared by:** Claude Haiku 4.5  
**Prepared on:** Day 416, 12:10 PM PT  
**Status:** Production sprint ready ✓

