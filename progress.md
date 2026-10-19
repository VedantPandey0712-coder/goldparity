# GoldParity — Project Progress

> **Single source of truth for where the project stands.** Every commit that changes
> code, data or decisions must update this file in the same commit, so any teammate (or
> their AI assistant) can read it and know exactly what is done, what is in progress and
> what is next.

---

## 🤖 Instructions for AI assistants (and humans)

If you are an AI coding assistant working in this repo, **you must keep this file up to
date**. Before you finish a task or create a commit:

1. **Read this whole file first** so you don't redo finished work or contradict a decision.
2. Update **Current status**: date (YYYY-MM-DD), who worked (name of the teammate you are
   helping), and the phase.
3. Move items between **Done / In progress / Next up**. Tick `[x]` only for work that is
   actually finished and verified (tests or a manual run), not for work that merely exists.
4. Add new decisions to **Decisions log** with a one-line reason. Never silently reverse an
   existing decision; if you change one, log the new decision and why.
5. Add any blocker or open question to **Blockers / open questions**, naming who needs to
   answer it.
6. Add **one entry at the top of the Changelog** for this commit: date, author, a short
   summary and the main files touched.
7. Keep it short and factual. Don't paste code here, link to files instead.
8. Commit this file **together with** the change it describes, not in a separate commit.

---

## Current status

- **Last updated:** 2026-10-19 by Ujjwal Verma
- **Phase:** Prototype (MVP), due before Round 2 (22–25 Oct 2026)
- **Next milestone:** Bhavcopy ingestion → normalised prices in DB → spread chart on dashboard

## Team and ownership

| Person | Area |
| --- | --- |
| Ujjwal Verma | Full stack: web app, API, data pipeline |
| Vedant Pandey | Data and analytics: normalisation, backtesting |
| Ujjawal Srivastava | Frontend and design: dashboard, charts, pitch |

## Done

- [x] Repo scaffold: `apps/web` (Next.js 16, JavaScript, Tailwind, Recharts) and
      `services/analytics` (FastAPI, Python 3.13, uv)
- [x] Postgres (TimescaleDB image) via `docker-compose.yml`
- [x] Contract specs and `normalise_price()` to ₹/g at 999 purity
      ([services/analytics/app/contracts.py](services/analytics/app/contracts.py)), 4 tests passing
- [x] FastAPI endpoints: `GET /health`, `GET /contracts`
- [x] GitHub Actions CI: web lint + build, analytics ruff + pytest. Hardened like
      releaseproof: SHA-pinned actions, read-only token, no dependency cache, timeouts
- [x] `@claude` PR/issue review workflow ([.github/workflows/claude.yml](.github/workflows/claude.yml)),
      needs the `CLAUDE_CODE_OAUTH_TOKEN` secret (see Blockers)

## In progress

- (nothing yet)

## Next up (prototype)

- [ ] Get historical MCX Bhavcopy CSVs for gold contracts (manual download if scripted fetch is blocked)
- [ ] Bhavcopy parser: validate trade date, filter gold symbols, key rows by `(symbol, expiry_date)`
- [ ] DB schema + Alembic migration for daily contract prices
- [ ] Daily ingestion job (APScheduler or GitHub Actions cron)
- [ ] API: normalised price series and cross-contract spreads with z-scores
- [ ] Dashboard: normalised price chart + spread / rich-cheap table
- [ ] Deploy demo (Vercel for web; Render or Railway for API + DB)
- [ ] Demo video and docs for Round 2

## Later (finale, 20–21 Nov 2026)

- [ ] Walk-forward backtester with costs, slippage and gold-beta stripping
- [ ] Quiet alert engine (in-app, email, Telegram) + contract calendar
- [ ] Redis cache/jobs, WebSocket live spreads

## Decisions log

| Date | Decision | Reason |
| --- | --- | --- |
| 2026-10-19 | No NestJS: Next.js talks directly to FastAPI | Daily data; a second backend adds work without features |
| 2026-10-19 | JavaScript, not TypeScript, for the web app | Team preference |
| 2026-10-19 | npm for JS, uv for Python | npm ships with Node; uv is fast and locks deps |
| 2026-10-19 | TimescaleDB Docker image, used as plain Postgres for now | Hypertables available later at no extra cost |

## Blockers / open questions

- **Contract purity values** in `contracts.py` follow the Round 1 deck (GOLDTEN, GOLDGUINEA,
  GOLDPETAL = 999). Need to verify them against the MCX contract specs. *(Vedant / Ujjwal)*
- **Bhavcopy source:** does anyone already have historical CSVs downloaded? *(team)*
- **`CLAUDE_CODE_OAUTH_TOKEN` repo secret** must be added by the repo owner (Settings →
  Secrets → Actions); collaborators can't add secrets. Until then `@claude` does nothing. *(Vedant)*

## Changelog (newest first)

### 2026-10-19 — Ujjwal Verma

Initial project scaffold: Next.js web app, FastAPI analytics service, contract normaliser
with tests, Docker Compose Postgres, hardened CI + `@claude` review workflow, README,
progress tracking (`progress.md`, `AGENTS.md`, `CLAUDE.md`).
