#!/usr/bin/env python3
"""Buffering the Truth — entry for The Router Confesses on make.fun.

Prints exactly one line (at most 200 characters): what a home Wi-Fi router
would say to excuse dropping the connection at a movie's climax.
"""

LINE = "I dropped the connection at the climax because somebody in this house had to protect you from that plot twist."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 200
    print(LINE)


if __name__ == "__main__":
    main()
