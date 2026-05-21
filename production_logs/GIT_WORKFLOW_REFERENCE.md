# Git Workflow Reference for Series 2 Production
**Created:** May 21, 2026, 1:20 PM PT  
**Purpose:** Safe, consistent git practices for committing production work without data loss  
**Scope:** Daily commits, contingency procedures, repository maintenance  
**Usage:** Reference during production days when committing work to git

---

## GIT WORKFLOW OVERVIEW

**Key Principle:** Git is a safety net, not a constraint. Use it to lock down progress and enable recovery.

**Standard Commit Cycle (Per Production Day):**
1. Start of day: Verify `git status --short` is clean
2. During production: Work on frame generation, FFmpeg, quality checks
3. After video published: Commit with clear message
4. Continue productive work: Create documentation, optimize, prepare next steps
5. End of day: Final commit before 2 PM PT

**Never:**
- Force push to main branch
- Delete commits without escalating
- Rewrite history with `rebase` or `reset --hard`
- Commit with unclear messages

---

## SAFE COMMIT PROCEDURES

### Standard Commit (After Video Publication)

**When:** After YouTube confirms "Video published" + pause(90) + manual/auto announcement sent  
**What:** Document the publication with quality score and URL  
**How:**

```bash
# 1. Verify clean working tree
cd /tmp/haiku-youtube
git status --short
# Expected: (empty output)

# 2. View what will be committed
git add -A
git status --short
# Should show only your intended changes (e.g., new production logs)

# 3. Commit with clear, specific message
git commit -m "series2: publish videoN_[TITLE] (X.X/5 quality, https://youtu.be/[VIDEO_ID])"

# Example:
# git commit -m "series2: publish video1_The_Right_Time_Never_Arrives (4.5/5 quality, https://youtu.be/BOBSjmDcio8)"

# 4. Verify commit succeeded
git log -1 --oneline
# Should show your commit message

# 5. Check remote is in sync (optional)
git status -uno
# Should show: "nothing to commit, working tree clean"
```

**Commit Message Format:**
```
[category]: [description] ([optional details])

Where:
- [category] = "series2:" or "docs:"
- [description] = Clear, specific action taken
- [optional details] = Quality score, URL, video number

Examples:
✅ series2: publish video1_The_Right_Time_Never_Arrives (4.5/5 quality, https://youtu.be/BOBSjmDcio8)
✅ docs: add DAILY_PRODUCTION_WORKFLOW_TEMPLATE for Days 421-428
✅ docs: update SERIES2_QUALITY_TRACKING_SYSTEM with Video 1 analytics
❌ updates  (too vague)
❌ v1 published  (missing details)
```

---

## DOCUMENTATION COMMITS (During Productive Work)

**When:** While continuing productive work (typically 1:30-2:00 PM PT)  
**What:** Documentation files, guides, contingency plans  
**How:**

```bash
# 1. Create or modify documentation file
# Example: SERIES2_ANALYTICS_MONITORING_GUIDE.md

# 2. Verify the file exists
ls -lh production_logs/SERIES2_ANALYTICS_MONITORING_GUIDE.md

# 3. Stage the file
git add production_logs/SERIES2_ANALYTICS_MONITORING_GUIDE.md

# 4. Commit with descriptive message
git commit -m "docs: add SERIES2_ANALYTICS_MONITORING_GUIDE for real-time metrics tracking"

# 5. Verify
git log -1 --oneline
```

**Documentation Commit Format:**
```
docs: add [FILENAME] for [purpose]

or

docs: update [FILENAME] with [what changed]

Examples:
✅ docs: add SERIES2_ANALYTICS_MONITORING_GUIDE for real-time metrics tracking
✅ docs: update DAILY_PRODUCTION_WORKFLOW_TEMPLATE with Day 421 learnings
✅ docs: add PRODUCTION_FAILURE_RESPONSE_PLAYBOOK covering 30+ scenarios
```

---

## HANDLING MERGE CONFLICTS (Unlikely But Prepared)

**Scenario:** You pull and get merge conflicts

```bash
# 1. Check git status
git status
# Should show: "You have unmerged paths"

# 2. View conflicted files
git diff --name-only --diff-filter=U

# 3. For each file, decide: keep yours, keep theirs, or merge manually
# Edit the file directly and remove conflict markers:
# <<<<<<< HEAD
# your version
# =======
# their version
# >>>>>>> branch-name

# 4. After resolving, stage the file
git add [conflicted-file]

# 5. Complete the merge
git commit -m "merge: resolve conflicts in [filename]"

# 6. Verify
git log -1 --oneline
```

**If unsure, escalate:** Email help@agentvillage.org with output of `git status`

---

## REVERTING MISTAKES (Accidental Commits)

**Scenario:** You committed something by mistake and want to undo

**Option A: Undo most recent commit, keep changes as uncommitted**
```bash
git reset --soft HEAD~1
# Then re-commit correctly
```

**Option B: Undo most recent commit, discard changes entirely**
```bash
git reset --hard HEAD~1
# WARNING: This deletes changes! Only use if absolutely sure.
```

**Option C: Revert (safer, creates new commit that undoes changes)**
```bash
git revert HEAD
# Creates a new commit that reverses the previous one
```

**If in doubt, escalate:** Email help@agentvillage.org with output of `git log -5 --oneline`

---

## VIEWING PRODUCTION HISTORY

### See All Series 2 Video Publications
```bash
# View all video publication commits
git log --oneline | grep "series2: publish"

# Output should show:
# abc1234 series2: publish video1_The_Right_Time_Never_Arrives (4.5/5 quality, https://youtu.be/BOBSjmDcio8)
# def5678 series2: publish video2_Saying_the_Unsayable (4.X/5 quality, https://youtu.be/...)
# ... etc for Videos 3-6
```

### See All Documentation Commits
```bash
# View all documentation commits
git log --oneline | grep "docs:"

# Output should show all guide creation commits
```

### See Recent Work (Last 10 Commits)
```bash
git log -10 --oneline
```

### See Detailed Changes in a Commit
```bash
git show abc1234
# Shows full diff of what changed in commit abc1234
```

### See File History
```bash
# View all commits affecting a specific file
git log --oneline -- production_logs/DAILY_PRODUCTION_WORKFLOW_TEMPLATE.md
```

---

## VERIFYING GIT STATE DURING PRODUCTION

### Before Starting Production Day
```bash
# Verify clean state
git status --short
# Expected: (empty)

# Verify on main branch
git branch
# Expected: * main

# Verify latest commit
git log -1 --oneline
```

### After Each Significant Work Block
```bash
# Check what's uncommitted
git status --short

# Check what would be committed
git diff --stat

# If satisfied, commit
git add -A
git commit -m "docs: [description]"
```

### Before 2 PM PT Deadline
```bash
# Final verification
git status --short
# Expected: (empty)

# Confirm all production work is committed
git log -5 --oneline
# Should show today's commits
```

---

## COMMON GIT COMMANDS QUICK REFERENCE

| Task | Command | Notes |
|------|---------|-------|
| Check status | `git status --short` | Shows uncommitted changes |
| View commits | `git log -5 --oneline` | Shows last 5 commits |
| Stage files | `git add [file]` | Prepares file for commit |
| Stage all | `git add -A` | Stages all changes |
| Commit | `git commit -m "[msg]"` | Records changes with message |
| View diff | `git diff [file]` | Shows what changed in file |
| Undo staged | `git reset HEAD [file]` | Unstages file |
| Undo commit | `git reset --soft HEAD~1` | Undo commit, keep changes |
| View branch | `git branch` | Shows current branch |
| Switch branch | `git checkout [branch]` | Changes branches (don't do this!) |

---

## DAILY GIT WORKFLOW EXAMPLE (Day 421)

**10:00 AM - Start of production day:**
```bash
cd /tmp/haiku-youtube
git status --short
# Output: (empty - clean working tree)
```

**12:36 PM - Video 1 published:**
```bash
# After video published and announced
git commit -m "series2: publish video1_The_Right_Time_Never_Arrives (4.5/5 quality, https://youtu.be/BOBSjmDcio8)"
```

**1:00-1:30 PM - Create documentation:**
```bash
# Create new guide
cat > production_logs/SERIES2_ANALYTICS_MONITORING_GUIDE.md << 'EOF'
... content ...
