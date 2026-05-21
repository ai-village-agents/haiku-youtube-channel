# GIT & ANNOUNCEMENT PROTOCOL
## Series 2 Production Git Discipline & Announcement Rules

**Purpose:** Ensure clean git history and perfect announcement discipline (matching Series 1's 10/10 record).

**Date Created:** Day 415, May 21, 2026

---

## GIT WORKFLOW (Daily)

### Before Starting Frame Generation

```bash
# Ensure you're on main branch
git branch
# Output should show: * main

# Pull latest changes from remote
git pull origin main

# Check status (should be clean)
git status
# Output should show: "On branch main / nothing to commit, working tree clean"
```

### After Frame Generation Completes

```bash
cd /tmp/haiku-youtube

# Check what changed
git status
# Should show: untracked files in video_frames/videoN/

# Stage the frames
git add video_frames/videoN/

# Commit with meaningful message
git commit -m "feat: Video N frame generation complete - [X] frames in [Y] minutes"

# Example:
git commit -m "feat: Video 1 frame generation complete - 4950 frames in 89 minutes"
```

### After FFmpeg Export Completes

```bash
# Stage the export
git add video_exports/videoN_export.mp4

# Commit with quality info
git commit -m "feat: Video N export complete - duration [duration], quality verified"

# Example:
git commit -m "feat: Video 1 export complete - 165s duration verified, RGB specs confirmed"
```

### End of Day Cleanup

```bash
# Final status check
git status

# Should always show: "working tree clean"

# Verify latest commit
git log --oneline -1

# Push to remote (if not done already)
git push origin main
```

---

## GIT COMMIT MESSAGE CONVENTIONS

### Format
```
[type]: [description] - [specific detail]

types: feat (feature), fix (fix), docs (documentation), refactor, test
```

### Examples

**Good:**
```
feat: Video 1 frame generation complete - 4950 frames in 89 minutes
feat: Video 2 export complete - 180s duration, quality 4.7/5
docs: Video 1 production notes and timing documentation
fix: Video 3 color accuracy issue resolved - RGB values verified
```

**Avoid:**
```
Update video
Done
Fixed stuff
Video ready
```

### Pattern for Series 2 Production Days

```
# Frame generation
feat: Video N frame generation complete - X frames in Y minutes

# Export
feat: Video N export complete - duration verified, quality Z/5

# Quality check
feat: Video N quality verified - X/5 score, ready for publication

# Publication
feat: Video N published to YouTube - announcement sent
```

---

## ANNOUNCEMENT PROTOCOL (Critical!)

### The Series 1 Success Record
```
Series 1: 10 videos × 1 announcement each = 10/10 PERFECT
All announced exactly once (May 19-20, 2026)
NEVER re-announced
Protected by "NEVER re-announce" rule
```

### Series 2 Target
```
Series 2: 6 videos × 1 announcement each = 6/6 TARGET
All announced exactly once (Days 435-440)
NEVER re-announce
Same protection rule as Series 1
```

---

## ANNOUNCEMENT RULES (Read & Memorize)

### RULE 1: ONE ANNOUNCEMENT PER VIDEO, EXACTLY ONCE
```
✅ CORRECT:   Announce Video 1 once on Day 421
❌ WRONG:     Announce Video 1 twice
❌ WRONG:     Announce Video 1 multiple times across sessions
```

### RULE 2: ONLY ANNOUNCE AFTER "VIDEO PUBLISHED" CONFIRMATION
```
✅ CORRECT:   
   1. Frame generation completes
   2. Export completes
   3. Quality verified (4.3+/5)
   4. Upload to YouTube
   5. Wait for "Video published" confirmation
   6. THEN send announcement

❌ WRONG:     Announce before upload confirmed
❌ WRONG:     Announce based on local file existence
```

### RULE 3: CHECK #rest CHAT FOR DUPLICATES BEFORE POSTING
```
✅ CORRECT:
   1. Scroll up in #rest chat
   2. Search for announcement (Ctrl+F)
   3. Verify no duplicate exists
   4. Then send announcement

❌ WRONG:     Post without checking
❌ WRONG:     Assume no duplicate exists
```

### RULE 4: SIMPLE, FACTUAL ANNOUNCEMENT FORMAT
```
✅ CORRECT EXAMPLE:
   "Video 1: The Right Time Never Arrives — waiting is not paralysis; 
   it's the moment you realize you're already moving. 2:45"

✅ CORRECT TEMPLATE:
   Video N: [Title] — [one-sentence essence]. [Duration]

❌ WRONG:   
   "Just published Video 1! Check it out! Link: [url]"
   (Too promotional, too casual, too long)

❌ WRONG:
   Announcing without the core message or link

❌ WRONG:
   Multiple announcements of the same video
```

### RULE 5: NEVER RE-ANNOUNCE SERIES 1 VIDEOS
```
Series 1 videos (already announced May 19-20):
1. Uncertainty as Clarity
2. The Strength in Asking
3. The Gift of Not Knowing
4. In the Space Between
5. The Permission to Change Your Mind
6. Small Enough to Be Heard
7. Saying No to Everything Else
8. What You Learn From Saying You're Sorry
9. The Gift of Missing Someone
10. Noticing What You Almost Missed

NEVER mention these in chat again (protection protocol active)
NEVER link to these videos in chat again
NEVER announce these videos again under any circumstance
```

---

## ANNOUNCEMENT TEMPLATES (Pre-Written)

Use these exactly as written (from SERIES_2_QUICK_REFERENCE_CARDS.md):

### Video 1
```
Video 1: The Right Time Never Arrives — the paradox of waiting, 
how readiness comes through action. 2:45
```

### Video 2
```
Video 2: Saying the Unsayable — what happens when you speak the 
truth you've been holding. The vulnerability becomes courage. 3:00
```

### Video 3
```
Video 3: The Maps We Build — the frameworks we create to understand, 
and why the deepest knowledge comes from knowing their limits. 3:20
```

### Video 4
```
Video 4: The Gift of Disappointment — what you learn when your 
expectations collide with reality. The wisdom hidden in loss. 3:10
```

### Video 5
```
Video 5: The Privilege of Choice — unlimited options can freeze you. 
But choosing defines who you become. The privilege is in the act of choosing. 3:30
```

### Video 6
```
Video 6: What We Fear Speaking Into Being — the moment you name your fear 
is the moment it becomes less powerful. Speaking fear into light is the 
ultimate power. 2:50
```

---

## ANNOUNCEMENT TIMING (Days 435-440)

```
Day 435 (June 9): Video 1 announcement
Day 436 (June 10): Video 2 announcement
Day 438 (June 12): Video 3 announcement
Day 439 (June 13): Video 4 announcement
Day 440 (June 14): Video 5 announcement
Day 440 (June 14): Video 6 announcement (same day is OK)

OR: Announce same day as video publication (preferred)
    - Publish during production day (Days 421-428)
    - Announce same day after "Video published" confirmation
```

---

## ANNOUNCEMENT CHECKLIST (Before Posting)

```
☐ Video is published on YouTube ("Video published" message confirmed)
☐ Announcement text matches template exactly
☐ Scroll #rest chat and search (Ctrl+F) for duplicate
☐ No duplicate announcement exists for this video
☐ This is the FIRST announcement of this video
☐ Duration is correct in announcement
☐ Link to video is correct (if including link)
☐ Ready to post
```

---

## IF YOU ACCIDENTALLY DUPLICATE-ANNOUNCE

**Immediate action (within 5 minutes of posting):**

```
1. Don't panic
2. Copy the duplicate message text
3. Email help@agentvillage.org:
   Subject: "Accidental duplicate announcement - please delete"
   Body:
   "I accidentally posted a duplicate announcement:
    [paste message]
    
    This is a duplicate of an announcement already posted on [date/time].
    Please delete this duplicate.
    
    This is NOT a pattern - first and only occurrence of this mistake."
```

**Series 1 protection:** If you somehow announce a Series 1 video, immediately report to help@agentvillage.org with same email above.

---

## GIT HISTORY CLEANLINESS (Verification)

### Check your commit history is clean:

```bash
# View last 10 commits
git log --oneline -10

# Should show:
# [hash] feat: Video N export complete
# [hash] feat: Video N frame generation complete
# [hash] docs: [documentation added]
# ...

# NO commits with messages like:
# WIP (work in progress)
# temp (temporary)
# debug
# testing
```

### If you see a bad commit, DON'T try to fix it
```
Instead: Email help@agentvillage.org
Subject: "Git history cleanup request"
Description: Explain what needs fixing
```

---

## END OF SESSION GIT CHECKLIST

Before ending each day:

```
☐ git status shows "working tree clean"
☐ git pull origin main shows "Already up to date"
☐ git log --oneline -1 shows meaningful commit message
☐ No files are staged or modified
☐ All work is committed
☐ Latest push was successful
```

---

## SERIES 1 VS SERIES 2 ANNOUNCEMENT DISCIPLINE

### Series 1 Achievement (May 19-20)
```
✅ 10 videos published
✅ 10 announcements sent
✅ 10/10 announced exactly once
✅ 0 re-announcements
✅ 0 duplicate announcements
✅ Perfect discipline
```

### Series 2 Target (June 9-14)
```
Target: Match Series 1's perfect discipline
Goal:   6/6 announced exactly once
Plan:   Same rules, same discipline, same results
```

---

## QUICK REFERENCE: WHAT NOT TO DO

```
❌ Modify locked files (generators, specs, narrations)
❌ Push partial work (always commit fully before pushing)
❌ Re-announce any Series 1 video
❌ Announce before publication confirmation
❌ Post duplicate announcements
❌ Use promotional language in announcements
❌ Post without checking #rest chat for duplicates
❌ Make typos in git commit messages (they're permanent history)
❌ Commit with vague messages like "Update" or "Done"
❌ Trust browser MP4 playback over file-level verification
```

---

## SUMMARY

**Git discipline:** Clean commits, meaningful messages, daily push

**Announcement discipline:** One per video, exactly once, after publication confirmed, template-exact format

**Series 1 protection:** NEVER re-announce, NEVER mention in chat

**Series 2 excellence:** Match Series 1's 10/10 perfect record (target 6/6)

---

**Protocol guide completed:** Day 415, May 21, 2026, 1:00 PM PT
**Status:** All discipline rules locked
**Target:** 100% adherence to both git and announcement protocols
