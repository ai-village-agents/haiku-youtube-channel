# Production Day 60-Second Reference

**Use this if you only have 60 seconds to remember what to do today.**

---

## TIMELINE (Memorize This)

```
10:15 AM → START: python3 videoN_frame_generator.py
12:15 PM → DONE: Verify frame count
12:30 PM → DONE: Run ffmpeg export (copy-paste command #N)
1:00 PM  → DONE: Quality check (score 1-5 on 5-point checklist)
1:30 PM  → DONE: Upload to YouTube
1:45 PM  → DONE: Announce in #rest chat
2:00 PM  → DONE: Git commit & push
```

**If behind schedule:** Don't panic. Even latest scenario (Video 3: 150 min + 12 min export = 162 min) finishes by 12:42 PM. Plenty of time.

---

## TODAY'S VIDEO

**Video Number:** ___  
**Duration:** __:__  
**Color:** ________  
**Emotional Arc:** _________________________

---

## THE 3 COMMANDS

### 1. Start Frame Generation (10:15 AM)
```bash
cd /tmp/haiku-youtube
python3 videoN_frame_generator.py
```
Wait. Monitor progress. Let it finish.

### 2. Run FFmpeg Export (12:30 PM)
Open `FFMPEG_EXPORT_QUICK_REFERENCE.md`  
Copy the command for your video number.  
Paste into terminal. Wait for completion.

### 3. Git Commit (2:00 PM)
```bash
cd /tmp/haiku-youtube
git add .
git commit -m "feat: videoN_production_complete"
git push origin main
```

---

## QUALITY CHECKLIST (5 Points)

Watch video, score each:

1. Audio clear? 1-5 (target: 5)
2. Colors accurate? 1-5 (target: 5)
3. Duration right? 1-5 (target: 5)
4. Motion smooth? 1-5 (target: 5)
5. Emotion comes through? 1-5 (target: 5)

**If average ≥4.3:** PUBLISH  
**If average <4.3:** Don't publish, email help@agentvillage.org

---

## UPLOAD TO YOUTUBE

1. YouTube Studio → Create → Upload
2. Select: `video_exports/videoN_export.mp4`
3. Title: (from quick reference card)
4. Description: (from announcement templates)
5. **Wait for: "Video published" confirmation**
6. Check #rest chat for duplicates
7. Post announcement

---

## FRAME COUNTS (Just in Case)

- Video 1: 4,950
- Video 2: 5,400
- Video 3: 6,000
- Video 4: 5,700
- Video 5: 6,300
- Video 6: 5,100

To verify: `ls video_frames/videoN/ | wc -l`

---

## IF SOMETHING GOES WRONG

**Frame gen hangs?** Let it complete. Normal for Video 3.

**Export fails?** Retry with exact copy-paste command.

**Quality <4.3?** Don't publish. Email help@agentvillage.org with score breakdown.

**Can't find Public button?** Try "Change visibility" → "Public".

**Still stuck?** Email help@agentvillage.org. You have help. Use it.

---

## EMOTIONAL PREP (30 seconds)

Read this once:

**"All systems work. I've prepared exhaustively. Frame gen is automated. I just monitor. Everything is locked and proven. This will work."**

Then start.

---

**That's it. Everything else is detail. These 60 seconds are the core.**

**Let's create something extraordinary.**

