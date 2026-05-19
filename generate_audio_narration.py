#!/usr/bin/env python3
"""
Generate audio narration for YouTube videos using Google Text-to-Speech (gTTS)
"""

import json
from gtts import gTTS
from pathlib import Path
import time

def generate_narration():
    """Generate audio narration for all videos"""
    
    # Load narration timing data
    with open('narration_timing.json', 'r') as f:
        data = json.load(f)
    
    # Create audio directory if it doesn't exist
    audio_dir = Path('video_assets/audio')
    audio_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate narration for each video
    for video in data['videos']:
        video_id = video['id']
        video_title = video['title']
        
        # Concatenate all narration segments
        full_narration = " ".join([
            frame['narration_segment'] 
            for frame in video['frames']
        ])
        
        # Create output filename
        output_file = audio_dir / f'video{video_id:02d}_narration.mp3'
        
        print(f"\n[Video {video_id}] {video_title}")
        print(f"Duration: {video['duration_seconds']} seconds")
        print(f"Narration length: {len(full_narration)} characters")
        print(f"Output: {output_file}")
        
        try:
            # Create TTS object and save to file
            tts = gTTS(full_narration, lang='en', slow=False)
            tts.save(str(output_file))
            print(f"✓ Generated {output_file}")
            
            # Small delay to avoid rate limiting
            time.sleep(1)
            
        except Exception as e:
            print(f"✗ Error generating narration for video {video_id}: {e}")
    
    print("\n✓ All narration files generated successfully!")

if __name__ == '__main__':
    generate_narration()
