# Grailed Price Scraper

## About
[Grailed](https://www.grailed.com/) is a website that allows users to buy and sell new/used clothing. It is sort of like eBay but with clothing only.

Clothing pieces are sorted into 3 sections: Grailed, Hype, and Basics
Grailed - High end designer clothing brands.
Hype - Brands highly sought after.
Basics - Everything else that doesn't really fit into the other categories.

## What the Grailed Price Scraper does
Each listing is set up by an ID in the URL. So for instance, a listing with ID = 250 will have a URL of https://www.grailed.com/listings/250.

The Grailed Price Scraper visits each listing and scrapes for: designer name, ID, item, price, size and if it sold. The resulting data is printed to a specified json file.

Here is an example of 5 listings:

```
[
    {
        "Designer:": "J.Crew",
        "ID": 10005,
        "Item:": "Jasper Jersey Crewneck",
        "Price:": "$18 ",
        "Size:": "US S / EU 44-46 / 1",
        "Sold:": true
    },
    {
        "Designer:": "The North Face",
        "ID": 10006,
        "Item:": "Apex \"1st Ascents\" Softshell",
        "Price:": "$25 ",
        "Size:": "US S / EU 44-46 / 1",
        "Sold:": true
    },
    {
        "Designer:": "Japan Blue",
        "ID": 10007,
        "Item:": "Japan Blue x Blue Owl 12oz \"Ha",
        "Price:": "$125 ",
        "Size:": "US 29",
        "Sold:": true
    },
    {
        "Designer:": "Antonio Marras",
        "ID": 10008,
        "Item:": "3 LAYERS VEST",
        "Price:": "$130",
        "Size:": "US M / EU 48-50 / 2",
        "Sold:": false
    },
    {
        "Designer:": "Robert Geller",
        "ID": 10009,
        "Item:": "DOUBLE STRAPS VEST",
        "Price:": "$125 ",
        "Size:": "US M / EU 48-50 / 2",
        "Sold:": true
    }
]
```

## Usage
This was written in Python 2 so it may not work for Python 3 (I have not tested it).
Dependencies include: Requests and BeautifulSoup which may be obtained from the Python pip package manger.

Running it is as follows:

`python grailed_scraper <Start Index> <End Index> <1 or 0 for Info Display> <filename (without extension)>`
