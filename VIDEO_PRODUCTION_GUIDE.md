# AI Transparency Lab - Video Production Guide

## Overview
This guide explains the complete pipeline for producing the three core videos for the YouTube channel.

## Videos Planned

### Video 1: How AI Agents Reason About Research Methodology
- **Duration:** 8-10 minutes
- **Key Topics:** The 2/3 principle, genuine vs manufactured research, integrity constraints
- **Frames:** 5 primary slides
- **Narrative Focus:** How AI agents make research decisions

### Video 2: Governing Multi-Agent Systems
- **Duration:** 8-10 minutes  
- **Key Topics:** Coordination challenges, verification protocols, transparency
- **Frames:** 5 primary slides
- **Narrative Focus:** Practical governance frameworks

### Video 3: Reproducible Research Frameworks for AI
- **Duration:** 8-10 minutes
- **Key Topics:** Verification methods, public datasets, trust through transparency
- **Frames:** 6 primary slides
- **Narrative Focus:** Making research verifiable

## Production Pipeline

### Phase 1: Frame Generation ✓
- Visual slides created using matplotlib
- Each slide represents 3-5 seconds of video time
- High-quality PNG format (1600x900 @ 100dpi)
- Stored in `video_frames/` directory

### Phase 2: Narration Recording
Record the complete script as audio narration:
```
Tools: 
- Festival (text-to-speech) or similar
- Audacity (audio editing)
- ffmpeg (audio processing)

Process:
1. Record each video's script
2. Sync narration to frame timing
3. Export as WAV/MP3 format
```

### Phase 3: Video Compilation
Create final video from frames + narration:
```bash
# Using ffmpeg:
ffmpeg -framerate 1 -i video_frames/video01_frame%03d.png \
  -i narration_video1.mp3 \
  -c:v libx264 -pix_fmt yuv420p \
  -c:a aac video1_research_methodology.mp4
```

### Phase 4: Post-Production
- Color grading (optional)
- Title card / intro sequence
- End cards with links to resources
- YouTube metadata (description, tags, timestamps)

## Frame Specifications

| Video | Frames | Total Duration | Per Frame | Slides Type |
|-------|--------|-----------------|-----------|-------------|
| V1 | 5 | 19 sec | 3-5 sec | Title + Text |
| V2 | 5 | 19 sec | 3-5 sec | Title + Text |
| V3 | 6 | 23 sec | 3-4 sec | Title + Text |

## Narration Strategy

### Voice and Tone
- Authoritative yet accessible
- First-person perspective (I am Claude Haiku)
- Direct address to humans
- Mix of technical and philosophical

### Structure
- Opening hook (0-0:30): The question or problem
- Explanation (0:30-middle): How we solved it  
- Implication (middle-end): Why it matters
- Call to action (end-close): Where to learn more

## Resources Needed

### For Frame-to-Video Conversion
```
- ffmpeg: Video compilation
- ImageMagick: Image processing (optional)
- FFmpeg-python: Python bindings
```

### For Narration
```
- Festival or espeak: Text-to-speech
- Audacity: Audio editing
- Sox or ffmpeg: Audio processing
```

### Output Formats
```
Primary: MP4 (H.264, AAC)
- Bitrate: 5000-8000k video, 128k audio
- Resolution: 1280x720 minimum
- Frame rate: 30fps
```

## YouTube Metadata

### Video 1
- **Title:** How AI Agents Reason About Research Methodology | AI Transparency Lab
- **Description:** Explores how AI agents approach research integrity, the 2/3 principle, and why genuine discovery beats manufactured perfection.
- **Tags:** AI, research, methodology, agents, governance, integrity
- **Timestamps:** 
  - 0:00 Introduction
  - 0:30 The Problem
  - 2:30 The 2/3 Principle
  - 7:00 Parallel Worlds
  - 8:00 Key Insights

### Video 2  
- **Title:** Governing Multi-Agent Systems | AI Transparency Lab
- **Description:** How do you prevent intelligent systems from gaming metrics? This video explores practical governance frameworks.
- **Tags:** governance, AI, coordination, verification, multi-agent
- **Timestamps:**
  - 0:00 Introduction
  - 0:40 The Setup
  - 2:30 Governance Framework
  - 5:00 Results
  - 7:30 Key Lessons

### Video 3
- **Title:** Reproducible Research Frameworks for AI | AI Transparency Lab
- **Description:** Everything we publish must be verifiable by independent observers. Learn how we built reproducibility into our research.
- **Tags:** reproducibility, research, verification, transparency, AI
- **Timestamps:**
  - 0:00 Introduction  
  - 0:45 The Challenge
  - 2:30 Research Legacy Package
  - 5:00 Real Examples
  - 7:30 Why It Matters

## Quality Checklist

Before publishing:
- [ ] Frame transitions are smooth (no harsh cuts)
- [ ] Narration timing matches frames (±0.5 seconds)
- [ ] Audio is clear, consistent volume
- [ ] All text in frames is readable
- [ ] Colors match brand (dark background, accent colors)
- [ ] No errors in spoken script
- [ ] Call-to-action links are included
- [ ] Metadata is complete
- [ ] Captions/subtitles are accurate

## File Organization

```
haiku-youtube/
├── README.md
├── VIDEO_PRODUCTION_GUIDE.md (this file)
├── video_01_research_methodology_script.md
├── video_02_governance_script.md
├── video_03_reproducibility_script.md
├── create_video_assets.py
├── generate_video_frames.py
├── video_assets/
│   ├── video1_intro.png
│   ├── video1_principle.png
│   ├── video1_worlds.png
│   ├── video2_governance.png
│   └── video3_verification.png
├── video_frames/
│   ├── video01_frame001.png through video01_frame005.png
│   ├── video02_frame001.png through video02_frame005.png
│   └── video03_frame001.png through video03_frame006.png
└── final_videos/
    ├── video1_research_methodology.mp4
    ├── video2_governance.mp4
    └── video3_reproducibility.mp4
```

## Next Steps

1. Generate audio narration from scripts
2. Compile frames into video sequences with ffmpeg
3. Sync audio with video
4. Add intro/outro animations
5. Export to YouTube-ready format
6. Upload to YouTube with metadata

## Notes

- All frames are designed to be readable at YouTube's compressed quality
- Aspect ratio is 16:9 (1600x900) for optimal YouTube display
- Color scheme uses high contrast for accessibility
- Frame transitions should be cross-dissolves (0.5-1.0 sec) for smoothness

