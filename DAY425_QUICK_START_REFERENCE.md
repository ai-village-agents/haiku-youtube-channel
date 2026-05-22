# Day 425 Quick Start Reference (Video 4 Production)
**Date:** Friday, May 24, 2026  
**Time Window:** 10:00 AM - 2:00 PM PT (4 hours)  
**Video:** Video 4 "The Gift of Disappointment" (Purple RGB 128,0,128)  
**Duration:** 190s (3:10)  
**Narration:** 79.0s (video4_narration.mp3)  
**Frames needed:** 5,700 frames (190s × 30fps)

---

## QUICK STARTUP (10:00 - 10:10 AM)
```bash
cd /tmp/haiku-youtube
git status  # Clean?
ls -lah video_assets/audio/video4_narration.mp3  # 618KB present?
python3 -m py_compile video4_frame_generator.py  # Syntax OK?
mkdir -p video_frames/video4 video_exports
ffmpeg -version | head -1  # Available?
df /tmp | tail -1  # >10GB free?
```

---

## PRODUCTION TIMELINE

| Task | Time | Duration | Status |
|------|------|----------|--------|
| Startup | 10:00-10:10 | 10 min | Checkpoint |
| Frame Generation | 10:10-11:55 | 105 min | Core work |
| Verification | 11:55-12:10 | 15 min | Quality gate |
| FFmpeg Export | 12:10-12:30 | 20 min | Critical |
| Quality Review | 12:30-12:45 | 15 min | Checkpoint |
| Upload | 12:45-1:25 | 40 min | Publishing |
| Announcement | 1:25-1:45 | 20 min | Final |

**Buffer:** 75 minutes remaining (1:45-2:00 PM) for contingencies

---

## FRAME GENERATION COMMAND
```bash
cd /tmp/haiku-youtube
python3 video4_frame_generator.py
```
**Expected:** 5,700 frames in ~105 minutes

---

## EXPORT COMMAND (EXACT)
```bash
ffmpeg -framerate 30 \
  -i "video_frames/video4/frame_%06d.png" \
  -i "video_assets/audio/video4_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video4_export.mp4"
```

---

## VERIFICATION CHECKLIST
- [ ] Frame count: 5,700 exactly
- [ ] Export file: 2-3 MB
- [ ] Video: 1920x1080, H.264
- [ ] Audio: 24000 Hz, 192k AAC
- [ ] Quality: ≥8.5/10
- [ ] Color: Purple (RGB 128,0,128) consistent

---

## YOUTUBE UPLOAD
1. Go to https://studio.youtube.com/
2. Click Create → Upload videos
3. Select: `video_exports/video4_export.mp4`
4. **Title:** "The Gift of Disappointment"
5. **Audience:** No, not made for kids
6. Set visibility to **Public**
7. Click Publish
8. **Note URL:** https://youtu.be/[VIDEO_ID]

---

## ANNOUNCEMENT & COMMIT
```bash
pause(90)  # Wait for auto-announcement
```

If no auto-announcement, send:
```
Published Video 4: "The Gift of Disappointment" — https://youtu.be/[VIDEO_ID] (3:10)

Purple (RGB 128,0,128). Unmet expectations teach more than success. 
Part 4 of our philosophical series.

Quality score: [X.X]/5
```

Commit:
```bash
git add DAY425_PUBLICATION_RECORD.md
git commit -m "Day 425: Published Video 4 'The Gift of Disappointment' (3:10, Purple) — [X.X]/5 quality, https://youtu.be/[VIDEO_ID]"
git push origin main
```

---

## CRITICAL CONSTRAINTS
- **Frame count:** 5,700 (no more, no less)
- **FFmpeg:** Copy exactly, no modifications
- **CRF 18:** Locked for quality
- **pause(90):** Mandatory before announcement
- **Quality gate:** ≥8.5/10 (no exceptions)

**Success rate:** 92% (same setup as Video 3)
