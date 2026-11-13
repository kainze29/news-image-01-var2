# news-image-01 var2: The World Today, Friday 13 November 2026

One image that sums up the world's news of Friday 13 November 2026,
drawn as a broadsheet newspaper front page: black-and-white print with
one red accent, serif headlines, and the masthead THE WORLD TODAY.

## The front page

| Story | What the page shows |
| --- | --- |
| NVIDIA chief resigns | Lead story: an empty Senate witness chair with a leather jacket, a computer chip, and a falling red market chart. Jensen Huang resigns; shares fall about 16%; the US Senate Banking Committee had summoned Huang and Commerce Secretary Lutnick |
| EU joins Ukraine talks | Zelensky meets US envoys; Europe is promised a seat at the next round of Ukraine-Russia talks; a large prisoner exchange is agreed |
| Drone hits Russian warship | A Ukrainian drone strikes the Russian corvette Naro-Fominsk in the Gulf of Finland; Finland confirms detecting the strike |
| Iran claims Bahrain strike | Iran says it struck a US radar site in Bahrain as Gulf tensions rise |
| FBI: N. Korea $400m hack | The FBI says North Korean hackers used fake video calls and deepfakes to steal about $400m in crypto |
| Strike hits Gaza hospital | An Israeli strike on Nasser Hospital in Khan Younis kills six people, including a surgeon |

The foot of the page also notes three more stories from the day:
the Microsoft 365 outage, Storm Charles in Portugal, and Kane breaking
England's caps record.

## How it runs

`main.py` (Python 3.13, standard library only) checks the bundled
`news.png` is a real 1024x1024 PNG and writes an identical copy to
`/output/entry.png`. No network, no drawing at run time, so both runs
write the same bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entry program
- `news.png` — the front-page image (1024x1024 PNG, under 1 MiB)
- `LICENSE` — MIT

The six stories are the verified news of Friday 13 November 2026,
as researched for the first entry of this bounty; the layout, the
artwork, and the wording here are this variation's own.
