#!/usr/bin/env python3
"""
Test all 6 frame generators to ensure production readiness
"""

import subprocess
import sys
from pathlib import Path

def test_generator(video_num):
    """Test a single video generator"""
    
    generator_script = f"/tmp/haiku-youtube/video{video_num}_frame_generator.py"
    
    if not Path(generator_script).exists():
        print(f"✗ Video {video_num}: Generator not found")
        return False
    
    try:
        print(f"\n🎬 Testing Video {video_num} frame generator...")
        result = subprocess.run(
            ["python3", generator_script],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print(f"✓ Video {video_num}: Generator successful")
            return True
        else:
            print(f"✗ Video {video_num}: Generator failed")
            if result.stderr:
                print(f"  Error: {result.stderr[:200]}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"✗ Video {video_num}: Generator timeout")
        return False
    except Exception as e:
        print(f"✗ Video {video_num}: Error - {e}")
        return False

def main():
    """Test all generators"""
    
    print("=" * 70)
    print("TESTING ALL FRAME GENERATORS - SERIES 2")
    print("=" * 70)
    
    results = {}
    for video_num in range(1, 7):
        results[video_num] = test_generator(video_num)
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for video_num in range(1, 7):
        status = "✅ PASS" if results[video_num] else "❌ FAIL"
        print(f"Video {video_num}: {status}")
    
    print(f"\nOverall: {passed}/{total} generators operational")
    
    if passed == total:
        print("\n🎉 All generators ready for production!")
        return True
    else:
        print(f"\n⚠️ {total - passed} generator(s) need attention")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
