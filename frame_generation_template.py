#!/usr/bin/env python3
"""
Frame Generation Template System for Series 2 Video Production
Provides reusable functions for creating animation frames
"""

from PIL import Image, ImageDraw
import json
import os
import math

class FrameGenerator:
    """Base class for generating animated video frames"""
    
    def __init__(self, output_dir, color_spec, resolution=(1920, 1080)):
        self.output_dir = output_dir
        self.color_spec = color_spec
        self.resolution = resolution
        self.width, self.height = resolution
        os.makedirs(output_dir, exist_ok=True)
    
    def create_base_image(self, bg_color=None):
        """Create a base image with background color"""
        if bg_color is None:
            bg_color = tuple(self.color_spec['background']['rgb'])
        return Image.new('RGB', self.resolution, color=bg_color)
    
    def ease_in_out(self, t):
        """Ease-in-out interpolation (0.0 to 1.0)"""
        if t < 0.5:
            return 2 * t * t
        else:
            return 1 - pow(-2 * t + 2, 2) / 2
    
    def ease_out(self, t):
        """Ease-out interpolation"""
        return 1 - pow(1 - t, 3)
    
    def interpolate_color(self, color1, color2, progress):
        """Interpolate between two RGB colors"""
        r = int(color1[0] + (color2[0] - color1[0]) * progress)
        g = int(color1[1] + (color2[1] - color1[1]) * progress)
        b = int(color1[2] + (color2[2] - color1[2]) * progress)
        return (r, g, b)


class Video1Generator(FrameGenerator):
    """Generate frames for Video 1: 'The Right Time Never Arrives'"""
    
    def __init__(self, output_dir, color_spec):
        super().__init__(output_dir, color_spec)
        self.total_frames = 4950  # 165 seconds × 30 fps
    
    def generate_scene1_frame(self, frame_num):
        """
        Scene 1: Opening (0:00-0:25)
        Clock fade-in
        Frames 0-750 (25 seconds at 30fps)
        """
        # Fade in over first 45 frames (1.5 seconds)
        fade_progress = min(frame_num / 45, 1.0)
        fade_progress = self.ease_in_out(fade_progress)
        
        img = self.create_base_image()
        draw = ImageDraw.Draw(img, 'RGBA')
        
        # Clock circle (center of screen)
        clock_center_x, clock_center_y = self.width // 2, self.height // 2
        clock_radius = 200
        clock_color_rgb = tuple(self.color_spec['primary_color']['rgb'])
        clock_alpha = int(255 * fade_progress)
        clock_color = clock_color_rgb + (clock_alpha,)
        
        # Draw clock outline
        bbox = [
            clock_center_x - clock_radius,
            clock_center_y - clock_radius,
            clock_center_x + clock_radius,
            clock_center_y + clock_radius
        ]
        draw.ellipse(bbox, outline=clock_color, width=3)
        
        # Add glow effect
        glow_alpha = int(50 * fade_progress)
        glow_color = clock_color_rgb + (glow_alpha,)
        glow_radius = clock_radius + 20
        glow_bbox = [
            clock_center_x - glow_radius,
            clock_center_y - glow_radius,
            clock_center_x + glow_radius,
            clock_center_y + glow_radius
        ]
        draw.ellipse(glow_bbox, outline=glow_color, width=1)
        
        # After fade-in, add subtle rotation pulse
        if frame_num > 45:
            pulse_frame = (frame_num - 45) % 60  # 2-second pulse cycle
            pulse_progress = pulse_frame / 60
            glow_intensity = int(80 * (0.5 + 0.5 * math.sin(pulse_progress * 2 * math.pi)))
            glow_color_pulse = clock_color_rgb + (glow_intensity,)
            draw.ellipse(glow_bbox, outline=glow_color_pulse, width=1)
        
        return img
    
    def generate_frame(self, frame_num):
        """Generate a single frame based on frame number"""
        if frame_num < 750:
            return self.generate_scene1_frame(frame_num)
        else:
            # Placeholder for other scenes
            return self.create_base_image()


class Video6Generator(FrameGenerator):
    """Generate frames for Video 6: 'What We Fear Speaking Into Being'"""
    
    def __init__(self, output_dir, color_spec):
        super().__init__(output_dir, color_spec)
        self.total_frames = 5100  # 170 seconds × 30 fps
    
    def generate_scene1_frame(self, frame_num):
        """
        Scene 1: Opening Darkness (0:00-0:25)
        Fade from black with subtle shapes
        Frames 0-750 (25 seconds at 30fps)
        """
        # Very slow fade in, shapes barely visible
        fade_progress = min(frame_num / 60, 1.0) * 0.15  # 0-15% brightness
        fade_progress = self.ease_out(fade_progress)
        
        img = self.create_base_image((0, 0, 0))  # Pure black start
        draw = ImageDraw.Draw(img, 'RGBA')
        
        # Add subtle white outlines suggesting shapes
        white_alpha = int(200 * fade_progress)
        white_color = (200, 200, 200, white_alpha)
        
        # Draw abstract threatening shapes
        # Shape 1: jagged edge on left
        points_1 = [
            (100, 300), (150, 280), (200, 320), (180, 400), (120, 380)
        ]
        draw.polygon(points_1, outline=white_color, width=2)
        
        # Shape 2: looming presence in upper right
        points_2 = [
            (1600, 200), (1800, 250), (1750, 400), (1650, 380)
        ]
        draw.polygon(points_2, outline=white_color, width=2)
        
        # Shape 3: vague form in center-bottom
        points_3 = [
            (800, 700), (900, 650), (1000, 700), (950, 850), (850, 850)
        ]
        draw.polygon(points_3, outline=white_color, width=1)
        
        return img
    
    def generate_frame(self, frame_num):
        """Generate a single frame based on frame number"""
        if frame_num < 750:
            return self.generate_scene1_frame(frame_num)
        else:
            # Placeholder for other scenes
            return self.create_base_image((0, 0, 0))


def generate_test_frames():
    """Generate test frames for production validation"""
    
    # Load color specs
    with open('/tmp/haiku-youtube/production_configs/color_specifications.json', 'r') as f:
        color_specs = json.load(f)
    
    test_output = '/tmp/haiku-youtube/test_frames'
    os.makedirs(test_output, exist_ok=True)
    
    # Test Video 1 opening
    print("Generating Video 1 test frames...")
    v1_gen = Video1Generator(
        os.path.join(test_output, 'video1'),
        color_specs['video_specific']['video1']
    )
    
    # Generate first 150 frames (5 seconds) for testing
    for i in range(0, 150, 5):  # Every 5th frame for quick test
        frame = v1_gen.generate_frame(i)
        frame.save(os.path.join(test_output, 'video1', f'frame_{i:05d}.png'))
    
    print(f"✓ Video 1 test frames saved to {test_output}/video1/")
    
    # Test Video 6 opening
    print("Generating Video 6 test frames...")
    v6_gen = Video6Generator(
        os.path.join(test_output, 'video6'),
        color_specs['video_specific']['video6']
    )
    
    # Generate first 150 frames for testing
    for i in range(0, 150, 5):  # Every 5th frame for quick test
        frame = v6_gen.generate_frame(i)
        frame.save(os.path.join(test_output, 'video6', f'frame_{i:05d}.png'))
    
    print(f"✓ Video 6 test frames saved to {test_output}/video6/")
    
    return test_output


if __name__ == '__main__':
    test_dir = generate_test_frames()
    print(f"\n✓ Test frames generated successfully")
    print(f"✓ Output directory: {test_dir}")
    print(f"✓ Ready for quality validation")
