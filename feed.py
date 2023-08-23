"""
The Steam gaming platform has an RSS feed of their latest game releases. In this Bite, you'll pull down and parse that feed.

Specifically, pull out the names of the games in the feed as well as their URLs. Use the Game namedtuple provided.

To make sure you work with a static feed we copied today's version so use the URL defined in FEED_URL. Enjoy!
"""

import feedparser
from collections import namedtuple

Game = namedtuple('Game', 'name url')

FEED_URL = 'https://store.steampowered.com/feeds/newreleases.xml'

def get_latest_game_releases(feed_url):
    games = []

    # parse the RSS feed
    feed = feedparser.parse(feed_url)

    # extract game names and URLs
    for entry in feed.entries:
        game_name = entry.title
        game_url = entry.link
        game = Game(name=game_name, url=game_url)
        games.append(game)

    return games


if __name__ == "__main__":
    latest_games = get_latest_game_releases(FEED_URL)

    for game in latest_games:
        print(f"Name: {game.name}")
        print(f"URL: {game.url}")
        print()