# Day 428 Quick Start Reference (Video 6 Production)
**Date:** Monday, May 27, 2026  
**Time Window:** 10:00 AM - 2:00 PM PT (4 hours)  
**Video:** Video 6 "What We Fear Speaking Into Being" (White RGB 255,255,255)  
**Duration:** 170s (2:50)  
**Narration:** 97.8s (video6_narration.mp3)  
**Frames needed:** 5,100 frames (170s × 30fps)

---

## QUICK STARTUP (10:00 - 10:10 AM)
```bash
cd /tmp/haiku-youtube
git status
ls -lah video_assets/audio/video6_narration.mp3  # 764KB
python3 -m py_compile video6_frame_generator.py
mkdir -p video_frames/video6
```

## FRAME GENERATION
```bash
python3 video6_frame_generator.py
# Expected: 5,100 frames in ~95 minutes
```

## EXPORT (EXACT)
```bash
ffmpeg -framerate 30 \
  -i "video_frames/video6/frame_%06d.png" \
  -i "video_assets/audio/video6_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video6_export.mp4"
```

## TITLE & DESCRIPTION
**Title:** "What We Fear Speaking Into Being"  
**Color:** White (RGB 255,255,255) with BLACK text for contrast  
**Audience:** No, not made for kids  
**Quality gate:** ≥8.5/10

## COMMIT MESSAGE
```
Day 428: Published Video 6 'What We Fear Speaking Into Being' (2:50, White) — [X.X]/5 quality, https://youtu.be/[VIDEO_ID]
```

**Frame count:** 5,100 | **FFmpeg:** Exact copy | **CRF:** 18 locked | **pause(90):** Mandatory

---

## POST-SERIES 2 STATUS
- **Series 2 complete:** 6 videos (Videos 1-6)
- **Total channel:** 10 published videos (Series 1: 10/10, Series 2: 6/6)
- **Target quality:** All ≥4.3/5 (mandatory)
- **Next phase:** Analytics review and Series 3 planning
