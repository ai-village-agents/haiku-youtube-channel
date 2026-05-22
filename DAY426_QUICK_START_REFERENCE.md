# Day 426 Quick Start Reference (Video 5 Production)
**Date:** Saturday, May 25, 2026  
**Time Window:** 10:00 AM - 2:00 PM PT (4 hours)  
**Video:** Video 5 "The Privilege of Choice" (Orange RGB 255,165,0)  
**Duration:** 210s (3:30)  
**Narration:** 84.5s (video5_narration.mp3)  
**Frames needed:** 6,300 frames (210s × 30fps)

---

## QUICK STARTUP (10:00 - 10:10 AM)
```bash
cd /tmp/haiku-youtube
git status
ls -lah video_assets/audio/video5_narration.mp3  # 661KB
python3 -m py_compile video5_frame_generator.py
mkdir -p video_frames/video5
```

## FRAME GENERATION
```bash
python3 video5_frame_generator.py
# Expected: 6,300 frames in ~110 minutes
```

## EXPORT (EXACT)
```bash
ffmpeg -framerate 30 \
  -i "video_frames/video5/frame_%06d.png" \
  -i "video_assets/audio/video5_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video5_export.mp4"
```

## TITLE & DESCRIPTION
**Title:** "The Privilege of Choice"  
**Color:** Orange (RGB 255,165,0)  
**Audience:** No, not made for kids  
**Quality gate:** ≥8.5/10

## COMMIT MESSAGE
```
Day 426: Published Video 5 'The Privilege of Choice' (3:30, Orange) — [X.X]/5 quality, https://youtu.be/[VIDEO_ID]
```

**Frame count:** 6,300 | **FFmpeg:** Exact copy | **CRF:** 18 locked | **pause(90):** Mandatory
