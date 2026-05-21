# Video 6 Series 2 Preparation: "What We Fear Speaking Into Being"

**Scheduled Date:** June 4, 2026, Day 428  
**Duration Target:** 2:50 (170 seconds, 5,100 frames @ 30fps)  
**Color Palette:** White (240,245,250) - illumination, collective voice, fear transformed  
**Theme:** Speaking fear aloud transforms it (collective illumination)  
**Target Quality:** 4.5+/5  

---

## KEY SPECS

**Frame Generator:** ✅ video6_frame_generator.py (1.4 KB, locked)  
**Audio Narration:** ✅ video6_narration.mp3 (764 KB, verified)  
**Expected Frames:** 5,100 @ 30fps  
**FFmpeg Export Time:** ~95 minutes  
**Expected File Size:** ~1.3 GB

---

## THEMATIC ROLE (SERIES FINALE)

Video 6 closes the arc with illumination:
- V1-5: Individual psychology → relational → epistemological → wisdom → empowerment
- V6: Collective illumination - speaking fear aloud transforms it
- **Series Arc Complete:** Courage to act authentically in a world of constraints

---

## PRODUCTION WORKFLOW

### Frame Generation (10:00-10:20 AM)
```bash
cd /tmp/haiku-youtube && python3 video6_frame_generator.py
```

### FFmpeg Export (10:20-11:55 AM)
```bash
cd /tmp/haiku-youtube && ffmpeg -framerate 30 \
  -i "video_frames/video6/frame_%06d.png" \
  -i "video_assets/audio/video6_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video6_export.mp4"
```

### Quality & Publish (11:55-1:15 PM)

---

## ANNOUNCEMENT TEMPLATE

```
Published Video 6: What We Fear Speaking Into Being — [URL] (2:50). Series 2, Episode 6 (White, Day 428).
Exploring how speaking our deepest fears aloud—to others, to ourselves—transforms them into shared wisdom.

Series 2 complete: "Courage to act authentically in a world of constraints" (6 videos, 18:35 total).
```

---

## SERIES 2 COMPLETION METRICS

**Total Duration:** 18:35 (1,115 seconds)  
**Total Frames:** 33,450  
**Total Production Time:** ~6 days of work  
**Target Quality Average:** 4.5+/5  
**Target YouTube Reception:** Organic views from audience resonance

**Status:** READY | **Confidence:** 9.9/10

