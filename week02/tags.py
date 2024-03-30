from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')


def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall"""
    with open(RSS_FEED, 'r', encoding='utf-8') as file:
        rss_content = file.read()
    tags = TAG_HTML.findall(rss_content)
    return [tag.replace('-', ' ') for tag in tags]

def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)"""
    tag_counter = Counter(tags)
    return tag_counter.most_common(TOP_NUMBER)


def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    similar_pairs = set()
    for tag1, tag2 in product(tags, repeat=2):
        if tag1 == tag2:
            continue
        similarity_ratio = SequenceMatcher(None, tag1, tag2).ratio()
        if similarity_ratio > SIMILAR:
            similar_pairs.add((tag1, tag2))
    
    return similar_pairs


if __name__ == "__main__":
    tags = get_tags()
    print(tags)
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))