"""
Can you help PyBites automate their Amazon affiliation link creation?

Complete the generate_affiliation_link(url) function below which should convert the following links:

https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/?keywords=war+of+art
https://amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/ref=sr_1_1
https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/?qid=1537226234
https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X
https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/1449340377/
... into the following affiliation links respectively:

http://www.amazon.com/dp/1936891026/?tag=pyb0f-20
http://www.amazon.com/dp/1936891026/?tag=pyb0f-20
http://www.amazon.com/dp/1936891026/?tag=pyb0f-20
http://www.amazon.com/dp/020161622X/?tag=pyb0f-20
http://www.amazon.com/dp/1449340377/?tag=pyb0f-20
Hint: regex might be overkill here! 
"""
import re

def generate_affiliate_links(url):
    # Extracting the ASIN (Amazon Standarad Identification number) from the URL
    match = re.search(r'/dp/(\w+)', url)
    # print(match)

    if match:
        asin = match.group(1)
        affiliation_link = f"http://www.amazon.com/dp/{asin}/?tag=pyb0f-20"
        return affiliation_link
    else:
        return "Invalid URL format"

# test cases

urls = [
    "https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/?keywords=war+of+art",
    "https://amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/ref=sr_1_1",
    "https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/?qid=1537226234",
    "https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X",
    "https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/1449340377/"
]


for url in urls:
    print(generate_affiliate_links(url))