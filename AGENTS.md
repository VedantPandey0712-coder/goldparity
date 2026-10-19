# Instructions for AI coding assistants

This file is read automatically by Claude Code (via `CLAUDE.md`), Codex, Cursor, Copilot and
similar tools.

## Progress tracking (required)

- **Before starting work, read [progress.md](progress.md)** to see what is done, in progress,
  decided and blocked.
- **Before every commit, update progress.md** following the instructions at the top of that
  file, and include it in the same commit.

## Project rules

- Web app (`apps/web`) is **JavaScript, not TypeScript**. Use npm, not pnpm or yarn.
- No NestJS. The Next.js app calls the FastAPI service (`services/analytics`) directly.
- Python service uses Python 3.13 and uv. Run `uv run pytest` and `uv run ruff check .`
  before committing.
- Prices are normalised to ₹ per gram at 999 purity. Contract specs live in
  `services/analytics/app/contracts.py`; don't hard-code them elsewhere.
- Contracts are keyed by `(symbol, expiry_date)`. Never stitch contracts into one continuous series.
