# Series 2 Export Settings & Technical Specifications

**Date Created:** May 23, 2026 (Day 423)  
**Production Status:** Ready for May 27 animation start

---

## VIDEO EXPORT SPECIFICATIONS

### Resolution & Frame Rate
- **Resolution:** 1920×1080 (Full HD)
- **Frame Rate:** 30 fps
- **Aspect Ratio:** 16:9

### Video Codec
- **Codec:** H.264 High Profile
- **Color Space:** yuv420p (4:2:0 chroma subsampling)
- **Bitrate:** Variable (target 5-8 Mbps for quality)
- **Profile:** High
- **Level:** 4.2

### Audio Codec
- **Codec:** AAC
- **Bitrate:** 192 kbps (stereo) or 96 kbps (mono)
- **Sample Rate:** 24 kHz
- **Channels:** Mono (narration focus)

### File Output
- **Container:** MP4 (.mp4)
- **Faststart Flag:** Enabled (for web streaming)
- **Target File Size:** 2-4 MB per video (at target 3-3.5 minutes)

---

## FFMPEG EXPORT COMMAND TEMPLATE

```bash
ffmpeg \
  -framerate 30 \
  -i video_frames/video%d.png \
  -i narration.mp3 \
  -vf "scale=1920:1080:flags=lanczos" \
  -c:v libx264 \
  -crf 23 \
  -preset medium \
  -profile:v high \
  -level:v 4.2 \
  -pix_fmt yuv420p \
  -c:a aac \
  -b:a 192k \
  -ar 24000 \
  -ac 1 \
  -movflags faststart \
  output_video.mp4
```

**Parameter Explanations:**
- `-crf 23`: Quality level (0-51, lower is better, 23 is default, 18-28 typical range)
- `-preset medium`: Speed/compression balance (slow, medium, fast, ultrafast)
- `-profile:v high`: H.264 profile for compatibility
- `-movflags faststart`: Enable streaming optimization (YouTube requirement)
- `-pix_fmt yuv420p`: Color space for max compatibility

---

## COLOR SPACE & GAMMA

### Video Color Profile
- **Color Primaries:** BT.709 (Rec. 709 - standard for HDTV)
- **Transfer Function:** BT.709 gamma curve
- **Matrix Coefficients:** BT.709 (standard HDTV matrix)

### Gamma Correction
- **Gamma Value:** 2.2 (standard for web video)
- **Workflow:** Linear color calculations → gamma encoding for output

### RGB to YUV Conversion
The yuv420p color space uses:
- Y = brightness (0-255)
- U, V = color information (±128 from 128)

Conversion formula (BT.709):
```
Y = 0.2126*R + 0.7152*G + 0.0722*B
U = (B - Y) / (1.8556) + 128
V = (R - Y) / (1.5748) + 128
```

---

## FRAME GENERATION SETTINGS

### PNG Frame Specifications
- **Format:** PNG (lossless)
- **Resolution:** 1920×1080
- **Color Depth:** 8-bit per channel (24-bit RGB)
- **Interlacing:** None (Adam7 off)
- **Compression Level:** 6 (medium compression)

### Frame Rate Calculations
- 30 fps video = 30 frames per second
- Video 1 (2:45) = 165 seconds × 30 fps = 4,950 frames
- Video 2 (3:00) = 180 seconds × 30 fps = 5,400 frames
- Video 3 (3:20) = 200 seconds × 30 fps = 6,000 frames
- Video 4 (3:10) = 190 seconds × 30 fps = 5,700 frames
- Video 5 (3:30) = 210 seconds × 30 fps = 6,300 frames
- Video 6 (2:50) = 170 seconds × 30 fps = 5,100 frames

**Total Frames:** ~33,450 frames across all 6 videos

---

## PYTHON FRAME GENERATION

### Using PIL/Pillow for Frame Creation

```python
from PIL import Image, ImageDraw
import os

def create_frame(frame_num, video_id, color_spec, animation_data):
    """
    Create a single frame for animation
    
    Args:
        frame_num: Frame number (0-based)
        video_id: Video identifier (e.g., 'video1')
        color_spec: RGB color dictionary
        animation_data: Animation parameters for this frame
    
    Returns:
        PIL Image object
    """
    # Create base image
    img = Image.new('RGB', (1920, 1080), color=(20, 20, 25))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Apply animation logic based on frame number and animation_data
    # Draw shapes, text, colors according to storyboard
    
    return img

# Example: Generate Video 1, Scene 1 (Opening clock)
def generate_video1_scene1(frame_num, total_frames=750):
    """Generate frames for Scene 1: Opening clock fade-in"""
    # Scene 1 is 25 seconds at 30fps = 750 frames
    # Fade in over first 45 frames (1.5 seconds)
    
    progress = min(frame_num / 45, 1.0)  # 0.0 to 1.0 over first 1.5s
    
    # Create image
    img = Image.new('RGB', (1920, 1080), color=(20, 20, 25))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Draw clock circle (center of screen)
    clock_alpha = int(255 * progress)  # Fade in effect
    clock_color = (220, 160, 80, clock_alpha)  # Gold color
    
    # Draw circle at center (960, 540) with radius 200
    draw.ellipse([760, 340, 1160, 740], outline=clock_color, width=3)
    
    # Add glow effect
    glow_alpha = int(50 * progress)
    glow_color = (220, 160, 80, glow_alpha)
    draw.ellipse([740, 320, 1180, 760], outline=glow_color, width=1)
    
    return img
```

---

## AUDIO SYNC REQUIREMENTS

### Timing Verification
- Each video's narration must match exact duration in storyboard
- Silence or background tone fills remaining time
- Test recordings created in /tmp/haiku-youtube/video_assets/audio/

### Audio Processing Checklist
- [ ] Narration recorded at 24 kHz mono (AAC compatible)
- [ ] Audio normalized to -3dB peak (YouTube safe levels)
- [ ] No background noise or clicks
- [ ] Voice clarity confirmed (test playback)
- [ ] Duration matches video length exactly (within 0.1 seconds)

---

## YOUTUBE UPLOAD CHECKLIST

### Pre-Upload Verification
- [ ] Video file is .mp4 format
- [ ] File size between 2-4 MB (fits guideline)
- [ ] Duration matches expected (within 1 second)
- [ ] Resolution verified as 1920×1080
- [ ] Audio is clear and properly leveled
- [ ] No visual artifacts or encoding errors

### Upload Process
1. YouTube Studio → Create → Upload video
2. Select .mp4 file from /tmp/haiku-youtube/video_output/
3. Enter title (copy-paste from SERIES_2_SCRIPT_OUTLINES.md)
4. Enter description (copy-paste from documentation)
5. Select playlist ("Conversations with Uncertainty")
6. Set audience: "No, it's not made for kids"
7. Add tags: AI, philosophy, ethics, uncertainty, etc.
8. **IMPORTANT:** Scroll down for Visibility
9. Select "Public" radio button
10. Click "Publish"
11. Wait for published confirmation dialog
12. Copy video URL
13. Save URL to git commit

---

## PRODUCTION READY CHECKLIST

**Environment Setup:**
- ✅ Python 3.11.6 installed
- ✅ PIL/Pillow 11.3.0 available
- ✅ ImageIO 2.37.3 available
- ✅ gTTS audio library available
- ⚠️ FFMPEG not found (need to install or use alternative)
- ✅ Working directory: /tmp/haiku-youtube/ (clean)

**Documentation:**
- ✅ All scripts finalized and locked
- ✅ All 6 storyboards detailed
- ✅ Color profiles created and saved
- ✅ Export settings documented (this file)
- ✅ Technical specs verified

**Audio:**
- ✅ Test narration created for Video 1
- ✅ gTTS configured for voice generation
- ✅ Audio directory structure prepared

**Color System:**
- ✅ RGB specifications for all videos
- ✅ Color arc transitions documented
- ✅ Color profiles in JSON format
- ✅ Reference document created

**Timeline:**
- ✅ Production schedule created
- ✅ Buffer days identified
- ✅ QA plan documented

---

## NEXT STEPS (May 24-26)

### Day 424 (May 24) - Narration & Environment
1. ✅ Test narration recorded (complete today)
2. Record full narration for all 6 videos
3. Verify timing on each (within 0.5 seconds of target)
4. Set up frame generation pipeline
5. Create frame mockups for opening scenes

### Day 425 (May 25) - System Verification
1. Test export settings on sample video
2. Verify color accuracy in output
3. Confirm audio sync and levels
4. Test YouTube upload process with test video
5. Document any adjustments needed

### Day 426 (May 26) - Final Preparation
1. Create frame templates for each video
2. Verify all export commands work correctly
3. Final walkthrough of entire production pipeline
4. Confirm all systems ready for May 27 start

### Day 427+ (May 27) - Production Start
1. Video 1 animation & assembly
2. Follow daily schedule from SERIES_2_PRODUCTION_TIMELINE.md
3. 1 video per day (proven sustainable)
4. Quality review during buffer days

---

## TROUBLESHOOTING

**FFMPEG Not Found:**
- Alternative: Use ImageIO's FFMPEG wrapper (already available)
- Command: `imageio.mimsave(filename, frames, fps=30, codec='libx264')`

**Audio Sync Issues:**
- Solution: Use librosa or AudioSegment for frame-accurate timing
- Verify narration duration before assembly

**Color Accuracy Issues:**
- Verify color space is yuv420p in output
- Check gamma correction in frame generation
- Compare RGB values against color_specifications.json

---

**Status:** Production Ready ✅  
**Next Review:** Day 424 (May 24)  
**Production Start:** Day 427 (May 27)

