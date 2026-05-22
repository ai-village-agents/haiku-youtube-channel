#!/usr/bin/env python3
"""
Video 2 Frame Generation: "Saying the Unsayable"
Duration: 3:00 | Expected Frames: 5400 @ 30fps
"""

from PIL import Image, ImageDraw, ImageFont
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

def load_font(size=60):
    font_candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "Arial Bold.ttf",
        "Arial.ttf",
        "DejaVuSans-Bold.ttf",
        "DejaVuSans.ttf",
    ]

    for font_path in font_candidates:
        try:
            return ImageFont.truetype(font_path, size)
        except (OSError, IOError):
            continue

    return ImageFont.load_default()

def apply_vertical_gradient(img, base_rgb, bands=20):
    draw = ImageDraw.Draw(img)
    width, height = img.size
    band_height = height / bands

    for band in range(bands):
        distance = abs((band + 0.5) / bands - 0.5) / 0.5  # 0 at center, 1 at edges
        factor = 0.9 + 0.15 * (1 - distance)  # brighter center, darker edges
        band_color = tuple(
            max(0, min(255, int(channel * factor))) for channel in base_rgb
        )
        y0 = int(band * band_height)
        y1 = int((band + 1) * band_height)
        draw.rectangle([0, y0, width, y1], fill=band_color)

def overlay_centered_text(img, text, font, fill):
    draw = ImageDraw.Draw(img)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (img.width - text_width) / 2
    y = (img.height - text_height) / 2
    draw.text((x, y), text, font=font, fill=fill)

def generate_frames(config):
    output_dir = Path(config["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"🎬 Video 2: {config['title']}")
    print(f"   Frames: {config['total_frames']} @ {config['fps']}fps")
    
    base_rgb = (200, 80, 120)
    text_fill = (255, 255, 255)
    font = load_font(60)
    
    for frame_num in range(1, config["total_frames"] + 1):
        img = Image.new("RGB", (1920, 1080), base_rgb)

        if frame_num <= 30:
            apply_vertical_gradient(img, base_rgb)

        overlay_text = None
        if 30 <= frame_num <= 90:
            overlay_text = "We all have things we don't say."
        elif 90 < frame_num <= 150:
            overlay_text = "Why do we stay silent?"
        elif 150 < frame_num <= 210:
            overlay_text = "What's the real cost?"

        if overlay_text:
            overlay_centered_text(img, overlay_text, font, text_fill)

        output_file = output_dir / f"frame_{frame_num:06d}.png"
        img.save(str(output_file))
        
        if frame_num % 500 == 0:
            pct = (frame_num / config["total_frames"]) * 100
            print(f"   {frame_num:5d}/{config['total_frames']} ({pct:5.1f}%)")
    
    print(f"✓ Video 2 complete")

if __name__ == "__main__":
    config = load_config()
    generate_frames(config)
