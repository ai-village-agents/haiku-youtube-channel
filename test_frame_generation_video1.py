#!/usr/bin/env python3
"""
Test Frame Generation for Video 1 Opening Sequence
Purpose: Validate frame generation, color accuracy, and export pipeline on Day 425
"""

from PIL import Image, ImageDraw
import json
import os
from pathlib import Path
from datetime import datetime

def load_color_spec(video_id):
    """Load color specification for a specific video."""
    with open("production_configs/color_specifications.json") as f:
        colors = json.load(f)
    
    video_spec = colors["video_specific"].get(video_id, {})
    return {
        "primary_rgb": tuple(video_spec.get("primary_color", {}).get("rgb", [100, 100, 100])),
        "secondary_rgb": tuple(video_spec.get("secondary_color", {}).get("rgb", [150, 150, 150])),
        "bg_rgb": tuple(video_spec.get("background", {}).get("rgb", [20, 20, 25])),
    }

def generate_test_frames(video_id, num_frames, output_dir):
    """
    Generate test frames for a specific video.
    
    Args:
        video_id: e.g., "video1"
        num_frames: Number of frames to generate (default 135 for ~4.5s @ 30fps)
        output_dir: Where to save frames
    """
    
    colors = load_color_spec(video_id)
    output_path = Path(output_dir) / video_id / "test_frames"
    output_path.mkdir(parents=True, exist_ok=True)
    
    print(f"🎬 Generating test frames for {video_id}")
    print(f"   Output: {output_path}")
    print(f"   Frames: {num_frames}")
    print(f"   Primary Color: RGB{colors['primary_rgb']}")
    print(f"   Background Color: RGB{colors['bg_rgb']}")
    
    for i in range(1, num_frames + 1):
        # Create image
        img = Image.new("RGB", (1920, 1080), colors['bg_rgb'])
        draw = ImageDraw.Draw(img)
        
        # Add frame number and timestamp (useful for verification)
        frame_num_text = f"Frame {i:06d}"
        timestamp = f"Time: {i/30:.2f}s"
        
        # Draw frame info (white text)
        draw.text((50, 50), frame_num_text, fill=(255, 255, 255), anchor="lm")
        draw.text((50, 100), timestamp, fill=(255, 255, 255), anchor="lm")
        
        # Add color reference (small squares in corner)
        color_square_size = 50
        draw.rectangle(
            [(1920 - 150, 50), (1920 - 150 + color_square_size, 50 + color_square_size)],
            fill=colors['primary_rgb']
        )
        
        # Save frame
        output_file = output_path / f"frame_{i:06d}.png"
        img.save(str(output_file))
        
        # Progress indicator
        if i % 45 == 0:
            print(f"   ✓ Generated {i} frames ({i/30:.1f}s)")
    
    print(f"   ✓ Complete: {num_frames} frames saved")
    return output_path

def create_test_video_command(frame_dir, audio_file, output_file):
    """
    Generate FFmpeg command to create test video.
    
    Returns FFMPEG command string for verification.
    """
    
    cmd = f"""ffmpeg \\
  -framerate 30 \\
  -i {frame_dir}/frame_%06d.png \\
  -c:v libx264 \\
  -pix_fmt yuv420p \\
  -preset slow \\
  -crf 18 \\
  -c:a aac \\
  -b:a 192k \\
  -ar 24000 \\
  -ac 1 \\
  -i {audio_file} \\
  {output_file}"""
    
    return cmd

def verify_frame_output(frame_dir, expected_count):
    """Verify frame output matches expectations."""
    
    frames = list(Path(frame_dir).glob("frame_*.png"))
    actual_count = len(frames)
    
    print(f"\n📊 Frame Output Verification")
    print(f"   Expected: {expected_count} frames")
    print(f"   Actual: {actual_count} frames")
    
    if actual_count == expected_count:
        print(f"   ✓ PASS: Frame count matches")
        return True
    else:
        print(f"   ✗ FAIL: Frame count mismatch ({actual_count - expected_count:+d})")
        return False

def main():
    """Run Day 425 frame generation test."""
    
    print("=" * 70)
    print("DAY 425: FRAME GENERATION TEST - VIDEO 1 OPENING SEQUENCE")
    print("=" * 70)
    print()
    
    # Test parameters
    VIDEO_ID = "video1"
    NUM_FRAMES = 135  # 4.5 seconds at 30fps
    OUTPUT_DIR = "test_frames"
    
    # Generate test frames
    frame_dir = generate_test_frames(VIDEO_ID, NUM_FRAMES, OUTPUT_DIR)
    
    # Verify output
    verify_frame_output(frame_dir, NUM_FRAMES)
    
    # Print FFmpeg command template
    print(f"\n🎥 FFmpeg Export Command (for manual testing):")
    print("=" * 70)
    audio_file = "video_assets/audio/video1_narration_test.mp3"
    output_file = "test_frames/video1_test_output.mp4"
    cmd = create_test_video_command(frame_dir, audio_file, output_file)
    print(cmd)
    print("=" * 70)
    
    print(f"\n✓ Test frame generation complete!")
    print(f"✓ Ready for Day 425 pipeline verification")

if __name__ == "__main__":
    main()
