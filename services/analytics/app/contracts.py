"""MCX gold contract specs and normalisation to rupees per gram at 999 purity."""

from dataclasses import dataclass

TARGET_PURITY = 999


@dataclass(frozen=True)
class ContractSpec:
    symbol: str
    lot_grams: float
    quote_grams: float  # price is quoted per this many grams
    purity: int  # fineness in parts per thousand


# Values follow the Round 1 deck. TODO: verify purity against the MCX contract specification
# pages before relying on these numbers.
CONTRACTS: dict[str, ContractSpec] = {
    spec.symbol: spec
    for spec in (
        ContractSpec("GOLDM", lot_grams=100, quote_grams=10, purity=995),
        ContractSpec("GOLDTEN", lot_grams=10, quote_grams=10, purity=999),
        ContractSpec("GOLDGUINEA", lot_grams=8, quote_grams=8, purity=999),
        ContractSpec("GOLDPETAL", lot_grams=1, quote_grams=1, purity=999),
    )
}


def normalise_price(symbol: str, quoted_price: float) -> float:
    """Convert an MCX quoted price into rupees per gram of 999 gold."""
    spec = CONTRACTS[symbol]
    per_gram = quoted_price / spec.quote_grams
    return per_gram * TARGET_PURITY / spec.purity
