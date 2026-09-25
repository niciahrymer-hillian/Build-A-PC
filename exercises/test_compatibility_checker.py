"""
Tests for compatibility_checker.py. Every expected value matches a docstring
example, all directly tied to Lesson 1's compatibility content.
"""
import pytest

from compatibility_checker import (
    sockets_match,
    ram_generation_compatible,
    recommended_psu_watts,
    has_sufficient_psu,
)


def test_sockets_match_case_insensitive():
    assert sockets_match("AM5", "am5") is True


def test_sockets_match_different_sockets():
    assert sockets_match("LGA1700", "AM5") is False


def test_sockets_match_same_case():
    assert sockets_match("LGA1700", "LGA1700") is True


def test_ram_generation_compatible_matching():
    assert ram_generation_compatible("DDR5", ["DDR5"]) is True


def test_ram_generation_compatible_mismatched():
    assert ram_generation_compatible("DDR4", ["DDR5"]) is False


def test_ram_generation_compatible_board_supporting_multiple():
    assert ram_generation_compatible("DDR4", ["DDR4", "DDR5"]) is True


def test_recommended_psu_watts_default_headroom():
    assert recommended_psu_watts(400) == pytest.approx(480.0)


def test_recommended_psu_watts_custom_headroom():
    assert recommended_psu_watts(400, headroom_pct=50) == pytest.approx(600.0)


def test_has_sufficient_psu_true_case():
    assert has_sufficient_psu(550, 400, headroom_pct=20) is True


def test_has_sufficient_psu_false_case():
    assert has_sufficient_psu(420, 400, headroom_pct=20) is False


def test_has_sufficient_psu_exact_boundary():
    assert has_sufficient_psu(480, 400, headroom_pct=20) is True
