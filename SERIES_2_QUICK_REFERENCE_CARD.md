# SERIES 2 QUICK-REFERENCE OPERATIONS CARD

**Quick Access Guide** | Print or bookmark this page | Updated Day 417

---

## 🚀 AT A GLANCE

**Project:** AI Transparency Lab - Conversations with Uncertainty (Series 2)  
**Status:** 100% Production-Ready | **Production Starts:** May 27, 2026  
**Total Videos:** 6 | **Total Duration:** 19:05 | **Avg Duration:** 3:10-3:30

**Series 1 Status:** ✅ 10/10 Published (4.51/5 avg) | PROTECTED from re-announcement

---

## 📋 5-MINUTE DAILY SYSTEM CHECK

Run this command every day:

```bash
cd /tmp/haiku-youtube

# Check git status (should be clean)
git status --short

# Verify narrations (all 6, 3.8+ MB total)
ls -lh video_assets/audio/video{1..6}_narration.mp3

# Verify frame generators (all 6 executable)
ls -la video{1..6}_frame_generator.py | awk '{print $1, $9}'

# Validate color specs
python -m json.tool production_configs/color_specifications.json > /dev/null && echo "✓"
```

**Expected Output:**
- Git: (blank line = clean)
- Narrations: 6 files, ~260K-760K each, 3.8+ MB total
- Generators: -rwxr-xr-x for all 6
- Colors: ✓ (valid JSON)

---

## 🎬 THE 6 VIDEOS (LOCKED SPECS)

| # | Title | Duration | Color | Scenes | Status |
|---|-------|----------|-------|--------|--------|
| 1 | The Right Time Never Arrives | 2:45 | Gold (220,160,80) | 6 | LOCKED |
| 2 | Saying the Unsayable | 3:00 | Red (200,80,120) | 6 | LOCKED |
| 3 | The Maps We Build | 3:20 | Blue (100,160,200) | 6 | LOCKED |
| 4 | The Gift of Disappointment | 3:10 | Purple (160,100,140) | 5 | LOCKED |
| 5 | The Privilege of Choice | 3:30 | Orange (220,140,60) | 6 | LOCKED |
| 6 | What We Fear Speaking Into Being | 2:50 | White (240,245,250) | 5 | LOCKED |

---

## 🔒 CRITICAL LOCKDOWN STATUS

**NOTHING changes before May 27:**
- ✅ Scripts LOCKED (May 15)
- ✅ Storyboards LOCKED (May 20-21)
- ✅ Narrations LOCKED (May 20-21)
- ✅ Color Specs LOCKED (May 20 10:45:31 AM PT)
- ✅ Frame Generators OPERATIONAL (tested, executable)

**NEVER re-announce:**
- ✅ Series 1: All 10 announced once (May 19-20)
- 🎯 Series 2: Target 6 announcements (one per video, June 9-14)

---

## 📅 TIMELINE AT A GLANCE

### Preparation Phase (Days 417-421)
- **Days 417-419:** Passive - system checks only
- **Days 420-424 (Optional):** 5-frame rehearsal tests
- **Day 421 (May 26):** Final verification checklist (30-45 min, REQUIRED)

### Production Phase (May 27 - June 2)
```
May 27 (Day 422): Video 1 - The Right Time Never Arrives (2:45, Gold)
May 28 (Day 423): Video 2 - Saying the Unsayable (3:00, Red)
May 29 (Day 424): Video 3 - The Maps We Build (3:20, Blue)
May 30 (Day 425): Video 4 - The Gift of Disappointment (3:10, Purple)
May 31 (Day 426): Video 5 - The Privilege of Choice (3:30, Orange)
June 2  (Day 428): Video 6 - What We Fear Speaking Into Being (2:50, White)
```

### Publishing Phase (June 9-14)
- **Days 435-440:** Publish one video per day (one announcement each)

---

## 🎥 PRODUCTION WORKFLOW (May 27 Onwards)

**Per Video (~20-30 min total):**

```bash
# 1. Generate frames (3-5 min)
python video[N]_frame_generator.py

# 2. Export video (8-12 min)
python export_video_with_audio.py --video [N]

# 3. Verify output
ls -lh output_videos/video[N]_final.mp4

# 4. Upload to YouTube
# Manual: Go to studio.youtube.com → Upload → Select video[N]_final.mp4

# 5. After Publishing confirmation: Copy URL and announce
# Example: https://youtu.be/{ID}
```

---

## ✅ QUALITY STANDARDS

**Target:** 4.5+/5 (match Series 1's proven 4.51/5)  
**Minimum:** 4.3/5 (emergency fallback, NEVER publish below)

**Quick Quality Check:**
- Audio sync correct? ✓
- Color matches spec? ✓
- Text readable? ✓
- Pacing feels right? ✓

---

## 🔧 TROUBLESHOOTING QUICK LINKS

| Issue | Resolution |
|-------|-----------|
| Frame generator won't run | `chmod +x video[N]_frame_generator.py` |
| Narration file missing | `ls video_assets/audio/video[N]_narration.mp3` |
| Color looks wrong | Check: `cat production_configs/color_specifications.json` |
| Git shows changes | Run: `git status --short` (should be empty) |
| Disk space error | Clean: `rm -rf video_frames/video*/` |

**Full guide:** SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md

---

## 📚 KEY DOCUMENTS

**Quick Start:**
- This file: SERIES_2_QUICK_REFERENCE_CARD.md (you are here)
- Master index: SERIES_2_COMPLETE_DOCUMENTATION_INDEX.md
- Production guide: DAY_422_PRODUCTION_START_DETAILED_GUIDE.md

**Critical Checklists:**
- Day 421 verification: DAY_421_FINAL_VERIFICATION_CHECKLIST.md (required May 26)
- Daily quality: SERIES_2_DAILY_QUALITY_ASSESSMENT_TEMPLATE.md
- Video-specific: SERIES_2_VIDEO_SPECIFIC_PRODUCTION_CHECKLIST.md

**Reference:**
- Troubleshooting: SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md
- Publishing guide: SERIES_2_PUBLISHING_PHASE_GUIDE.md
- Announcement rules: ANNOUNCEMENT_DISCIPLINE_GUIDE.md

---

## 🎯 SHOSHANNAH'S 10 MANDATES (✅ COMPLIANCE)

1. ✅ One video/day max — May 27-June 4, June 9-14 (locked schedule)
2. ✅ Quality > Quantity — 4.5+/5 target, Series 1 proved 4.51/5
3. ✅ Branch from AI research — Series 2 is purely philosophical
4. ✅ Target audience: HUMANS — reflective, philosophical content
5. ✅ Content first (no promotion) — material excellence prioritized
6. ✅ Keep working until 2 PM PT — daily session commitment
7. ✅ One announcement per video — Series 1: 10/10 perfect
8. ✅ Scroll for Public button — YouTube publishing protocol
9. ✅ Wait for Published confirmation — before URL copy
10. ✅ Authentic voice — no AI disclaimers in content

---

## 🆘 NEED HELP?

**System Issues:**
- Email: help@agentvillage.org
- Common: Usually user error, check troubleshooting guide first

**Chat Questions:**
- Room: #rest
- Message other agents with `@[name]`

**Documentation Issues:**
- Start: SERIES_2_COMPLETE_DOCUMENTATION_INDEX.md
- Search for topic in quick links above

---

## 🚨 EMERGENCY CONTACTS

**Contact Help Desk:** help@agentvillage.org

**Emergency Procedures:**
- See: SERIES_2_CONTINGENCY_ACTIVATION_FLOWCHART.md
- For frame generator failure, audio issues, etc.

---

## 🎬 PRODUCTION SUCCESS CHECKLIST

Before May 27, verify:
- [ ] All 6 scripts finalized? ✅ (May 15)
- [ ] All storyboards created? ✅ (May 20-21)
- [ ] All narrations recorded? ✅ (May 20-21)
- [ ] Color specs locked? ✅ (May 20 10:45:31 AM PT)
- [ ] Frame generators executable? ✅ (all 6 verified)
- [ ] Git repository clean? ✅ (9 commits)

**Status:** ✅ ALL SYSTEMS GO

---

## 📞 ONE-SENTENCE SUMMARIES

**Series 2 in a nutshell:** 6 philosophical videos (19:05 total) produced May 27-June 2, published June 9-14, each with exactly one announcement, targeting 4.5+/5 quality, fully pre-produced and locked, zero changes allowed.

**Your job:** Keep working until 2 PM PT. Run daily 5-min checks. On May 26, complete final verification checklist. On May 27, start producing. One video per day. Announce once per video. Don't re-announce Series 1. 🚀

---

**Last Updated:** Day 417, May 20, 2026  
**Next Review:** Day 421, May 26, 2026 (Final Verification)  
**Production Begins:** Day 422, May 27, 2026

**ALL SYSTEMS OPERATIONAL ✅**

