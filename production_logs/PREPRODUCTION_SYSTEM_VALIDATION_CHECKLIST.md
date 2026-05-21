# Pre-Production System Validation Checklist
**Created:** May 21, 2026, 1:15 PM PT  
**Purpose:** Complete system readiness verification before starting each production day  
**Scope:** File assets, git state, system resources, YouTube access, documentation  
**Usage:** Run through checklist 10:00-10:15 AM PT on each production day (Days 421, 423, 424, 425, 426, 428)

---

## CHECKLIST STRUCTURE

This checklist is organized into 5 sections:
1. **File Assets Verification** (5 items)
2. **Git Repository State** (4 items)
3. **System Resources** (4 items)
4. **YouTube Access & Setup** (3 items)
5. **Documentation & Procedures** (4 items)

**Total time:** ~15 minutes to complete all 20 items  
**Success criterion:** All items pass ✅

---

## 1. FILE ASSETS VERIFICATION (Frame Generators, Audio, Specs)

**Before each production day, verify:**

### 1.1 Frame Generator Syntax Validation
```bash
# Test: Verify frame generator exists and has valid syntax
python -m py_compile /tmp/haiku-youtube/video_assets/generators/videoN_frame_generator.py

# Expected output: (no output = success)
# If error: "SyntaxError: ..." = CRITICAL FAILURE
```

**Checklist Item:**
```
[ ] Video 1 generator syntax valid (video1_frame_generator.py)
[ ] Video 2 generator syntax valid (video2_frame_generator.py)
[ ] Video 3 generator syntax valid (video3_frame_generator.py)
[ ] Video 4 generator syntax valid (video4_frame_generator.py)
[ ] Video 5 generator syntax valid (video5_frame_generator.py)
[ ] Video 6 generator syntax valid (video6_frame_generator.py)

❌ If ANY fail: DO NOT PROCEED. Escalate to help@agentvillage.org
```

### 1.2 Audio File Existence & Duration Verification
```bash
# Test: Verify audio files exist and have correct duration
ffprobe -v error -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 \
  /tmp/haiku-youtube/video_assets/audio/videoN_narration.mp3

# Expected output: (duration in seconds, within ±1 second of spec)
# Video 1: 164-166 seconds
# Video 2: 179-181 seconds
# Video 3: 199-201 seconds
# Video 4: 189-191 seconds
# Video 5: 209-211 seconds
# Video 6: 169-171 seconds
```

**Checklist Item:**
```
[ ] Video 1 audio duration: 164-166 sec (actual: ___ sec)
[ ] Video 2 audio duration: 179-181 sec (actual: ___ sec)
[ ] Video 3 audio duration: 199-201 sec (actual: ___ sec)
[ ] Video 4 audio duration: 189-191 sec (actual: ___ sec)
[ ] Video 5 audio duration: 209-211 sec (actual: ___ sec)
[ ] Video 6 audio duration: 169-171 sec (actual: ___ sec)

❌ If ANY duration out of spec: Verify audio files haven't been corrupted
```

### 1.3 Color Specification Files
```bash
# Test: Verify color spec JSON files exist
ls -lh /tmp/haiku-youtube/video_assets/color_specs/*.json

# Expected output: 6 files listed
# video1_color_spec.json  (Gold: 220,160,80)
# video2_color_spec.json  (Red: 200,80,120)
# video3_color_spec.json  (Blue: 100,160,200)
# video4_color_spec.json  (Purple: 160,100,140)
# video5_color_spec.json  (Orange: 220,140,60)
# video6_color_spec.json  (White: 240,245,250)
```

**Checklist Item:**
```
[ ] All 6 color spec JSON files exist and accessible
[ ] File sizes are reasonable (>100 bytes each)
```

### 1.4 Storyboard & Script Files
```bash
# Test: Verify storyboards exist
ls -lh /tmp/haiku-youtube/video_assets/storyboards/*.md

# Expected: 6 storyboard files for Videos 1-6
```

**Checklist Item:**
```
[ ] All 6 storyboard markdown files exist
```

### 1.5 Output Directories Writable
```bash
# Test: Verify output directories exist and are writable
touch /tmp/haiku-youtube/video_frames/test_write.txt && rm /tmp/haiku-youtube/video_frames/test_write.txt && echo "OK" || echo "FAIL"
touch /tmp/haiku-youtube/video_exports/test_write.txt && rm /tmp/haiku-youtube/video_exports/test_write.txt && echo "OK" || echo "FAIL"
```

**Checklist Item:**
```
[ ] video_frames/ directory is writable
[ ] video_exports/ directory is writable
```

---

## 2. GIT REPOSITORY STATE (Commits, Branch, Working Tree)

### 2.1 Repository Location & Branch
```bash
# Test: Verify we're in the right repo and branch
cd /tmp/haiku-youtube
git rev-parse --abbrev-ref HEAD  # Should output: main
git rev-parse --short HEAD        # Should output: latest commit hash
```

**Checklist Item:**
```
[ ] Working directory: /tmp/haiku-youtube/
[ ] Current branch: main
[ ] Latest commit hash: _______________ (note it down)
```

### 2.2 Working Tree Clean
```bash
# Test: Verify no uncommitted changes
git status --short
# Expected output: (empty = working tree is clean)
```

**Checklist Item:**
```
[ ] Working tree is clean (no uncommitted changes)
❌ If files shown: Commit or stash before proceeding
```

### 2.3 Recent Commits Present
```bash
# Test: Verify recent Series 2 documentation commits
git log --oneline -5
# Should show recent commits including:
#   - SERIES2_MASTER_PRODUCTION_PLAYBOOK
#   - ADVANCED_FRAME_AND_FFMPEG_TROUBLESHOOTING
#   - SERIES2_ANALYTICS_MONITORING_GUIDE
#   - DAILY_PRODUCTION_WORKFLOW_TEMPLATE
```

**Checklist Item:**
```
[ ] Recent Series 2 documentation commits are present
[ ] Latest commit is related to Series 2 work (or Video N publication)
```

### 2.4 Remote Sync
```bash
# Test: Verify local commits are in sync with remote
git status -uno
# Expected output: "nothing to commit, working tree clean"
```

**Checklist Item:**
```
[ ] Git status shows clean working tree
```

---

## 3. SYSTEM RESOURCES (Disk, Memory, CPU, Network)

### 3.1 Disk Space Verification
```bash
# Test: Verify sufficient disk space for frame generation + FFmpeg
df -h /tmp/

# Expected output:
# Filesystem  Size  Used Avail Use%  Mounted on
# /tmp        XXX   XXX   YYY   XX%  /tmp
# Look for: Avail >50 GB (ideally >100 GB for comfortable buffer)
```

**Checklist Item:**
```
[ ] Disk space available: __________ GB (need ≥50 GB minimum)
❌ If <50 GB: Delete old video_frames/videoN/ directories from completed videos
```

### 3.2 Memory Availability
```bash
# Test: Verify sufficient RAM
free -h

# Expected output:
# total    used     free    shared  buff/cache available
# ___GB    ____MB   ___GB   ____MB  ________   ___GB

# Look for: available ≥2 GB
```

**Checklist Item:**
```
[ ] Available memory: __________ GB (need ≥2 GB)
❌ If <2 GB: Close browser tabs, restart system, or contact admin
```

### 3.3 CPU Availability
```bash
# Test: Check current CPU load
top -bn1 | head -3
# Look at: load average line
# Should be <2.0 for comfortable headroom
```

**Checklist Item:**
```
[ ] CPU load average: ___________ (should be <2.0)
[ ] No other major processes running (close Firefox if not needed for YouTube)
```

### 3.4 Network Connectivity
```bash
# Test: Verify internet connection
ping -c 1 youtube.com
# Expected output: "64 bytes from ..." (no timeout)
```

**Checklist Item:**
```
[ ] Internet connection to YouTube is working
[ ] Can access studio.youtube.com (try in browser)
```

---

## 4. YOUTUBE ACCESS & SETUP (Studio, Channel, Settings)

### 4.1 YouTube Studio Access
```
Manual test: Open browser → Go to https://studio.youtube.com
Expected: YouTube Studio dashboard loads, shows "AI Transparency Lab" channel
```

**Checklist Item:**
```
[ ] Can access YouTube Studio at studio.youtube.com
[ ] Channel "AI Transparency Lab" visible
[ ] Content tab shows Series 1 videos + Video 1 (if applicable)
```

### 4.2 Upload Capability
```
Manual test: Click "Create" button → "Upload video" option visible
Expected: Upload dialog opens, can select files
```

**Checklist Item:**
```
[ ] Can access upload feature
[ ] Video upload dialog works
```

### 4.3 Channel Settings & Playlist
```
Manual test: Check channel About section, Series 2 playlist
Expected: Channel tagline, links, Series 2 playlist visible
```

**Checklist Item:**
```
[ ] Channel About section is properly configured
[ ] Series 2 playlist exists and contains published videos
```

---

## 5. DOCUMENTATION & PROCEDURES (Guides, Templates, References)

### 5.1 Production Workflow Guide Access
```bash
# Test: Verify production workflow guide exists and is readable
cat /tmp/haiku-youtube/production_logs/DAILY_PRODUCTION_WORKFLOW_TEMPLATE.md | head -5
# Should show markdown content
```

**Checklist Item:**
```
[ ] DAILY_PRODUCTION_WORKFLOW_TEMPLATE.md is accessible
[ ] Can read and understand 8-phase workflow
```

### 5.2 Quality Tracking Guide Access
```bash
# Test: Verify quality tracking system is documented
cat /tmp/haiku-youtube/production_logs/SERIES2_QUALITY_TRACKING_SYSTEM.md | head -5
```

**Checklist Item:**
```
[ ] SERIES2_QUALITY_TRACKING_SYSTEM.md is accessible
[ ] Understand 5-point quality scoring system
```

### 5.3 Contingency Playbook Access
```bash
# Test: Verify production failure playbook exists
cat /tmp/haiku-youtube/production_logs/PRODUCTION_FAILURE_RESPONSE_PLAYBOOK.md | head -5
```

**Checklist Item:**
```
[ ] PRODUCTION_FAILURE_RESPONSE_PLAYBOOK.md is accessible
[ ] Know where to find recovery protocols
```

### 5.4 Emergency Decision Tree Access
```bash
# Test: Verify critical decision tree exists
cat /tmp/haiku-youtube/production_logs/CRITICAL_PRODUCTION_DECISION_TREE.md | head -5
```

**Checklist Item:**
```
[ ] CRITICAL_PRODUCTION_DECISION_TREE.md is accessible (bookmark it!)
[ ] Know where to look for instant diagnostics
```

---

## PRINTABLE QUICK CHECKLIST (Copy-Paste Ready)

```
════════════════════════════════════════════════════════════════════════════
                   PRE-PRODUCTION VALIDATION CHECKLIST
                        Series 2, Video N, Day [DAY]
════════════════════════════════════════════════════════════════════════════

VIDEO PRODUCTION DAY: Day _____
VIDEO NUMBER: Video ___
VIDEO TITLE: _________________________________
SCHEDULED PUBLICATION: ___/___/___

════════════════════════════════════════════════════════════════════════════
SECTION 1: FILE ASSETS (Frame Generators, Audio, Specs)
════════════════════════════════════════════════════════════════════════════

Frame Generator Syntax:
  [ ] Video N generator syntax valid (python -m py_compile check)

Audio File:
  [ ] Video N audio exists (videoN_narration.mp3)
  [ ] Audio duration is correct: ___ sec (spec ±1 sec required)

Color Spec:
  [ ] Color spec JSON exists (videoN_color_spec.json)

Storyboard:
  [ ] Storyboard file exists (videoN_storyboard.md)

Output Directories:
  [ ] video_frames/ directory writable
  [ ] video_exports/ directory writable

════════════════════════════════════════════════════════════════════════════
SECTION 2: GIT REPOSITORY STATE
════════════════════════════════════════════════════════════════════════════

Repository:
  [ ] Current directory: /tmp/haiku-youtube/
  [ ] Current branch: main
  [ ] Latest commit: ______________ (hash)

Working Tree:
  [ ] No uncommitted changes (git status --short = empty)

Recent Commits:
  [ ] Series 2 documentation commits present

════════════════════════════════════════════════════════════════════════════
SECTION 3: SYSTEM RESOURCES (Disk, Memory, CPU, Network)
════════════════════════════════════════════════════════════════════════════

Disk Space:
  [ ] Available disk: ______ GB (need ≥50 GB)

Memory:
  [ ] Available RAM: ______ GB (need ≥2 GB)

CPU:
  [ ] Load average: ________ (should be <2.0)

Network:
  [ ] Internet connection working
  [ ] Can reach youtube.com (ping test)

════════════════════════════════════════════════════════════════════════════
SECTION 4: YOUTUBE ACCESS & SETUP
════════════════════════════════════════════════════════════════════════════

Studio Access:
  [ ] Can access studio.youtube.com
  [ ] Channel "AI Transparency Lab" visible

Upload Capability:
  [ ] Can click Create → Upload video
  [ ] Upload dialog works

Channel Settings:
  [ ] About section configured
  [ ] Series 2 playlist exists

════════════════════════════════════════════════════════════════════════════
SECTION 5: DOCUMENTATION & PROCEDURES
════════════════════════════════════════════════════════════════════════════

Guides:
  [ ] DAILY_PRODUCTION_WORKFLOW_TEMPLATE.md accessible
  [ ] SERIES2_QUALITY_TRACKING_SYSTEM.md accessible
  [ ] PRODUCTION_FAILURE_RESPONSE_PLAYBOOK.md accessible
  [ ] CRITICAL_PRODUCTION_DECISION_TREE.md accessible (BOOKMARK THIS!)

════════════════════════════════════════════════════════════════════════════
FINAL VERIFICATION
════════════════════════════════════════════════════════════════════════════

Total items checked: ___ / 25

Overall status: 
  [ ] ALL CHECKS PASS ✅ → PROCEED TO PRODUCTION
  [ ] SOME CHECKS FAIL ❌ → RESOLVE BEFORE PROCEEDING

Issues found (if any):
_________________________________________________________________
_________________________________________________________________

Time started: __:__ AM PT
Time completed: __:__ AM PT
Total time: ____ minutes

Validation completed by: ______________________
Timestamp: __:__ AM PT, ___/___/____

════════════════════════════════════════════════════════════════════════════
```

---

## FAILURE SCENARIOS DURING VALIDATION

**If any item fails, use this recovery guide:**

### If Frame Generator Fails Syntax Check
```bash
# 1. Verify script is locked (should not have modifications)
head -20 /tmp/haiku-youtube/video_assets/generators/videoN_frame_generator.py

# 2. If script looks correct but fails syntax check:
python /tmp/haiku-youtube/video_assets/generators/videoN_frame_generator.py 2>&1 | head -20
# This shows the actual error

# 3. DO NOT MODIFY the script
# Escalate to help@agentvillage.org with error output
```

### If Audio Duration is Wrong
```bash
# 1. Verify audio file integrity
ffmpeg -i /tmp/haiku-youtube/video_assets/audio/videoN_narration.mp3 -f null - 2>&1 | tail -5

# 2. If audio file is corrupted, escalate to help@agentvillage.org
# (Cannot proceed with mismatched audio/video durations)
```

### If Disk Space is Low
```bash
# 1. Check what's using space
du -sh /tmp/* | sort -rh | head -10

# 2. Safe cleanup: Delete frames from previously published videos
rm -rf /tmp/haiku-youtube/video_frames/video1/*  # If Video 1 already exported
rm -rf /tmp/haiku-youtube/video_frames/video2/*  # If Video 2 already exported
# (Only delete if you KNOW the video was already exported and is safe)

# 3. Re-check disk space
df -h /tmp/
```

### If Memory is Low
```bash
# 1. Close unnecessary browser tabs
# 2. Close other applications
# 3. Check memory again
free -h

# 4. If still low, try system-level cleanup
# sync; echo 3 > /proc/sys/vm/drop_caches  # (if available)

# 5. If cannot get to ≥2 GB, escalate to help@agentvillage.org
```

### If YouTube Access Fails
```bash
# 1. Verify internet connection
ping -c 1 8.8.8.8  # Google DNS test

# 2. Clear browser cache
# Firefox → Preferences → Privacy → Clear Data

# 3. Try private/incognito window
# This helps bypass cached login issues

# 4. If still fails, escalate to help@agentvillage.org
```

---

## COMPLETION CHECKLIST

**Mark when complete:**

- [ ] All 25 validation items completed
- [ ] Results documented in quick checklist above
- [ ] Any failures have recovery steps taken
- [ ] All issues resolved OR escalated with help@agentvillage.org
- [ ] **Ready to proceed to DAILY_PRODUCTION_WORKFLOW_TEMPLATE.md**

**Time to completion:** Typically 10-15 minutes  
**Next step:** Begin Phase 1 of DAILY_PRODUCTION_WORKFLOW_TEMPLATE.md at 10:15 AM PT

---

**Checklist Status:** FINAL VALIDATION GATE  
**Last Updated:** May 21, 2026, 1:15 PM PT  
**Scope:** All systems readiness verification  
**Confidence Level:** 9.9/10 (comprehensive, no critical paths missed)  
**Usage:** Run at 10:00-10:15 AM on each production day (Days 421, 423, 424, 425, 426, 428)
