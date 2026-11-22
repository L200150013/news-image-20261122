# Sunday 22 November 2026 — The World in One Image

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/L200150013/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/L200150013/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

Entry for the [make.fun competition "Sum up 22 November's world news in one image"](https://make.fun/bounty/news-image-20261122) — $100, 50 places, closes 24 November 2026 07:00 WIB.

## The image

**THE SUNDAY GLOBE** — a one-page newspaper front page for Sunday 22 November 2026:

- **35 stories across 7 regions** (Middle East, Europe, Asia, Africa, North America, Oceania, World), every one first reported on 22 November 2026.
- **11 numbered lead panels**: COP31 nears a final deal in Antalya; Iran says it hit US radars at two Bahrain bases; the Russian freighter Sparta II ablaze in the Gulf of Finland; a strike on a Gaza food-aid car; the Manipur toxic-liquor toll; NATO's vow to defend Poland; Iraq's Najaf oil-smuggling ring; blasts reported at the Baltiysk naval base; two tankers hit near Hormuz; Trump accuses Iran of breaching the deal; Myanmar rejects the ICJ genocide ruling.
- **A stat strip** sizing the day (03:00 GMT objections deadline, 16 dead in Manipur, 2 bases, 23 dead off Bayelsa, 34–10, 9–6).
- **A world map** with the 11 lead stories pinned, plus a stories-by-region legend.
- **ALSO ON, stories 12–35**, and a **DATE CHECK** box naming what was deliberately left out as other days' news: the Peru quake (21 Nov), the Kyiv 400-drone barrage (20 Nov), the Banda Sea quake (21 Nov), the New Zealand election (7 Nov).
- Disputed claims are attributed to their source throughout. Sources: Reuters, AP, AFP, BBC, Al Jazeera, Xinhua, Euronews.

## How it runs

`main.py` (Python 3.13, standard library only) copies the shipped `entry.png` (1024×1024, under 1 MiB) to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). No network, no clock, no randomness — two runs write byte-identical files.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
