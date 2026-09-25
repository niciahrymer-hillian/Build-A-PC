# Exercises — Build Compatibility Checker

A hands-on companion to Lesson 1 (compatibility) in the interactive tour. The same checks the lesson
describes doing by hand before buying anything — socket match, RAM generation, PSU headroom — written
as reusable functions instead of a one-time mental exercise.

## Setup

```bash
# from this exercises/ folder
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install pytest
```

## Run the tests

```bash
pytest -v
```

You'll see 11 failing tests — every function in `compatibility_checker.py` currently raises
`NotImplementedError`.

## What to do

Open `compatibility_checker.py`. Implement in this order:

1. `sockets_match` — a case-insensitive string comparison.
2. `ram_generation_compatible` — membership check against a board's supported generations.
3. `recommended_psu_watts` — apply a headroom percentage to a component load figure.
4. `has_sufficient_psu` — reuse `recommended_psu_watts` to answer yes/no for a specific PSU.

## When you're done

All 11 tests passing means you have a reusable checklist you can actually run against real parts the
next time you're planning a build — not just something you remembered to think about once.
