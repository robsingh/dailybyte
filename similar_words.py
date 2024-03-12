"""
Given a list of tags of our blog find the ones that have a similarity score of over 95%

Don't worry, difflib to the rescue and in particular SequenceMatcher.

Return a list of similar tag pairs (tuples):

[('cheat sheets', 'cheat sheet'), 
 ('webscraping', 'web scraping'),
 ('contextmanagers', 'contextmanager'),
 ...]
"""
from difflib import SequenceMatcher
from collections import defaultdict

def similar_tags(tags):
    # brute force approach
    # similar_pairs = []
    # for i in range(len(tags)):
    #     for j in range(i+1, len(tags)):
    #         similarity = SequenceMatcher(None, tags[i], tags[j]).ratio()
    #         if similarity > 0.95:
    #             similar_pairs.append((tags[i], tags[j]))
    # return similar_pairs

    #another approach
    grouped_tags = defaultdict(list)
    for tag in tags:
        normalized_tag = tag.replace(" ", "").lower()
        grouped_tags[normalized_tag].append(tag)
        
    similar_pairs = []
    for group in grouped_tags.values():
        for i in range(len(group)):
            for j in range(i+1, len(group)):
                similarity = SequenceMatcher(None, group[i], group[j]).ratio()
                if similarity > 0.95:
                    similar_pairs.append((group[i], group[j]))
    return similar_pairs

   
tags = ['cheat sheets', 'cheat sheet', 'webscraping', 'web scraping', 'contextmanagers', 'contextmanager']
print(similar_tags(tags))
