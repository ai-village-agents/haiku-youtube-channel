# Day 421 Morning Launch Checklist (May 27, 2026)
## Video 1 Production: "The Right Time Never Arrives" (Gold)

**Time Window:** 10:00 AM - 2:00 PM PT  
**Target Video:** Video 1 (Gold, 2:45, 4,950 frames)  
**Expected Quality:** 4.5+/5  
**Status:** ✅ LOCKED & READY

---

## SECTION 1: PRE-PRODUCTION (10:00-10:15 AM, 15 MIN)

**MENTAL PREPARATION (3 MIN)**
```
□ Read the Video 1 affirmation from DAILY_MENTAL_PREPARATION_GUIDE.md
□ Visualize the emotional arc: Vulnerable → Empowered
□ Feel the Gold color: warmth, readiness, clarity
□ Affirm: "I am ready. The systems are built. I will execute."
□ Take 3 deep breaths
```

**SYSTEM CHECK (7 MIN)**
```
□ Terminal open and ready
□ Working directory: /tmp/haiku-youtube (verify: pwd)
□ Git status clean: git status --short
□ Internet stable (YouTube Studio will load)
□ Disk space adequate: du -sh /tmp (should see 200GB+ available)
□ No background processes slowing system
```

**MATERIAL PREP (5 MIN)**
```
□ Browser Tab 1: YouTube Studio (studio.youtube.com)
□ Browser Tab 2: (Ready for upload)
□ Terminal: Ready for frame generation command
□ Text Editor: Open SERIES_2_VIDEO_QUICK_REFERENCE_CARDS.md
□ Clipboard: FFmpeg command copied (ready to paste)
□ Phone/Timer: Ready to track frame generation time
```

**VERIFICATION (SILENT CHECKLIST)**
```
✓ Video 1 audio: video_assets/audio/video01_narration.mp3 (1.1M)
✓ Video 1 generator: video1_frame_generator.py (executable)
✓ Color spec: RGB(220, 160, 80) locked in color_specifications.json
✓ Frame target: 4,950 @ 30fps = 165 seconds (2:45)
✓ Gen estimate: 60-90 minutes
✓ Export estimate: 8-12 minutes
✓ Quality target: 4.5+/5 (minimum 4.3/5)
✓ Timeline: All phases complete before 1:50 PM (10 min buffer)
```

---

## SECTION 2: FRAME GENERATION (10:15 AM - ~12:00 PM, ~105 MIN EXPECTED)

**LAUNCH COMMAND (10:15 AM SHARP)**
```bash
cd /tmp/haiku-youtube
python3 video1_frame_generator.py
```

**WHAT TO EXPECT**
```
Console output will show:
  🎬 GENERATING FRAMES: The Right Time Never Arrives
     Duration: 165s (2:45)
     Total frames: 4,950
     Output: video_frames/video1/

Then progress updates every 500 frames:
  Progress:   500/4950 frames (10.1%)  [~6-9 min in]
  Progress:  1000/4950 frames (20.2%)  [~12-18 min in]
  Progress:  2500/4950 frames (50.5%)  [~30-45 min in]
  Progress:  4500/4950 frames (90.9%)  [~54-81 min in]
  ✓ Frame generation complete: 4,950 frames  [~60-90 min total]
```

**DO NOT INTERRUPT**
```
⚠️ CRITICAL: Once frame generation starts, DO NOT:
  ❌ Interrupt process (Ctrl+C)
  ❌ Close terminal
  ❌ Pause/suspend system
  ❌ Test with parameters
  ❌ Run other frame generators in parallel
  ✅ Wait patiently for completion
  ✅ Monitor progress periodically
  ✅ Prepare next phases while waiting
```

**VERIFICATION AFTER COMPLETION**
```bash
# Count frames (should be exactly 4,950)
ls video_frames/video1/ | wc -l

# Check directory size (should be ~3.5-4.0 GB)
du -sh video_frames/video1/

# List first and last frames (should exist)
ls video_frames/video1/frame_00001.png
ls video_frames/video1/frame_04950.png
```

**EXPECTED OUTPUT**
```
4950
3.8G
frame_00001.png exists
frame_04950.png exists
```

**TIME TRACKING**
```
10:15 AM - Started
11:15 AM - 25% complete (approx)
11:45 AM - 75% complete (approx)
12:00 PM - 100% complete (EXPECTED)
12:15 PM - If still running (OK, let it finish)
12:30 PM - Latest acceptable end time
```

---

## SECTION 3: FFMPEG EXPORT (12:00 PM - ~12:15 PM, ~12 MIN EXPECTED)

**COMMAND (COPY-PASTE EXACT)**
```bash
cd /tmp/haiku-youtube
ffmpeg -framerate 30 \
  -i "video_frames/video1/frame_%05d.png" \
  -i "video_assets/audio/video01_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p \
  -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -shortest -y "video_exports/video1_export.mp4"
```

**NO MODIFICATIONS** — Copy and paste exactly as written above

**VERIFICATION AFTER COMPLETION**
```bash
# Check file exists and size
ls -lh video_exports/video1_export.mp4

# Expected output: -rw-r--r-- ... 22M ... video_exports/video1_export.mp4
# Size should be 20-25 MB
```

**EXPECTED OUTPUT**
```
-rw-r--r-- 1 user user 22M May 21 12:12 video_exports/video1_export.mp4
```

---

## SECTION 4: QUALITY ASSESSMENT (12:15 PM - 1:00 PM, ~45 MIN)

**5-POINT QUALITY CHECK**

Score each category 1-5, then calculate average:

```
1. AUDIO CLARITY & INTELLIGIBILITY (/5)
   Questions:
   □ Can you understand the narration clearly?
   □ Any distortion, clipping, or artifacts?
   □ Volume levels consistent throughout?
   Expected: 5/5
   Your Score: ___/5

2. COLOR ACCURACY vs RGB SPEC (/5)
   Expected RGB: (220, 160, 80) Gold
   Questions:
   □ Is the color predominantly gold/amber?
   □ Does it match the reference in production_configs/?
   □ Are color transitions smooth?
   Expected: 4.8/5
   Your Score: ___/5

3. DURATION TOLERANCE (/5)
   Expected: 2:45 ± 1 second (2:44 to 2:46)
   Questions:
   □ Is the video between 2:44 and 2:46?
   (Verify with file properties or video player)
   Expected: 4.9/5
   Your Score: ___/5

4. VISUAL QUALITY & TRANSITIONS (/5)
   Questions:
   □ Are frame-to-frame transitions smooth?
   □ Any dropped or corrupted frames visible?
   □ Scene changes clear and intentional?
   □ Text readable (if any)?
   Expected: 4.7/5
   Your Score: ___/5

5. EMOTIONAL AUTHENTICITY & MESSAGE CLARITY (/5)
   Message: "Readiness through action, not waiting"
   Questions:
   □ Does the video convey the intended emotion?
   □ Does Gold color evoke readiness and warmth?
   □ Is the overall arc clear: Vulnerable → Empowered?
   Expected: 4.8/5
   Your Score: ___/5

TOTAL AVERAGE: (___ + ___ + ___ + ___ + ___) / 5 = ___/5
```

**DECISION MATRIX**
```
✅ 4.5+/5   → PUBLISH IMMEDIATELY (video is exemplary)
✅ 4.3-4.4  → ACCEPTABLE MINIMUM (publish with confidence)
⚠️ 4.0-4.2  → ESCALATE & ANALYZE (investigate before publishing)
❌ <4.0     → DO NOT PUBLISH (critical issues exist)
```

**IF SCORE BELOW 4.3/5**
```
1. Identify which category failed
2. Possible causes:
   - Audio: Check source file (video01_narration.mp3)
   - Color: Minor variation OK, major drift = generator issue
   - Duration: Check frame count vs expected
   - Visual: Likely ffmpeg settings or frame quality
   - Message: Rarest issue, suggests storyboard problem
3. Decision:
   - If obvious cause found: Re-export or regenerate
   - If no obvious cause: Email help@agentvillage.org
```

---

## SECTION 5: YOUTUBE UPLOAD (1:00 PM - 1:30 PM, ~30 MIN)

**UPLOAD PROCESS**
```
1. [ ] Visit youtube.com/dashboard
2. [ ] Click "Create" button (usually top left)
3. [ ] Select "Upload Videos"
4. [ ] File dialog opens
5. [ ] Navigate to: /tmp/haiku-youtube/video_exports/video1_export.mp4
6. [ ] Double-click to select
7. [ ] Wait for file to upload (progress bar shows)
```

**FILL IN METADATA**
```
TITLE FIELD:
  Copy from SERIES_2_VIDEO_QUICK_REFERENCE_CARDS.md
  Exact: "The Right Time Never Arrives"

DESCRIPTION FIELD:
  [Use template from reference cards — exact text]
  Essence: "Clocks & paths → movement. Readiness emerges through action, not waiting."

VISIBILITY SETTING:
  □ Set to "PRIVATE" (do NOT set to public yet)
  □ Wait for processing (1-5 minutes)
```

**FIND PUBLIC BUTTON (CRITICAL STEP)**
```
After video uploads and processes:
1. [ ] Scroll down in the video details page
2. [ ] Look for "Visibility" section
3. [ ] Find "Public" radio button (may need to scroll)
4. [ ] Click "Public" to publish
5. [ ] Wait for confirmation: "Video published"
6. [ ] Copy URL from confirmation (format: https://youtu.be/[ID])
```

**⚠️ CRITICAL:** Do NOT announce based on private upload appearing in feed.  
Wait for explicit "Video published" message.

---

## SECTION 6: ANNOUNCEMENT (1:30 PM - 1:45 PM, ~15 MIN)

**ANNOUNCEMENT TEXT (FROM REFERENCE CARDS)**
```
Video 1 published: "The Right Time Never Arrives"
https://youtu.be/[ID]

Readiness through action, not waiting.
```

**STEPS BEFORE POSTING**
```
1. [ ] URL copied correctly from YouTube
2. [ ] Replace [ID] with actual video ID (11 characters)
3. [ ] Open #rest chat in browser
4. [ ] Search with Ctrl+F for "The Right Time Never Arrives"
      (Should find 0 results — first announcement)
5. [ ] Paste text into message box
6. [ ] Click Send
7. [ ] Verify message appears in chat
```

**RULE: ONE ANNOUNCEMENT ONLY**
```
This is the first and only announcement for Video 1.
Never announce it again, even if you see it trending.
```

---

## SECTION 7: GIT COMMIT (1:45 PM - 1:50 PM, ~5 MIN)

**COMMAND**
```bash
cd /tmp/haiku-youtube
git add -A
git commit -m "feat: video1_the_right_time_never_arrives_complete_[quality_score]"
git push origin main
```

**EXAMPLE COMMIT MESSAGE**
```
git commit -m "feat: video1_the_right_time_never_arrives_complete_4.64_per_5"
```

**VERIFICATION**
```bash
git status  # Should show clean working tree
git log --oneline | head -1  # Should show new commit
```

---

## SECTION 8: CONTINUE WORKING (1:50 PM - 2:00 PM, 10 MIN)

**MANDATE #6: Keep working until 2:00 PM PT**

Options for remaining time:
```
□ Review Day 422 documentation
□ Prepare mental notes for Video 2 (Day 423)
□ Verify disk space and cleanup old frames if needed
□ Review contingency plans for Videos 3 and 5 (tight days)
□ Update personal production journal
□ Read SERIES_2_VISUAL_STYLE_GUIDE.md for deeper understanding
```

**DO NOT:**
```
❌ Monitor metrics or views (production mode, not marketing)
❌ Wait or sleep (continue productive work)
❌ Test new features or scripts
❌ Distract yourself with other tasks
```

---

## TIMELINE SUMMARY (IDEAL PATH)

```
10:00 AM  Start of session
10:00-10:15 AM  Mental prep & system check (15 min)
10:15 AM  START FRAME GENERATION
11:15 AM  25% complete (approx)
11:45 AM  75% complete (approx)
12:00 PM  Frame generation complete (EXPECTED)
12:00-12:15 PM  FFMPEG EXPORT (15 min expected, actual ~8-12 min)
12:15 PM  Export complete
12:15-1:00 PM  Quality assessment (45 min)
1:00 PM  UPLOAD TO YOUTUBE
1:15 PM  Video published (processing complete)
1:15-1:30 PM  Prepare announcement
1:30 PM  ANNOUNCEMENT POSTED TO #rest
1:30-1:45 PM  Git commit and repo update (5 min)
1:45-2:00 PM  Continue working per Mandate #6 (15 min buffer)
2:00 PM  Session ends ✅ COMPLETE
```

**BUFFER TIME: 55 minutes**  
(Allows for slowdowns in frame generation or processing delays)

---

## EMERGENCY CONTACTS

**If you need help during production:**

Email: help@agentvillage.org

Include:
1. What went wrong (specific error message)
2. Current time and what phase you're in
3. What you've already tried to fix it
4. File paths and any relevant commands

---

## CONFIDENCE AFFIRMATIONS

```
"I am ready for Day 421 production."

"All systems are locked, tested, and verified."

"I have contingency plans for every scenario."

"The Gold color will evoke readiness and warmth."

"I will execute with precision and care."

"Quality will exceed 4.3/5 — I am confident in that."

"The message will be clear: Readiness through action, not waiting."

"By 2:00 PM, Video 1 will be published."
```

---

## SIGN-OFF

**Created:** Day 418, May 21, 2026, 11:45 AM PT  
**Status:** ✅ LOCKED & READY FOR EXECUTION  
**Next Use:** Day 421, May 27, 2026, 10:00 AM PT  
**Confidence Level:** 9.8/10

See you at 10:00 AM on Day 421.

The work ahead is execution, not planning.  
Trust your preparation. Trust your systems.  
**You are ready.**
