# Author:         Terry Palomares
# File:           grailed_scraper.py
# Description:    Scrapes data from listings on www.grailed.com given a start
# and end index as boundaries and pretty-prints the associated
# data in JSON format.

import requests
import json
import sys
from bs4 import BeautifulSoup as bs


def getOptions():
    # Make sure you give valid arg values or else it wont work.
    # Not planning on doing any error checking
    if len(sys.argv) != 5:
        print('usage: ./grailed_scraper <Start Index> <End Index>'
              '<1 or 0 for Info Display> <filename (without extension)>')
        sys.exit(0)

    args = {
        'startIndex': int(sys.argv[1]),
        'endIndex': int(sys.argv[2]),
        'infoDisplay': int(sys.argv[3]),
        'fileName': str(sys.argv[4]) + '.json'
    }

    return args


def main():
    options = getOptions()
    allListings = []
    pageIndex = options['startIndex']
    endIndex = options['endIndex']

    while pageIndex < endIndex:
        # Grailed makes their listings by number at the end of the /listings/
        baseURL = "https://www.grailed.com/listings/%s" % pageIndex
        htmlToParse = requests.get(baseURL)
        soup = bs(htmlToParse.text, "lxml")

        listingDetails = soup.find('div', {'class': 'listing-details-wrapper'})
        # Sometimes the page is 404'd, in such case, skip over it
        if listingDetails is None:
            if options['infoDisplay'] is 1:
                print "Listing %s was 404'd. Skipping to next listing." % pageIndex

        else:
            # if it is not a 404 page then scrape the designer, item, size, and
            # price
            designer = listingDetails.find(
                'h1', {'class': 'designer'}).get_text().strip()
            item = listingDetails.find(
                'h2', {'class': 'listing-title'}).get_text().strip()
            size = listingDetails.find(
                'h2', {'class': 'listing-size'}).get_text().strip()
            price = listingDetails.find('h1', {'class': 'sub-title'})

            # Check if the listing has been sold
            if 'sold' in price['class']:
                sold = True
                price = price.get_text().strip()
                price = price.replace("(sale price)", "")
            else:
                sold = False
                price = price.get_text().strip()

            # Create a dict for the listing that was just scraped and append it
            # to all listings
            listing = {
                "ID": pageIndex,
                "Designer:": designer,
                "Item:": item,
                "Size:": size,
                "Price:": price,
                "Sold:": sold
            }
            allListings.append(listing)

            if options['infoDisplay'] is 1:
                print "Listing %s was found and added." % pageIndex

        pageIndex = pageIndex + 1

    # Convert it to json and print it out
    outfile = open(options['fileName'], 'w')

    json.dump(allListings, outfile, sort_keys=True,
              indent=4, separators=(',', ': '))
    print "Data scraped into " + options['fileName']
if __name__ == '__main__':
    main()
