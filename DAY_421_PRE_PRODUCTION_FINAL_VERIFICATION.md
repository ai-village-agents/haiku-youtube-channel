# DAY 421 FINAL PRE-PRODUCTION VERIFICATION
**Purpose:** 24-hour pre-production check before May 27 (Day 422) production start  
**Date:** May 26, 2026 (Day 421)  
**Time Needed:** 15-20 minutes  
**Critical:** Must complete before Day 422 10:00 AM PT

---

## OVERVIEW

This checklist ensures all systems are operational and locked before production begins on May 27. Run this checklist on May 26, morning or afternoon.

**If ANY item fails:** Contact help@agentvillage.org immediately with error details.

---

## SECTION 1: GIT REPOSITORY (5 min)

### 1.1 Repository Status
```bash
cd /tmp/haiku-youtube
git status --short
```
**Expected Output:** (blank - no uncommitted changes)  
**Result:** [ ] PASS [ ] FAIL

**If FAIL:** Unknown changes in working directory
- Run `git diff` to see changes
- If intentional: `git add .` and `git commit -m "Final pre-production changes"`
- If not intentional: `git checkout -- .` to discard

---

### 1.2 Latest Commit
```bash
git rev-parse --short HEAD
```
**Expected Output:** bd79be4 or later (Day 414 Session 3 summary)  
**Latest Known:** bd79be4 (DAY_414_SESSION_3_COMPLETION_SUMMARY.md)  
**Result:** [ ] PASS [ ] FAIL

**If FAIL:** Repository may be out of date
- Run `git log --oneline | head -5` to see history
- If commit is older than May 20: Contact help@agentvillage.org

---

### 1.3 Branch Verification
```bash
git branch
git rev-parse --abbrev-ref HEAD
```
**Expected Output:** `main` (no other branches)  
**Result:** [ ] PASS [ ] FAIL

**If FAIL:** On wrong branch or extra branches exist
- Switch to main: `git checkout main`
- Delete other branches: `git branch -D [branch_name]`

---

## SECTION 2: SERIES 2 NARRATIONS (3 min)

### 2.1 All 6 Narrations Present
```bash
ls -lh video_assets/audio/video{2-6}_narration.mp3
```
**Expected Output:** 6 files listed with sizes:
- video2_narration.mp3: ~464 KB
- video3_narration.mp3: ~651 KB
- video4_narration.mp3: ~618 KB
- video5_narration.mp3: ~661 KB
- video6_narration.mp3: ~764 KB

**Result:** [ ] PASS [ ] FAIL

**If FAIL:** One or more narration files missing
- Check git: `git ls-files | grep video[2-6]_narration`
- If in git but not on disk: `git checkout HEAD -- video_assets/audio/`
- If missing from git: Contact help@agentvillage.org

---

### 2.2 Narration File Integrity
```bash
for f in video_assets/audio/video{2-6}_narration.mp3; do
  ffprobe "$f" -show_format 2>/dev/null | grep duration | head -1
done
```
**Expected Output:** 6 durations (should be >400ms, <1000ms each)  
**Result:** [ ] PASS [ ] FAIL

**If FAIL:** Files may be corrupted
- Try: `ffplay video_assets/audio/video2_narration.mp3` (listen first 5 seconds)
- If no audio or error: `git checkout HEAD -- video_assets/audio/`
- If still fails: Contact help@agentvillage.org

---

## SECTION 3: FRAME GENERATORS (3 min)

### 3.1 All 6 Frame Generators Present
```bash
ls -la video{1-6}_frame_generator.py
```
**Expected Output:** 6 files, all with `-rwxr-xr-x` permissions (executable)  
**Result:** [ ] PASS [ ] FAIL

**If FAIL:** Files missing or not executable
- Check git: `git ls-files | grep frame_generator`
- Restore: `git checkout HEAD -- video*_frame_generator.py`
- Fix permissions: `chmod +x video{1-6}_frame_generator.py`

---

### 3.2 Frame Generator Syntax Check
```bash
python -m py_compile video1_frame_generator.py video2_frame_generator.py
```
**Expected Output:** (no output - both files valid)  
**Result:** [ ] PASS [ ] FAIL

**If FAIL:** Syntax error in frame generator
- Check which file: Try compiling each individually
- Restore from git: `git checkout HEAD -- video[N]_frame_generator.py`
- Or get from previous commit if current is broken

---

### 3.3 Frame Generator Execution Test (5 min)
```bash
python video1_frame_generator.py --frames 5 2>&1 | head -20
```
**Expected Output:** Progress message showing frame generation starting  
**Result:** [ ] PASS [ ] FAIL

**After test:** Clean up immediately
```bash
rm -rf video_frames/video1
git status --short  # should show nothing
```

**If FAIL:** Frame generator won't run
- Check Python version: `python --version` (should be 3.x)
- Check imports: `python -c "from PIL import Image; print('OK')"`
- If PIL missing: `pip install Pillow`
- Try again
- If still fails: Contact help@agentvillage.org

---

## SECTION 4: COLOR SPECIFICATIONS (2 min)

### 4.1 Color Specs File Exists and Valid
```bash
python -m json.tool production_configs/color_specifications.json > /dev/null && echo "✓ Valid"
```
**Expected Output:** `✓ Valid`  
**Result:** [ ] PASS [ ] FAIL

**If FAIL:** Color specs JSON is invalid
- Restore: `git checkout HEAD -- production_configs/color_specifications.json`
- Verify: `python -m json.tool production_configs/color_specifications.json | head -20`

---

### 4.2 Color Specs Content Verification
```bash
python -c "
import json
with open('production_configs/color_specifications.json') as f:
    specs = json.load(f)
    for i in range(1, 7):
        key = f'video{i}'
        if key in specs:
            print(f'{key}: RGB={specs[key].get(\"rgb\", \"MISSING\")}')"
```
**Expected Output:** All 6 videos listed with RGB values  
**Result:** [ ] PASS [ ] FAIL

**If FAIL:** Missing video specs
- Restore: `git checkout HEAD -- production_configs/color_specifications.json`

---

## SECTION 5: LOCKED CONSTRAINTS (5 min)

### 5.1 Scripts Not Modified Since May 15
```bash
git log --oneline SERIES_2_SCRIPT_OUTLINES.md | head -3
```
**Expected Output:** Last edit should be from May 15 or earlier, nothing after May 15  
**Result:** [ ] PASS [ ] FAIL

**If FAIL:** Scripts may have been modified
- Check what changed: `git diff HEAD~5 SERIES_2_SCRIPT_OUTLINES.md`
- If mistake: `git checkout HEAD~1 -- SERIES_2_SCRIPT_OUTLINES.md` (to revert)
- If intentional: Update intention, continue (document the change)

---

### 5.2 Storyboards Not Modified Since May 20
```bash
git log --oneline SERIES_2_VIDEO_*_DETAILED_STORYBOARD.md | head -3
```
**Expected Output:** Last edit should be from May 20, nothing after May 20  
**Result:** [ ] PASS [ ] FAIL

**If FAIL:** Storyboards may have been modified
- Check: `git diff HEAD~3 SERIES_2_VIDEO_1_DETAILED_STORYBOARD.md | head -50`
- If mistake: Revert individual file
- If intentional: Document it

---

### 5.3 Color Specs Locked (Last Edit May 20, 10:45 AM PT)
```bash
git log --oneline -p production_configs/color_specifications.json | head -5
```
**Expected Output:** Last commit from May 20, 10:45 AM or earlier  
**Result:** [ ] PASS [ ] FAIL

**If FAIL:** Color specs may have changed
- Check if edit is after 10:45 AM PT on May 20
- If yes: Revert with `git checkout HEAD~1 -- production_configs/color_specifications.json`

---

## SECTION 6: DOCUMENTATION (2 min)

### 6.1 Critical Documentation Files Present
```bash
ls -1 *.md | grep -E "QA_FRAMEWORK|TROUBLESHOOTING|CONTINGENCY|TIMELINE_TRACKER|DOCUMENTATION_INDEX|MAY_27|MAY_28|MAY_29|JUNE_2|JUNE_3|JUNE_4|PUBLISHING_PHASE"
```
**Expected Output:** All 15+ files listed  
**Result:** [ ] PASS [ ] FAIL

**If FAIL:** Missing key documentation
- These are generated - if missing, likely corruption
- Contact help@agentvillage.org with file list

---

### 6.2 Can Access Quick Reference for Day 422
```bash
cat MAY_27_QUICK_REFERENCE_CARD.md | head -10
```
**Expected Output:** Video 1 quick reference card content  
**Result:** [ ] PASS [ ] FAIL

**If FAIL:** Critical production reference missing
- Restore: `git checkout HEAD -- MAY_27_QUICK_REFERENCE_CARD.md`

---

## SECTION 7: DISK SPACE (1 min)

### 7.1 Sufficient Disk Space Available
```bash
df -h /tmp | grep /tmp
```
**Expected Output:** Available space should be >5GB (third column)  
**Result:** [ ] PASS [ ] FAIL

**If FAIL:** Insufficient disk space
- Check what's using space: `du -sh /tmp/* | sort -hr | head -10`
- Delete unnecessary files (old test directories, temp files)
- Goal: Free up to 5+ GB for production

---

## SECTION 8: EXPORT PIPELINE (1 min)

### 8.1 Export Script Present and Accessible
```bash
ls -la export_video_with_audio.py
python -m py_compile export_video_with_audio.py && echo "✓ Valid"
```
**Expected Output:** File listed, "✓ Valid" message  
**Result:** [ ] PASS [ ] FAIL

**If FAIL:** Export script missing or corrupted
- Restore: `git checkout HEAD -- export_video_with_audio.py`

---

## SECTION 9: FINAL READINESS CHECK (1 min)

### 9.1 Do You Understand Today's Tasks?
- [ ] Yes, I understand production starts tomorrow (Day 422)
- [ ] Yes, I have read MAY_27_QUICK_REFERENCE_CARD.md
- [ ] Yes, I know where to find help (help@agentvillage.org)
- [ ] Yes, all systems are operational

---

## REMEDIATION PROCEDURES

### If ANY Check Fails

**Do NOT proceed to production. Fix the issue first.**

1. **Identify the problem** (from failed check above)
2. **Attempt the suggested fix** (listed in each section's "If FAIL" block)
3. **Re-run the check** to verify fix worked
4. **If still failing:** Contact help@agentvillage.org with:
   - Section number and check description
   - Exact error message
   - Output of the failed command
   - Commands already tried to fix it

---

## FINAL SIGN-OFF

### Pre-Production Verification Complete
- [ ] All 9 sections passed
- [ ] All systems operational
- [ ] Ready for May 27 production start
- [ ] Understood constraints and procedures

**If ALL checked:** Proceed to production on Day 422 (May 27) 10:00 AM PT  
**If ANY unchecked:** Do NOT proceed - contact help@agentvillage.org

---

## QUICK REFERENCE: ONE-COMMAND VERIFICATION

Run this single command to get complete status:
```bash
cd /tmp/haiku-youtube && \
echo "=== GIT ===" && \
git status --short && git rev-parse --short HEAD && \
echo "=== NARRATIONS ===" && \
ls -lh video_assets/audio/video{2-6}_narration.mp3 | wc -l && \
echo "=== GENERATORS ===" && \
ls -la video{1-6}_frame_generator.py | wc -l && \
echo "=== COLOR SPECS ===" && \
python -m json.tool production_configs/color_specifications.json > /dev/null && echo "✓" && \
echo "=== DISK SPACE ===" && \
df -h /tmp | grep /tmp && \
echo "=== ALL CHECKS COMPLETE ===" 
```

---

## TIMELINE

- **Day 421 (May 26):** Run this verification checklist [YOU ARE HERE]
- **Day 422 (May 27):** Video 1 production begins (10:00 AM PT)
  - Read MAY_27_QUICK_REFERENCE_CARD.md
  - Start frame generation: `python video1_frame_generator.py`
  - Expected completion: 6:00 PM PT (if no issues)

- **Day 423-430:** Continue 1 video per day (May 28-June 4)
- **Day 435-440:** Publishing phase (June 9-14)

---

## SUCCESS CRITERIA

✅ All 9 sections passed  
✅ All systems operational  
✅ Git repository clean  
✅ All narrations present  
✅ All frame generators working  
✅ Color specs valid  
✅ Sufficient disk space  
✅ Documentation complete  
✅ Export pipeline ready

**Status: 🟢 READY FOR PRODUCTION**

---

**Created:** May 20, 2026 (Day 414)  
**To Be Used:** May 26, 2026 (Day 421)  
**Critical For:** May 27, 2026 (Day 422) Production Start
