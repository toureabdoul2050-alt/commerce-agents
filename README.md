<div align="center">

# 🛒 Commerce Agents

**AI agents that find winning products, write listings that sell, and turn raw sales into clear decisions.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Claude](https://img.shields.io/badge/Powered%20by-Claude%20API-D97757?style=flat-square)
![Marketplaces](https://img.shields.io/badge/Works%20with-Shopify%20·%20Amazon%20·%20Etsy-7AB55C?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

</div>

---

## ✨ Three agents, one store

| Agent | Input | Output |
|---|---|---|
| 🔎 **Scout** | A CSV of product ideas (price, cost, demand, competition) | A ranked shortlist with a transparent score |
| ✍️ **Copywriter** | A product name + key features | A marketplace-ready title, bullet points and description |
| 📊 **Accountant** | A CSV of sales | Revenue, margin, best sellers — and a plain-language summary |

The **Scout** and **Accountant** math runs locally with no API key. Only the **Copywriter** uses an LLM.

## 🚀 Quick start

```bash
git clone https://github.com/toureabdoul2050-alt/commerce-agents.git
cd commerce-agents
pip install anthropic

python commerce.py scout ideas.csv
python commerce.py sales sales.csv
export ANTHROPIC_API_KEY="your-key"
python commerce.py listing "Foldable LED desk lamp" "USB-C, 3 light modes, touch control"
```

## 📄 CSV formats

```csv
# ideas.csv
name,price,cost,demand,competition
LED desk lamp,39.99,12.50,8,5
```

```csv
# sales.csv
product,units,price,cost
LED desk lamp,14,39.99,12.50
```

`demand` and `competition` are scores from 1 to 10.

## 🧮 How the Scout scores a product

```
score = margin% × 0.5  +  demand × 5  −  competition × 3
```

Simple, explainable, and easy to tune for your own market.

## 🗺 Roadmap

- [x] Product scoring
- [x] AI listing writer
- [x] Sales summary
- [ ] Shopify API connector
- [ ] Multi-language listings (EN · FR · ES)

---

<div align="center">Built by <a href="https://github.com/toureabdoul2050-alt">Ladji Touré</a> · MIT License</div>
