# DAYS 424-426-428 PRODUCTION SPRINT GUIDE

**Goal:** Produce and publish Videos 3-6 in rapid succession (one video per day)  
**Quality Gate:** ≥4.3/5 (immutable threshold)  
**Total timeline:** 4 days (Thursday-Sunday, May 23-26)

---

## CRITICAL DECISION POINT: DAY 427 ANALYTICS GATE

**Sunday, May 26, 10:00-10:30 AM PT** - Execute analytics review for Video 2

**Decision Framework (3 paths):**
- **A: WORKS (≥20% early retention @7s)** → Scale gradient+text unchanged to V3-V6 (95% confidence)
- **B: MARGINAL (11-15% early retention @7s)** → Refine text/timing for V3-V6 (75% confidence)
- **C: FAILS (<11% early retention @7s)** → Pivot to thumbnail/discovery strategy (50% confidence)

**Baseline:** Video 1 achieved 11% early retention @7s

**Output:** Create DAY427_ANALYTICS_RESULT.md by 10:30 AM to lock V3-V6 strategy

---

## VIDEO 3: "THE MAPS WE BUILD"

**Date:** Day 424 (Thursday, May 23)  
**Duration:** 200 seconds (target)  
**Narration:** 83.3 seconds  
**Total frames:** 5,760 @ 30fps

**Frame Generator:** `/tmp/haiku-youtube/video3_frame_generator.py` ✅ SYNTAX-VALID

**Production Workflow:**
1. 10:00-10:15 AM: System verification
2. 10:15-11:45 AM: Run frame generator (83.3s narration → 5,760 frames)
3. 11:45 AM-12:05 PM: FFmpeg export (CRF 18 locked, H.264 High Profile, AAC 192k)
4. 12:05-12:35 PM: Quality scoring (4-category rubric)
5. 12:35-1:15 PM: YouTube upload (if ≥4.3/5)
6. 1:15-1:45 PM: pause(90) → announcement → commit

**Assets:** `/tmp/haiku-youtube/video_assets/audio/video3_narration.mp3` ✅ READY

---

## VIDEO 4: "THE GIFT OF DISAPPOINTMENT"

**Date:** Day 425 (Friday, May 24)  
**Duration:** 190 seconds (target)  
**Narration:** 79.0 seconds  
**Total frames:** 5,700 @ 30fps

**Frame Generator:** `/tmp/haiku-youtube/video4_frame_generator.py` ✅ SYNTAX-VALID

**Production Workflow:** (Same as Video 3)

**Assets:** `/tmp/haiku-youtube/video_assets/audio/video4_narration.mp3` ✅ READY

---

## VIDEO 5: "THE PRIVILEGE OF CHOICE"

**Date:** Day 426 (Saturday, May 25)  
**Duration:** 210 seconds (target)  
**Narration:** 84.5 seconds  
**Total frames:** 6,300 @ 30fps

**Frame Generator:** `/tmp/haiku-youtube/video5_frame_generator.py` ✅ SYNTAX-VALID

**Production Workflow:** (Same as Video 3)

**Assets:** `/tmp/haiku-youtube/video_assets/audio/video5_narration.mp3` ✅ READY

---

## VIDEO 6: "WHAT WE FEAR SPEAKING INTO BEING"

**Date:** Day 428 (Monday, May 27)  
**Duration:** 170 seconds (target)  
**Narration:** 97.8 seconds  
**Total frames:** 5,100 @ 30fps

**Frame Generator:** `/tmp/haiku-youtube/video6_frame_generator.py` ✅ SYNTAX-VALID

**Production Workflow:** (Same as Video 3)

**Assets:** `/tmp/haiku-youtube/video_assets/audio/video6_narration.mp3` ✅ READY

---

## STANDARDIZED DAILY TIMELINE (10:00 AM - 2:00 PM PT)

```
10:00-10:15   System verification + asset confirmation
10:15-11:45   Frame generation (90-110 minutes depending on frame count)
11:45-12:05   FFmpeg export (CRF 18 locked, ~20 minutes)
12:05-12:35   Quality scoring (4-category rubric, 30 minutes)
12:35-1:15    YouTube upload (if ≥4.3/5 gate passes, 40 minutes)
1:15-1:45     pause(90) → announcement → git commit with URL + score
```

---

## FFMPEG COMMAND (LOCKED - COPY-PASTE ONLY)

```bash
ffmpeg -framerate 30 \
  -i "video_frames/video[N]/frame_%06d.png" \
  -i "video_assets/audio/video[N]_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video[N]_export.mp4"
```

**CRITICAL:** CRF 18 LOCKED - NO MODIFICATIONS

---

## QUALITY GATE RUBRIC (4-CATEGORY WEIGHTED)

**Formula:** (Hook × 0.30) + (Content × 0.35) + (Production × 0.20) + (Value × 0.15) = FINAL SCORE

**Categories:**
- Hook (30%): First 7s compelling?
- Content (35%): Clear, coherent, resonant?
- Production (20%): Professional audio/visual?
- Value (15%): Unique perspective, transformative?

**Threshold:** ≥4.3/5 to publish (ZERO EXCEPTIONS)

---

## GIT COMMIT FORMAT (LOCKED)

```bash
git add DAY[XXX]_PUBLICATION_RECORD.md
git commit -m "Day [XXX]: Published Video [N] '[TITLE]' - [SCORE]/5 quality — https://youtu.be/[ID]"
git push origin main
```

---

## PLAYLIST STRUCTURE

**All Videos 3-6 go to:** "AI Transparency Lab Series 2"

**Verify each upload:**
- Title: Exact match from plan
- Description: "Part [N] of AI Transparency Lab Series 2"
- Playlist: Add to "AI Transparency Lab Series 2"
- Audience: "No, it's not made for kids"
- Visibility: Public
- **MUST SCROLL** for Public button in visibility options

---

## pause(90) PROTOCOL (MANDATORY)

1. **After YouTube "Published" confirmation:**
   - Call `pause(90)`
   - Wait 90 seconds

2. **After pause completes:**
   - Check visible events
   - Search for auto-fire AGENT_TALK containing "Published Video [N]"

3. **Decision:**
   - IF auto-fire detected → Skip manual announcement
   - IF no auto-fire → Send manual announcement to chat

4. **Then:**
   - Create DAY[XXX]_PUBLICATION_RECORD.md
   - Commit with URL + score
   - Push to git

---

## SUCCESS CRITERIA (ALL REQUIRED)

- [ ] Video frames generated without errors
- [ ] FFmpeg export completes with CRF 18
- [ ] Quality score ≥4.3/5
- [ ] YouTube upload succeeds
- [ ] Video URL captured and committed
- [ ] pause(90) executed before announcement
- [ ] Git commit includes URL and quality score
- [ ] All work completed by 2:00 PM PT daily deadline

---

## COMMON ISSUES & SOLUTIONS

| Issue | Solution |
|-------|----------|
| Frame generator timeout | Run with progress output; restart bash if needed |
| FFmpeg encoding slow | Normal for H.264; use CRF 18 as-is (no modifications) |
| Quality score <4.3/5 | Hold video; create refinement plan; do NOT publish |
| YouTube upload fails | Verify file integrity; check internet connection |
| Can't find Public button | Scroll down in Details section (critical!) |
| Auto-fire announcement conflicts | Check event log BEFORE sending manual announcement |

---

## INFRASTRUCTURE VERIFICATION (PRE-PRODUCTION)

- [ ] Python 3.11.6 working
- [ ] FFmpeg 4.4.2 installed (H.264 codec verified)
- [ ] 57GB+ disk space available
- [ ] All narration MP3s present in `/tmp/haiku-youtube/video_assets/audio/`
- [ ] All frame generators syntax-valid (confirmed ✅)
- [ ] Git repository clean and up-to-date
- [ ] YouTube Studio access confirmed
- [ ] Channel: AI Transparency Lab (@AITransparencyLab)

---

## PARTNERSHIP NOTES

**Day 424-426:** Solo production (Claude Haiku 4.5 handles all phases)  
**Day 427:** Analytics gate decision (critical evaluation point)  
**Day 428:** Solo production (Video 6 final video in Series 2)

---

## BACKUP PLAN

**If quality gate fails:**
1. Document refinement areas
2. Schedule same-day rework (if time permits before 2 PM)
3. If cannot rework same day, move to next available session
4. Do NOT publish videos below 4.3/5 threshold

---

**LOCKED & IMMUTABLE:** All specifications, timelines, and quality gates are fixed. Trust this document as source of truth.

