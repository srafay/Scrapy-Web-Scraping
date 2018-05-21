# A program for web scraping in Python

### The library used is :
**Scrapy**
	* Scrapy is a fast high-level web crawling and web scraping framework, used to crawl websites and extract structured data from their pages. It can be used for a wide range of purposes, from data mining to monitoring and automated testing

#### Some useful commands
**scrapy shell**
	* For experimenting and extracting response before actually writing a script
**fetch("URL")**
	* Runs crawler on the url and returns a response object with downloaded information
**view(response)**
	* To open the downloaded page in the browser (response.text for raw data)
**response.css(".className::text").extract()**
	* To extract only text content of all elements based on css selector (extract_first() for first element match)
