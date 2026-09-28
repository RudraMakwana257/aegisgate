"""Smoke tests for AegisGate."""

import aegisgate


def test_package_has_version() -> None:
    assert aegisgate.__version__ == "0.1.0"
