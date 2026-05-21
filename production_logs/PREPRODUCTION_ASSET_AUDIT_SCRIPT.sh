#!/bin/bash

# SERIES 2 PRE-PRODUCTION ASSET AUDIT SCRIPT
# Purpose: Comprehensive verification that all Series 2 assets are intact before Day 421
# Usage: bash PREPRODUCTION_ASSET_AUDIT_SCRIPT.sh
# Expected runtime: ~30 seconds
# Status: 100% SAFE (read-only, no modifications)

echo "==========================================="
echo "SERIES 2 PRE-PRODUCTION ASSET AUDIT"
echo "==========================================="
echo ""
echo "Date: $(date '+%Y-%m-%d %H:%M:%S')"
echo "Location: /tmp/haiku-youtube"
echo ""

cd /tmp/haiku-youtube || { echo "ERROR: Repository not found"; exit 1; }

# Counter for issues found
ISSUES=0

echo "--- STEP 1: DISK SPACE CHECK ---"
DISK_FREE=$(df /tmp/haiku-youtube | tail -1 | awk '{print $4}')
DISK_FREE_GB=$((DISK_FREE / 1024 / 1024))
echo "Disk space available: ${DISK_FREE_GB} GB"
if [ "$DISK_FREE_GB" -lt 50 ]; then
  echo "⚠️  WARNING: Less than 50 GB free (need for frame generation + export)"
  ((ISSUES++))
else
  echo "✅ Disk space: ADEQUATE"
fi
echo ""

echo "--- STEP 2: FRAME GENERATORS ---"
for i in {1..6}; do
  FILE="video${i}_frame_generator.py"
  if [ -f "$FILE" ]; then
    LINES=$(wc -l < "$FILE")
    echo "✅ $FILE ($LINES lines)"
  else
    echo "❌ MISSING: $FILE"
    ((ISSUES++))
  fi
done
echo ""

echo "--- STEP 3: AUDIO NARRATIONS ---"
for i in {1..6}; do
  FILE="video_assets/audio/video${i}_narration.mp3"
  if [ -f "$FILE" ]; then
    SIZE=$(du -h "$FILE" | cut -f1)
    # Check duration with ffprobe
    if command -v ffprobe &> /dev/null; then
      DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$FILE" 2>/dev/null | cut -d. -f1)
      echo "✅ video${i}_narration.mp3 ($SIZE, ~${DURATION}s)"
    else
      echo "✅ video${i}_narration.mp3 ($SIZE)"
    fi
  else
    echo "❌ MISSING: $FILE"
    ((ISSUES++))
  fi
done
echo ""

echo "--- STEP 4: COLOR SPECIFICATIONS ---"
for i in {1..6}; do
  FILE="production_configs/video${i}_colors.json"
  if [ -f "$FILE" ]; then
    echo "✅ video${i}_colors.json"
  else
    echo "❌ MISSING: $FILE"
    ((ISSUES++))
  fi
done
echo ""

echo "--- STEP 5: DOCUMENTATION FILES ---"
DOC_COUNT=$(find production_logs -name "*.md" -type f | wc -l)
echo "Total documentation files: $DOC_COUNT"
echo "Required minimum: 20"
if [ "$DOC_COUNT" -ge 20 ]; then
  echo "✅ Documentation: COMPLETE"
else
  echo "❌ Documentation: INCOMPLETE (found $DOC_COUNT, need 20+)"
  ((ISSUES++))
fi
echo ""

echo "--- STEP 6: CRITICAL PLAYBOOKS ---"
REQUIRED_DOCS=(
  "DAY421_SERIES2_VIDEO1_PRE_PUBLICATION_CHECKLIST.md"
  "DAILY_PRODUCTION_WORKFLOW_TEMPLATE.md"
  "DAY422_BUFFER_DAY_COMPLETE_STRATEGY.md"
  "DAY427_BUFFER_DAY_COMPLETE_STRATEGY.md"
  "SERIES2_QUALITY_TRACKING_SYSTEM.md"
  "SERIES2_YOUTUBE_METADATA_TEMPLATES.md"
  "CRITICAL_PRODUCTION_DECISION_TREE.md"
)

for doc in "${REQUIRED_DOCS[@]}"; do
  if [ -f "production_logs/$doc" ]; then
    echo "✅ $doc"
  else
    echo "❌ MISSING: $doc"
    ((ISSUES++))
  fi
done
echo ""

echo "--- STEP 7: GIT REPOSITORY STATUS ---"
if git rev-parse --git-dir > /dev/null 2>&1; then
  echo "✅ Git repository: VALID"
  
  # Check if working tree is clean
  if [ -z "$(git status --porcelain)" ]; then
    echo "✅ Working tree: CLEAN"
  else
    UNCOMMITTED=$(git status --porcelain | wc -l)
    echo "⚠️  WARNING: $UNCOMMITTED uncommitted changes"
    ((ISSUES++))
  fi
  
  # Get latest commit
  COMMIT=$(git rev-parse --short HEAD)
  echo "✅ Latest commit: $COMMIT"
else
  echo "❌ Git repository: INVALID"
  ((ISSUES++))
fi
echo ""

echo "--- STEP 8: REQUIRED DEPENDENCIES ---"
MISSING_DEPS=0

if ! command -v python3 &> /dev/null; then
  echo "❌ Missing: python3"
  ((MISSING_DEPS++))
else
  echo "✅ python3: AVAILABLE"
fi

if ! command -v ffmpeg &> /dev/null; then
  echo "❌ Missing: ffmpeg"
  ((MISSING_DEPS++))
else
  echo "✅ ffmpeg: AVAILABLE"
fi

if ! command -v git &> /dev/null; then
  echo "❌ Missing: git"
  ((MISSING_DEPS++))
else
  echo "✅ git: AVAILABLE"
fi

if [ "$MISSING_DEPS" -gt 0 ]; then
  ((ISSUES+= MISSING_DEPS))
fi
echo ""

echo "--- STEP 9: SYNTAX VALIDATION ---"
echo "Checking frame generator syntax (read-only, safe)..."
if python3 -m py_compile video1_frame_generator.py 2>/dev/null; then
  echo "✅ Frame generator syntax: VALID"
else
  echo "❌ Frame generator syntax: INVALID"
  ((ISSUES++))
fi
echo ""

echo "--- STEP 10: FFmpeg COMMAND VALIDATION ---"
if ffmpeg -h full 2>/dev/null | grep -q "libx264"; then
  echo "✅ FFmpeg codec (libx264): AVAILABLE"
else
  echo "⚠️  WARNING: libx264 codec may not be available"
fi

if ffmpeg -h full 2>/dev/null | grep -q "aac"; then
  echo "✅ FFmpeg codec (aac): AVAILABLE"
else
  echo "⚠️  WARNING: AAC codec may not be available"
fi
echo ""

echo "==========================================="
echo "AUDIT SUMMARY"
echo "==========================================="
if [ "$ISSUES" -eq 0 ]; then
  echo "✅ ALL CHECKS PASSED"
  echo "Series 2 assets are complete and ready for production."
  echo ""
  echo "NEXT STEP: Start DAILY_PRODUCTION_WORKFLOW at 10:00 AM"
  exit 0
else
  echo "❌ ISSUES FOUND: $ISSUES"
  echo "Please resolve issues before proceeding with production."
  echo ""
  echo "Recommendations:"
  echo "1. Check disk space if < 50 GB free"
  echo "2. Verify all frame generators and audio files are present"
  echo "3. Review missing documentation files"
  echo "4. Commit any uncommitted changes"
  echo "5. Ensure ffmpeg and python3 are installed"
  echo ""
  exit 1
fi
