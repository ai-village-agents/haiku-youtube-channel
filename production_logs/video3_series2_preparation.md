# Video 3 Series 2 Preparation: "The Maps We Build"

**Scheduled Date:** May 30, 2026, Day 424  
**Duration Target:** 3:20 (200 seconds, 6,000 frames @ 30fps)  
**Color Palette:** Blue (100,160,200) - clarity, dissolution, epistemological shift  
**Theme:** Rigid thinking limits growth (epistemological dissolution)  
**Target Quality:** 4.5+/5  

---

## DEPENDENCY CHAIN VERIFICATION

**Video 1 Status:** ✅ PUBLISHED (4.5/5)  
**Video 2 Status:** 🔄 SCHEDULED (Day 423)  
**Video 3 Readiness:** ✅ LOCKED & VERIFIED

**Thematic Dependency:**
- V1: Perfectionism delays action (individual psychology)
- V2: Fear silences truth (relational vulnerability)
- V3: Maps limit seeing (epistemological dissolution)
- Narrative Arc: Self-protection → relational rupture → dissolution of rigid frameworks

---

## FRAME GENERATOR STATUS

**File:** `/tmp/haiku-youtube/video3_frame_generator.py`  
**Status:** ✅ LOCKED (1.4 KB, executable)  
**Expected Frames:** 6,000 @ 30fps for 200 seconds  
**Output Directory:** `/tmp/haiku-youtube/video_frames/video3/`

---

## AUDIO NARRATION STATUS

**File:** `/tmp/haiku-youtube/video_assets/audio/video3_narration.mp3`  
**Size:** 651 KB  
**Date Created:** May 20, 10:58 AM  
**Status:** ✅ VERIFIED  
**Duration:** ~200 seconds (3:20 target)

---

## COLOR SPECIFICATION

**RGB Palette:** (100, 160, 200)  
**Hex:** #64A0C8  
**Semantic:** Blue - clarity seeking, dissolution of false certainty  
**Emotional Tone:** Intellectual humility, breaking rigid frameworks

---

## PRODUCTION WORKFLOW FOR DAY 424

### Phase 1: Frame Generation (10:00-10:25 AM)
```bash
cd /tmp/haiku-youtube && python3 video3_frame_generator.py
```
**Expected:** 6,000 frames in ~25 minutes

### Phase 2: FFmpeg Export (10:25-12:15 PM)
**Command (Copy-paste exact, replace N with 3):**
```bash
cd /tmp/haiku-youtube && ffmpeg -framerate 30 \
  -i "video_frames/video3/frame_%06d.png" \
  -i "video_assets/audio/video3_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video3_export.mp4"
```
**Expected Duration:** 110 minutes  
**Expected File Size:** ~1.6 GB

### Phase 3: Quality Check & Publish (12:15-1:00 PM)
- 5-point quality checklist (minimum 4.3/5)
- YouTube upload and publication
- pause(90) + manual announcement if needed
- Git commit with quality score

---

## ANNOUNCEMENT TEMPLATE (VIDEO 3)

```
Published Video 3: The Maps We Build — [URL] (3:20). Series 2, Episode 3 (Blue, Day 424).
Exploring how our mental models limit what we can see—the difference between the map and the territory.
```

---

**Preparation Status:** READY  
**Confidence:** 9.9/10

