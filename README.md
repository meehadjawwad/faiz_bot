# Aim

A Twitter bot that:

1. automatically tweets a verse from Faiz's poetry after regular intervals
2. automatically likes and replies with a verse from Faiz's poetry to every tweet that mentions the bot

---

# Hardware Used

```
MacBook Pro (Retina, 13-inch, Early 2015)
Processor: 2.9 GHz Dual-Core Intel Core i5
Memory: 8 GB 1867 MHz DDR3
OS: macOS Big Sur (version 11.2)
```

# Technologies Used

```
- python
- selenium
- tweepy
- PyCharm
- pythonanywhere
```

# Breakdown of Aim

1. **Automatically tweets a verse after regular intervals:**
    1. Access an online poetry resource
    2. Scrape verses of poetry and store them in a list
    3. Conduct appropriate formatting
    4. Write main code
2. **Automatically likes and replies with a verse to every tweet that mentions the bot:**
    1. Extract the Tweet_ID of the most recent tweet that mentions the bot
    2. Save the Tweet_ID in a separate text file
    3. 

## Aim 1 - Tweets

### Getting Poetry

I decided I wanted to store and access poetry  through a list; and I came upon this decision due to the following reasons:

- It woud be easy to format the elements.
- The order is not important.
- It would be easier to delete and add elements.

###Web scraping

I used ```selenium webdriver``` to automate this process.

After initiating the webdriver, the first step was to access [Faiz's Ghazals on Rekhta](https://www.rekhta.org/poets/faiz-ahmad-faiz/ghazals) which is a repository of Faiz's poetry and contains links to individual ghazals.

The second step was to save all the links (to individual ghazals) in a list, which was performed through a simple for loop.

The third step was to access each link and save the verses in a new list. This was performed through a three-layered for loop.

In the end, I had a list that contained all the verses from all the links in the original parent page. Every element of the list was a couplet (with some exceptions, of course).

###Formatting the list

Some basic formatting was performed on the list such as removing duplicates and blank entries, and replacing `,` with `\`

###Tweeting

Using the ```update_status``` method in ```tweepy```, I used a while loop to publish a tweet every 4 hours. The content of the tweet was simply an element from the poetry list, chosen at random.

## Aim 2 - Likes and Replies

###Organising Mentions

The first step was to access and store all the tweets that need to be liked and replied to (all the tweets that mention the bot).

The `mentions_timeline` method in `tweepy` is useful because it allows you tu specify the 'since_id' in regards to the tweets you want returned.

I made a new text file in order to access and store all the tweets that are returned, and two functions to read and write to the file.
The first function stores the tweet_id of every mention that the bot receives to the file, and the second function reads the tweet_id from the file.

###Liking and Replying

