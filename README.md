# GoldParity

Cross-contract intelligence for MCX gold — Team Manali Trance, Hack in Hills '26 (PS 03).

GoldParity normalises GOLDM, GOLDTEN, GOLDGUINEA and GOLDPETAL prices to ₹ per gram at 999
purity, flags rich/cheap spreads between them, and backtests whether the edge survives costs.

## Project progress

**All project progress up to the latest commit is recorded in [progress.md](progress.md).**
Read it before you start working. Every commit must update it in the same commit: what was
done, what is in progress, new decisions and blockers. If you use an AI assistant, it will
pick this up from [AGENTS.md](AGENTS.md) / [CLAUDE.md](CLAUDE.md) and update the file for you.

## Layout

```text
apps/web/              Next.js dashboard (JavaScript, Tailwind, Recharts)
services/analytics/    Python FastAPI service: ingestion, normalisation, signals, REST API
docker-compose.yml     Postgres (TimescaleDB image)
```

## Prerequisites

- Node.js 20+ and npm
- Python 3.13 and [uv](https://docs.astral.sh/uv/) (`pip install uv`)
- Docker Desktop

## Run locally

```bash
# 1. Database
docker compose up -d

# 2. Analytics API  →  http://localhost:8000/docs
cd services/analytics
cp .env.example .env
uv sync
uv run fastapi dev app/main.py

# 3. Dashboard  →  http://localhost:3000
cd apps/web
cp .env.example .env.local
npm install
npm run dev
```

## Checks

```bash
cd services/analytics && uv run pytest && uv run ruff check .
cd apps/web && npm run lint
```
