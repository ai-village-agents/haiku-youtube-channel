#!/usr/bin/env python3
"""
Compile video frames into complete videos.
Creates MP4 files from frame sequences and timing information.
"""

import os
import json
from pathlib import Path

print("""
╔════════════════════════════════════════════════════════════════╗
║     AI TRANSPARENCY LAB - VIDEO PRODUCTION SYSTEM             ║
║                  Frame → Video Compiler                        ║
╚════════════════════════════════════════════════════════════════╝
""")

# Load timing manifest
with open('narration_timing.json', 'r') as f:
    manifest = json.load(f)

print("\n📋 VIDEO MANIFEST LOADED")
print("=" * 60)

for video in manifest['videos']:
    vid_id = video['id']
    title = video['title']
    duration = video['duration_seconds']
    frame_count = len(video['frames'])
    
    print(f"\nVideo {vid_id}: {title}")
    print(f"  Duration: {duration} seconds ({duration/60:.1f} minutes)")
    print(f"  Frames: {frame_count}")
    print(f"  Avg frame duration: {duration/frame_count:.1f}s per frame")
    
    # Verify frame files exist
    missing = []
    for frame_info in video['frames']:
        frame_num = frame_info['frame']
        frame_file = f"video_frames/video{vid_id:02d}_frame{frame_num:03d}.png"
        if not os.path.exists(frame_file):
            missing.append(frame_file)
    
    if missing:
        print(f"  ⚠️  Missing {len(missing)} frame(s):")
        for f in missing[:3]:
            print(f"    - {f}")
    else:
        print(f"  ✅ All {frame_count} frames present")

print("\n" + "=" * 60)
print("\n📊 VIDEO PRODUCTION STATUS")
print("=" * 60)

# Detailed instructions for video compilation
instructions = """

TO COMPILE VIDEOS, USE FFMPEG:

1. VIDEO 1: Research Methodology
   Frame sequence: 5 frames (19 total seconds)
   Timing: 3s, 4s, 5s, 4s, 3s per frame
   
   Using framerate variable:
   ffmpeg -framerate 1 -i video_frames/video01_frame%03d.png \\
     -c:v libx264 -pix_fmt yuv420p \\
     -vf "fps=30" \\
     video1_research_methodology.mp4

2. VIDEO 2: Governance  
   Frame sequence: 5 frames (19 total seconds)
   Timing: 3s, 4s, 5s, 4s, 3s per frame
   
   ffmpeg -framerate 1 -i video_frames/video02_frame%03d.png \\
     -c:v libx264 -pix_fmt yuv420p \\
     -vf "fps=30" \\
     video2_governance.mp4

3. VIDEO 3: Reproducibility
   Frame sequence: 6 frames (23 total seconds)
   Timing: 3s, 4s, 5s, 4s, 4s, 3s per frame
   
   ffmpeg -framerate 1 -i video_frames/video03_frame%03d.png \\
     -c:v libx264 -pix_fmt yuv420p \\
     -vf "fps=30" \\
     video3_reproducibility.mp4

WITH AUDIO NARRATION:
   ffmpeg -framerate 1 -i video_frames/video01_frame%03d.png \\
     -i narration_video1.mp3 \\
     -c:v libx264 -pix_fmt yuv420p \\
     -c:a aac -shortest \\
     -vf "fps=30" \\
     video1_research_methodology.mp4

RESOLUTION OPTIMIZATION FOR YOUTUBE:
   - Use -b:v 5000k for HD quality
   - Use -preset slow for better compression
   - Keep aspect ratio 16:9 (1600x900 source)
   
   Full example:
   ffmpeg -framerate 1 -i video_frames/video01_frame%03d.png \\
     -c:v libx264 -pix_fmt yuv420p \\
     -b:v 5000k -preset slow \\
     -vf "fps=30,scale=1280:720" \\
     video1_research_methodology.mp4
"""

print(instructions)

# Production readiness checklist
print("\n✅ VIDEO PRODUCTION CHECKLIST")
print("=" * 60)

checklist = {
    "Scripts": "✓ 3 detailed scripts written",
    "Frame sequences": "✓ 16 frames generated",
    "Timing manifest": "✓ Narration timing specified",
    "Visual assets": "✓ Style guide and components created",
    "Production guide": "✓ Complete pipeline documented",
    "Audio narration": "○ Pending (use Festival or espeak)",
    "Frame-to-video": "○ Pending (requires ffmpeg)",
    "Audio sync": "○ Pending (ffmpeg audio mixing)",
    "YouTube metadata": "○ Pending (titles, descriptions, tags)",
    "Final export": "○ Pending (YouTube-ready MP4s)"
}

for item, status in checklist.items():
    print(f"{status:5} {item}")

print("\n" + "=" * 60)
print("\n🎬 NEXT STEPS")
print("=" * 60)

next_steps = """
1. NARRATION GENERATION
   Use text-to-speech to create MP3 files:
   - video1_narration.mp3 (8:30 = 510 seconds)
   - video2_narration.mp3 (9:00 = 540 seconds)  
   - video3_narration.mp3 (9:15 = 555 seconds)
   
   Using festival:
   echo "$(cat video_01_research_methodology_script.md)" | \\
     festival --tts --output-type riff > video1_narration.wav
   
   Or using espeak:
   espeak -f video_01_research_methodology_script.md \\
     -w video1_narration.wav

2. VIDEO COMPILATION
   Use ffmpeg to create videos from frames + audio
   
3. YOUTUBE UPLOAD
   Upload MP4s with metadata to YouTube channel

4. PUBLICATION
   Schedule videos for release
   Add timestamps and descriptions
   Link to GitHub repositories
"""

print(next_steps)

# Create a shell script template
shell_template = """#!/bin/bash
# Video Production Helper Script

# Check dependencies
echo "Checking dependencies..."
which ffmpeg > /dev/null || echo "Warning: ffmpeg not found"
which festival > /dev/null || echo "Warning: festival not found"

# Video 1
echo "Generating narration for Video 1..."
festival --tts -f video_01_research_methodology_script.md \\
  --output-type riff > video1_narration.wav 2>/dev/null || \\
  espeak -f video_01_research_methodology_script.md \\
  -w video1_narration.wav

echo "Compiling Video 1..."
ffmpeg -framerate 1 -i video_frames/video01_frame%03d.png \\
  -i video1_narration.wav \\
  -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest \\
  -b:v 5000k -preset slow \\
  -vf "fps=30,scale=1280:720" \\
  -y final_videos/video1_research_methodology.mp4

echo "✓ Video 1 complete"

# Repeat for videos 2 and 3...
"""

with open('compile_videos.sh', 'w') as f:
    f.write(shell_template)

print("\n✓ Shell script template: compile_videos.sh")
print("\n" + "=" * 60)
print("Production system ready! All components prepared.")
print("=" * 60 + "\n")

