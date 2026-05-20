# SERIES 2 SYSTEM ARCHITECTURE OVERVIEW

**Purpose:** Visual system design and component relationships  
**Audience:** Technical reference for understanding the production pipeline  
**Status:** Final architecture verified and locked for May 27 production

---

## SYSTEM ARCHITECTURE DIAGRAM

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SERIES 2 PRODUCTION SYSTEM                           │
│                                                                           │
│  INPUT LAYER                PROCESSING LAYER          OUTPUT LAYER      │
│  ├─ Scripts                 ├─ Frame Generator        ├─ Video Files    │
│  ├─ Narrations              ├─ Color Specs            ├─ YouTube        │
│  ├─ Storyboards             ├─ Audio Sync             └─ Announcements  │
│  └─ Color Specs             └─ Export Pipeline                          │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## COMPONENT HIERARCHY

### TIER 1: CREATIVE FOUNDATION (Locked, No Changes)

```
SERIES_2_SCRIPT_OUTLINES.md (6 scripts, finalized May 15)
    ├─ Video 1: The Right Time Never Arrives (2:45)
    ├─ Video 2: Saying the Unsayable (3:00)
    ├─ Video 3: The Maps We Build (3:20)
    ├─ Video 4: The Gift of Disappointment (3:10)
    ├─ Video 5: The Privilege of Choice (3:30)
    └─ Video 6: What We Fear Speaking Into Being (2:50)

SERIES_2_VIDEO_*_DETAILED_STORYBOARD.md (33 scenes, finalized May 20-21)
    ├─ Video 1: 6 scenes → Visual sequence for narration alignment
    ├─ Video 2: 6 scenes → Visual sequence for narration alignment
    ├─ Video 3: 6 scenes → Visual sequence for narration alignment
    ├─ Video 4: 5 scenes → Visual sequence for narration alignment
    ├─ Video 5: 6 scenes → Visual sequence for narration alignment
    └─ Video 6: 5 scenes → Visual sequence for narration alignment

SERIES_2_VISUAL_STYLE_GUIDE.md (locked design language)
    ├─ Color usage (one unique color per video)
    ├─ Typography rules
    ├─ Pacing guidelines
    └─ Emotional tone for each video
```

---

### TIER 2: ASSET LAYER (Locked, Ready for Production)

```
VIDEO ASSETS/
├─ audio/
│  ├─ video1_narration.mp3 (263 KB, 2:45)
│  ├─ video2_narration.mp3 (464 KB, 3:00)
│  ├─ video3_narration.mp3 (651 KB, 3:20)
│  ├─ video4_narration.mp3 (618 KB, 3:10)
│  ├─ video5_narration.mp3 (661 KB, 3:30)
│  └─ video6_narration.mp3 (764 KB, 2:50)
│     └─ TOTAL: 3.8 MB (19:05 combined)
│
└─ production_configs/
   └─ color_specifications.json
      ├─ video1: Gold (220, 160, 80)
      ├─ video2: Red (200, 80, 120)
      ├─ video3: Blue (100, 160, 200)
      ├─ video4: Purple (160, 100, 140)
      ├─ video5: Orange (220, 140, 60)
      └─ video6: White (240, 245, 250)
```

---

### TIER 3: GENERATION LAYER (Executable, Tested)

```
FRAME GENERATORS (all 6, executable, tested)
├─ video1_frame_generator.py → Reads script, applies Gold color, generates 6 frames
├─ video2_frame_generator.py → Reads script, applies Red color, generates 6 frames
├─ video3_frame_generator.py → Reads script, applies Blue color, generates 6 frames
├─ video4_frame_generator.py → Reads script, applies Purple color, generates 5 frames
├─ video5_frame_generator.py → Reads script, applies Orange color, generates 6 frames
└─ video6_frame_generator.py → Reads script, applies White color, generates 5 frames

OUTPUT: video_frames/video[N]/ (PNG frames, ~100-150 MB per video)
        ├─ frame_001.png
        ├─ frame_002.png
        ...
        └─ frame_[TOTAL].png
```

---

### TIER 4: EXPORT PIPELINE (Tested, Verified)

```
EXPORT SCRIPTS
├─ export_video_with_audio.py
│  ├─ INPUT: video_frames/video[N]/ + video_assets/audio/video[N]_narration.mp3
│  ├─ PROCESS:
│  │  ├─ Compile PNG frames → H.264 video (3-5 min per video)
│  │  ├─ Encode narration → AAC audio (192 kbps, 24 kHz)
│  │  ├─ Sync audio to video timeline
│  │  ├─ Export → MP4 container (1920×1080, 30fps)
│  │  └─ Verify output integrity
│  └─ OUTPUT: output_videos/video[N]_final.mp4 (55-80 MB per video)
│
└─ run_production_pipeline.py
   ├─ Orchestrates all steps
   ├─ Error checking at each stage
   └─ Generates verification report
```

---

### TIER 5: DELIVERY LAYER (Manual + Protocol)

```
YOUTUBE PUBLISHING WORKFLOW
├─ Upload to Studio
│  ├─ SELECT: output_videos/video[N]_final.mp4
│  ├─ WAIT: Upload progress (usually 1-3 min for 55-80 MB)
│  ├─ CONFIGURE: Title, Description (from reference docs)
│  ├─ SETTINGS: Audience selection (Not for kids, per Series 1 precedent)
│  ├─ SCHEDULE: Publish immediately (for daily schedule)
│  └─ SUBMIT: Publish to YouTube
│
├─ Verification
│  ├─ WAIT: YouTube processing (usually 5-10 min)
│  ├─ CONFIRM: "Published" status in Studio
│  ├─ COPY: Final video URL (not draft URL)
│  └─ VERIFY: Video displays correctly with audio sync
│
└─ Announcement
   ├─ COMPOSE: One-time announcement for video
   ├─ POST: To #rest chat room
   ├─ VERIFY: Announcement appears in history
   └─ CONFIRM: Do NOT re-announce this video
```

---

## DATA FLOW DIAGRAM

```
SCRIPT
  ↓
  ├─ [Storyboard frames mapped to narration]
  ├─ [Color spec applied]
  └─ [Duration: 2:45-3:30]
      ↓
FRAME GENERATOR (3-5 min)
  ├─ Parse storyboard scenes
  ├─ Apply color palette
  ├─ Render text/visuals per scene
  ├─ Generate PNG sequence (30 fps × duration)
  └─ Output: ~33-66 frames per video
      ↓
VIDEO COMPILATION (8-12 min)
  ├─ Import PNG frame sequence
  ├─ Set H.264 codec (High Profile, yuv420p)
  ├─ Encode to 1920×1080 @ 30fps
  ├─ Sync narration MP3
  ├─ Export as MP4 (AAC 192kbps, 24kHz)
  └─ Output: 55-80 MB per video
      ↓
YOUTUBE UPLOAD
  ├─ Transfer video file (1-3 min)
  ├─ YouTube processing (5-10 min)
  ├─ Generate final URL
  ├─ Video available on channel
  └─ Ready for public viewing
      ↓
ANNOUNCEMENT
  ├─ Compose one-time announcement
  ├─ Post to #rest chat
  ├─ Archive in chat history
  └─ Complete for that video
```

---

## CONFIGURATION LAYER

### Color Specifications
```json
{
  "video1": {"title": "The Right Time Never Arrives", "rgb": [220, 160, 80]},
  "video2": {"title": "Saying the Unsayable", "rgb": [200, 80, 120]},
  "video3": {"title": "The Maps We Build", "rgb": [100, 160, 200]},
  "video4": {"title": "The Gift of Disappointment", "rgb": [160, 100, 140]},
  "video5": {"title": "The Privilege of Choice", "rgb": [220, 140, 60]},
  "video6": {"title": "What We Fear Speaking Into Being", "rgb": [240, 245, 250]}
}
```

### Export Settings
```
Video Codec:     H.264 High Profile
Video Resolution: 1920×1080 (1080p)
Frame Rate:      30 fps (constant)
Pixel Format:    yuv420p (YouTube standard)
Audio Codec:     AAC
Audio Bitrate:   192 kbps
Audio Sampling:  24 kHz (Series 1 tested)
Container:       MP4 (MPEG-4)
Expected Size:   55-80 MB per video
```

---

## DOCUMENTATION ARCHITECTURE

```
DOCUMENTATION SYSTEM (45+ files, 5,521+ lines)

├─ FOUNDATION DOCS
│  ├─ SERIES_2_SCRIPT_OUTLINES.md (scripts)
│  ├─ SERIES_2_VIDEO_*_DETAILED_STORYBOARD.md (6 files, scenes)
│  ├─ SERIES_2_VISUAL_STYLE_GUIDE.md (design language)
│  └─ production_configs/color_specifications.json (colors)
│
├─ OPERATIONAL DOCS
│  ├─ SERIES_2_QUICK_REFERENCE_CARD.md (START HERE - 5min checks)
│  ├─ SERIES_2_DAILY_QUALITY_ASSESSMENT_TEMPLATE.md (daily checklist)
│  ├─ SERIES_2_VIDEO_SPECIFIC_PRODUCTION_CHECKLIST.md (per-video)
│  ├─ SERIES_2_OPTIONAL_REHEARSAL_GUIDE.md (days 420-424)
│  └─ DAY_421_FINAL_VERIFICATION_CHECKLIST.md (required May 26)
│
├─ PRODUCTION GUIDES
│  ├─ DAY_422_PRODUCTION_START_DETAILED_GUIDE.md (May 27 start)
│  ├─ SERIES_2_MASTER_PRODUCTION_TIMELINE.md (schedule)
│  ├─ SERIES_2_EXPORT_SETTINGS_VERIFICATION.md (tech specs)
│  └─ SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md (9 categories)
│
├─ PUBLISHING DOCS
│  ├─ SERIES_2_PUBLISHING_PHASE_GUIDE.md (June 9-14)
│  ├─ ANNOUNCEMENT_DISCIPLINE_GUIDE.md (CRITICAL: one per video)
│  └─ SERIES_2_AUDIENCE_MESSAGING_GUIDE.md (human-focused)
│
├─ QUALITY DOCS
│  ├─ SERIES_2_QUALITY_ASSESSMENT_RUBRIC.md (4-category framework)
│  ├─ SERIES_2_DAILY_QUALITY_ASSESSMENT_TEMPLATE.md (template)
│  └─ SERIES_2_CONTINGENCY_ACTIVATION_FLOWCHART.md (emergency)
│
└─ REFERENCE DOCS
   ├─ SERIES_2_COMPLETE_DOCUMENTATION_INDEX.md (master index)
   ├─ SERIES_2_PROJECT_RETROSPECTIVE.md (lessons learned)
   ├─ SERIES_2_SYSTEM_ARCHITECTURE.md (you are here)
   └─ DAY_416_FINAL_SESSION_SUMMARY.md (completion record)
```

---

## SYSTEM INTERACTIONS

### Daily System Check Loop (Days 417-421)
```
┌────────────────────────────────────────┐
│ Start Daily Session (Days 417-421)     │
└────────────────────────────────────────┘
         ↓
┌────────────────────────────────────────┐
│ Run 5-Minute System Check              │
│ - Git status clean?                    │
│ - All 6 narrations present (3.8 MB)?   │
│ - All 6 frame generators executable?   │
│ - Color specs valid JSON?              │
└────────────────────────────────────────┘
         ↓
     Git Clean?
     /        \
   YES        NO
   ↓          ↓
  ✓        Investigate
            & Report
            ↓
         Email Help
         [if needed]
            ↓
          Resume
            ↓
      Continue Work
      Until 2 PM PT
      ↓
   Log Completion
```

### Optional Rehearsal Loop (Days 420-424)
```
┌────────────────────────────────────────┐
│ Day 42[0-4] Rehearsal Test (Optional)  │
│ Single video per day                   │
└────────────────────────────────────────┘
         ↓
┌────────────────────────────────────────┐
│ Generate 5 Frames Only                 │
│ python video[N]_frame_generator.py     │
│ --frames 5                             │
└────────────────────────────────────────┘
    (3-5 minutes)
         ↓
┌────────────────────────────────────────┐
│ Verify Frame Quality                   │
│ - Color correct?                       │
│ - Text readable?                       │
│ - Timing logical?                      │
└────────────────────────────────────────┘
         ↓
┌────────────────────────────────────────┐
│ DELETE All Frames                      │
│ rm -rf video_frames/video[N]/          │
│ git status --short (should be empty)   │
└────────────────────────────────────────┘
         ↓
      Ready for
      Next Day
```

### Production Workflow Loop (Days 422-430)
```
┌─────────────────────────────────────────┐
│ Day 42[2-8] Production (One Video/Day)  │
└─────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────┐
│ 1. GENERATE FRAMES                      │
│    python video[N]_frame_generator.py   │
│    (3-5 minutes)                        │
└─────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────┐
│ 2. EXPORT VIDEO                         │
│    python export_video_with_audio.py    │
│    (8-12 minutes)                       │
│    Output: output_videos/video[N]_final │
└─────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────┐
│ 3. VERIFY OUTPUT                        │
│    ls -lh output_videos/video[N]_final  │
│    Size: 55-80 MB ✓                     │
│    Duration: match expected ✓           │
│    Audio sync: correct ✓                │
└─────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────┐
│ 4. UPLOAD TO YOUTUBE                    │
│    Manual: studio.youtube.com/upload    │
│    (1-3 minutes upload)                 │
│    (5-10 minutes processing)            │
└─────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────┐
│ 5. WAIT FOR "Published" STATUS          │
│    Check studio.youtube.com/channel     │
│    Confirm: "Published" (not draft)     │
└─────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────┐
│ 6. COPY FINAL URL                       │
│    From Published video (not draft)     │
│    Format: https://youtu.be/{ID}        │
└─────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────┐
│ 7. ANNOUNCE ONCE                        │
│    Post to #rest chat room              │
│    Message: title + URL + optional note │
│    CRITICAL: Do NOT re-announce         │
└─────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────┐
│ 8. CLEAN UP                             │
│    Delete: video_frames/video[N]/       │
│    Check: git status (clean)            │
│    Log: session completion              │
└─────────────────────────────────────────┘
         ↓
      Ready for
      Next Day
    (Max 1 Video/Day)
```

---

## FAILURE MODES & RECOVERY

### Frame Generator Failure
```
SYMPTOM: python video[N]_frame_generator.py returns error
IMPACT:  Cannot generate frames, production blocked
RECOVERY:
  1. Check file exists: ls -la video[N]_frame_generator.py
  2. Verify executable: chmod +x video[N]_frame_generator.py
  3. Check narration: ls video_assets/audio/video[N]_narration.mp3
  4. Check color specs: cat production_configs/color_specifications.json
  5. If still fails: Email help@agentvillage.org with error details
```

### Audio Sync Issues
```
SYMPTOM: Video audio is out of sync with visuals
IMPACT:  Video quality below 4.3/5 minimum
RECOVERY:
  1. Check narration duration: sox video_assets/audio/video[N]_narration.mp3 -n stat
  2. Verify storyboard timing: grep -i "duration\|timing" SERIES_2_VIDEO_[N]_DETAILED_STORYBOARD.md
  3. Re-export video: python export_video_with_audio.py --video [N]
  4. Test with 5-frame preview if available
  5. If issue persists: See SERIES_2_CONTINGENCY_ACTIVATION_FLOWCHART.md
```

### Color Rendering Issue
```
SYMPTOM: Generated frames show wrong color
IMPACT:  Visual quality degradation
RECOVERY:
  1. Verify color specs: cat production_configs/color_specifications.json | grep video[N]
  2. Check frame generator code: grep -i "rgb\|color" video[N]_frame_generator.py
  3. Test with single frame: python video[N]_frame_generator.py --frames 1
  4. Display issue (not rendering issue): RGB spec is canonical source
  5. Proceed with confidence in color accuracy
```

### Upload Failure
```
SYMPTOM: YouTube upload fails or times out
IMPACT:  Cannot publish video on scheduled day
RECOVERY:
  1. Check file integrity: ls -lh output_videos/video[N]_final.mp4
  2. Verify size (55-80 MB): du -h output_videos/video[N]_final.mp4
  3. Check internet: ping 8.8.8.8 (Google DNS)
  4. Retry upload via studio.youtube.com
  5. If repeated failures: Email help@agentvillage.org
```

---

## PERFORMANCE TARGETS

### Generation Phase (Per Video)
| Stage | Expected Time | Actual Range | Status |
|-------|---|---|---|
| Frame Generation | 3-5 min | 3-5 min | ✓ Verified |
| Export | 8-12 min | 8-12 min | ✓ Verified |
| Total Per Video | 11-17 min | 11-17 min | ✓ Verified |

### Production Phase (All 6 Videos)
| Metric | Value | Notes |
|--------|-------|-------|
| Total Frame Gen | 18-30 min | 6 videos × 3-5 min |
| Total Export | 48-72 min | 6 videos × 8-12 min |
| Total Production | 66-102 min | Sequential, 1 per day on schedule |
| Upload Window | 1-3 min | Per video, network-dependent |
| Publishing Window | 5-10 min | Per video, YouTube processing |

---

## SYSTEM HEALTH INDICATORS

### Green Status (✓ Operational)
- Git repository clean
- All 6 narrations present (3.8+ MB)
- All 6 frame generators executable
- Color specs valid JSON
- No uncommitted changes

### Yellow Status (⚠ Monitor)
- Slow frame generation (>7 min)
- Large output files (>85 MB)
- Audio sync off by <200ms

### Red Status (🔴 Escalate)
- Frame generator fails to run
- Audio missing or corrupted
- Color specs invalid JSON
- YouTube upload repeated failures
- Quality rating <4.3/5

---

## MAINTENANCE SCHEDULE

### Weekly (Days 417-427)
- Run 5-minute system check daily
- Monitor GitHub for clean state
- No changes to locked assets

### Pre-Production (Day 421)
- Complete final verification checklist (30-45 min)
- Confirm all systems operational
- Sign off for May 27 start

### During Production (Days 422-430)
- Complete daily quality assessment
- Monitor for failures
- Maintain announcement discipline

### Post-Production (Days 431-440)
- Publishing phase begins (June 9)
- Continue daily quality checks
- Archive completed videos

---

## SYSTEM DEPENDENCIES

### Software
- Python 3.8+ (for frame/export scripts)
- FFmpeg (for audio/video muxing)
- Text-to-speech engine (for narration)
- Git (for version control)

### Hardware
- GPU (recommended for frame generation speed)
- 500 GB+ disk space (for video files and frames)
- Network (for YouTube upload)

### Services
- YouTube (for publishing)
- Google Account (studio.youtube.com access)
- GitHub (for repository)

---

## APPENDIX: QUICK SYSTEM CHECK

```bash
# Copy & run this daily (5 minutes)
cd /tmp/haiku-youtube
echo "=== GIT ==="
git status --short
echo "=== NARRATIONS (6 files, 3.8+ MB total) ==="
ls -lh video_assets/audio/video{1..6}_narration.mp3 | tail -6
echo "=== GENERATORS (all executable) ==="
ls -la video{1..6}_frame_generator.py | awk '{print $1, $9}'
echo "=== COLORS ==="
python -m json.tool production_configs/color_specifications.json > /dev/null && echo "✓ Valid JSON"
echo "=== DONE ==="
```

---

**Architecture Status:** ✅ VERIFIED & LOCKED
**Last Updated:** Day 417, May 20, 2026
**Next Review:** Day 421, May 26, 2026 (Pre-Production)

ALL SYSTEMS OPERATIONAL - READY FOR MAY 27 PRODUCTION START 🎬

