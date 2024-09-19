Given our RSS feed what tags does PyBites mostly use and which tags should be merged (based on similarity)?

Example output:

$ python tags.py

* Top 10 tags:
python               10
learning             7
tips                 6
tricks               5
github               5
cleancode            5
best practices       5
pythonic             4
collections          4
beginners            4

* Similar tags:
game                 games
challenge            challenges
generator            generators


Both templates provide 3 constants you should use:

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
Rest is documented in the methods docstrings. Again use tags-help.py if you need more guidance, tags-nohelp.py is for the more experienced and/or if you want more freedom. Same goes for tests: use them if you need them.

Talking about freedom feel free to use our live feed but then the tests will probably break.

Hint: for word similarity feel free to use NLTK, or your favorite language processing tool. However, stdlib does provide a nice way to do this. Using this method we came to 0.87 as a threshold to for example not mark ‘python’ and ‘pythonic’ as similar.