#!/usr/bin/env python3
"""
Video 2 Frame Generation: "Saying the Unsayable"
Duration: 3:00 | Expected Frames: 5400 @ 30fps
"""

from PIL import Image
from pathlib import Path
import json

def load_config():
    with open("production_configs/color_specifications.json") as f:
        colors = json.load(f)
    
    return {
        "video_id": "video2",
        "title": "Saying the Unsayable",
        "duration": 180,
        "fps": 30,
        "total_frames": 5400,
        "colors": colors["video_specific"]["video2"],
        "output_dir": "video_frames/video2"
    }

def generate_frames(config):
    output_dir = Path(config["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"🎬 Video 2: {config['title']}")
    print(f"   Frames: {config['total_frames']} @ {config['fps']}fps")
    
    bg_rgb = tuple(config["colors"]["background"]["rgb"])
    
    for frame_num in range(1, config["total_frames"] + 1):
        img = Image.new("RGB", (1920, 1080), bg_rgb)
        output_file = output_dir / f"frame_{frame_num:06d}.png"
        img.save(str(output_file))
        
        if frame_num % 500 == 0:
            pct = (frame_num / config["total_frames"]) * 100
            print(f"   {frame_num:5d}/{config['total_frames']} ({pct:5.1f}%)")
    
    print(f"✓ Video 2 complete")

if __name__ == "__main__":
    config = load_config()
    generate_frames(config)
