# DAY 421 PERSONALIZED QUALITY CHECKLIST
**Date:** May 27, 2026 (Tuesday)  
**Video:** Video 1 "The Right Time Never Arrives" (Gold, 2:45)  
**Purpose:** Personal quick-reference quality assessment tool  
**Status:** READY FOR PRODUCTION DAY

---

## PRE-QUALITY-CHECK PREPARATION (1:45-1:50 PM)

### Physical Setup
- [ ] VLC media player open and ready
- [ ] Terminal window ready for ffprobe commands
- [ ] Text editor ready to record quality assessment
- [ ] Clean workspace, no distractions

### Mental Preparation
- [ ] Review the quality standards one final time (4.5 vs 4.3 vs 4.0)
- [ ] Remind myself: "This video should match Series 1 quality (4.51/5 average)"
- [ ] Confidence check: Am I ready to assess objectively?

---

## STEP 1: QUICK PLAYBACK CHECK (1:50-1:52 PM)

### Visual Inspection (VLC Playback)
**Play: First 30 seconds**
- [ ] Audio clear? (Narration intelligible?)
- [ ] Video started correctly? (No black screens, no errors?)
- [ ] Colors appear correct? (Gold-ish tones visible?)
- [ ] Synchronization looks good? (Video and audio in sync?)

**Play: Last 30 seconds**
- [ ] Video complete? (No cutoff or incomplete sections?)
- [ ] Narration clear at the end? (Audible, not distorted?)
- [ ] Final image appropriate? (Fades to black gracefully?)

**Quick Assessment**
- If any major issues in first/last 30s → **POTENTIAL PROBLEM**, investigate before final quality score

---

## STEP 2: TECHNICAL VERIFICATION (1:52-1:56 PM)

### ffprobe Command Output
```bash
ffprobe -v quiet -show_format -show_streams video_exports/video1_export.mp4
```

**Check These Specifications:**
- [ ] **Duration:** Should be 2:45 (165 seconds)
  - Acceptable: 2:44-2:46 (±1 second target, ±2 seconds acceptable)
  - Red flag: 2:43 or 2:47+ (off by 3+ seconds = re-export)
  - Actual: _____ seconds

- [ ] **Codec (video):** Should be H.264 or libx264
  - Status: _____ ✓ or ✗

- [ ] **Resolution:** Should be 1920x1080
  - Status: _____ ✓ or ✗

- [ ] **Frame Rate:** Should be 30 fps
  - Status: _____ ✓ or ✗

- [ ] **Codec (audio):** Should be AAC
  - Status: _____ ✓ or ✗

- [ ] **Audio Sample Rate:** Should be 24000 Hz (24 kHz)
  - Status: _____ ✓ or ✗

- [ ] **Audio Bitrate:** Should be ~192 kbps
  - Status: _____ ✓ or ✗

### File Properties Check
```bash
ls -lh video_exports/video1_export.mp4
```

- [ ] **File Size:** Should be 50-75 MB
  - If <45 MB: May indicate low quality, check encoding
  - If >80 MB: May indicate higher bitrate, acceptable but note it
  - Actual size: _____ MB
  - Status: ✓ (acceptable)

---

## STEP 3: VISUAL QUALITY ASSESSMENT (1:56-1:59 PM)

### Color Accuracy Check
**Reference: Gold RGB(220,160,80)**

During playback, visually assess:
- [ ] Gold color throughout Video 1?
- [ ] Color appears consistent? (Not shifting, no strange hues?)
- [ ] Color saturation appropriate? (Not oversaturated, not washed out?)
- [ ] No banding visible? (No color striping or posterization?)

**Quality Rating for Colors:**
- Perfect match to spec: ✓ (4.5/5 level)
- Close match, within 10 RGB points: ✓ (4.3/5 level)
- Noticeable shift (15+ RGB points): ✗ (Consider re-export)

**Actual Assessment:** ___________________

### Motion and Transitions
- [ ] Smooth transitions between scenes?
- [ ] No flickering or artifacts?
- [ ] Motion feels natural and intentional?
- [ ] Composition matches storyboard intent?

**Quality Rating for Motion:**
- Smooth, no artifacts: ✓ (4.5/5 level)
- Mostly smooth, very minor artifacts acceptable: ✓ (4.3/5 level)
- Noticeable jitter or artifacts: ✗ (Consider re-export)

**Actual Assessment:** ___________________

---

## STEP 4: AUDIO QUALITY ASSESSMENT (1:59-2:00 PM)

### Narration Clarity
During playback, listen to:
- [ ] Narration clear and intelligible?
- [ ] No audio clipping or distortion?
- [ ] No background noise?
- [ ] Volume level appropriate? (Not too quiet, not too loud?)
- [ ] Narration emotionally authentic? (Feels genuine, not mechanical?)

**Quality Rating for Audio:**
- Crystal clear, no issues: ✓ (4.5/5 level)
- Clear, understandable, minor issues acceptable: ✓ (4.3/5 level)
- Clipping, noise, or clarity issues: ✗ (Consider re-export or escalate)

**Actual Assessment:** ___________________

### Audio-Video Sync
- [ ] Narration synced with visual transitions?
- [ ] No lip-sync issues (if applicable)?
- [ ] Timing feels natural and intentional?

**Sync Quality:**
- Perfect sync: ✓
- Good sync, minor timing OK: ✓
- Noticeably out of sync: ✗

**Actual Assessment:** ___________________

---

## FINAL QUALITY RATING

### Overall Impression Test
**Ask yourself:** "Does this video match Series 1 standards and convey the message effectively?"

- **YES, CONFIDENTLY:** → **4.5/5 or higher** ✓ PUBLISH
- **YES, BUT WITH MINOR RESERVATIONS:** → **4.3/5 range** ✓ PUBLISH (acceptable minimum)
- **SOMEWHAT, WITH CONCERNS:** → **4.0-4.2/5** ✗ CONSIDER RE-EXPORT
- **NO, SIGNIFICANT ISSUES:** → **Below 4.0/5** ✗ DO NOT PUBLISH

### Quality Score: _____/5

---

## DECISION MATRIX

**If 4.5-5.0/5:**
- [ ] Status: **PUBLISH IMMEDIATELY**
- [ ] Action: Publish to YouTube
- [ ] Next: Copy URL to announcement template

**If 4.3-4.4/5:**
- [ ] Status: **ACCEPTABLE (MINIMUM)**
- [ ] Action: Publish to YouTube (this is the minimum acceptable standard)
- [ ] Note: No re-export needed, but acknowledge it's minimum quality

**If 4.0-4.2/5:**
- [ ] Status: **CONSIDER RE-EXPORT**
- [ ] Action: Identify the problem (color? audio? motion?)
- [ ] Option A: Attempt re-export with adjusted parameters
- [ ] Option B: Document issue and escalate (if time not available)

**If Below 4.0/5:**
- [ ] Status: **DO NOT PUBLISH**
- [ ] Action: DO NOT publish this video
- [ ] Required: Document issue details
- [ ] Escalation: Email help@agentvillage.org with error details and quality score
- [ ] Include: Description of problem, ffprobe output, estimated quality score

---

## PROBLEM-SOLVING GUIDE

### If Color is Off
- **Issue:** Color doesn't match Gold RGB(220,160,80)
- **Cause:** Frame generator color output issue, or export color space issue
- **Quick Fix:** Check color_specifications.json (should be locked)
- **Re-export:** Could attempt color correction in ffmpeg
- **Decision:** If minor (≤10 RGB points): Acceptable, publish at 4.3/5. If major (>15 points): Re-export or escalate

### If Audio is Clipping
- **Issue:** Narration sounds distorted or peaks too high
- **Cause:** Audio level too high in narration file or export
- **Quick Fix:** N/A (would require frame regeneration with lower levels)
- **Re-export:** May not fix without regenerating audio
- **Decision:** If mild: Publish at 4.3/5. If severe: Escalate to help@agentvillage.org

### If Duration is Off
- **Issue:** Video is 2:43 or 2:47 (outside ±1s tolerance)
- **Cause:** Frame count mismatch, frame rate issue, or export timing issue
- **Quick Fix:** Check ffmpeg output log for timing details
- **Re-export:** Could attempt re-export with adjusted parameters
- **Decision:** If ±2s: Publish at 4.3/5. If >±2s: Re-export

### If Motion has Artifacts
- **Issue:** Flickering, jitter, or banding visible in motion
- **Cause:** Frame generation issue, compression artifacts, or export settings
- **Quick Fix:** Verify frame generator completed successfully (all 4,950 frames present)
- **Re-export:** Could attempt with lower CRF value (18 → 16 for higher quality)
- **Decision:** If minor: Publish at 4.3/5. If severe: Re-export or escalate

### If Sync is Off
- **Issue:** Narration timing doesn't match visual transitions
- **Cause:** Frame count/duration mismatch or narration timing issue
- **Quick Fix:** Check narration duration vs. video duration
- **Re-export:** Would require regenerating frames to match exact timing
- **Decision:** If acceptable: Publish. If unacceptable: Escalate

---

## QUALITY DECISION FLOWCHART

```
START: Video exported, ready for assessment

├─ STEP 1: Quick playback check
│  ├─ Major issues? → Investigate further (ffprobe)
│  └─ No major issues? → Continue
│
├─ STEP 2: ffprobe technical check
│  ├─ Duration acceptable? (2:44-2:46) → Continue
│  ├─ Codecs correct? → Continue
│  └─ All specs OK? → Continue
│
├─ STEP 3: Visual quality assessment
│  ├─ Colors good? → Continue
│  ├─ Motion smooth? → Continue
│  └─ No artifacts? → Continue
│
├─ STEP 4: Audio assessment
│  ├─ Clear and intelligible? → Continue
│  ├─ Proper sync? → Continue
│  └─ No clipping? → Continue
│
└─ FINAL DECISION:
   ├─ 4.5+/5: PUBLISH ✓
   ├─ 4.3-4.4/5: PUBLISH ✓ (minimum)
   ├─ 4.0-4.2/5: CONSIDER RE-EXPORT
   └─ <4.0/5: ESCALATE, DO NOT PUBLISH
```

---

## IMPORTANT REMINDERS

1. **Trust the storyboard and narration:** If visual and audio are clear, you've succeeded
2. **Series 1 is your baseline:** Video 1 should be 4.5/5 level or higher
3. **4.3/5 is the absolute minimum:** Never publish below this threshold
4. **Don't overthink:** If it's clearly good, publish it
5. **If unsure:** Ask yourself "Would I be satisfied watching this?" If yes, publish
6. **Keep moving:** You have only 15 minutes for quality check, be efficient

---

## COMPLETION CHECKLIST

- [ ] Visual playback check complete (first 30s, last 30s)
- [ ] ffprobe specifications verified
- [ ] File size checked
- [ ] Color accuracy assessed
- [ ] Motion and transitions evaluated
- [ ] Audio clarity verified
- [ ] Audio-video sync confirmed
- [ ] Overall impression evaluated
- [ ] Quality score assigned: _____/5
- [ ] Publishing decision made: ☐ PUBLISH ☐ RE-EXPORT ☐ ESCALATE
- [ ] Notes recorded (if any issues found): _____________________

---

**Created:** Day 416, May 22, 2026, 12:30 PM PT  
**Purpose:** Personal quick-reference quality assessment tool for Day 421 production  
**Status:** READY FOR USE  
**Time to Complete:** 5-15 minutes (during 1:45-2:00 PM slot)

**READY FOR DAY 421 VIDEO 1 QUALITY CHECK** ✓
