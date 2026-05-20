#!/usr/bin/env python3
"""
Create color profile files for Series 2 production
Based on SERIES_2_VISUAL_STYLE_GUIDE.md specifications
"""

import json
import os

# Color specifications from the visual style guide
COLOR_SPECS = {
    "base": {
        "background": {"rgb": [20, 20, 25], "hex": "#141419", "name": "Deep Charcoal"},
        "primary_text": {"rgb": [220, 160, 80], "hex": "#dca050", "name": "Gold/Warm"},
        "secondary": {"rgb": [180, 100, 140], "hex": "#b4648c", "name": "Mauve/Deep Rose"},
        "tertiary": {"rgb": [100, 160, 200], "hex": "#64a0c8", "name": "Blue/Teal"},
        "highlights": {"rgb": [245, 245, 245], "hex": "#f5f5f5", "name": "Near White"},
    },
    "video_specific": {
        "video1": {
            "title": "The Right Time Never Arrives",
            "primary_color": {"rgb": [220, 160, 80], "hex": "#dca050", "name": "Gold/Amber"},
            "secondary_color": {"rgb": [100, 160, 200], "hex": "#64a0c8", "name": "Blue accents"},
            "background": {"rgb": [20, 20, 25], "hex": "#141419", "name": "Deep Charcoal"},
        },
        "video2": {
            "title": "Saying the Unsayable",
            "primary_color": {"rgb": [200, 80, 120], "hex": "#c85078", "name": "Red/Crimson"},
            "secondary_color": {"rgb": [220, 160, 80], "hex": "#dca050", "name": "Gold accents"},
            "background": {"rgb": [20, 20, 25], "hex": "#141419", "name": "Deep Charcoal"},
        },
        "video3": {
            "title": "The Maps We Build",
            "primary_color": {"rgb": [100, 160, 200], "hex": "#64a0c8", "name": "Blue/Teal"},
            "secondary_color": {"rgb": [140, 140, 150], "hex": "#8c8c96", "name": "Gray"},
            "background": {"rgb": [20, 20, 25], "hex": "#141419", "name": "Deep Charcoal"},
            "color_arc": [
                {"rgb": [100, 160, 200], "hex": "#64a0c8", "label": "Teal (opening)"},
                {"rgb": [140, 140, 150], "hex": "#8c8c96", "label": "Gray (decay)"},
                {"rgb": [240, 245, 250], "hex": "#f0f5fa", "label": "White (dissolution)"},
                {"rgb": [200, 230, 245], "hex": "#c8e6f5", "label": "Pale Blue (emergence)"},
            ],
        },
        "video4": {
            "title": "The Gift of Disappointment",
            "primary_color": {"rgb": [160, 100, 140], "hex": "#a0648c", "name": "Purple"},
            "secondary_color": {"rgb": [220, 180, 100], "hex": "#dcb464", "name": "Gold"},
            "background": {"rgb": [20, 20, 25], "hex": "#141419", "name": "Deep Charcoal"},
            "color_arc": [
                {"rgb": [160, 100, 140], "hex": "#a0648c", "label": "Purple (opening)"},
                {"rgb": [200, 140, 80], "hex": "#c88c50", "label": "Orange (recognition)"},
                {"rgb": [220, 180, 100], "hex": "#dcb464", "label": "Gold (teaching)"},
            ],
        },
        "video5": {
            "title": "The Privilege of Choice",
            "primary_color": {"rgb": [220, 140, 60], "hex": "#dc8c3c", "name": "Orange"},
            "secondary_color": {"rgb": [240, 200, 100], "hex": "#f0c864", "name": "Pale Gold"},
            "background": {"rgb": [20, 20, 25], "hex": "#141419", "name": "Deep Charcoal"},
            "color_arc": [
                {"rgb": [220, 140, 60], "hex": "#dc8c3c", "label": "Bright Orange (opening)"},
                {"rgb": [180, 120, 50], "hex": "#b47832", "label": "Rust (multiplying)"},
                {"rgb": [100, 70, 50], "hex": "#644632", "label": "Brown (overwhelm)"},
                {"rgb": [220, 140, 60], "hex": "#dc8c3c", "label": "Orange (choice)"},
            ],
        },
        "video6": {
            "title": "What We Fear Speaking Into Being",
            "primary_color": {"rgb": [240, 245, 250], "hex": "#f0f5fa", "name": "White/Silver"},
            "secondary_color": {"rgb": [0, 0, 0], "hex": "#000000", "name": "Black"},
            "background": {"rgb": [0, 0, 0], "hex": "#000000", "name": "Black"},
            "color_arc": [
                {"rgb": [0, 0, 0], "hex": "#000000", "label": "Black (fear)"},
                {"rgb": [240, 245, 250], "hex": "#f0f5fa", "label": "White (revelation)"},
                {"rgb": [255, 255, 255], "hex": "#ffffff", "label": "Full White (power)"},
            ],
        },
    },
    "technical_specs": {
        "resolution": "1920x1080",
        "fps": 30,
        "codec": "H.264 High profile",
        "color_space": "yuv420p",
        "audio_codec": "AAC",
        "audio_bitrate": "192k",
        "audio_sample_rate": "24kHz",
        "audio_channels": "mono",
    },
}

# Create output directory
output_dir = '/tmp/haiku-youtube/production_configs'
os.makedirs(output_dir, exist_ok=True)

# Save the complete color specifications
spec_path = os.path.join(output_dir, 'color_specifications.json')
with open(spec_path, 'w') as f:
    json.dump(COLOR_SPECS, f, indent=2)
print(f"✓ Color specifications saved: {spec_path}")

# Create individual video color files
for video_id, specs in COLOR_SPECS['video_specific'].items():
    video_path = os.path.join(output_dir, f'{video_id}_colors.json')
    with open(video_path, 'w') as f:
        json.dump(specs, f, indent=2)
    print(f"✓ Video color config: {video_path}")

# Create a color reference document
ref_path = os.path.join(output_dir, 'COLOR_REFERENCE.md')
with open(ref_path, 'w') as f:
    f.write("# Series 2 Production Color Reference\n\n")
    f.write("## Base Colors (Used Across Series)\n\n")
    for color_name, color_spec in COLOR_SPECS['base'].items():
        rgb = color_spec['rgb']
        hex_val = color_spec['hex']
        name = color_spec['name']
        f.write(f"- **{color_name}**: RGB({rgb[0]}, {rgb[1]}, {rgb[2]}) | {hex_val} | {name}\n")
    
    f.write("\n## Video-Specific Colors\n\n")
    for video_id, specs in COLOR_SPECS['video_specific'].items():
        f.write(f"### {video_id.upper()}: {specs.get('title', 'N/A')}\n\n")
        f.write(f"**Primary**: RGB({specs['primary_color']['rgb'][0]}, {specs['primary_color']['rgb'][1]}, {specs['primary_color']['rgb'][2]}) | {specs['primary_color']['hex']} | {specs['primary_color']['name']}\n\n")
        f.write(f"**Secondary**: RGB({specs['secondary_color']['rgb'][0]}, {specs['secondary_color']['rgb'][1]}, {specs['secondary_color']['rgb'][2]}) | {specs['secondary_color']['hex']} | {specs['secondary_color']['name']}\n\n")
        
        if 'color_arc' in specs:
            f.write("**Color Arc (Transition sequence):**\n\n")
            for i, color in enumerate(specs['color_arc'], 1):
                f.write(f"  {i}. RGB({color['rgb'][0]}, {color['rgb'][1]}, {color['rgb'][2]}) | {color['hex']} | {color['label']}\n")
            f.write("\n")

print(f"✓ Color reference document: {ref_path}")

print("\n" + "="*60)
print("COLOR PROFILE SETUP COMPLETE")
print("="*60)
print(f"\nAll color files created in: {output_dir}")
print("\nReady for animation production:")
print("  ✓ RGB color specs locked")
print("  ✓ Video-specific configs generated")
print("  ✓ Color arc transitions documented")
print("  ✓ Technical specs confirmed")
