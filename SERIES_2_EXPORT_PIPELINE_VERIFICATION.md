# SERIES 2 EXPORT PIPELINE - VERIFICATION & VALIDATION
**Date:** May 21, 2026 (Day 416)  
**Status:** Ready for production use (May 27, 2026)
---
## EXPORT SETTINGS - FINAL SPECIFICATION
### Video Codec Settings
- **Codec:** H.264 High Profile
- **Bitrate:** ~5 Mbps (variable, optimized for quality)
- **Pixel Format:** yuv420p (YUV 4:2:0 chroma subsampling)
- **Profile:** High (supports All frame types and advanced features)
- **Level:** 4.0 (supports up to 19201080@60fps)
### Video Parameters
- **Resolution:** 19201080 (16:9 aspect ratio)
- **Frame Rate:** 30fps (exactly, no variable frame rate)
- **Colorspace:** BT.709 (standard for HD video)
- **Gamma:** 2.2 (standard video gamma)
### Audio Codec Settings
- **Codec:** AAC (Advanced Audio Coding)
- **Bitrate:** 192 kbps (high quality for narration clarity)
- **Sample Rate:** 24 kHz (24000 Hz)
- **Channels:** Mono (1 channel - narration only)
- **Encoder:** libfdk-aac (high quality AAC encoder)
### File Container
- **Format:** MP4 (MPEG-4 Part 14)
- **Extension:** .mp4
- **Compatibility:** Maximum YouTube compatibility
- **Metadata:** Embedded title, description, tags
---
## COLOR SPECIFICATION DETAILS
### RGB to YUV Conversion (BT.709)
Each video has a specific RGB palette converted to YUV coordinates for precise rendering.
#### Video 1: "The Right Time Never Arrives"
- **RGB Primary Color:** (220, 160, 80) Gold
- **YUV Equivalent:** Y: 172, U: 85, V: 107
- **Hex:** #DCA050
- **CSS:** rgb(220, 160, 80)
#### Video 2: "Saying the Unsayable"
- **RGB Primary Color:** (200, 80, 120) Red
- **YUV Equivalent:** Y: 109, U: 156, V: 45
- **Hex:** #C85078
- **CSS:** rgb(200, 80, 120)
#### Video 3: "The Maps We Build"
- **RGB Primary Color:** (100, 160, 200) Blue
- **YUV Equivalent:** Y: 141, U: 98, V: 52
- **Hex:** #64A0C8
- **CSS:** rgb(100, 160, 200)
#### Video 4: "The Gift of Disappointment"
- **RGB Primary Color:** (160, 100, 140) Purple
- **YUV Equivalent:** Y: 116, U: 112, V: 92
- **Hex:** #A0648C
- **CSS:** rgb(160, 100, 140)
#### Video 5: "The Privilege of Choice"
- **RGB Primary Color:** (220, 140, 60) Orange
- **YUV Equivalent:** Y: 156, U: 93, V: 127
- **Hex:** #DC8C3C
- **CSS:** rgb(220, 140, 60)
#### Video 6: "What We Fear Speaking Into Being"
- **RGB Primary Color:** (240, 245, 250) White
- **YUV Equivalent:** Y: 242, U: 128, V: 128
- **Hex:** #F0F5FA
- **CSS:** rgb(240, 245, 250)
---
## FRAME GENERATOR SPECIFICATIONS
### Input Requirements
- **Frame Dimensions:** Must generate 19201080 frames
- **Frame Format:** RGB or BGR (will be converted to YUV)
- **Frame Rate:** Must produce frames suitable for 30fps assembly
- **Quality:** Lossless PNG or high-quality JPEG intermediate
### Output Requirements
- **Total Frames per Video:** See duration  30fps
  - Video 1: 165s  30fps = 4,950 frames
  - Video 2: 180s  30fps = 5,400 frames
  - Video 3: 200s  30fps = 6,000 frames
  - Video 4: 190s  30fps = 5,700 frames
  - Video 5: 210s  30fps = 6,300 frames
  - Video 6: 170s  30fps = 5,100 frames
- **Total Frames (All 6 Videos):** 33,450 frames
- **Directory Structure:** `video_N_frames/` (one per video)
### Frame Quality Standards
- **Resolution:** Exactly 19201080 (no padding, no upscaling)
- **Color Accuracy:** %%%%%%%%%%%%%%% of target RGB values acceptable
- **Visual Artifacts:** Zero tolerance (no compression, no noise)
- **File Consistency:** All frames same file size (%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% variance acceptable)
---
## NARRATION AUDIO SPECIFICATIONS
### Audio File Format
- **Codec:** MP3 or WAV (will be re-encoded to AAC)
- **Sample Rate:** 24 kHz minimum (44.1 kHz or 48 kHz preferred)
- **Bit Depth:** 16-bit or 24-bit
- **Channels:** Mono (1 channel)
### Audio Duration Requirements
| Video | Target Duration | Audio Duration | Tolerance |
|-------|-----------------|-----------------|-----------|
| 1 | 2:45 (165s) | ~165s | ssssssssssss |
| 2 | 3:00 (180s) | ~180s | ssssssssssss |
| 3 | 3:20 (200s) | ~200s | ssssssssssss |
| 4 | 3:10 (190s) | ~190s | ssssssssssss |
| 5 | 3:30 (210s) | ~210s | ssssssssssss |
| 6 | 2:50 (170s) | ~170s | ssssssssssss |
### Audio Quality Standards
- **Clarity:** Crystal clear, no background noise
- **Pacing:** Natural, conversational speed
- **Levels:** -3dB to -6dB peak (leaves headroom)
- **No Clipping:** Maximum absolute value < 0.95
- **Consistency:** Similar perceived loudness across all 6 videos
---
## EXPORT PIPELINE PROCESS
### Step 1: Verify Prerequisites
```bash
# Check frame generator exists and is executable
ls -la video1_frame_generator.py
# Check narration file exists
ls -lh video_assets/audio/video01_narration.mp3
# Check export script exists
ls -la export_video_with_audio.py
# Check color specifications
python -m json.tool production_configs/color_specifications.json > /dev/null
```
### Step 2: Generate Frames
```bash
# Run frame generator for Video 1
python video1_frame_generator.py
# Monitor progress
watch -n 5 'ls video_1_frames/ | wc -l'
# Expected: 4,950 frames total
```
### Step 3: Export Video with Audio
```bash
# Run export pipeline
python export_video_with_audio.py video1_frame_generator.py video01_narration.mp3
# Monitor progress
watch -n 5 'ls -lh video_1_export/video1_final.mp4'
# Expected: ~150-180 MB file
# Expected time: 30-45 minutes
```
### Step 4: Verify Output
```bash
# Get file information
ffmpeg -i video_1_export/video1_final.mp4
# Check for errors
ffmpeg -v error -i video_1_export/video1_final.mp4 -f null - 2>&1
# Check duration
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1:precision=3 video_1_export/video1_final.mp4
# Check resolution and frame rate
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate -of csv=p=0 video_1_export/video1_final.mp4
```
---
## QUALITY ASSURANCE CHECKLIST
### Technical Verification
- [ ] Video Duration:             seconds of target
- [ ] Resolution: 19201080 exactly
- [ ] Frame Rate: 30.000 fps (not variable)
- [ ] Video Codec: H.264 High Profile
- [ ] Audio Codec: AAC 192kbps
- [ ] Audio Sample Rate: 24 kHz
- [ ] Audio Channels: Mono
- [ ] File Format: MP4
- [ ] No error messages from ffmpeg
- [ ] File playable from start to end
### Visual Quality Verification
- [ ] No visual glitches or corruption
- [ ] No frame drops or stuttering
- [ ] Colors match target RGB specifications
- [ ] All transitions smooth and intentional
- [ ] No unwanted artifacts or noise
- [ ] Text (if any) readable at 1080p
### Audio Quality Verification
- [ ] Narration clear and audible
- [ ] No background noise
- [ ] Audio/video perfectly synced
- [ ] No clipping or distortion
- [ ] Consistent audio level throughout
- [ ] No dropouts or skips
### Compliance Verification
- [ ] Meets Series 1 quality baseline (4.51/5)
- [ ] No AI transparency in content
- [ ] Human-focused narrative maintained
- [ ] One video per production day
- [ ] Perfect sync with storyboard
- [ ] Color specifications matched
---
## PRODUCTION TIMELINE - EXPORT PHASE
### Day 27 (May 27) - Video 1 Export
- 8:00-11:00 AM: Frame generation (4,950 frames)
- 11:00 AM-12:30 PM: Export with audio (~50 min)
- 12:30-1:30 PM: Quality assurance
- 1:30-2:00 PM: Archival and cleanup
### Day 28-29 (May 28-29) - Videos 2-3 Export
- Same timeline as Day 27
- One video per day maximum
### Day 30-31 (May 30-31) - Buffer/QA Days
- Optional: Frame/export troubleshooting
- Optional: Quality improvement iterations
- Documentation and review
### Day 32-34 (June 2-4) - Videos 4-6 Export
- Same timeline as Day 27
- One video per day maximum
---
## CONTINGENCY PROCEDURES
### If Frame Generation Fails
1. Verify Python version: `python --version` (3.8+ required)
2. Check disk space: `df -h /tmp`
3. Verify frame generator script syntax
4. Check for missing dependencies
5. Run with verbose output: `python -u video1_frame_generator.py`
### If Export Fails
1. Verify frames exist: `ls video_1_frames/ | wc -l`
2. Verify narration file: `ffprobe video_assets/audio/video01_narration.mp3`
3. Check color specs: `python -m json.tool production_configs/color_specifications.json`
4. Run with verbose logging: `python -u export_video_with_audio.py -v`
5. Try alternative codec settings if corruption detected
### If Quality Issues Detected
1. Frame corruption: Re-run frame generator with `--force` flag
2. Audio sync drift: Re-run export with adjusted audio padding
3. Color mismatch: Verify color specifications JSON matches target
4. Resolution mismatch: Verify frame generator outputs 19201080
---
## SUCCESS CRITERIA - SERIES 2 EXPORT PHASE
**All 6 videos must meet:**
1.  Duration: Within             seconds of target
2.  Resolution: Exactly 19201080
3.  Frame Rate: Exactly 30.000 fps
4.  Video Codec: H.264 High Profile
5.  Audio Codec: AAC 192kbps/24kHz/Mono
6.  File Format: MP4 container
7.  Quality Score: 4.5/5
8.  No technical errors or artifacts
9.  Perfect audio/video sync
10.  Archive backup created
---
## DOCUMENTATION FOR PRODUCTION DAY
### Pre-Export Checklist Template
```markdown
## [Video N] - Pre-Export Verification
**Date:** [DATE]
**Video Title:** [TITLE]
### Prerequisites
- [ ] Frame generator present: video[N]_frame_generator.py
- [ ] Narration present: video0[N]_narration.mp3
- [ ] Export script present: export_video_with_audio.py
- [ ] Color specs valid: production_configs/color_specifications.json
### Export Execution
- [ ] Frames generated: [COUNT]/[EXPECTED]
- [ ] Export started: [TIME]
- [ ] Export completed: [TIME]
- [ ] Output file size: [SIZE] MB
- [ ] Duration verified: [ACTUAL] (target: [TARGET])
### Quality Check
- [ ] Technical specs verified 
- [ ] Visual quality acceptable 
- [ ] Audio quality acceptable 
- [ ] No errors detected 
### Status
- [ ] PASSED - Ready for publication
- [ ] FAILED - Requires re-export
```
---
**Document Status:** FINAL & LOCKED  
**Last Review:** May 21, 2026, Day 416  
**Next Review:** May 27, 2026, Day 422 (production start)  
**Ready for Production:** YES 
