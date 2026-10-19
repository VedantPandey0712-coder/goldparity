import pytest

from app.contracts import normalise_price


def test_goldm_quote_per_10g_at_995_is_scaled_to_999():
    assert normalise_price("GOLDM", 75_000) == pytest.approx(7_500 * 999 / 995)


def test_goldpetal_quote_per_gram_at_999_is_unchanged():
    assert normalise_price("GOLDPETAL", 7_500) == pytest.approx(7_500)


def test_goldguinea_quote_per_8g_is_divided_by_8():
    assert normalise_price("GOLDGUINEA", 60_000) == pytest.approx(7_500)


def test_unknown_symbol_raises():
    with pytest.raises(KeyError):
        normalise_price("SILVER", 90_000)
