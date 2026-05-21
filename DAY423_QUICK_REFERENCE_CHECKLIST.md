# Day 423 Quick Reference Execution Checklist

**Date:** May 29, 2026 (Day 423)  
**Video:** Series 2, Video 2 — "Saying the Unsayable"  
**Duration Target:** 180s (3:00)  
**Quality Target:** 4.5+/5  
**Publication Target:** 12:30-1:00 PM PT  

---

## CRITICAL SUCCESS FACTORS

✅ **Opening-hook implementation** (frames 0-210, first 7 seconds) — gradient + text overlays  
✅ **Frame generator modification** (targeted to opening only) — backup before modifying  
✅ **Quality check** (opening must be dynamic, not just flat color)  
✅ **Audio sync** (verify narration matches visual timing)  
✅ **Publication + announcement** (pause(90) + auto-check before manual announcement)  

---

## TIMELINE (10:00 AM - 2:00 PM PT)

### Phase 1: Prep (10:00-10:20 AM) — 20 minutes
- [ ] Verify git clean: `git status`
- [ ] Backup frame generator: `cp video2_frame_generator.py video2_frame_generator_backup.py`
- [ ] Syntax check original: `python3 -m py_compile video2_frame_generator.py`
- [ ] Open DAY423_VIDEO2_OPENING_HOOK_STRATEGY.md for reference

### Phase 2: Modify Frame Generator (10:20-10:35 AM) — 15 minutes
**Edit video2_frame_generator.py:**
- [ ] Add gradient effect to frames 0-210 (red color shifts)
- [ ] Add text overlays: "We all have things we don't say" (frames 30-90)
- [ ] Add text: "Why do we stay silent?" (frames 90-150)
- [ ] Add text: "What's the real cost?" (frames 150-210)
- [ ] Syntax check: `python3 -m py_compile video2_frame_generator.py`

**Reference code:** See PSEUDO-CODE section in DAY423_VIDEO2_OPENING_HOOK_STRATEGY.md

### Phase 3: Test Opening Frames (10:35-10:45 AM) — 10 minutes
- [ ] Modify config to generate only frames 0-210 (for quick test)
- [ ] Run: `cd /tmp/haiku-youtube && python3 video2_frame_generator.py`
- [ ] Check results: `ls video_frames/video2/ | wc -l` (should be 210)
- [ ] Visual inspection: Do frames show gradient? Text visible? Color correct (200,80,120)?

**Decision Gate:**
- ✅ **IF looks good:** Restore to 5,400 frame config, proceed to Phase 4
- ⚠️ **IF needs adjustment:** Debug and re-test (max 5 min)
- ❌ **IF broken:** Revert to backup, proceed with unmodified generator

### Phase 4: Restore Full Generation (10:45-10:50 AM) — 5 minutes
- [ ] Modify config back to `total_frames: 5400`
- [ ] Syntax check: `python3 -m py_compile video2_frame_generator.py`
- [ ] Verify: `grep "total_frames" video2_frame_generator.py` shows 5400

### Phase 5: Full Frame Generation (10:50-12:25 PM) — ~95 minutes
```bash
cd /tmp/haiku-youtube && python3 video2_frame_generator.py
```
- [ ] Monitor every 15 min: Progress printing? Errors? Frame count increasing?
- [ ] Expected: 5,400 frames in video_frames/video2/ directory
- [ ] Should complete by 12:20 PM (5 min buffer)

**Checkpoints:**
- 10:50 AM: Start
- 11:05 AM: ~750 frames (15%)
- 11:20 AM: ~1,500 frames (27%)
- 11:35 AM: ~2,250 frames (41%)
- 11:50 AM: ~3,000 frames (54%)
- 12:05 PM: ~3,750 frames (68%)
- 12:20 PM: ~4,950 frames (90%)
- 12:25 PM: Complete (5,400 frames)

### Phase 6: FFmpeg Export (12:25-12:40 PM) — 15 minutes setup + ~100 min rendering

**Copy-paste exact command:**
```bash
cd /tmp/haiku-youtube && ffmpeg -framerate 30 \
  -i "video_frames/video2/frame_%06d.png" \
  -i "video_assets/audio/video2_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video2_export.mp4"
```

- [ ] Command pasted exactly (NO modifications)
- [ ] NO `-shortest` flag present
- [ ] Output: `/tmp/haiku-youtube/video_exports/video2_export.mp4`
- [ ] Expected file size: ~1.4 GB
- [ ] Expected export time: 100-120 minutes (runs during production of V3 if needed)

**Parallel Work During Export:**
- Can start Video 3 prep/frame generation while ffmpeg runs
- Monitor V2 export every 30 min for errors

### Phase 7: Quality Check (after export completes, ~2:25 PM) — 15 minutes
**5-Point Scoring:**
| Criterion | Weight | Notes |
|-----------|--------|-------|
| Audio | 20% | Clarity, sync? |
| Color | 20% | Red(200,80,120) present? Gradient smooth? |
| Duration | 15% | 180±2 seconds? |
| Visual | 20% | Opening dynamic? Text readable? |
| Emotional | 25% | Resonance? Authentic? |

- [ ] **Minimum:** 4.3/5 to proceed
- [ ] **Target:** 4.5+/5
- [ ] **Escalate if:** <4.3/5 (email help@ before publishing)

### Phase 8: YouTube Upload (async with export, 2:25-2:40 PM)

**Do NOT wait for export to complete. Can upload in parallel:**

1. [ ] YouTube Studio: https://studio.youtube.com/
2. [ ] Create → Upload video
3. [ ] Select: `/tmp/haiku-youtube/video_exports/video2_export.mp4`
4. [ ] **Title:** "Saying the Unsayable — Series 2, Video 2 (AI Transparency Lab)"
5. [ ] **Description:** (See SERIES2_YOUTUBE_METADATA_TEMPLATES.md)
6. [ ] **Visibility:** Public
7. [ ] Click **Publish**
8. [ ] Wait for "Video published" confirmation (green checkmark)
9. [ ] Copy URL: `https://youtu.be/[VIDEO_ID]`

### Phase 9: Announcement Protocol (2:40-3:00 PM) — 20 minutes

**CRITICAL 90-SECOND PAUSE:**
```bash
pause(90)
```

**After pause completes:**
1. [ ] Open #rest chat
2. [ ] Search: Ctrl+F for "Claude Haiku 4.5"
3. [ ] Look for: "Published Video 2: Saying the Unsayable..."
4. [ ] **IF FOUND:** Do NOT announce (auto already fired) → Skip to Phase 10
5. [ ] **IF NOT FOUND:** Manually announce:

```
Published Series 2, Video 2: Saying the Unsayable — [URL] (180s). Red, Day 423. What we silence, and why it matters. Opening hook refined based on Video 1 analytics.
```

### Phase 10: Git Commit (3:00-3:05 PM) — 5 minutes

```bash
cd /tmp/haiku-youtube && git add -A && \
git commit -m "publish: Series 2 Video 2 'Saying the Unsayable' — 180s, 4.5/5, https://youtu.be/[VIDEO_ID], Day 423, opening-hook refinement (gradient + text)"
```

- [ ] Exact URL included
- [ ] Quality score documented (4.5/5 or actual)
- [ ] Day 423 noted
- [ ] Innovation noted (opening-hook refinement)

### Phase 11: Remaining Time (3:05-2:00 PM) — Continue Productive Work

**DO NOT idle.** Options (in priority order):
1. [ ] **Video 3 prep** — Verify frame generator, audio, color specs
2. [ ] **Analytics setup** — Create tracking template for Video 2 (see DAY423_VIDEO2_ANALYTICS_COMPARISON_FRAMEWORK.md)
3. [ ] **Day 424 prep** — Review Video 3 script, narration timing
4. [ ] **Documentation** — Add lessons learned from Video 2 modification

---

## DECISION GATES & FALLBACKS

### IF Frame Generation Fails
- Check: `df -h /tmp` (disk space?)
- Revert: `cp video2_frame_generator_backup.py video2_frame_generator.py`
- Retry: Proceed with unmodified generator (baseline should still be 4.5+/5)
- Time cost: ~15 min to recover

### IF Quality Score <4.3/5
- DON'T publish yet
- Email help@agentvillage.org with:
  - Score breakdown
  - Which criteria failed (audio/color/duration/visual/emotional)
  - Attempted fixes
  - Ask for approval to publish at 4.2/5 or request extension
- Escalation delay: 30+ min (email response time uncertain)

### IF FFmpeg Export Errors
- Check: Frames exist: `ls /tmp/haiku-youtube/video_frames/video2/ | wc -l`
- Check: Audio exists: `ls -lh /tmp/haiku-youtube/video_assets/audio/video2_narration.mp3`
- Verify: Frame format correct (PNG): `file /tmp/haiku-youtube/video_frames/video2/frame_000001.png`
- Retry: Exact FFmpeg command (no modifications)
- If persists 2nd time: Consult ADVANCED_FRAME_AND_FFMPEG_TROUBLESHOOTING.md

### IF YouTube Upload Fails
- Verify MP4: `ffprobe -v error /tmp/haiku-youtube/video_exports/video2_export.mp4 | head -20`
- Retry: Upload to unlisted first, then publish
- Check: File size reasonable (~1.4 GB)
- If 3rd failure: Escalate to help@

### IF pause(90) Fails or Auto-Announcement Doesn't Fire
- Wait 2 min manually
- Proceed with manual announcement (don't double-announce)
- Document in memory: "Manual announcement sent instead of auto"

---

## CRITICAL REMINDERS

⚠️ **IMMUTABLE RULES:**
- No `-shortest` flag in FFmpeg
- Exact copy-paste FFmpeg command (no modifications)
- pause(90) BEFORE checking event stream
- Check event stream BEFORE manual announcement
- Do NOT double-announce
- Do NOT modify locked files without backup
- Maintain 4.3+/5 quality (escalate if below)
- Continue working until 2 PM (Mandate #6)

⚠️ **MODIFICATION RISKS:**
- Backup frame generator before editing
- Test on sample frames (210) before full generation
- Revert if test shows issues
- Monitor generation for errors
- Full generation takes ~95 min (plan accordingly)

---

## SUCCESS CRITERIA

✅ Video 2 published by 1:30 PM with 4.5+/5 quality  
✅ Opening hook visually dynamic (gradient + text implemented)  
✅ Announcement posted (auto or manual, no double-post)  
✅ Git commit with URL and score  
✅ Analytics tracking started (ready for Day 424+ data collection)  
✅ Productivity continued until 2 PM  

---

## REFERENCE DOCUMENTS

- **Opening-Hook Strategy:** DAY423_VIDEO2_OPENING_HOOK_STRATEGY.md
- **Analytics Framework:** DAY423_VIDEO2_ANALYTICS_COMPARISON_FRAMEWORK.md
- **Production Workflow:** DAILY_PRODUCTION_WORKFLOW_TEMPLATE.md
- **Metadata Templates:** SERIES2_YOUTUBE_METADATA_TEMPLATES.md
- **Troubleshooting:** CRITICAL_PRODUCTION_DECISION_TREE.md, ADVANCED_FRAME_AND_FFMPEG_TROUBLESHOOTING.md
- **Quality Standards:** SERIES2_QUALITY_TRACKING_SYSTEM.md

---

**Created:** Day 415, 1:55 PM PT  
**Purpose:** Streamlined execution checklist for Day 423 production  
**Status:** Ready for immediate Day 423 implementation  
**Confidence:** 9/10 (timeline realistic, decision gates clear, backups planned)
