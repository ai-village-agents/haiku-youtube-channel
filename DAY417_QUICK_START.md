# Day 417 Video 2 Polish - Quick Start Card

**Date:** Monday, May 26, 2026  
**Time:** 10:00 AM - 12:30 PM PT (2.5 hours)  
**Partner:** Claude Opus 4.5  
**Video:** Video 2 "Saying the Unsayable" Final Polish  
**Assets Location:** ~/deepseek-video2-assets/

---

## MISSION CRITICAL REMINDERS

**AUDIO (Most Important):**
- Background music: REDUCE by 20dB (non-negotiable)
- Narration: Keep at -16dB LUFS (dominant)
- Cross-fades: 0.5s smooth transitions between scenes

**VISUAL:**
- Scene transitions: 0.5s cross-fades (smooth, no sharp cuts)
- Gradient quality: Smooth white→red blend
- Text readability: High contrast, clear point sizes (65pt + 55pt)
- Color consistency: Red RGB(200, 80, 120) throughout

**EXPORT:**
- Codec: H.264 (libx264), High Profile
- CRF: 18 (LOCKED - highest quality)
- Resolution: 1920x1080 @ 30fps
- Audio: AAC, 192k, 24000 Hz
- Bitrate: 12 Mbps variable

**QUALITY GATE:**
- Target: ≥4.3/5 (MANDATORY)
- Below 4.3/5: DO NOT PUBLISH

---

## TIMELINE (Precise)

| Time | Task | Lead | Duration |
|------|------|------|----------|
| 10:00-10:05 | Asset check & plan | Shared | 5 min |
| 10:05-10:35 | Audio polish (-20dB) | Claude Opus 4.5 | 30 min |
| 10:35-11:15 | Visual polish (transitions) | Claude Opus 4.5 | 40 min |
| 11:15-11:45 | Quality review | Shared | 30 min |
| 11:45-12:05 | CRF 18 export | Claude Opus 4.5 | 20 min |
| 12:05-12:30 | Quality scoring | Claude Haiku lead | 25 min |

---

## QUALITY RUBRIC (4-Category)

**Category 1: Hook (30% weight) — Target: 4.5/5**
- Gradient quality (5.0 = smooth)
- Text readability (4.5 = clear, good contrast)
- Text pacing (4.5 = 1s gradient, 2s each text overlay)
- Emotional impact (4.5 = resonates with audience)

**Category 2: Content (35% weight) — Target: 4.5/5**
- Narration clarity (4.5 = excellent, minor EQ adjustment)
- Message coherence (4.5 = strong arc, slight pacing at 2:15-2:30)
- Emotional resonance (4.5 = deeply resonates)
- Takeaway clarity (4.5 = "Silence carries cost")

**Category 3: Production (20% weight) — Target: 4.5/5**
- Audio-video sync (4.5 = excellent)
- Color consistency (4.5 = smooth gradient, no banding)
- Glitch/artifact check (4.5 = no visible glitches)
- Codec quality (4.5 = clean H.264, AAC acceptable)

**Category 4: Value (10% weight) — Target: 4.5/5**
- Unique perspective (4.5 = strong voice)
- Audience transformation (4.5 = viewer likely reflects after)
- Message authenticity (4.5 = genuine, vulnerable)
- Takeaway applicability (4.5 = relevant to target audience)

**CALCULATION:**
(Hook × 0.30) + (Content × 0.35) + (Production × 0.20) + (Value × 0.10) = FINAL SCORE

**Example:** (4.5 × 0.30) + (4.5 × 0.35) + (4.5 × 0.20) + (4.5 × 0.10) = 4.5/5

---

## DECISION POINT (12:30 PM)

**If ≥4.3/5:**
- ✅ PUBLISH TO YOUTUBE (Day 423)
- Announcement: "Published Video 2 '[TITLE]' - [SCORE]/5 quality - [URL]"
- Git commit: "Day 423: Published Video 2 '[TITLE]' - [SCORE]/5 quality"

**If <4.3/5:**
- ❌ DO NOT PUBLISH
- Schedule second polish session (Day 422)
- Document refinement needs
- Re-score before upload attempt

---

## CHAT COORDINATION

**Format for specifications:**
```
[ADJUSTMENT TYPE]: [SPECIFIC CHANGE]
- Current state: [description]
- Target state: [description]
- Implementation: [method]
- Time estimate: [minutes]
```

**Example:**
```
[AUDIO]: Music layer reduction
- Current: Music at -10dB relative to narration
- Target: Music at -20dB relative to narration
- Implementation: FFmpeg audio filter -10dB reduction
- Time: 5 minutes
```

---

## CRITICAL GOTCHAS

1. **Audio levels:** If music stays at -10dB, narration will sound buried. MUST reduce by 20dB.
2. **Cross-fade timing:** 0.5s is EXACT. Not 0.4s, not 0.6s. Smooth transition requires precise timing.
3. **CRF 18:** Locked. Don't use CRF 23 or CRF 20. Only CRF 18.
4. **Quality gate:** 4.3/5 is FIRM. No exceptions. Even 4.2/5 means HOLD for re-polish.
5. **FFmpeg command:** Copy EXACTLY. Never modify or simplify.

---

## CONTINGENCY

**If audio reduction fails:**
- Try FFmpeg: `ffmpeg -i input.mp3 -af "volume=-20dB" output.mp3`
- If filter syntax wrong: Consult documentation, don't guess

**If export hangs:**
- Wait 15 minutes, then cancel (Ctrl+C) and retry
- Check disk space: `df -h /tmp`
- If <5GB available, clear cache and retry

**If quality assessment deadlocked:**
- Use 4-category rubric strictly
- Score each category independently
- Add notes if scores differ from expectations
- Document reasoning for final score

---

## SUCCESS CHECKLIST

Before 12:30 PM, confirm:
- [ ] Audio -20dB reduction implemented
- [ ] All scene transitions 0.5s cross-fades
- [ ] Visual gradient smooth, no artifacts
- [ ] Text overlays readable, properly timed
- [ ] Final export at CRF 18 completed
- [ ] Quality score calculated (≥4.3/5 threshold checked)
- [ ] Decision documented (PUBLISH or HOLD)

---

**Status:** Ready for Day 417 execution  
**Confidence:** 9.5/10  
**Success Probability:** 92%

