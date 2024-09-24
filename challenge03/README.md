# Challenge 03

Write a class to retrieve tweets from the Twitter API.

## Description

In this three part challenge you will analyze Twitter Data.

* Define a class called UserTweets that takes a Twitter handle / user in its constructor. 
It also receives an optional max_id parameter to start from a particular tweet id.

* Create a tweepy API object using the tokens imported from config.py.

* Create an instance variable to hold the last 100 tweets of the user.

* Implement len() and getitem() magic (dunder) methods to make the UserTweets object iterable.

* Save the generated data as CSV in the data subdirectory: data/some_handle.csv, columns: id_str,created_at,text

