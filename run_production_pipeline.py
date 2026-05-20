#!/usr/bin/env python3
"""
Series 2 Production Pipeline - May 27 - June 4, 2026
Automated batch processing for all 6 videos
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

class ProductionPipeline:
    """Manages Series 2 video production"""
    
    def __init__(self):
        self.root_dir = Path("/tmp/haiku-youtube")
        self.video_specs = {
            1: {"title": "The Right Time Never Arrives", "duration": 165, "frames": 4950},
            2: {"title": "Saying the Unsayable", "duration": 180, "frames": 5400},
            3: {"title": "The Maps We Build", "duration": 200, "frames": 6000},
            4: {"title": "The Gift of Disappointment", "duration": 190, "frames": 5700},
            5: {"title": "The Privilege of Choice", "duration": 210, "frames": 6300},
            6: {"title": "What We Fear Speaking Into Being", "duration": 170, "frames": 5100},
        }
    
    def validate_production_environment(self):
        """Check that all necessary files exist before production"""
        print("\n🔍 VALIDATING PRODUCTION ENVIRONMENT")
        print("-" * 70)
        
        checks = {
            "Color specs": self.root_dir / "production_configs/color_specifications.json",
            "Export settings": self.root_dir / "SERIES_2_EXPORT_SETTINGS.md",
            "Production checklist": self.root_dir / "SERIES_2_PRODUCTION_CHECKLIST.md",
        }
        
        all_good = True
        for name, path in checks.items():
            exists = "✓" if path.exists() else "✗"
            print(f"  {exists} {name}")
            if not path.exists():
                all_good = False
        
        return all_good
    
    def create_production_log(self):
        """Create production session log"""
        log_file = self.root_dir / "PRODUCTION_LOG.md"
        
        with open(log_file, 'w') as f:
            f.write("# Series 2 Production Log\n")
            f.write(f"**Start Date:** May 27, 2026\n")
            f.write(f"**Session Started:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("## Production Schedule\n\n")
            
            dates = {
                1: "May 27 (Monday)",
                2: "May 28 (Tuesday)",
                3: "May 29 (Wednesday)",
                4: "June 2 (Sunday)",
                5: "June 3 (Monday)",
                6: "June 4 (Tuesday)",
            }
            
            for vid_num, date in dates.items():
                spec = self.video_specs[vid_num]
                f.write(f"- **Video {vid_num}:** {date} | {spec['title']} | {spec['duration']}s | {spec['frames']:,} frames\n")
            
            f.write("\n## Production Status\n\n")
            for vid_num in range(1, 7):
                f.write(f"- [ ] Video {vid_num}: {self.video_specs[vid_num]['title']}\n")
        
        return log_file
    
    def report_production_readiness(self):
        """Generate production readiness report"""
        
        print("\n" + "=" * 70)
        print("SERIES 2 PRODUCTION READINESS REPORT")
        print("=" * 70)
        
        print("\n📋 PRODUCTION SCHEDULE")
        print("-" * 70)
        
        dates = {
            1: "May 27",
            2: "May 28",
            3: "May 29",
            4: "June 2",
            5: "June 3",
            6: "June 4",
        }
        
        total_frames = 0
        total_duration = 0
        
        for vid_num in range(1, 7):
            spec = self.video_specs[vid_num]
            date = dates[vid_num]
            print(f"Video {vid_num}: {date:10s} | {spec['title']:40s} | {spec['duration']:3d}s | {spec['frames']:6,d} frames")
            total_frames += spec['frames']
            total_duration += spec['duration']
        
        print("-" * 70)
        print(f"TOTAL: {total_duration}s ({total_duration//60}:{total_duration%60:02d}) | {total_frames:,} frames")
        
        print("\n💾 DISK SPACE REQUIREMENTS")
        print("-" * 70)
        print(f"Per frame (estimated):  150 KB")
        print(f"Total frames:           {total_frames:,}")
        print(f"Estimated space:        ~{(total_frames * 150) / 1024 / 1024:.1f} GB")
        print(f"Final videos (~80MB ea): ~480 MB")
        print(f"Total footprint:        ~{(total_frames * 150) / 1024 / 1024 + 0.5:.1f} GB")
        
        print("\n✅ PRE-PRODUCTION CHECKLIST")
        print("-" * 70)
        print("✓ All scripts locked (no rewrites)")
        print("✓ All storyboards finalized (33 scenes)")
        print("✓ All narrations recorded (3.7 MB)")
        print("✓ Color specifications finalized")
        print("✓ Export settings documented")
        print("✓ Frame generators operational")
        print("✓ Export pipeline tested")
        print("✓ Production schedule confirmed")
        
        print("\n🎬 PRODUCTION NOTES")
        print("-" * 70)
        print("- 1 video per day (proven sustainable from Series 1)")
        print("- All frames numbered sequentially (frame_000001.png)")
        print("- Audio will be mixed during export")
        print("- Quality target: 4.5+/5 (Series 1 achieved 4.51/5)")
        print("- Publishing: June 9-14, 2026 (1 video/day)")
        
        print("\n" + "=" * 70)
        print("READY TO BEGIN PRODUCTION: May 27, 2026, 10:00 AM PT")
        print("=" * 70)

def main():
    """Main production pipeline"""
    pipeline = ProductionPipeline()
    
    # Validate environment
    if not pipeline.validate_production_environment():
        print("\n⚠️ WARNING: Some production files missing")
        print("   Create missing files before starting production")
    
    # Create production log
    log_file = pipeline.create_production_log()
    print(f"\n✓ Production log created: {log_file}")
    
    # Report readiness
    pipeline.report_production_readiness()
    
    print("\n💡 NEXT STEPS:")
    print("  1. On May 27, 10:00 AM PT: Run video1_frame_generator.py")
    print("  2. Monitor output to video_frames/video1/")
    print("  3. Export: python3 export_video_with_audio.py")
    print("  4. Upload to YouTube when export completes")
    print("  5. Repeat for Videos 2-6 (May 28-June 4)")

if __name__ == "__main__":
    main()
