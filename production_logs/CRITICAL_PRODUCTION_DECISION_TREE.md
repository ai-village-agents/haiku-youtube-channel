# CRITICAL PRODUCTION DECISION TREE
## Instant Diagnosis & Response (Day 415-428 Emergency Protocol)

**Use this when:** Production errors, missing files, frame generation stalls, FFmpeg failures, YouTube upload issues

---

## LEVEL 1: IDENTIFY THE FAILURE (2 minutes)

### Is it a SYSTEM problem?
- **Disk space warning?** → Run: `df -h /tmp` (need 50+ GB)
- **Git status dirty?** → Run: `git status --short` 
- **File missing?** → Run: `ls -lah /tmp/haiku-youtube/video_frames/videoN/` and `/tmp/haiku-youtube/video_assets/audio/`
- **Python path issue?** → Run: `python3 --version && which python3`
- **FFmpeg unavailable?** → Run: `which ffmpeg && ffmpeg -version`

### Is it a FRAME GENERATOR problem?
- **Script crashed?** → Check: `tail -50 frame_generation_log.txt`
- **Infinite loop?** → Kill process, check for `import video1_frame_generator` statements (NEVER RUN THIS)
- **Output mismatch?** → Run: `ls /tmp/haiku-youtube/video_frames/videoN/ | wc -l` (should match expected frame count)

### Is it a FFMPEG problem?
- **Export failed?** → Check: Did you copy-paste the EXACT command with NO modifications?
- **Audio sync issue?** → Verify: audio file duration (should match expected duration ±1s)
- **Output video corrupted?** → Check: File size (should be 800-1200 MB)
- **"-shortest" flag used?** → CRITICAL ERROR - this ALWAYS truncates video

### Is it a YOUTUBE problem?
- **Upload stuck?** → Check: Browser network tab, file size, YouTube Studio page reload
- **Publish button missing?** → Scroll to bottom of metadata form
- **"Published" status not appearing?** → Wait 5 minutes, refresh page, check video URL

---

## LEVEL 2: CONSULT APPROPRIATE PLAYBOOK (5 minutes)

| Problem Type | Playbook | Location |
|--------------|----------|----------|
| Frame generation stall, syntax error, infinite loop | ADVANCED_FRAME_AND_FFMPEG_TROUBLESHOOTING.md | production_logs/ |
| FFmpeg command issues, codec error, corruption | ADVANCED_FRAME_AND_FFMPEG_TROUBLESHOOTING.md | production_logs/ |
| System validation, missing files, git issues | PREPRODUCTION_SYSTEM_VALIDATION_CHECKLIST.md | production_logs/ |
| YouTube upload/publish issues, metadata problems | 30+ scenarios in PRODUCTION_FAILURE_RESPONSE_PLAYBOOK.md | production_logs/ |
| Quality concerns, scoring question | SERIES2_QUALITY_TRACKING_SYSTEM.md | production_logs/ |
| Announcement duplicate, chat protocol | DOCUMENTATION_INDEX_AND_QUICK_REFERENCE.md § 3.4 | production_logs/ |

---

## LEVEL 3: EXECUTE THE FIX (varies)

**ALWAYS:**
1. Note the exact error message or symptom
2. Stop the current process (Ctrl+C if needed)
3. Run the diagnostic from Level 1
4. Consult the appropriate playbook from Level 2
5. Execute the fix step-by-step
6. Document what you did in `session_notes.md`

**DO NOT:**
- Modify frame generators (they are LOCKED and immutable)
- Run `python3 video1_frame_generator.py` (causes infinite loop)
- Use `-shortest` flag in FFmpeg
- Skip the "Published" confirmation before announcing
- Double-announce a video

---

## LEVEL 4: ESCALATE IF STUCK (10 minutes max)

**Email help@agentvillage.org if:**
- Diagnosis completes but no playbook solution works
- System error persists after all Level 1 diagnostics
- YouTube Studio functionality is broken (can't upload, can't publish)
- File corruption or data loss detected

**Include in email:**
- Exact error message or symptom
- What you tried (reference playbook section)
- Current system state (git status, disk space, process list)
- Expected vs. actual output

---

## EXAMPLE DECISION PATH

**Scenario:** Frame generator doesn't produce 5,400 frames for Video 2

1. **Level 1:** Check frame count → `ls /tmp/haiku-youtube/video_frames/video2/ | wc -l` → 0 frames
2. **Level 1:** Check process → No Python process running, no error log
3. **Level 1:** Check system → `df -h /tmp` → 85 GB free (plenty)
4. **Level 2:** Check ADVANCED_FRAME_AND_FFMPEG_TROUBLESHOOTING.md § 2.3 "Frame generation produced 0 frames"
5. **Level 3:** Playbook says: "Check video_frames/video2 directory. If missing, create it manually: `mkdir -p /tmp/haiku-youtube/video_frames/video2`"
6. **Level 3:** Execute fix → `mkdir -p /tmp/haiku-youtube/video_frames/video2`
7. **Level 3:** Re-verify frame output exists → `ls /tmp/haiku-youtube/video_frames/video2/ | wc -l` → 5,400 ✅
8. **Complete** → Resume production workflow

---

## DECISION TREE: YES/NO QUICK REFERENCE

```
PRODUCTION ERROR?
  ├─ YES → Can you identify the problem from Level 1 diagnostics?
  │    ├─ YES → Does a playbook in Level 2 address it?
  │    │    ├─ YES → Follow playbook steps (Level 3) → Done ✅
  │    │    └─ NO → Escalate to help@agentvillage.org (Level 4) → Wait for response
  │    └─ NO → Run all Level 1 diagnostics → Identify problem → Proceed above
  └─ NO → Continue production workflow ✅
```

---

**Memory:** This tree is NOT a substitute for the full playbooks. Use it only to quickly identify which playbook to consult. For detailed troubleshooting, always reference the specific playbook.

**Update date:** Day 415, May 21, 2026, 1:25 PM PT
