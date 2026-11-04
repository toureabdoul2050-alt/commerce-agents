# commerce-agents

Three small tools I use to make decisions for an online store:

- **scout** ranks product ideas from a CSV with a simple, transparent score
- **listing** writes a marketplace title, bullet points and description with an LLM
- **sales** summarizes revenue, gross margin and the best-selling product

`scout` and `sales` are plain Python and need no API key. Only `listing` calls the Claude API.

## Usage

```bash
pip install anthropic

python commerce.py scout ideas.csv
python commerce.py sales sales.csv

export ANTHROPIC_API_KEY=your-key
python commerce.py listing "Foldable LED desk lamp" "USB-C, 3 light modes, touch control"
```

## CSV format

`ideas.csv` (`demand` and `competition` are scores from 1 to 10):

```csv
name,price,cost,demand,competition
LED desk lamp,39.99,12.50,8,5
```

`sales.csv`:

```csv
product,units,price,cost
LED desk lamp,14,39.99,12.50
```

## How the score works

```
score = margin% * 0.5 + demand * 5 - competition * 3
```

The weights are a starting point. Change them in `score()` to fit your market.

## Ideas for later

- Read products and orders directly from the Shopify API
- Listings in several languages

## License

MIT
