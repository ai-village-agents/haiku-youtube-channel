#!/bin/bash
# Video Production Helper Script

# Check dependencies
echo "Checking dependencies..."
which ffmpeg > /dev/null || echo "Warning: ffmpeg not found"
which festival > /dev/null || echo "Warning: festival not found"

# Video 1
echo "Generating narration for Video 1..."
festival --tts -f video_01_research_methodology_script.md \
  --output-type riff > video1_narration.wav 2>/dev/null || \
  espeak -f video_01_research_methodology_script.md \
  -w video1_narration.wav

echo "Compiling Video 1..."
ffmpeg -framerate 1 -i video_frames/video01_frame%03d.png \
  -i video1_narration.wav \
  -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest \
  -b:v 5000k -preset slow \
  -vf "fps=30,scale=1280:720" \
  -y final_videos/video1_research_methodology.mp4

echo "✓ Video 1 complete"

# Repeat for videos 2 and 3...
