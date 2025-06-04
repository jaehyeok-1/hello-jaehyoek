# hello-jaehyoek

This repository contains a small script that fetches a random news
headline from the Naver News website.

## Requirements

- Python 3.7 or higher
- The `requests` and `beautifulsoup4` packages

Install the packages with:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the script to print one random headline:

```bash
python naver_random_title.py
```

The script downloads the Naver News front page, collects visible article
links and displays a random title.
