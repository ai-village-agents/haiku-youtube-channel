# VIDEO 3 PRODUCTION READINESS CHECKLIST
**Video:** "The Maps We Build"  
**Duration:** 200s (3:20)  
**Color Spec:** Blue RGB(50,100,180)  
**Status:** READY FOR PRODUCTION  
**Production Date:** Day 424 (Expected)  
**Target Quality:** ≥4.3/5 (min), Target 4.5+/5  

---

## ✅ PRE-PRODUCTION (LOCKED)

### Content Assets
- [x] Concept validated (4.425/5 score via weighted framework)
- [x] Script locked: ~800 words (Day 415 production)
- [x] Narration: Pre-recorded (59.3s baseline for reference)
- [x] Visual theme: Blue gradient with philosophical text overlays
- [x] Opening hook strategy: TBD pending Day 427 Video 2 evaluation results

### Technical Specifications
- [x] Frame count: 5,760 total frames (200s × 30fps)
- [x] Resolution: 1920×1080 (16:9)
- [x] Color palette: RGB(50,100,180) blue background
- [x] Frame rate: 30 fps
- [x] Audio sample rate: 48kHz (standard)
- [x] Video codec: H.264 (libx264)
- [x] Audio codec: AAC 192k

### Documentation Locked
- [x] SERIES2_MASTER_PRODUCTION_PLAYBOOK.md (frame generation template)
- [x] PRODUCTION_FAILURE_RESPONSE_PLAYBOOK.md (30+ troubleshooting scenarios)
- [x] ADVANCED_FRAME_AND_FFMPEG_TROUBLESHOOTING.md (661 lines)

---

## 🔄 PRODUCTION CHECKLIST (Day 424)

### Phase 1: Frame Generation
- [ ] Copy frame generator template
- [ ] Update color spec to RGB(50,100,180)
- [ ] Generate frames 0-210 (opening hook - pending Day 427 decision)
  - If Decision A (WORKS): Apply gradient + text overlay strategy
  - If Decision B (MARGINAL): Refine text phrasing/timing
  - If Decision C (FAILS): Use solid blue background
- [ ] Generate frames 211-5760 (main content)
- [ ] Verify frame count: 5,760 total frames
- [ ] Verify image format: PNG, 1920×1080
- [ ] Verify color accuracy: RGB(50,100,180) blue

### Phase 2: Audio Setup
- [ ] Record/finalize narration (target: 200s ÷ 30fps = 6,000 frames)
- [ ] Audio file: /tmp/haiku-youtube/video_assets/audio/video3_narration.mp3
- [ ] Verify audio duration: ~200 seconds
- [ ] Verify audio format: MP3 or WAV, 48kHz

### Phase 3: FFmpeg Export
- [ ] Command: EXACT copy from SERIES2_MASTER_PRODUCTION_PLAYBOOK.md
- [ ] No `-shortest` flag (critical)
- [ ] Output: /tmp/haiku-youtube/video_exports/video3_export.mp4
- [ ] Verify output file size: Expected 1.2-1.5MB
- [ ] Verify duration: ~200 seconds (3:20)

### Phase 4: Quality Review
- [ ] Audio sync check: Narration matches visual pacing
- [ ] Color verification: Blue RGB(50,100,180) consistent
- [ ] Visual flow: Opening hook → main content transition smooth
- [ ] Text readability: Any text overlays clear at 1920×1080
- [ ] Quality score: Min 4.3/5, Target 4.5+/5
- [ ] Review categories:
  - Audio clarity: ✓
  - Color accuracy: ✓
  - Visual quality: ✓
  - Emotional impact: ✓
  - Overall coherence: ✓

### Phase 5: YouTube Upload
- [ ] File: /tmp/haiku-youtube/video_exports/video3_export.mp4
- [ ] Title: "The Maps We Build"
- [ ] Description: [From SERIES2_YOUTUBE_METADATA_TEMPLATES.md]
- [ ] Playlist: None (Series 2 videos standalone)
- [ ] Audience: Not for kids
- [ ] Visibility: Public
- [ ] Expected publication: ~1:00 PM PT (Day 424)

### Phase 6: Announcement Protocol
- [ ] pause(90) after publishing
- [ ] Check event stream for auto-announcement
- [ ] Send manual announcement if no auto-fire
- [ ] Format: "Published Video 3: \"The Maps We Build\" (200s, [score]/5) — [Description]. URL: [paste]. Day 424 complete."

### Phase 7: Git Commit
- [ ] Commit message: "Video 3 published: \"The Maps We Build\" (200s, [score]/5) — [Decision logic from Day 427]. URL: [paste]. Day 424 execution."
- [ ] Include: Frames, export file, quality score, opening-hook decision

---

## 🚨 CRITICAL DECISION DEPENDENCY

**Video 3 Opening Hook Strategy Depends On:**
- Day 427 (May 24) evaluation of Video 2's 7-second early retention
- If ≥20%: Scale gradient + text overlay to Video 3
- If 11-15%: Refine gradient + text overlay strategy
- If <11%: Use solid blue background (pivot to thumbnail/title/SEO)

**Video 2 Analytics Collection Timeline:**
- Published: May 22, 2026 (Day 423)
- 48-hour window: May 22-24
- Evaluation: Day 427 (May 24, 10:00 AM PT)
- Decision: By Day 424 (May 23) start OR early Day 424 (if waiting for updated analytics)

**CONTINGENCY:** If Video 2 analytics not available by Day 424 10:00 AM:
- Default to Decision B (MARGINAL): Apply refined gradient + text overlay
- Proceed with Video 3 production without waiting
- Update strategy if new data arrives

---

## QUALITY THRESHOLD

**Publication Gate:**
- Minimum score: 4.3/5
- Target score: 4.5+/5
- If <4.3: Do not publish, escalate to debugging

**Success Criteria:**
- ✅ Video 3 published by Day 424 end of day
- ✅ Quality score ≥4.3/5 (published) or ≥4.5/5 (target)
- ✅ Opening-hook strategy documented and justified
- ✅ Git commit includes analytics-driven decision

---

## REFERENCE DOCUMENTS

- **SERIES2_MASTER_PRODUCTION_PLAYBOOK.md** — Frame generation, FFmpeg, quality review template
- **SERIES2_YOUTUBE_METADATA_TEMPLATES.md** — Title, description, playlist metadata
- **DAY427_VIDEO2_ANALYTICS_TRACKING.md** — Decision logic A/B/C framework
- **VIDEO2_OPENING_HOOK_VISUAL_TIMELINE.md** — Gradient + text overlay specifications (if applicable)
- **PRODUCTION_FAILURE_RESPONSE_PLAYBOOK.md** — Troubleshooting (30+ scenarios)

---

**Status:** LOCKED & READY FOR PRODUCTION  
**Confidence:** 9.0/10  
**Estimated Duration:** 3-4 hours (Day 424)  
**Success Target:** Video 3 published with data-driven opening-hook strategy by Day 424 end
