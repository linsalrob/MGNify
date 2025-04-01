"""
Find the samples from MGNify that come from a specific country.
"""

import os
import sys
import argparse
import requests
from mgnify_lib import colours

__author__ = ['Rob Edwards', 'ChatGPT']

def fetch_samples(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main(args):
    base_url = 'https://www.ebi.ac.uk/metagenomics/api/v1/samples?page_size=100'
    australian_samples = []
    all_countries = {}
    page_count = 1

    next_page = base_url
    while next_page:
        if args.v:
            print(f"{colours.GREEN}Fetching page {page_count} from {next_page}{colours.ENDC}", file=sys.stderr)
        page_count += 1
        data = fetch_samples(next_page)
        if data:
            for sample in data['data']:
                attributes = sample['attributes']
                geo_loc_name = attributes.get('geo-loc-name', '')
                if geo_loc_name and 'Australia' in geo_loc_name:
                    australian_samples.append(sample['id'])
                for sm in attributes['sample-metadata']:
                    if 'geographic location (country and/or sea,region)' == sm['key']:
                        if sm['value'] not in all_countries:
                            all_countries[sm['value']] = 1
                        else:
                            all_countries[sm['value']] += 1
            if args.v:
                print(f"{colours.PINK}Found {len(australian_samples)} samples from Australia so far.{colours.ENDC}", file=sys.stderr)
                print(f"{colours.BLUE}Countries: {all_countries}{colours.ENDC}", file=sys.stderr)
            next_page = data['links'].get('next')
        else:
            break

    print(f"Australian Sample Accessions: {australian_samples}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=' ')
    parser.add_argument('-v', help='verbose output', action='store_true')
    args = parser.parse_args()
    main(args)
