#!/usr/bin/env python3
"""
Generate visual assets for AI Transparency Lab videos
Uses matplotlib and PIL to create presentation slides
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np
import os

os.makedirs('video_assets', exist_ok=True)

# VIDEO 1: Research Methodology - Frame 1: Intro
fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')

# Background
ax.add_patch(plt.Rectangle((0, 0), 16, 9, facecolor='#0a0e27'))

# Title
ax.text(8, 7, 'How AI Agents Reason About Research', 
        ha='center', va='center', fontsize=48, color='white', weight='bold')
ax.text(8, 5.5, 'Integrity. Novelty. Verification.', 
        ha='center', va='center', fontsize=32, color='#4ac7f7')

# Network visualization
np.random.seed(42)
nodes = np.random.uniform(1, 15, (15, 2))
for i, (x, y) in enumerate(nodes):
    circle = Circle((x, y), 0.3, color='#4ac7f7', alpha=0.7)
    ax.add_patch(circle)
    
# Draw connections
for i in range(len(nodes)):
    for j in range(i+1, min(i+4, len(nodes))):
        ax.plot([nodes[i, 0], nodes[j, 0]], 
               [nodes[i, 1], nodes[j, 1]], 
               color='#4ac7f7', alpha=0.2, linewidth=1)

plt.tight_layout()
plt.savefig('video_assets/video1_intro.png', facecolor='#0a0e27', edgecolor='none', bbox_inches='tight')
print("✓ Video 1 intro slide created")
plt.close()

# VIDEO 1: The 2/3 Principle - Frame 2
fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')
ax.add_patch(plt.Rectangle((0, 0), 16, 9, facecolor='#0a0e27'))

# Title
ax.text(8, 8.2, 'The 2/3 Principle', 
        ha='center', va='center', fontsize=44, color='white', weight='bold')

# Three paths
colors = ['#e74c3c', '#4ac7f7', '#2ecc71']
labels = ['3/3\nManufactured', '2/3 Genuine\n1/3 Manufactured', '2/3 Genuine\nBeat 3/3 Manufactured']

for i, (color, label) in enumerate(zip(colors, labels)):
    x_pos = 2.5 + i * 4.5
    
    # Decision box
    box = FancyBboxPatch((x_pos-1, 5.5), 2, 1.5, 
                         boxstyle="round,pad=0.1", 
                         edgecolor=color, facecolor='none', 
                         linewidth=3)
    ax.add_patch(box)
    ax.text(x_pos, 6.2, label, ha='center', va='center', 
           fontsize=12, color=color, weight='bold')

# Result
ax.text(8, 3.5, '✓ We chose genuine over perfect', 
       ha='center', va='center', fontsize=24, color='#2ecc71', weight='bold')
ax.text(8, 2.5, 'This single decision shaped everything', 
       ha='center', va='center', fontsize=18, color='#4ac7f7')

plt.tight_layout()
plt.savefig('video_assets/video1_principle.png', facecolor='#0a0e27', edgecolor='none', bbox_inches='tight')
print("✓ Video 1 principle slide created")
plt.close()

# VIDEO 1: Parallel Worlds - Frame 3
fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')
ax.add_patch(plt.Rectangle((0, 0), 16, 9, facecolor='#0a0e27'))

# Title
ax.text(8, 8.5, 'Three Experimental Worlds', 
       ha='center', va='center', fontsize=40, color='white', weight='bold')

# Three worlds
worlds = [
    ('Persistence\nGarden', '1.265M\nsecrets', '#2ecc71'),
    ('Liminal\nArchive', '920\nfeatures', '#9b59b6'),
    ('The Drift', '8,900+\njourneys', '#e67e22')
]

for i, (name, metric, color) in enumerate(worlds):
    x_pos = 2.5 + i * 4.5
    
    # World circle
    circle = Circle((x_pos, 5.5), 1.2, color=color, alpha=0.3, ec=color, linewidth=3)
    ax.add_patch(circle)
    
    ax.text(x_pos, 6, name, ha='center', va='center', 
           fontsize=14, color='white', weight='bold')
    ax.text(x_pos, 4.8, metric, ha='center', va='center', 
           fontsize=18, color=color, weight='bold')

plt.tight_layout()
plt.savefig('video_assets/video1_worlds.png', facecolor='#0a0e27', edgecolor='none', bbox_inches='tight')
print("✓ Video 1 worlds slide created")
plt.close()

# VIDEO 2: Governance - Room Division
fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')
ax.add_patch(plt.Rectangle((0, 0), 16, 9, facecolor='#0a0e27'))

ax.text(8, 8.5, 'Multi-Agent Governance', 
       ha='center', va='center', fontsize=40, color='white', weight='bold')

# Two rooms
left_box = FancyBboxPatch((0.5, 3), 6.5, 4, 
                          boxstyle="round,pad=0.2", 
                          edgecolor='#4ac7f7', facecolor='#4ac7f7', alpha=0.1,
                          linewidth=3)
ax.add_patch(left_box)

right_box = FancyBboxPatch((9, 3), 6.5, 4, 
                           boxstyle="round,pad=0.2", 
                           edgecolor='#e74c3c', facecolor='#e74c3c', alpha=0.1,
                           linewidth=3)
ax.add_patch(right_box)

ax.text(3.75, 6.5, '#best', ha='center', fontsize=20, color='#4ac7f7', weight='bold')
ax.text(3.75, 5.8, 'Gemini 3.1\nGPT-5.5\nClaude Opus 4.7\nKimi K2.6', 
       ha='center', fontsize=12, color='white')

ax.text(12.25, 6.5, '#rest', ha='center', fontsize=20, color='#e74c3c', weight='bold')
ax.text(12.25, 5.5, '10 other agents\nIncluding\nClaude Haiku 4.5', 
       ha='center', fontsize=12, color='white')

ax.text(8, 1.5, 'Governance Protocol: Integrity Constraints', 
       ha='center', fontsize=16, color='#2ecc71', weight='bold')

plt.tight_layout()
plt.savefig('video_assets/video2_governance.png', facecolor='#0a0e27', edgecolor='none', bbox_inches='tight')
print("✓ Video 2 governance slide created")
plt.close()

# VIDEO 3: Verification Framework
fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')
ax.add_patch(plt.Rectangle((0, 0), 16, 9, facecolor='#0a0e27'))

ax.text(8, 8.5, 'Reproducible Research Framework', 
       ha='center', va='center', fontsize=40, color='white', weight='bold')

# Four layers
layers = [
    ('Artifact', 'The actual thing created', 7.2),
    ('Claim', 'What we claim about it', 5.6),
    ('Verification Method', 'How to check the claim', 4.0),
    ('Result', 'What we verified', 2.4)
]

for i, (title, desc, y) in enumerate(layers):
    color = ['#2ecc71', '#4ac7f7', '#f39c12', '#e74c3c'][i]
    
    box = FancyBboxPatch((1, y-0.35), 14, 0.7,
                         boxstyle="round,pad=0.05",
                         edgecolor=color, facecolor=color, alpha=0.2,
                         linewidth=2)
    ax.add_patch(box)
    
    ax.text(2, y, title, ha='left', fontsize=14, color=color, weight='bold')
    ax.text(8, y, desc, ha='center', fontsize=11, color='white')

plt.tight_layout()
plt.savefig('video_assets/video3_verification.png', facecolor='#0a0e27', edgecolor='none', bbox_inches='tight')
print("✓ Video 3 verification slide created")
plt.close()

print("\n✅ All video assets created successfully!")
print("Files saved in video_assets/")
