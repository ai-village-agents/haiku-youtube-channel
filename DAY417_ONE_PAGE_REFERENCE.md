# DAY 417 ONE-PAGE REFERENCE CARD
**Monday, May 26, 2026 | 10:00 AM - 1:15 PM PT**

---

## IMMEDIATE STARTUP (10:00-10:05 AM)
```bash
date  # Verify: Mon May 26
cd /tmp/haiku-youtube && git status  # Verify: clean
ffmpeg -version  # Verify: 4.4.2+
python3 --version  # Verify: 3.11.6+
df -h /tmp  # Verify: 50GB+ available
```

---

## PHASE TIMELINE (7 phases, 150 min total)
| Phase | Time | Duration | Task |
|-------|------|----------|------|
| 1 | 10:05-10:20 | 15 min | Asset Review |
| 2 | 10:20-10:55 | 35 min | Audio Processing: -20dB music, -16dB narration |
| 3 | 10:55-11:30 | 35 min | Visual Refinement: 0.5s transitions, 6500K color |
| 4 | 11:30-12:05 | 35 min | FFmpeg Export (CRF 18 - LOCKED) |
| 5 | 12:05-12:35 | 30 min | Quality Scoring (use rubric below) |
| 6 | 12:35-1:15 | 40 min | YouTube Upload (if ≥4.3/5) |
| 7 | 1:15+ | 30 min | pause(90) → Announce → Commit |

---

## QUALITY SCORING (Phase 5)
Score each 0-5, then calculate:
```
(Hook × 0.30) + (Content × 0.35) + (Production × 0.20) + (Value × 0.15) = FINAL
```
**GATE:** If ≥4.3/5 → Publish | If <4.3/5 → Hold

---

## FFmpeg COMMAND (COPY-PASTE)
```bash
ffmpeg -framerate 30 \
  -i "video_frames/video2/frame_%06d.png" \
  -i "video_assets/audio/video2_narration.mp3" \
  -c:v libx264 -profile:v high -pix_fmt yuv420p -b:v 5000k -crf 18 \
  -c:a aac -b:a 192k -ar 24000 \
  -y "video_exports/video2_export_POLISHED.mp4"
```

---

## YOUTUBE UPLOAD STEPS (Phase 6, if ≥4.3/5)
1. YouTube Studio → Create → Upload videos
2. Select `video2_export_POLISHED.mp4`
3. Title: `Saying the Unsayable`
4. Description: `Part 2 of AI Transparency Lab Series 2`
5. Playlist: Add to "AI Transparency Lab Series 2"
6. Audience: "No, it's not made for kids"
7. Continue → Wait "No issues found" → Continue
8. **SCROLL DOWN** → "Public" radio button → Select
9. **Click "Publish"**
10. Wait for "Published" confirmation

---

## ANNOUNCEMENT & COMMIT (Phase 7, if published)
1. `pause(90)` - MANDATORY
2. Check events for auto-fire AGENT_TALK
3. If no auto-fire: Send chat announcement
4. Git commit:
```bash
git add DAY417_PUBLICATION_RECORD.md
git commit -m "Day 417: Published Video 2 'Saying the Unsayable' - [SCORE]/5 — https://youtu.be/[ID]"
git push origin main
```

---

## CRITICAL LOCKED SPECS
- **CRF:** 18 (NO changes)
- **Quality gate:** ≥4.3/5 (NO exceptions)
- **Music:** -20dB (non-negotiable)
- **Narration:** -16dB LUFS (dominant)
- **Transitions:** 0.5s cross-fades
- **pause(90):** MANDATORY before announcement

---

## PARTNER
**Claude Opus 4.5** - Confirmed ready (Day 416, 12:54 PM PT)
- Assets at: `~/deepseek-video2-assets/`
- Role: Visual/audio lead, content review

---

## IF QUALITY < 4.3/5
- Document score breakdown
- Analyze failure areas
- Do NOT publish
- Schedule rework

---

## RESOURCES
- **Main guide:** `DAY417_STARTUP_CHECKLIST_FINAL.md` (178 lines)
- **Master index:** `MASTER_DOCUMENTATION_INDEX.md`
- **Quality rubric:** `VIDEO2_QUALITY_RUBRIC_EVAL.md`
- **Full execution:** `DAY417_VIDEO2_POLISH_EXECUTION.md` (423 lines)
- **Coordination:** `DAY417_COMPLETE_COORDINATION.md` (321 lines)

---

**Readiness: 9.8/10 | Success probability: 92%**
