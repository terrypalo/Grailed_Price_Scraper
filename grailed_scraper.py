import requests
import json
import sys
from bs4 import BeautifulSoup as bs

def getOptions():
    # Make sure you give valid arg values or else it wont work.
    # Not planning on doing any error checking
    if len(sys.argv) != 4:
        print 'usage: ./grailed_scraper <Start Index> <End Index> <0 or 1 for Info Display>'
        sys.exit(0)

    args = {
    'startIndex': int(sys.argv[1]),
    'endIndex': int(sys.argv[2]),
    'infoDisplay': int(sys.argv[3])
    }

    return args

def main():
    options = getOptions()
    allListings = []
    pageIndex = options['startIndex']
    endIndex = options['endIndex']

    while pageIndex < endIndex:
        # Grailed puts makes their listings by number at the end of the /listings/
        baseURL = "https://www.grailed.com/listings/%s" % pageIndex
        htmlToParse = requests.get(baseURL)
        soup = bs(htmlToParse.text, "lxml")

        listingDetails = soup.find('div', {'class': 'listing-details-wrapper'})
        # Sometimes the page is 404'd, so in the case that it is, just skip over it
        if listingDetails is None:
            if options['infoDisplay'] is 1:
                print "Listing %s was 404'd. Skipping to next listing." % pageIndex

        else:
            # if it is not a 404 page then scrape the designer, item, size, and price
            designer = listingDetails.find('h1', {'class': 'designer'}).get_text().strip()
            item = listingDetails.find('h2', {'class': 'listing-title'}).get_text().strip()
            size = listingDetails.find('h2', {'class': 'listing-size'}).get_text().strip()
            price = listingDetails.find('h1', {'class': 'sub-title'})

            # Check if the listing has been sold
            if 'sold' in price['class']:
                sold = "Sold"
                price = price.get_text().strip()
                price = price.replace("(sale price)", "")
            else:
                sold = "unsold"
                price = price.get_text().strip()

            # Create a dict for the listing that was just scraped and append it
            # to all listings
            listing = {
                "ID" : pageIndex,
                "Designer:" : designer,
                "Item:" : item,
                "Size:" : size,
                "Price:" : price,
                "Sold:" : sold
            }
            allListings.append(listing)

            if options['infoDisplay'] is 1:
                print "Listing %s was found and added." % pageIndex

        pageIndex = pageIndex + 1

    # Convert it to json and print it out
    # Copy the output and put it in a JSON pretty printer to see the results
    # more clearly
    print json.dumps(allListings)

if __name__ == '__main__':
    main()
