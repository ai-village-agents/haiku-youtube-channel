#!/usr/bin/env python3
"""
Test narration recording for Series 2 Video 1: "The Right Time Never Arrives"
Target duration: 2:45 (165 seconds)
"""

from gtts import gTTS
import os

# Full script for Video 1
script = """
There's a moment we're all waiting for.
The right time to start. The right conditions to begin.
We tell ourselves: when this changes, I'll begin. When that improves, I'll try.
But conditions rarely line up perfectly.
And we keep waiting.
For the perfect timing. The ideal circumstances. The moment we feel ready.
But the right time might not arrive.
And this moment is here.
"""

# Create output directory if needed
output_dir = '/tmp/haiku-youtube/video_assets/audio'
os.makedirs(output_dir, exist_ok=True)

# Create gTTS object with slower speed
tts = gTTS(text=script, lang='en', slow=True)

# Save the audio file
output_path = os.path.join(output_dir, 'video1_narration_test.mp3')
tts.save(output_path)

print(f"✓ Narration test created: {output_path}")
print(f"✓ Script length: {len(script.split())} words")
print(f"✓ Target duration: 2:45 (165 seconds)")
print(f"✓ Note: Actual duration will be verified after generation")
