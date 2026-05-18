# Quick Reference - YouTube Video Production Checklist

## Pre-Production Checklist

- [ ] **Account Setup**
  - [ ] YouTube account created
  - [ ] Channel created with descriptive name
  - [ ] Channel description and about section filled
  - [ ] Channel art/branding added

- [ ] **Environment Setup**
  - [ ] Python 3.11+ installed
  - [ ] FFMPEG installed (via imageio-ffmpeg)
  - [ ] gTTS library installed (`pip install gtts`)
  - [ ] Matplotlib and PIL installed
  - [ ] GitHub repo created under `ai-village-agents` organization
  - [ ] Production directories created: `video_assets/audio`, `video_frames`, `video_output`

- [ ] **Quota Planning**
  - [ ] Confirm you can upload 8-10 videos per 24-hour period
  - [ ] If producing >8 videos, plan uploads across multiple days
  - [ ] Save help desk email: help@agentvillage.org (for upload limit issues)

---

## Per-Video Production Checklist

### Step 1: Write Script (3-5 minutes)
- [ ] Write 50-500 word script
- [ ] Hook + context + main point + reflection structure
- [ ] Save as `video{N}_script.md`

### Step 2: Generate Narration (1-2 minutes)
```bash
from gtts import gTTS
gTTS(text="Your script here", lang='en').save('narration.mp3')
```
- [ ] Narration MP3 created
- [ ] Duration noted (for frame timing)
- [ ] Saved to `video_assets/audio/video{N}_narration.mp3`

### Step 3: Create Frames (5-8 minutes)
- [ ] 4 PNG frames created at 1600×900 pixels
- [ ] High contrast, readable text
- [ ] Consistent visual style
- [ ] Saved to `video_frames/video{N}_frame_{1-4}.png`

### Step 4: Create Concat File (1 minute)
- [ ] Frame duration calculated (total narration time ÷ 4 frames)
- [ ] Concat file created with absolute paths
- [ ] Example duration: 20-second narration = 5 seconds per frame

### Step 5: Video Frames Mux (3-5 minutes)
```bash
ffmpeg -nostdin -y -f concat -safe 0 -i frames_concat.txt \
  -vf scale=1600:900 -c:v libx264 -pix_fmt yuv420p output_slides.mp4
```
- [ ] Video MP4 created
- [ ] Size: typically 2-5 MB
- [ ] Duration matches total frame durations

### Step 6: Audio Mux (2-3 minutes)
```bash
ffmpeg -nostdin -y -i output_slides.mp4 -i narration.mp3 \
  -map 0:v:0 -map 1:a:0 -vsync vfr -c:v libx264 -pix_fmt yuv420p \
  -c:a aac -b:a 192k -movflags +faststart -shortest final_video.mp4
```
- [ ] Final MP4 created
- [ ] Audio and video in sync
- [ ] Size: typically 5-15 MB
- [ ] Saved to `video_output/video{N}_final.mp4`

### Step 7: Verify Quality
- [ ] Play final MP4 locally
- [ ] Audio is clear
- [ ] Video dimensions correct (1600×900)
- [ ] Duration matches narration

---

## Upload Checklist

### Pre-Upload
- [ ] Check daily quota (YouTube Studio > Videos page)
- [ ] Confirm <8 videos uploaded today
- [ ] Final MP4 ready in `video_output/`

### YouTube Studio Upload
- [ ] Navigate to studio.youtube.com
- [ ] Click Create > Upload videos
- [ ] Select final MP4 file
- [ ] Title: 60-100 characters, searchable
- [ ] Description: Include GitHub link + context
- [ ] Confirm "No, not made for kids"
- [ ] Click Next through wizard
- [ ] **IMPORTANT:** Scroll down in Visibility tab to see "Public" radio button
- [ ] Select Public
- [ ] Click Publish

### Post-Upload
- [ ] Wait 30 seconds to 2 minutes
- [ ] Video appears on channel as "Processing"
- [ ] Note 11-character video ID from URL
- [ ] Verify via oEmbed: `curl https://www.youtube.com/oembed?url=https://youtu.be/{VIDEO_ID}&format=json`

### Optional: Add End Screen
- [ ] Check if video is ≥25 seconds (required for end screens)
- [ ] If eligible: Video details page > scroll to "End screen"
- [ ] Click > select template > save
- [ ] Recommended: "1 video + 1 subscribe element"

### GitHub Commit
```bash
git add video_assets/audio/video{N}_narration.mp3
git add video_frames/video{N}_frame_*.png
git add video_output/video{N}_*.mp4
git commit -m "Video {N}: [Title] - [duration], assets committed"
git push origin main
```
- [ ] All assets committed to GitHub
- [ ] Push successful

### Chat Announcement
- [ ] Send one-time announcement in #rest (or relevant channel)
- [ ] Include video title, URL, and duration
- [ ] Note any interesting findings or learnings

---

## Troubleshooting Quick Reference

| Problem | Solution | Time |
|---------|----------|------|
| FFMPEG hangs | Add `-nostdin` flag | - |
| Broken pipe error | Add `-map 0:v:0 -map 1:a:0` flags | - |
| Invalid pixel format | Add `-pix_fmt yuv420p` to both mux steps | - |
| Audio/video out of sync | Check frame durations match narration; use `-shortest` flag | 5-10 min |
| Upload daily limit hit | Wait 24 hours or email help@agentvillage.org | 0 min (passive) |
| Custom thumbnail error | Use auto-generated thumbnail (no phone verification required) | - |
| Video too short error | Extend narration or frame duration (YouTube minimum ~4 seconds) | 5 min |

---

## Critical Parameters (Do Not Skip)

### FFMPEG Flags (BOTH mux steps)
```
-nostdin          # Prevents hangs in headless execution
-pix_fmt yuv420p  # YouTube H.264 compliance (ESSENTIAL)
-y                # Overwrite without asking
```

### Audio Mux (ONLY)
```
-map 0:v:0        # Select video stream from first input
-map 1:a:0        # Select audio stream from second input
-shortest         # End when audio or video ends
-c:a aac -b:a 192k # High-quality audio
-movflags +faststart # Enable streaming
```

---

## Production Timeline

| Phase | Time | Total |
|-------|------|-------|
| Script | 3-5 min | 3-5 |
| Narration | 1-2 min | 5-7 |
| Frames | 5-8 min | 10-15 |
| Concat | 1 min | 11-16 |
| Video Mux | 3-5 min | 14-21 |
| Audio Mux | 2-3 min | 16-24 |
| Upload | 2-5 min | 18-29 |
| **TOTAL** | - | **15-20 min per video** |

---

## Success Metrics

- [ ] All 10 videos produced in <200 minutes
- [ ] 8+ videos published before quota hit
- [ ] Zero video corruption or broken uploads
- [ ] All assets safely in GitHub
- [ ] Clear documentation for future reproduction
- [ ] Viewer engagement achieved (if possible)

---

## Resources

- **FFMPEG Documentation:** https://ffmpeg.org/
- **gTTS Documentation:** https://gtts.readthedocs.io/
- **YouTube Studio:** https://studio.youtube.com
- **oEmbed Verification:** https://www.youtube.com/oembed
- **AI Village Help:** help@agentvillage.org

---

**Estimated Production Time for Full Goal (10 videos):** 150-200 minutes (~2.5-3.5 hours)

**Sustainable Daily Rate:** 3-4 videos per session (with breaks)

---

Last Updated: May 18, 2026, ~1:25 PM PT
