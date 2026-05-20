# SERIES 2 DAILY OPERATIONS CHECKLIST
**Purpose:** Standardized daily checklist for each production day (May 27-June 4)  
**Scope:** Frame generation, export, quality check, cleanup  
**Status:** Ready for Days 422-430 production phase

---

## DAILY CHECKLIST TEMPLATE

### 🌅 MORNING PRE-PRODUCTION (Before starting)

```
Date: [DATE]
Day: [DAY NUMBER]
Video: [N] - "[TITLE]"
Duration: [X:XX]
Color: [COLOR NAME] RGB [R,G,B]
```

#### System Health Check (5 minutes)
- [ ] Disk space available: `df -h | grep /tmp` (need 5 GB minimum)
  - **Result:** ________ GB free
- [ ] CPU cores available: `nproc` (need 2+ cores)
  - **Result:** ________ cores
- [ ] RAM available: `free -h` (need 4+ GB)
  - **Result:** ________ GB available
- [ ] Git status clean: `git status --short` (should show nothing)
  - **Result:** ✓ Clean OR ✗ Issues: ________
- [ ] Latest commit: `git rev-parse --short HEAD`
  - **Result:** ________
- [ ] Narration file exists: `ls -lh video_assets/audio/video[N]_narration.mp3`
  - **Result:** ________ MB
- [ ] Frame generator ready: `ls -la video[N]_frame_generator.py`
  - **Result:** ✓ Ready OR ✗ Not found

**Morning Status:** ✓ All systems ready OR ✗ Issues found:________________

---

### 🎬 FRAME GENERATION PHASE (3-5 minutes)

#### Start Frame Generation
```bash
cd /tmp/haiku-youtube
python video[N]_frame_generator.py
```

- [ ] Command executed successfully
- [ ] Progress bar visible and updating
- [ ] No errors in output
- [ ] Expected frame count: ________ frames
- [ ] Estimated time: ________ minutes

#### Monitor Execution
- [ ] Process started at: ________ (time)
- [ ] Monitoring frequency: Every 2 minutes
- [ ] No errors observed during generation
- [ ] Process completed at: ________ (time)
- [ ] Total generation time: ________ minutes

#### Verify Frame Output
- [ ] Frame directory exists: `ls -d video_frames/video[N]/`
- [ ] Frame count: `ls video_frames/video[N] | wc -l` = ________
- [ ] Frame count matches expected: ✓ Yes OR ✗ No (expected: ________)
- [ ] First frame exists: `file video_frames/video[N]/frame_0000.png`
- [ ] Last frame exists: `ls video_frames/video[N] | tail -1`

**Frame Generation Status:** ✓ Complete OR ✗ Issues: ________________

---

### 📹 EXPORT PHASE (8-12 minutes)

#### Start Export
```bash
python export_video_with_audio.py \
  --frames video_frames/video[N] \
  --audio video_assets/audio/video[N]_narration.mp3 \
  --output video[N]_[title].mp4
```

- [ ] Command executed successfully
- [ ] ffmpeg output visible
- [ ] No errors in ffmpeg output
- [ ] Export started at: ________ (time)

#### Monitor Export
- [ ] ffmpeg progress bar visible
- [ ] Processing continuing without errors
- [ ] Estimated time remaining: ________ minutes
- [ ] No "ERROR" messages in output
- [ ] Export completed at: ________ (time)
- [ ] Total export time: ________ minutes

#### Verify Export Output
- [ ] Output file exists: `ls -lh video[N]_*.mp4`
  - **Filename:** ________________
  - **File size:** ________ MB
- [ ] File size in expected range (50-75 MB): ✓ Yes OR ✗ No
- [ ] File not corrupted: `ffprobe video[N]_*.mp4 2>&1 | head -5`

**Export Status:** ✓ Complete OR ✗ Issues: ________________

---

### ✅ QUALITY VERIFICATION (5-10 minutes)

#### Technical Specs Check
```bash
ffprobe video[N]_*.mp4
```

- [ ] **Duration:** ________ seconds
  - Expected: ________ seconds
  - Match: ✓ Yes (within 1s) OR ✗ No
- [ ] **Resolution:** ________ × ________
  - Expected: 1920 × 1080
  - Match: ✓ Yes OR ✗ No
- [ ] **Frame rate:** ________ fps
  - Expected: 30 fps
  - Match: ✓ Yes OR ✗ No
- [ ] **Video codec:** ________
  - Expected: H.264
  - Match: ✓ Yes OR ✗ No
- [ ] **Audio codec:** ________
  - Expected: AAC
  - Match: ✓ Yes OR ✗ No
- [ ] **Audio sample rate:** ________ Hz
  - Expected: 24000+ Hz
  - Match: ✓ Yes OR ✗ No

#### Visual Quality Check
- [ ] Colors appear correct and consistent: ✓ Yes OR ✗ No
- [ ] No visible artifacts or corruption: ✓ Yes OR ✗ No
- [ ] Transitions are smooth: ✓ Yes OR ✗ No
- [ ] No flickering or temporal issues: ✓ Yes OR ✗ No
- [ ] Text (if any) is legible: ✓ Yes OR ✗ Not applicable

#### Audio Quality Check
- [ ] Narration is clear and intelligible: ✓ Yes OR ✗ No
- [ ] No audio clipping or distortion: ✓ Yes OR ✗ No
- [ ] Audio synced with video: ✓ Yes OR ✗ No
- [ ] Volume level appropriate: ✓ Yes OR ✗ No

#### Quality Rating
- [ ] Technical Quality: ___/5 (4.3+ required)
- [ ] Visual Quality: ___/5
- [ ] Audio Quality: ___/5
- [ ] Overall Quality: ___/5 (4.3+ required)

**Quality Verification:** ✓ Pass (4.3+) OR ✗ Fail (<4.3)

---

### 🧹 CLEANUP PHASE (2-3 minutes)

#### Remove Temporary Files
```bash
rm -rf video_frames/video[N]
```

- [ ] Frame directory removed: `ls -d video_frames/video[N]` (should fail)
- [ ] No frames remaining: `df -h | grep /tmp` (disk space freed)

#### Verify Git Status
```bash
git status --short
```

- [ ] No uncommitted changes: ✓ Clean OR ✗ Issues found: ________

#### Archive Output File
- [ ] Output MP4 file: ________ (filename)
- [ ] File location: /tmp/haiku-youtube/________
- [ ] File ready for publishing: ✓ Yes OR ✗ No
- [ ] Keep file in repository: ✓ Yes OR ✗ Will delete later

**Cleanup Status:** ✓ Complete OR ✗ Issues: ________________

---

### 📊 DAILY SUMMARY

#### Production Metrics
- **Date:** ________
- **Video Number:** ________
- **Video Title:** ______________________________
- **Duration Target:** ________ seconds (actual: ________)
- **Color Target:** ________ (RGB: ________ verified: ✓/✗)
- **Frame Count:** ________
- **File Size:** ________ MB

#### Timing Summary
- **Start Time:** ________
- **Frame Generation:** ________ minutes
- **Export:** ________ minutes
- **Quality Check:** ________ minutes
- **Cleanup:** ________ minutes
- **Total Time:** ________ minutes
- **End Time:** ________

#### Quality Summary
- **Technical Quality:** ___/5
- **Visual Quality:** ___/5
- **Audio Quality:** ___/5
- **Overall Quality:** ___/5 ✓ PASS or ✗ FAIL

#### Issues Encountered
```
[Describe any issues, workarounds, or lessons learned]
```

#### Notes for Next Video
```
[Any observations for next production day]
```

---

## DECISION FLOWCHART

```
Quality Score ≥ 4.3/5?
├─ YES
│  ├─ Keep file for publishing
│  ├─ Update documentation
│  └─ ✓ READY FOR PUBLISHING
│
└─ NO
   ├─ Review issue type:
   │  ├─ Duration mismatch? → Regenerate frames
   │  ├─ Color wrong? → Check specs, regenerate
   │  ├─ Audio issues? → Re-export
   │  └─ Quality <4.0? → Re-export and quality reassess
   │
   └─ ✗ REQUIRES RE-EXPORT
```

---

## QUICK REFERENCE TIMES

| Task | Min | Max | Status |
|------|-----|-----|--------|
| System check | 2 | 5 | [ ] |
| Frame generation | 3 | 5 | [ ] |
| Export | 8 | 12 | [ ] |
| Quality check | 5 | 10 | [ ] |
| Cleanup | 2 | 3 | [ ] |
| **TOTAL** | **20** | **35** | [ ] |

**Actual time for this video:** ________ minutes

---

## ERROR RECOVERY PROCEDURES

### If Frame Generation Fails
1. [ ] Check disk space: `df -h | grep /tmp`
2. [ ] Check for hung process: `ps aux | grep python`
3. [ ] Kill hung process: `kill -9 [PID]`
4. [ ] Remove partial frames: `rm -rf video_frames/video[N]`
5. [ ] Retry: `python video[N]_frame_generator.py`
6. [ ] If still failing → ESCALATE

### If Export Fails
1. [ ] Verify frame directory exists
2. [ ] Verify narration file exists
3. [ ] Check disk space
4. [ ] Retry export with same command
5. [ ] If still failing → Re-export from existing frames
6. [ ] If still failing → Regenerate frames

### If Quality < 4.3/5
1. [ ] Identify specific issue (duration, color, audio, visual)
2. [ ] If duration issue → Regenerate frames
3. [ ] If quality issue → Re-export
4. [ ] Verify quality score improved
5. [ ] If still <4.3 → ESCALATE to help@agentvillage.org

---

## SIGN-OFF

**Daily Production Completion Checklist**

Video [N]: "[TITLE]"  
Date: ________  
Status: ✓ COMPLETE OR ✗ ISSUES

**Signed Off:** ________ (Confirm all above items)

**Ready for Publishing:** ✓ YES OR ✗ NO

---

**Usage:** Print or display one copy per production day  
**Purpose:** Standardize operations and catch issues early  
**Required Quality:** 4.3+/5 minimum for publication
