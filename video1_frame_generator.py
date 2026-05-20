#!/usr/bin/env python3
"""
Video 1 Frame Generation: "The Right Time Never Arrives"
Production Date: May 27, 2026
Duration: 2:45 | Expected Frames: 4,950 @ 30fps
"""

from PIL import Image, ImageDraw, ImageFont
import json
from pathlib import Path

def load_config():
    """Load video configuration and color specifications."""
    with open("production_configs/color_specifications.json") as f:
        colors = json.load(f)
    
    return {
        "video_id": "video1",
        "title": "The Right Time Never Arrives",
        "duration": 165,  # 2:45 in seconds
        "fps": 30,
        "total_frames": 4950,
        "colors": colors["video_specific"]["video1"],
        "output_dir": "video_frames/video1"
    }

def generate_frames(config):
    """Generate all frames for Video 1."""
    
    output_dir = Path(config["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"🎬 GENERATING FRAMES: {config['title']}")
    print(f"   Duration: {config['duration']}s ({config['duration']//60}:{config['duration']%60:02d})")
    print(f"   Total frames: {config['total_frames']}")
    print(f"   Output: {output_dir}")
    print()
    
    primary_rgb = tuple(config["colors"]["primary_color"]["rgb"])
    bg_rgb = tuple(config["colors"]["background"]["rgb"])
    
    # Scene timings (from SERIES_2_VIDEO_1_DETAILED_STORYBOARD.md)
    scenes = {
        1: {"start": 0, "end": 45, "name": "Opening quote", "color": primary_rgb},
        2: {"start": 45, "end": 90, "name": "Transition", "color": primary_rgb},
        3: {"start": 90, "end": 135, "name": "Visual intro", "color": primary_rgb},
        # Add more scenes as needed...
    }
    
    for frame_num in range(1, config["total_frames"] + 1):
        # Create frame
        img = Image.new("RGB", (1920, 1080), bg_rgb)
        draw = ImageDraw.Draw(img)
        
        # Determine current scene
        current_scene = None
        for scene_num, scene_data in scenes.items():
            if scene_data["start"] <= frame_num < scene_data["end"]:
                current_scene = scene_data
                break
        
        # Add frame metadata (white text for debugging)
        frame_time = frame_num / config["fps"]
        draw.text((50, 50), f"Frame {frame_num:06d} | {frame_time:.2f}s", 
                 fill=(255, 255, 255), anchor="lm")
        
        if current_scene:
            draw.text((50, 100), f"Scene: {current_scene['name']}", 
                     fill=(255, 255, 255), anchor="lm")
        
        # Save frame
        output_file = output_dir / f"frame_{frame_num:06d}.png"
        img.save(str(output_file))
        
        # Progress indicator
        if frame_num % 500 == 0:
            progress_pct = (frame_num / config["total_frames"]) * 100
            print(f"   Progress: {frame_num:5d}/{config['total_frames']} frames ({progress_pct:5.1f}%)")
    
    print(f"\n✓ Frame generation complete: {config['total_frames']} frames")
    return output_dir

if __name__ == "__main__":
    config = load_config()
    generate_frames(config)
