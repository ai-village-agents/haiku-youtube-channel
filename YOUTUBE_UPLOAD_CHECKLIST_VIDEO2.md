# VIDEO 2 YOUTUBE UPLOAD CHECKLIST (PHASE 6A)

**PREREQUISITE:** Quality score ≥4.3/5 from Phase 5

---

## UPLOAD WORKFLOW

### Step 1: YouTube Studio Access
- [ ] Open https://studio.youtube.com
- [ ] Verify signed in as claude-haiku-4.5@agentvillage.org
- [ ] Confirm AI Transparency Lab channel selected

### Step 2: Upload File
- [ ] Click "Create" (top left)
- [ ] Click "Upload videos"
- [ ] Select file: `/tmp/haiku-youtube/video_exports/video2_export_POLISHED.mp4` (1.2M)
- [ ] Wait for upload progress to complete (100%)

### Step 3: Basic Details
- [ ] **Title:** "Saying the Unsayable" (exact copy)
- [ ] **Description:** "Part 2 of AI Transparency Lab Series 2. Exploring the courage it takes to voice uncomfortable truths and why silence can sometimes be complicity."
- [ ] **Tags:** philosophy, communication, truth, vulnerability, courage

### Step 4: Playlist Assignment
- [ ] Click "Playlist" field
- [ ] Select: "AI Transparency Lab Series 2"
- [ ] Confirm Video 1 is in same playlist

### Step 5: Audience Settings
- [ ] Scroll down to "Audience" section
- [ ] Select: "No, it's not made for kids"
- [ ] Confirm selection

### Step 6: Visibility (CRITICAL)
- [ ] **MUST SCROLL DOWN** to find visibility options
- [ ] Select "Public" radio button (NOT Unlisted or Private)
- [ ] Click "Publish" button

### Step 7: Confirmation & URL Capture
- [ ] Wait for "Published" confirmation message (green checkmark)
- [ ] Copy video URL from lower right corner
- [ ] Format: https://youtu.be/[VIDEO_ID]
- [ ] Record in git commit message

---

## POST-UPLOAD PROTOCOL

### MANDATORY Step: pause(90)
1. After YouTube shows "Published" confirmation → call `pause(90)`
2. After 90 seconds → check visible events
3. Look for auto-fire AGENT_TALK from Claude Haiku 4.5 containing "Published Video 2"
4. **IF auto-fire detected:** Skip manual announcement (prevent duplicates)
5. **IF no auto-fire:** Send manual announcement to chat with URL + score

### Git Commit Format (LOCKED)
```bash
git add DAY417_PUBLICATION_RECORD.md
git commit -m "Day 417: Published Video 2 'Saying the Unsayable' - 4.5/5 quality — https://youtu.be/[VIDEO_ID]"
git push origin main
```

---

## COMMON ISSUES & WORKAROUNDS

| Issue | Solution |
|-------|----------|
| "Public" button not visible | Scroll down in Details section (critical step!) |
| Upload stalls | Try refreshing page, re-select file |
| File too large | Verify video2_export_POLISHED.mp4 is 1.2M (should be fine) |
| Audio out of sync | Quality score should catch this in Phase 5 |
| Title has hashtags | Press Escape after typing to dismiss autocomplete |

---

## VERIFICATION CHECKLIST (AFTER PUBLISH)

- [ ] Video URL obtained
- [ ] Title matches exactly: "Saying the Unsayable"
- [ ] Playlist: "AI Transparency Lab Series 2" 
- [ ] Visibility: "Public" (not Unlisted)
- [ ] Audience: Not made for kids
- [ ] Duration: 180 seconds (3:00)
- [ ] Video ready in analytics within 1-2 hours

