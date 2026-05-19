#!/usr/bin/env python3
"""
Compile videos from frame sequences and audio using moviepy
"""

import json
from pathlib import Path
from moviepy import ImageClip, concatenate_videoclips, AudioFileClip

def compile_videos():
    """Compile all videos from frames and audio"""
    
    # Load narration timing data
    with open('narration_timing.json', 'r') as f:
        data = json.load(f)
    
    # Create output directory
    output_dir = Path('video_output')
    output_dir.mkdir(exist_ok=True)
    
    # Compile each video
    for video in data['videos']:
        video_id = video['id']
        video_title = video['title']
        
        print(f"\n[Video {video_id}] {video_title}")
        print(f"Duration: {video['duration_seconds']} seconds")
        
        # Load frames and create clips
        clips = []
        frame_dir = Path('video_frames')
        
        for frame_info in video['frames']:
            frame_num = frame_info['frame']
            frame_duration = frame_info['time_end'] - frame_info['time_start']
            
            frame_file = frame_dir / f'video{video_id:02d}_frame{frame_num:03d}.png'
            
            if not frame_file.exists():
                print(f"✗ Frame file not found: {frame_file}")
                continue
            
            print(f"  Frame {frame_num}: {frame_file.name} ({frame_duration}s)")
            
            # Create clip from image
            clip = ImageClip(str(frame_file))
            clip = clip.with_duration(frame_duration)
            clips.append(clip)
        
        if not clips:
            print(f"✗ No clips found for video {video_id}")
            continue
        
        # Concatenate all clips
        video_clip = concatenate_videoclips(clips)
        
        # Load audio
        audio_file = Path('video_assets/audio') / f'video{video_id:02d}_narration.mp3'
        
        if not audio_file.exists():
            print(f"✗ Audio file not found: {audio_file}")
            continue
        
        print(f"  Audio: {audio_file.name}")
        
        # Add audio to video
        audio_clip = AudioFileClip(str(audio_file))
        
        # Adjust audio/video duration mismatch
        print(f"  Video duration: {video_clip.duration:.1f}s, Audio duration: {audio_clip.duration:.1f}s")
        
        if audio_clip.duration > video_clip.duration:
            print(f"  Truncating audio to match video")
            audio_clip = audio_clip.subclipped(0, video_clip.duration)
        
        # Set audio to video
        final_clip = video_clip.with_audio(audio_clip)
        
        # Output filename (use safe characters)
        safe_title = video_title.lower().replace(" ", "_").replace("|", "").replace("/", "")
        output_file = output_dir / f'video{video_id:02d}_{safe_title}.mp4'
        
        print(f"  Writing to: {output_file}")
        print(f"  (This may take a few minutes...)")
        
        # Write video file
        try:
            final_clip.write_videofile(
                str(output_file),
                fps=30,
                codec='libx264',
                audio_codec='aac'
            )
            print(f"✓ Video {video_id} compiled successfully!")
        except Exception as e:
            print(f"✗ Error compiling video {video_id}: {e}")
        finally:
            # Clean up
            try:
                if hasattr(video_clip, 'close'):
                    video_clip.close()
                if hasattr(audio_clip, 'close'):
                    audio_clip.close()
                if hasattr(final_clip, 'close'):
                    final_clip.close()
            except:
                pass
    
    print("\n✓ All videos compiled successfully!")
    print(f"Output directory: {output_dir}")

if __name__ == '__main__':
    compile_videos()
