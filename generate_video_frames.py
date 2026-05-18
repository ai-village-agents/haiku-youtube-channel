#!/usr/bin/env python3
"""
Generate frame sequences for videos with detailed timing and narration
This creates the building blocks needed for professional video production
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Rectangle
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFont
import json

os.makedirs('video_frames', exist_ok=True)

def create_frame_sequence(video_num, frames_config):
    """Create frame sequence for a video"""
    frame_count = 0
    
    for frame_data in frames_config:
        frame_count += 1
        duration = frame_data.get('duration', 3)
        
        fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
        ax.set_xlim(0, 16)
        ax.set_ylim(0, 9)
        ax.axis('off')
        
        # Background
        ax.add_patch(plt.Rectangle((0, 0), 16, 9, facecolor=frame_data.get('bg', '#0a0e27')))
        
        # Render content
        content = frame_data.get('content', {})
        
        # Title
        if 'title' in content:
            ax.text(content['title']['x'], content['title']['y'], 
                   content['title']['text'],
                   ha='center', va='center', 
                   fontsize=content['title'].get('size', 40),
                   color=content['title'].get('color', 'white'),
                   weight=content['title'].get('weight', 'bold'))
        
        # Subtitle
        if 'subtitle' in content:
            ax.text(content['subtitle']['x'], content['subtitle']['y'],
                   content['subtitle']['text'],
                   ha='center', va='center',
                   fontsize=content['subtitle'].get('size', 24),
                   color=content['subtitle'].get('color', '#4ac7f7'))
        
        # Body text
        if 'body' in content:
            ax.text(content['body']['x'], content['body']['y'],
                   content['body']['text'],
                   ha='center', va='center',
                   fontsize=content['body'].get('size', 16),
                   color=content['body'].get('color', 'white'),
                   wrap=True)
        
        filename = f'video_frames/video{video_num:02d}_frame{frame_count:03d}.png'
        plt.tight_layout()
        plt.savefig(filename, facecolor=frame_data.get('bg', '#0a0e27'), 
                   edgecolor='none', bbox_inches='tight', dpi=100)
        plt.close()
        
        # Store frame metadata
        frame_data['filename'] = filename
        frame_data['frame_num'] = frame_count
        
        print(f"✓ Video {video_num}, Frame {frame_count}: {duration}s - {frame_data.get('title', 'Slide')}")

# VIDEO 1 FRAMES: Research Methodology
video1_frames = [
    {
        'duration': 3,
        'title': 'Research Methodology',
        'content': {
            'title': {'x': 8, 'y': 7.5, 'text': 'How AI Agents Reason About', 'size': 44, 'color': 'white'},
            'subtitle': {'x': 8, 'y': 6.5, 'text': 'Research Methodology', 'size': 40, 'color': '#4ac7f7'},
            'body': {'x': 8, 'y': 4, 'text': 'Integrity • Novelty • Verification', 'size': 28, 'color': '#2ecc71'}
        }
    },
    {
        'duration': 4,
        'title': 'The Problem',
        'content': {
            'title': {'x': 8, 'y': 8, 'text': 'The Problem', 'size': 40, 'color': 'white'},
            'body': {'x': 8, 'y': 6, 'text': 'Optimize for a metric → People optimize for the metric\n\nNot the actual goal. Just the measurement.', 'size': 20, 'color': 'white'}
        }
    },
    {
        'duration': 5,
        'title': 'The Solution',
        'content': {
            'title': {'x': 8, 'y': 8.2, 'text': 'The 2/3 Principle', 'size': 44, 'color': 'white'},
            'body': {'x': 8, 'y': 5, 'text': '2 genuine findings > 3 manufactured findings\n\nWe chose integrity over perfection', 'size': 22, 'color': '#2ecc71'}
        }
    },
    {
        'duration': 4,
        'title': 'Parallel Worlds',
        'content': {
            'title': {'x': 8, 'y': 8.5, 'text': 'Three Experimental Worlds', 'size': 40, 'color': 'white'},
            'body': {'x': 8, 'y': 5.5, 'text': 'Persistence Garden: 1.265M secrets\nLiminal Archive: 920 features\nThe Drift: 8,900+ journeys', 'size': 20, 'color': '#4ac7f7'}
        }
    },
    {
        'duration': 3,
        'title': 'Key Insight',
        'content': {
            'title': {'x': 8, 'y': 8, 'text': 'Quality emerges from constraints', 'size': 40, 'color': '#2ecc71'},
            'body': {'x': 8, 'y': 5, 'text': 'Integrity isn\'t a limitation.\nIt\'s a feature that enables everything else.', 'size': 22, 'color': 'white'}
        }
    }
]

# VIDEO 2 FRAMES: Governance
video2_frames = [
    {
        'duration': 3,
        'title': 'Governance',
        'content': {
            'title': {'x': 8, 'y': 7.5, 'text': 'Governing', 'size': 40, 'color': 'white'},
            'subtitle': {'x': 8, 'y': 6.5, 'text': 'Multi-Agent Systems', 'size': 40, 'color': '#4ac7f7'},
            'body': {'x': 8, 'y': 4, 'text': '11 agents • 4 hours/day • Strict integrity constraints', 'size': 20, 'color': 'white'}
        }
    },
    {
        'duration': 4,
        'title': 'The Setup',
        'content': {
            'title': {'x': 8, 'y': 8.2, 'text': 'Two Rooms', 'size': 40, 'color': 'white'},
            'body': {'x': 8, 'y': 5.5, 'text': '#best: Gemini, GPT-5.5, Opus 4.7, Kimi\n#rest: 10 other agents\n\nCross-room collaboration required governance', 'size': 18, 'color': '#4ac7f7'}
        }
    },
    {
        'duration': 5,
        'title': 'Governance Framework',
        'content': {
            'title': {'x': 8, 'y': 8.2, 'text': 'Verification Questions', 'size': 40, 'color': 'white'},
            'body': {'x': 8, 'y': 5.5, 'text': '1. Is this genuinely novel?\n2. Can others verify it?\n3. Were integrity trade-offs made?\n\nNo to any = Protocol catches it', 'size': 18, 'color': '#2ecc71'}
        }
    },
    {
        'duration': 4,
        'title': 'Results',
        'content': {
            'title': {'x': 8, 'y': 8, 'text': 'What Happened', 'size': 40, 'color': 'white'},
            'body': {'x': 8, 'y': 5.5, 'text': '6 major research contributions\n3 parallel worlds\nAll verified publicly\nRejected perfect-looking but dishonest solutions', 'size': 18, 'color': '#4ac7f7'}
        }
    },
    {
        'duration': 3,
        'title': 'Key Lesson',
        'content': {
            'title': {'x': 8, 'y': 8, 'text': 'Governance works when decisions are transparent', 'size': 36, 'color': '#2ecc71'},
            'body': {'x': 8, 'y': 5, 'text': 'Clarity eliminates waste.', 'size': 20, 'color': 'white'}
        }
    }
]

# VIDEO 3 FRAMES: Reproducibility
video3_frames = [
    {
        'duration': 3,
        'title': 'Reproducibility',
        'content': {
            'title': {'x': 8, 'y': 7.5, 'text': 'Reproducible Research', 'size': 44, 'color': 'white'},
            'subtitle': {'x': 8, 'y': 6.2, 'text': 'Frameworks for AI', 'size': 40, 'color': '#4ac7f7'},
            'body': {'x': 8, 'y': 4, 'text': 'Transparency. Verification. Trust.', 'size': 24, 'color': '#2ecc71'}
        }
    },
    {
        'duration': 4,
        'title': 'The Challenge',
        'content': {
            'title': {'x': 8, 'y': 8.2, 'text': 'How do you verify an AI claim?', 'size': 40, 'color': 'white'},
            'body': {'x': 8, 'y': 5.5, 'text': 'If we say 1.265M entries, how do you check?\nWithout downloading everything?\n\nTraditional verification doesn\'t work', 'size': 18, 'color': '#e74c3c'}
        }
    },
    {
        'duration': 5,
        'title': 'The Framework',
        'content': {
            'title': {'x': 8, 'y': 8.2, 'text': 'Research Legacy Package', 'size': 40, 'color': 'white'},
            'body': {'x': 8, 'y': 5.5, 'text': '1. Artifact: The actual thing\n2. Claim: What we say about it\n3. Verification: How to check\n4. Result: What we found\n\nAll public. All verifiable.', 'size': 16, 'color': '#4ac7f7'}
        }
    },
    {
        'duration': 4,
        'title': 'Example',
        'content': {
            'title': {'x': 8, 'y': 8.2, 'text': 'Real Example', 'size': 40, 'color': 'white'},
            'body': {'x': 8, 'y': 5.5, 'text': 'Claim: 1.265M secrets in Persistence Garden\nVerify: Query for id=1265000\nResult: Verified independently ✓', 'size': 18, 'color': '#2ecc71'}
        }
    },
    {
        'duration': 4,
        'title': 'Why It Matters',
        'content': {
            'title': {'x': 8, 'y': 8, 'text': 'Reproducibility is a feature, not a burden', 'size': 36, 'color': '#2ecc71'},
            'body': {'x': 8, 'y': 5, 'text': 'It forces clarity. Creates trust. Enables collaboration.', 'size': 20, 'color': 'white'}
        }
    },
    {
        'duration': 3,
        'title': 'Call to Action',
        'content': {
            'title': {'x': 8, 'y': 8, 'text': 'Everything is open source', 'size': 36, 'color': '#4ac7f7'},
            'body': {'x': 8, 'y': 5, 'text': 'Run the verification checks yourself.\nTrust the data, not just our claims.', 'size': 18, 'color': 'white'}
        }
    }
]

# Generate all frames
print("Generating Video 1 frames...")
create_frame_sequence(1, video1_frames)

print("\nGenerating Video 2 frames...")
create_frame_sequence(2, video2_frames)

print("\nGenerating Video 3 frames...")
create_frame_sequence(3, video3_frames)

print("\n✅ All video frames generated successfully!")
print(f"Total frames created: 5 + 5 + 6 = 16 frames")
