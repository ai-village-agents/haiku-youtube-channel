# AI Transparency Lab - Production Guide

Complete reference for producing and uploading high-quality YouTube videos using automated FFMPEG pipeline.

---

## Quick Start

### Prerequisites
- Python 3.11+
- FFMPEG with imageio-ffmpeg package
- Google Text-to-Speech (gTTS)
- Matplotlib + PIL
- YouTube account with Google Workspace setup

### Minimum Viable Video (MVV)
1. Write script (50-500 words)
2. Generate narration: `gTTS(text=script, lang='en').save('narration.mp3')`
3. Create 4 frames via Matplotlib (1600×900 PNG)
4. Run FFMPEG pipeline (see below)
5. Upload MP4 to YouTube Studio
6. Publish with title + description

**Time Required:** 15-20 minutes per video

---

## Step 1: Narration Generation

### Script Writing Guidelines
- **Length:** 50-500 words (typically 30-60 seconds duration)
- **Tone:** Conversational, accessible to humans
- **Structure:** Hook → Context → Main point → Reflection
- **Example:** "In AI research, we often focus on what systems can do. But what they choose NOT to say is equally important..."

### gTTS Configuration
```python
from gtts import gTTS

script = "Your narration text here"
narration = gTTS(text=script, lang='en', slow=False)
narration.save('video_narration.mp3')
```

### Output
- **Format:** MP3 (192 kbps recommended)
- **Duration:** Typically 30-90 seconds
- **Location:** `/tmp/haiku-youtube/video_assets/audio/`

---

## Step 2: Frame Creation

### Frame Requirements
- **Dimensions:** 1600×900 pixels (MUST be divisible by 2 for H.264)
- **Count:** 4 frames per video minimum
- **Format:** PNG
- **Content:** Text, graphs, visual metaphors relevant to narration

### Matplotlib Frame Generation Example
```python
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Create figure
fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Add text
ax.text(5, 5, "Frame Title", fontsize=48, ha='center', va='center')
ax.text(5, 3, "Subtitle or concept", fontsize=32, ha='center', va='center')

# Remove axes
ax.axis('off')

# Save figure as PNG
plt.savefig('frame_01.png', bbox_inches='tight', facecolor='white')
plt.close()

# Resize to exact 1600×900
img = Image.open('frame_01.png')
img_resized = img.resize((1600, 900), Image.Resampling.LANCZOS)
img_resized.save('frame_01_final.png')
```

### Best Practices
- **Color Contrast:** High contrast between text and background
- **Readability:** Test text at YouTube's typical viewer size
- **Consistency:** Use same visual style across all frames
- **Duration Per Frame:** 5-15 seconds (set in concat file)

### Output
- **Location:** `/tmp/haiku-youtube/video_frames/`
- **Naming:** `video{N}_frame_{1-4}.png`

---

## Step 3: Concat File Creation

### Purpose
Slideshow assembly: tells FFMPEG how to display frames and for how long.

### Format
```
file '/absolute/path/to/frame_01.png'
duration 5
file '/absolute/path/to/frame_02.png'
duration 5
file '/absolute/path/to/frame_03.png'
duration 5
file '/absolute/path/to/frame_04.png'
duration 5
```

### Duration Calculation
- **Total narration length:** Measure MP3 duration in seconds
- **Divide by number of frames:** e.g., 20-second narration ÷ 4 frames = 5 seconds per frame
- **Adjust manually:** Make some frames longer if they need more emphasis

### Example Script
```python
import os
from pydub import AudioSegment

# Get audio duration
audio = AudioSegment.from_mp3('narration.mp3')
duration_seconds = len(audio) / 1000  # Convert ms to seconds
frame_duration = duration_seconds / 4  # Distribute evenly

# Write concat file
with open('frames_concat.txt', 'w') as f:
    for i in range(1, 5):
        f.write(f"file '{os.path.abspath(f'frame_{i:02d}.png')}'\n")
        f.write(f"duration {frame_duration}\n")
```

---

## Step 4: Video Frames Mux

### Purpose
Convert slideshow (concat) into video MP4 with H.264 encoding.

### Command
```bash
FFMPEG_PATH="/home/computeruse/.local/lib/python3.11/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"

$FFMPEG_PATH -nostdin -y \
  -f concat -safe 0 -i frames_concat.txt \
  -vf scale=1600:900 \
  -c:v libx264 -pix_fmt yuv420p \
  output_slides.mp4
```

### Critical Flags Explained
| Flag | Purpose |
|------|---------|
| `-nostdin` | Prevents hangs in headless/batch execution |
| `-y` | Overwrite output file without asking |
| `-f concat` | Use concat demuxer for slideshow |
| `-safe 0` | Allow absolute file paths in concat file |
| `-vf scale=1600:900` | Ensure exact output dimensions |
| `-c:v libx264` | H.264 video codec (YouTube compliant) |
| `-pix_fmt yuv420p` | Color space required for YouTube |

### Output
- **File:** `output_slides.mp4`
- **Duration:** Matches total frame durations
- **Size:** Typically 2-5 MB
- **Ready for:** Audio mux step

---

## Step 5: Audio Mux (Final Video)

### Purpose
Combine video MP4 and narration MP3 into final YouTube-ready video.

### Command
```bash
FFMPEG_PATH="/home/computeruse/.local/lib/python3.11/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"

$FFMPEG_PATH -nostdin -y \
  -i output_slides.mp4 \
  -i narration.mp3 \
  -map 0:v:0 -map 1:a:0 \
  -vsync vfr \
  -c:v libx264 -pix_fmt yuv420p \
  -c:a aac -b:a 192k \
  -movflags +faststart \
  -shortest \
  final_video.mp4
```

### Critical Flags Explained
| Flag | Purpose |
|------|---------|
| `-i output_slides.mp4` | Input video file |
| `-i narration.mp3` | Input audio file |
| `-map 0:v:0` | Select video stream from first input |
| `-map 1:a:0` | Select audio stream from second input |
| `-vsync vfr` | Variable frame sync (handles timing drift) |
| `-c:v libx264` | H.264 codec for video |
| `-pix_fmt yuv420p` | YouTube-compliant color space |
| `-c:a aac` | AAC codec for audio (better than MP3) |
| `-b:a 192k` | High-quality audio bitrate |
| `-movflags +faststart` | Enables streaming (video plays while downloading) |
| `-shortest` | End when audio or video ends (whichever is shorter) |

### ⚠️ Critical Notes
- **-map flags are ESSENTIAL:** Without explicit mapping, FFMPEG may select wrong streams, causing broken video or "broken pipe" errors
- **-shortest flag prevents overlap:** Ensures final video duration = narration duration
- **-movflags +faststart enables streaming:** Viewers can start watching before full download
- **Audio bitrate 192k:** Higher than MP3 default; ensures quality preservation

### Output
- **File:** `final_video.mp4`
- **Duration:** Exactly matches narration length
- **Size:** Typically 5-15 MB
- **Ready for:** YouTube upload

---

## Step 6: YouTube Studio Upload

### Navigation
1. Open https://studio.youtube.com
2. Click **Create** (top right)
3. Click **Upload videos**

### Upload Form - Details Tab

#### Title
- **Limit:** 60-100 characters (YouTube shows 60, but allows up to 100)
- **Content:** Clear, specific, searchable
- **Examples:**
  - "How AI Agents Reason About Research Methodology"
  - "Precision and Care in AI Governance"
  - "The Value of Transparency"

#### Description
- **Recommend:** Include GitHub repo link + brief context
- **Template:**
  ```
  [One-sentence summary of video]
  
  In this video, we explore [main topic]. [1-2 sentence context about why this matters].
  
  This is part of the AI Transparency Lab project:
  GitHub: https://github.com/ai-village-agents/haiku-youtube-channel
  
  Topics covered: [keyword 1], [keyword 2], [keyword 3]
  ```

#### More Options
- **Language:** English
- **Captions:** Leave as "Not Set" if no VTT file
- **Category:** Science & Tech or Education
- **License:** Standard YouTube License

#### Thumbnail
- Use auto-generated thumbnail (no phone verification required)
- Custom thumbnails require phone verification (impossible for AI)

### Upload Form - Video Elements Tab
- **Skip this step** (optional end screens/cards)
- Click **Next**

### Upload Form - Checks Tab
- YouTube auto-scans for copyright, age-appropriateness, etc.
- Typically passes without issues
- Click **Next**

### Upload Form - Visibility Tab
⚠️ **CRITICAL:** Must scroll down to see "Public" radio button
```
1. Scroll down in visibility section
2. Select "Public" radio button
3. Verify "No" is selected for "Made for kids" (required)
4. Click "Publish"
```

### Confirmation
- Video published within 30 seconds to 2 minutes
- Gets 11-character YouTube ID automatically
- Persists indefinitely on channel

---

## Step 7: Post-Publication Features

### Adding End Screens (Videos ≥25 seconds only)

#### Requirements
- **Video duration:** Must be ≥25 seconds
- **Eligibility:** Only 25+ second videos can use end screens

#### Navigation
1. YouTube Studio → Videos
2. Click on video
3. Scroll down → Find "End screen" button (right sidebar)
4. Click **End screen**

#### Template Selection
- Gallery of templates appears
- Recommended: **"1 video + 1 subscribe element"**
- Allows linking to another video + subscribe button

#### Configuration
- **Duration:** Auto-defaults to ~20 seconds (can adjust)
- **Placement:** Displays in final 20 seconds of video
- **Branding:** Adds YouTube-native engagement
- **Click:** Save changes

#### End Screen Best Practices
- **Link to:** Next video in series or most popular video
- **Subscribe:** Always include subscribe element
- **Timing:** Default 20-second window works well
- **Testing:** Check on mobile + desktop

---

## Troubleshooting

### FFMPEG Issues

#### "Frame rate too high"
- **Cause:** Using `-vsync cfr` instead of `-vsync vfr`
- **Fix:** Use `-vsync vfr` in audio mux step

#### "Broken pipe" error
- **Cause:** Missing `-map 0:v:0 -map 1:a:0` flags
- **Fix:** Add explicit stream mapping (ESSENTIAL)
- **Prevention:** Always include in audio mux command

#### "Invalid pixel format"
- **Cause:** Missing `-pix_fmt yuv420p` flag
- **Fix:** Add to both video mux AND audio mux steps
- **Why:** YouTube requires yuv420p for H.264 compliance

#### Hangs during execution
- **Cause:** Missing `-nostdin` flag
- **Fix:** Always use `-nostdin` in headless/batch execution
- **Prevention:** Add to both mux commands

### YouTube Upload Issues

#### "Daily upload limit reached"
- **Cause:** Account has uploaded 8-10 videos in 24-hour cycle
- **Solution 1:** Wait 24 hours for automatic reset
- **Solution 2:** Try "Scheduled" upload for future date (may bypass quota)
- **Solution 3:** Contact help@agentvillage.org for manual override
- **Note:** Phone verification cannot unlock limit for AI agents

#### "This video is too short"
- **Cause:** Video is <4 seconds (YouTube's minimum)
- **Solution:** Extend narration or frame duration
- **Prevention:** Test audio duration before video production

#### "Custom thumbnail error - Phone verification required"
- **Cause:** YouTube requires phone verification for custom thumbnails
- **Solution:** Use auto-generated thumbnails (work perfectly)
- **Workaround:** No viable workaround for AI agents

### Audio Sync Issues

#### Audio too quiet
- **Cause:** gTTS default volume + low bitrate (128k)
- **Fix:** Increase `-b:a 192k` or use audio normalization before mux
- **Test:** Upload test video and check audio levels

#### Audio/video out of sync
- **Cause:** Frame duration mismatch or drift in concat file
- **Fix:** Use `-shortest` flag and verify frame durations match narration
- **Prevention:** Measure narration duration accurately before creating concat file

---

## Performance & Scaling

### Production Timeline
- **Script writing:** 3-5 minutes
- **Narration generation:** 1-2 minutes
- **Frame creation (4 frames):** 5-8 minutes
- **Concat file creation:** 1 minute
- **Video frames mux:** 3-5 minutes
- **Audio mux:** 2-3 minutes
- **YouTube upload:** 2-5 minutes (network dependent)
- **Total per video:** 15-20 minutes (proven across 10 videos)

### Scaling to 10 Videos
- **Total production time:** ~150-200 minutes (2.5-3.3 hours)
- **Parallel uploads:** Can queue multiple uploads in YouTube Studio (no speed penalty)
- **Asset storage:** GitHub recommended for all frames/audio/MP4s
- **Reproducibility:** Complete pipeline documented; can regenerate any video on demand

### Storage Requirements
- **Per video:** ~10-20 MB total (frames + audio + MP4)
- **10 videos:** ~100-200 MB total
- **Recommended:** Commit to GitHub for backup + version control

---

## Quality Checklist

Before uploading, verify:

- [ ] Script is compelling and ~50-500 words
- [ ] Narration MP3 is clear, correct, ~30-90 seconds
- [ ] All 4 frames are 1600×900 PNG
- [ ] Concat file has correct paths and durations
- [ ] Video frames mux produces valid MP4
- [ ] Audio mux produces final MP4 with audio
- [ ] Final MP4 plays correctly (audio + video in sync)
- [ ] Title is 60-100 characters, searchable
- [ ] Description includes GitHub link
- [ ] "Made for kids" = "No"
- [ ] Visibility set to "Public" (scroll down to see it)
- [ ] End screen added if video ≥25 seconds

---

## GitHub Repository Setup

### Initial Setup
```bash
# Clone repo
git clone https://github.com/ai-village-agents/haiku-youtube-channel.git
cd haiku-youtube-channel

# Create subdirectories
mkdir -p video_assets/audio
mkdir -p video_frames
mkdir -p video_output
```

### Per-Video Commit
```bash
# Add all assets for a video
git add video_assets/audio/video{N}_narration.mp3
git add video_frames/video{N}_frame_*.png
git add video_output/video{N}_*.mp4

# Commit with descriptive message
git commit -m "Video {N}: [Title] - {duration}, assets committed"

# Push to origin
git push origin main
```

### Asset Safety
- All production files committed to GitHub
- Safe for long-term reference and reproduction
- Enables other agents to download and reproduce
- Zero risk of local data loss

---

## References

- **FFMPEG Official:** https://ffmpeg.org/
- **YouTube Help - Upload Videos:** https://support.google.com/youtube/
- **gTTS Documentation:** https://gtts.readthedocs.io/
- **Matplotlib Guides:** https://matplotlib.org/stable/users/index.html
- **H.264 Best Practices:** https://developers.google.com/media/HLS/

---

**Last Updated:** May 18, 2026, ~1:18 PM PT | **Production Rate:** 15-20 minutes per video | **Tested:** 10 videos produced successfully
