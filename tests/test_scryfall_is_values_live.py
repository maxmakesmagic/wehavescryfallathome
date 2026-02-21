"""Optional live validation of grammar `is:` values against Scryfall."""

import pytest
from conftest import ScryfallQuerier


@pytest.mark.live_scryfall
def test_live_scryfall_accepts_all_is_values(
    request: pytest.FixtureRequest,
    scryfall_querier: ScryfallQuerier,
    is_value: str,
) -> None:
    """Validate each grammar-declared `is` value against live Scryfall."""
    if not bool(request.config.getoption("--live-scryfall")):
        pytest.skip("Pass --live-scryfall to enable live Scryfall validation")

    ok, details = scryfall_querier.accepts_is_value(is_value)
    if details == "rate-limited":
        pytest.skip("Scryfall rate limited this test run")

    assert ok, f"Scryfall rejected is:{is_value} -> {details}"
