#!/usr/bin/env python3

import sys
import json
import requests
import click
from urllib import request
from bs4 import BeautifulSoup


@click.command()
@click.option('--uri', default='', help="Media URI that you want to download")
@click.option('--output', default=False, help="Output file.")
def main(uri, output):
    try:
        page   = BeautifulSoup(requests.get(uri).text, 'html.parser')
        media  = page.find('meta', property='og:image')['content']

        if not output:
            output = media.split("/")[-1]
            output = output.split("?")[0]

        request.urlretrieve(media, output)

    except IndexError:
        print("No URL!")
    except ValueError:
        print("Invalid URL")
    except requests.exceptions.MissingSchema:
        print("Invalid URL")

if __name__ == "__main__":
    main()
    
