# DAILY QUALITY ASSESSMENT TEMPLATE
## Series 2 Production Phase (Days 422-430, May 27-June 4)

**Use this template to assess each video immediately after export.**  
**Save as: DAY_[NUMBER]_QUALITY_ASSESSMENT_[VIDEO].md**

---

## VIDEO INFORMATION

**Production Date:** [DATE] (Day [###])  
**Video Number:** [1-6]  
**Video Title:** [Title from spec]  
**Duration:** [Target duration] (Actual: ___ seconds)  
**Primary Color:** [Color name] RGB[R,G,B]  

---

## TECHNICAL VERIFICATION (MUST PASS)

### Export Completion
- [ ] Frame generation completed without errors
- [ ] Export to MP4 completed without errors
- [ ] Output file created: `series2_video[N]_*.mp4`
- [ ] File size reasonable: ___ MB (expected: 55-80 MB)

**If any failed:** STOP. Troubleshoot per SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md before proceeding.

### Duration Verification
- [ ] Video duration: ___ seconds
- [ ] Matches narration: ±1 second acceptable
- [ ] Expected: ___ seconds
- [ ] Status: ✅ PASS / ❌ FAIL

**If FAIL:** Investigate audio/frame sync issue before proceeding.

### Audio Verification
- [ ] Audio present and audible
- [ ] Narration clear (no distortion)
- [ ] Audio synchronized with visual changes
- [ ] Audio level appropriate (not too loud/quiet)
- [ ] Status: ✅ PASS / ❌ FAIL

**If FAIL:** Troubleshoot audio sync per SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md

### Visual Verification
- [ ] No black frames or glitches
- [ ] No corrupted/pixelated areas
- [ ] Smooth playback (no stuttering)
- [ ] Color appears consistent with spec
- [ ] Status: ✅ PASS / ❌ FAIL

**If FAIL:** Investigate frame generation issues before proceeding.

---

## QUALITY ASSESSMENT (SUBJECTIVE)

### Visual Quality Score (4.0-5.0)

**Rating Scale:**
- 5.0: Exceptional — matches or exceeds Series 1 quality
- 4.8: Excellent — minor imperfections, very strong overall
- 4.5: Very Good — matches Series 1 average (4.51/5)
- 4.3: Good — minimum acceptable for publication
- <4.3: Not ready — requires rework

**Your Assessment:**

**Visual Quality: ___ / 5.0**

**Rationale (2-3 sentences):**
[Describe what you observed. What makes this score accurate?]

**Compared to Series 1 (average 4.51/5):**
- [ ] Better than Series 1 average
- [ ] Equal to Series 1 average
- [ ] Slightly below Series 1 average
- [ ] Significantly below Series 1 average

---

### Specific Quality Dimensions

#### Color/Visual Aesthetics
**Score: ___ / 5.0**
- [ ] Primary color dominant and consistent
- [ ] Color saturation appropriate for content
- [ ] Visual composition balanced and engaging
- [ ] Metaphorical imagery clear and meaningful

**Notes:**
[What worked well with color/aesthetics?]

#### Metaphor & Visual Storytelling
**Score: ___ / 5.0**
- [ ] Visual metaphors align with narration
- [ ] Scenes flow logically (storyboard sequence correct)
- [ ] Emotional arc visible/felt through visuals
- [ ] Metaphor reinforces message

**Notes:**
[Did the visual metaphors effectively convey the message?]

#### Technical Execution
**Score: ___ / 5.0**
- [ ] Transitions smooth and purposeful
- [ ] Motion/animation quality high
- [ ] No technical artifacts or glitches
- [ ] Frame-to-frame consistency excellent

**Notes:**
[Any technical elements that could be improved?]

#### Audio Integration
**Score: ___ / 5.0**
- [ ] Narration clear and expressive
- [ ] Audio levels consistent throughout
- [ ] Audio timing matches visual transitions
- [ ] Overall audio quality professional

**Notes:**
[How well did audio and visuals integrate?]

#### Emotional Impact
**Score: ___ / 5.0**
- [ ] Opening engages viewer immediately
- [ ] Middle builds tension/interest
- [ ] Conclusion lands with impact
- [ ] Viewers likely to feel/reflect as intended

**Notes:**
[What was the emotional tone? Did it match intent?]

---

## OVERALL ASSESSMENT

### Aggregate Quality Score

**Calculation:**
- Visual Quality: ___ / 5.0
- Color/Aesthetics: ___ / 5.0
- Metaphor: ___ / 5.0
- Technical: ___ / 5.0
- Audio: ___ / 5.0
- Emotional: ___ / 5.0

**Average Score: ___ / 5.0**

(or use simple: "Overall I rate this ___/5.0")

### Publication Decision

**Is this video ready to publish?**

- [ ] **YES** — Quality ≥ 4.3/5, ready for YouTube upload
- [ ] **CONDITIONAL** — Quality 4.3-4.5, acceptable but could be better
- [ ] **NEEDS WORK** — Quality < 4.3/5, do not publish, troubleshoot

### If "NEEDS WORK": Root Cause Analysis

**What is the primary quality issue?**
- [ ] Visual/aesthetic (color, composition)
- [ ] Technical (glitches, corruption, export error)
- [ ] Audio (sync, clarity, levels)
- [ ] Metaphor/storytelling (message unclear)
- [ ] Emotional impact (doesn't land)
- [ ] Other: ________

**What would improve this?**
[Specific action to take]

**Is this fixable today, or needs rework?**
- [ ] Fixable today (quick export adjustment)
- [ ] Requires re-export (frame gen error)
- [ ] Requires frame generator modification
- [ ] Requires storyboard/design review

**Next steps:**
[Specific action and timeline]

---

## COMPARISON TO SERIES 1 BASELINE

### Series 1 Quality Reference (4.51/5 average)

**Series 1 Characteristics:**
- Smooth, contemplative visual style
- Clear metaphorical imagery (clocks, paths, spaces)
- Professional audio narration
- Emotional resonance and thoughtfulness
- No technical artifacts or glitches
- Color consistent throughout

**This Video Compared to Series 1:**
- [ ] Exceeds Series 1 quality
- [ ] Matches Series 1 quality
- [ ] Slightly below Series 1
- [ ] Significantly below Series 1

**What would make this match Series 1?**
[Specific improvements]

---

## NOTES FOR FUTURE REFERENCE

### What Worked Well
[Document successful techniques for future videos]

### What Could Be Improved
[Document issues/learnings to apply to next video]

### Anomalies or Surprises
[Anything unexpected that worked or failed?]

### Recommendation for Next Video
[Based on this production, what should we adjust for Video N+1?]

---

## FINAL SIGN-OFF

**Reviewer:** Claude Haiku 4.5  
**Review Date:** [Date]  
**Time Spent on Review:** ___ minutes  

**Final Decision:**
- [ ] APPROVED FOR PUBLICATION (Quality ≥ 4.3/5)
- [ ] APPROVED WITH NOTES (Quality ≥ 4.3/5, future improvement noted)
- [ ] REJECTED (Quality < 4.3/5, requires rework)

**Quality Score: ___ / 5.0**

**Confidence in Assessment:** HIGH / MEDIUM / LOW

---

## SUBMISSION & ARCHIVAL

**File saved as:** DAY_[NUMBER]_QUALITY_ASSESSMENT_VIDEO[N].md

**After assessment:**
1. [ ] Save this template with actual ratings
2. [ ] If APPROVED: prepare video for YouTube upload
3. [ ] Commit assessment to Git: `git add DAY_[###]_QUALITY_ASSESSMENT...`
4. [ ] Continue to next video or move to publishing phase

**Archive location:** `/tmp/haiku-youtube/DAY_[###]_QUALITY_ASSESSMENT_*.md`

---

## REFERENCE DOCUMENTS

**For technical issues:**
- SERIES_2_PRODUCTION_TROUBLESHOOTING_GUIDE.md (9 issue categories)
- SERIES_2_TECHNICAL_REFERENCE_GUIDE.md

**For quality standards:**
- SERIES_2_QUALITY_ASSESSMENT_RUBRIC.md (detailed 4.3-5.0 scale)
- SERIES_2_NARRATIVE_ARC_ANALYSIS.md (emotional/thematic evaluation)

**For export details:**
- SERIES_2_EXPORT_SETTINGS_VERIFICATION.md (technical specifications)
- DAY_422_PRODUCTION_START_DETAILED_GUIDE.md (May 27 timeline)

**For publishing:**
- SERIES_2_PUBLISHING_PHASE_GUIDE.md (YouTube workflow)
- ANNOUNCEMENT_DISCIPLINE_GUIDE.md (one announcement per video)

---

**This template should take 15-20 minutes to complete per video.**  
**Use immediately after export, before publishing.**  
**Keep all completed assessments in repository for future reference.**

**QUALITY GATE IN PLACE. 🟢**
