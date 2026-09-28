# ADR 0001: Tech stack

## Status
Accepted

## Context
AegisGate needs a fast-to-build API, strong typing, and good AI ecosystem fit.

## Decision
Python 3.12, FastAPI, PostgreSQL, SQLAlchemy/Alembic, pytest, uv, ruff, mypy.
Custom policy engine (not OPA) to demonstrate core design depth.

## Alternatives considered
- Go: faster runtime, slower iteration for me right now.
- OPA/Rego: mature, but hides the core logic I want to build and learn.

## Consequences
Python is slower than Go, acceptable because policy evaluation is
in-memory and cheap. Revisit if benchmarks show otherwise.
