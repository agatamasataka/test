#!/usr/bin/env python3
"""Simple quit smoking tracker.

This script calculates the time elapsed since you stopped smoking.
"""

from __future__ import annotations

import argparse
from datetime import datetime


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Quit smoking counter")
    parser.add_argument(
        "start_date",
        help="Date of the last cigarette in YYYY-MM-DD format",
    )
    parser.add_argument(
        "--cigs-per-day",
        type=float,
        default=None,
        help="Average cigarettes per day before quitting",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        start = datetime.strptime(args.start_date, "%Y-%m-%d")
    except ValueError as exc:
        raise SystemExit(f"Invalid date format: {args.start_date}") from exc

    now = datetime.now()
    delta = now - start

    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    print(f"Smoke-free for {days} days, {hours} hours, {minutes} minutes.")

    if args.cigs_per_day is not None:
        total_cigs = args.cigs_per_day * delta.total_seconds() / 86400
        print(f"Estimated cigarettes not smoked: {int(total_cigs)}")


if __name__ == "__main__":
    main()
