"""Smoke tests for cvo260917."""

from cvo260917 import hello


def test_sanity() -> None:
    """Sanity check."""
    assert True


def test_integration() -> None:
    """Integration test for hello function."""
    assert hello() == 'Hello you from cvo260917!'
