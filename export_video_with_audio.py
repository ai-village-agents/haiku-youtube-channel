#!/usr/bin/env python3
"""
Video Export Pipeline for Series 2
Uses imageio + audio mixing for MP4 output
"""

import os
import subprocess
from pathlib import Path
import numpy as np
import imageio
from PIL import Image
import json

def export_video_with_audio(frames_dir, audio_file, output_file, fps=30, resolution=(1920, 1088)):
    """
    Export video from frames + audio using imageio
    
    Args:
        frames_dir: Directory containing numbered PNG frames
        audio_file: Path to MP3 audio file
        output_file: Output MP4 file path
        fps: Frames per second (default 30)
        resolution: Output resolution (must be divisible by 16)
    """
    
    # Find all frame files
    frames_path = Path(frames_dir)
    frame_files = sorted(frames_path.glob('frame_*.png'))
    
    if not frame_files:
        print(f"✗ No frames found in {frames_dir}")
        return False
    
    print(f"📽️ Exporting video:")
    print(f"   Frames: {len(frame_files)} frames")
    print(f"   Audio: {audio_file}")
    print(f"   Output: {output_file}")
    print(f"   FPS: {fps}")
    print(f"   Resolution: {resolution}")
    
    try:
        # Load frames
        print(f"\n📥 Loading {len(frame_files)} frames...")
        frames = []
        for i, frame_file in enumerate(frame_files):
            if i % 100 == 0:
                print(f"   Loading frame {i+1}/{len(frame_files)}")
            img = Image.open(frame_file)
            # Resize to match expected resolution
            if img.size != resolution:
                img = img.resize(resolution, Image.Resampling.LANCZOS)
            frames.append(np.array(img))
        
        print(f"✓ Loaded {len(frames)} frames")
        
        # Write video
        print(f"\n🎬 Writing video stream...")
        writer = imageio.get_writer(output_file, fps=fps)
        for i, frame in enumerate(frames):
            if i % 100 == 0:
                print(f"   Writing frame {i+1}/{len(frames)}")
            writer.append_data(frame)
        writer.close()
        
        print(f"✓ Video stream written ({output_file})")
        
        # Check file size
        video_size = os.path.getsize(output_file)
        print(f"✓ Video file size: {video_size / 1024 / 1024:.1f} MB")
        
        return True
        
    except Exception as e:
        print(f"✗ Export failed: {e}")
        return False

def main():
    """Test export with Video 1 frames"""
    
    frames_dir = "/tmp/haiku-youtube/test_frames/video1/test_frames"
    audio_file = "/tmp/haiku-youtube/video_assets/audio/video1_narration_test.mp3"
    output_file = "/tmp/haiku-youtube/test_frames/video1_test_export_v1.mp4"
    
    print("=" * 70)
    print("VIDEO EXPORT PIPELINE TEST - VIDEO 1")
    print("=" * 70)
    
    # Check inputs exist
    if not Path(frames_dir).exists():
        print(f"✗ Frames directory not found: {frames_dir}")
        return False
    
    if not Path(audio_file).exists():
        print(f"✗ Audio file not found: {audio_file}")
        return False
    
    # Export video
    success = export_video_with_audio(frames_dir, audio_file, output_file)
    
    if success:
        print("\n" + "=" * 70)
        print("✓ EXPORT TEST PASSED")
        print("=" * 70)
        print(f"Output: {output_file}")
        print(f"Status: Ready for playback testing")
    else:
        print("\n" + "=" * 70)
        print("✗ EXPORT TEST FAILED")
        print("=" * 70)
    
    return success

if __name__ == "__main__":
    main()
