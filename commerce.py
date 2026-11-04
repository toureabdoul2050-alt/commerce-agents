"""Commerce Agents — Scout (product scoring), Copywriter (AI listings), Accountant (sales).

Usage:
    python commerce.py scout ideas.csv
    python commerce.py sales sales.csv
    python commerce.py listing "Product name" "key features"
"""
import csv
import os
import sys

MODEL = os.getenv("COMMERCE_MODEL", "claude-sonnet-5-5")


def read_csv(path: str) -> list:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# 🔎 Scout ---------------------------------------------------------------
def score(row: dict) -> float:
    price, cost = float(row["price"]), float(row["cost"])
    margin_pct = (price - cost) / price * 100 if price else 0
    return round(margin_pct * 0.5 + float(row["demand"]) * 5 - float(row["competition"]) * 3, 1)


def scout(path: str) -> None:
    rows = sorted(read_csv(path), key=score, reverse=True)
    print(f"{'Rank':<5}{'Product':<30}{'Score':>7}")
    for i, row in enumerate(rows, 1):
        print(f"{i:<5}{row['name'][:29]:<30}{score(row):>7}")


# 📊 Accountant ----------------------------------------------------------
def sales(path: str) -> None:
    rows = read_csv(path)
    revenue = profit = 0.0
    best = ("", 0.0)
    for row in rows:
        units, price, cost = int(row["units"]), float(row["price"]), float(row["cost"])
        r, p = units * price, units * (price - cost)
        revenue, profit = revenue + r, profit + p
        if p > best[1]:
            best = (row["product"], p)
    margin = profit / revenue * 100 if revenue else 0
    print(f"Revenue:      {revenue:,.2f}")
    print(f"Gross profit: {profit:,.2f}  ({margin:.1f}% margin)")
    print(f"Best seller:  {best[0]}  ({best[1]:,.2f} profit)")


# ✍️ Copywriter ----------------------------------------------------------
def listing(name: str, features: str) -> None:
    import anthropic

    prompt = (
        f"Write a marketplace listing for: {name}.\nKey features: {features}.\n"
        "Return: a title under 80 characters, 5 benefit-focused bullet points, "
        "and a 3-sentence description. Be honest — no claims that are not in the features."
    )
    response = anthropic.Anthropic().messages.create(
        model=MODEL, max_tokens=700, messages=[{"role": "user", "content": prompt}]
    )
    print(response.content[0].text.strip())


if __name__ == "__main__":
    commands = {"scout": scout, "sales": sales, "listing": listing}
    if len(sys.argv) < 3 or sys.argv[1] not in commands:
        sys.exit(__doc__)
    commands[sys.argv[1]](*sys.argv[2:])
