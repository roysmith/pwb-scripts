#!/usr/bin/env python

import os
from pathlib import Path

from pywikibot import Site, Category

def main():
    os.environ['PYWIKIBOT_DIR'] = str(Path(__file__).resolve().parent)
    site = Site('en', 'wikipedia')
    living_people = Category(site, 'Living people')
    for article in Category(site, 'Minnesota politicians').articles(recurse=6):
        if living_people in article.categories() and not article.protection():
            print(article)
        


if __name__ == "__main__":
    main()
