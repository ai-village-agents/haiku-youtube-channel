#!/bin/bash

# Day 424 System Health Check Script
# Purpose: Verify all critical production components before Video 3 production
# Usage: bash SYSTEM_HEALTH_CHECK_DAY424.sh
# Output: Color-coded status report with detailed pass/fail results

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  DAY 424 SYSTEM HEALTH CHECK - \"The Maps We Build\"${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

PASSED=0
FAILED=0
WARNINGS=0

# Helper functions
pass() {
    echo -e "${GREEN}✅ PASS${NC}: $1"
    ((PASSED++))
}

fail() {
    echo -e "${RED}❌ FAIL${NC}: $1"
    ((FAILED++))
}

warn() {
    echo -e "${YELLOW}⚠️  WARN${NC}: $1"
    ((WARNINGS++))
}

# ============================================================================
# 1. REPOSITORY INTEGRITY
# ============================================================================
echo -e "${BLUE}1. REPOSITORY INTEGRITY${NC}"
echo "─────────────────────────────────────────────────────"

# Git status
if [ -d .git ]; then
    if git status --porcelain | grep -q .; then
        fail "Git working tree has uncommitted changes"
    else
        pass "Git working tree is clean"
    fi
else
    fail "Git repository not found"
fi

# Branch verification
BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
if [ "$BRANCH" = "main" ]; then
    pass "On main branch"
else
    fail "Not on main branch (currently: $BRANCH)"
fi

# Commit count
COMMITS=$(git rev-list --count HEAD 2>/dev/null)
if [ "$COMMITS" -ge 279 ]; then
    pass "Commit count sufficient ($COMMITS commits)"
else
    fail "Commit count too low ($COMMITS, expected ≥279)"
fi

echo ""

# ============================================================================
# 2. CRITICAL FILES & DIRECTORIES
# ============================================================================
echo -e "${BLUE}2. CRITICAL FILES & DIRECTORIES${NC}"
echo "─────────────────────────────────────────────────────"

# Check production directories
for dir in video_frames video_assets video_exports production_logs; do
    if [ -d "$dir" ]; then
        pass "Directory exists: $dir"
    else
        fail "Directory missing: $dir"
    fi
done

# Check audio subdirectory
if [ -d "video_assets/audio" ]; then
    pass "Audio directory exists"
else
    fail "Audio directory missing"
fi

echo ""

# ============================================================================
# 3. NARRATION FILES
# ============================================================================
echo -e "${BLUE}3. NARRATION FILES (Video 3-6)${NC}"
echo "─────────────────────────────────────────────────────"

NARRATION_REQUIRED=("video3_narration.mp3:651" "video4_narration.mp3:632" "video5_narration.mp3:676" "video6_narration.mp3:782")

for item in "${NARRATION_REQUIRED[@]}"; do
    FILE="${item%:*}"
    EXPECTED_KB="${item#*:}"
    
    if [ -f "video_assets/audio/$FILE" ]; then
        SIZE=$(du -k "video_assets/audio/$FILE" | cut -f1)
        LOWER=$((EXPECTED_KB - 50))
        UPPER=$((EXPECTED_KB + 50))
        
        if [ "$SIZE" -ge "$LOWER" ] && [ "$SIZE" -le "$UPPER" ]; then
            pass "Narration file OK: $FILE ($SIZE KB)"
        else
            warn "Narration file size unexpected: $FILE ($SIZE KB, expected ~${EXPECTED_KB} KB)"
        fi
    else
        fail "Narration file missing: $FILE"
    fi
done

echo ""

# ============================================================================
# 4. FRAME GENERATORS
# ============================================================================
echo -e "${BLUE}4. FRAME GENERATORS${NC}"
echo "─────────────────────────────────────────────────────"

GENERATORS=("video3_frame_generator.py" "video4_frame_generator.py" "video5_frame_generator.py" "video6_frame_generator.py")

for gen in "${GENERATORS[@]}"; do
    if [ -f "$gen" ]; then
        if [ -x "$gen" ]; then
            pass "Frame generator executable: $gen"
        else
            warn "Frame generator exists but not executable: $gen"
        fi
    else
        fail "Frame generator missing: $gen"
    fi
done

# Check Python syntax
if command -v python3 &> /dev/null; then
    for gen in video3_frame_generator.py; do
        if python3 -m py_compile "$gen" 2>/dev/null; then
            pass "Python syntax valid: $gen"
        else
            fail "Python syntax error in: $gen"
        fi
    done
else
    warn "Python3 not available for syntax check"
fi

echo ""

# ============================================================================
# 5. DOCUMENTATION
# ============================================================================
echo -e "${BLUE}5. DOCUMENTATION${NC}"
echo "─────────────────────────────────────────────────────"

DOCS_REQUIRED=(
    "DAY424_PREFLIGHT_CHECKLIST.md"
    "DAY424_QUICK_REFERENCE_CARD.md"
    "VIDEO3_DETAILED_EXECUTION_GUIDE.md"
    "VIDEO3_PRODUCTION_READINESS_CHECKLIST.md"
    "QUALITY_SCORING_CALCULATOR_TOOL.md"
    "DAY427_QUICK_DECISION_CARD.md"
)

for doc in "${DOCS_REQUIRED[@]}"; do
    if [ -f "$doc" ]; then
        LINES=$(wc -l < "$doc")
        if [ "$LINES" -gt 10 ]; then
            pass "Documentation file substantial: $doc ($LINES lines)"
        else
            warn "Documentation file may be incomplete: $doc ($LINES lines)"
        fi
    else
        fail "Documentation missing: $doc"
    fi
done

echo ""

# ============================================================================
# 6. DEPENDENCIES & TOOLS
# ============================================================================
echo -e "${BLUE}6. DEPENDENCIES & TOOLS${NC}"
echo "─────────────────────────────────────────────────────"

# FFmpeg
if command -v ffmpeg &> /dev/null; then
    FFM_VERSION=$(ffmpeg -version 2>&1 | head -1)
    if echo "$FFM_VERSION" | grep -q "libx264"; then
        pass "FFmpeg installed with H.264 support"
    else
        warn "FFmpeg installed but H.264 support unclear"
    fi
else
    fail "FFmpeg not found in PATH"
fi

# Python3
if command -v python3 &> /dev/null; then
    pass "Python3 installed"
    
    # Check PIL/Pillow
    if python3 -c "from PIL import Image" 2>/dev/null; then
        pass "PIL/Pillow available"
    else
        fail "PIL/Pillow not available"
    fi
    
    # Check NumPy
    if python3 -c "import numpy" 2>/dev/null; then
        pass "NumPy available"
    else
        fail "NumPy not available"
    fi
else
    fail "Python3 not found in PATH"
fi

# Git
if command -v git &> /dev/null; then
    pass "Git installed"
else
    fail "Git not found in PATH"
fi

echo ""

# ============================================================================
# 7. DISK SPACE
# ============================================================================
echo -e "${BLUE}7. DISK SPACE${NC}"
echo "─────────────────────────────────────────────────────"

AVAILABLE=$(df /tmp | awk 'NR==2 {print $4}')
AVAILABLE_GB=$((AVAILABLE / 1024 / 1024))

if [ "$AVAILABLE_GB" -gt 2 ]; then
    pass "Sufficient disk space: ${AVAILABLE_GB} GB available in /tmp"
else
    fail "Insufficient disk space: only ${AVAILABLE_GB} GB available (need ≥2 GB)"
fi

echo ""

# ============================================================================
# 8. PRODUCTION READINESS
# ============================================================================
echo -e "${BLUE}8. PRODUCTION READINESS SUMMARY${NC}"
echo "─────────────────────────────────────────────────────"

echo ""
echo -e "${GREEN}PASSED: $PASSED${NC}"
echo -e "${YELLOW}WARNINGS: $WARNINGS${NC}"
echo -e "${RED}FAILED: $FAILED${NC}"
echo ""

if [ "$FAILED" -eq 0 ]; then
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}  ✅ SYSTEM READY FOR DAY 424 PRODUCTION${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    exit 0
else
    echo -e "${RED}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${RED}  ❌ SYSTEM NOT READY - $FAILED CRITICAL ISSUES FOUND${NC}"
    echo -e "${RED}═══════════════════════════════════════════════════════════════${NC}"
    exit 1
fi
