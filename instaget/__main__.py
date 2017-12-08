#!/usr/bin/env python3

import sys
import json
import requests
from urllib import request
from bs4 import BeautifulSoup

def main():
    try:
        url   = sys.argv[1]

        page  = BeautifulSoup(requests.get(url).text, 'html.parser')
        image = page.find_all('script')

        image = image[2].text.replace("window._sharedData = ", "")
        image = image.replace(";", "")

        image_uri  = json.loads(image)['entry_data']['PostPage'][0]['graphql']['shortcode_media']['display_url']
        image_file = image_uri.split("/")[-1]

        request.urlretrieve(image_uri, image_file)
    except IndexError:
        print("No URL!")
    except json.decoder.JSONDecodeError:
        print("Invalid URL")
    except requests.exceptions.MissingSchema:
        print("Invalid URL")

if __name__ == "__main__":
    main()
    