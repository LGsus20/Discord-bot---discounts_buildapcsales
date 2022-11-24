
import praw
import math
import datetime

USERNAME = ''
PASSWORD = ''
APP_NAME = 'LG1'
PERSONAL_ID = ''
CLIENT_SECRET = ''
REQUEST = 7
topics_dict = { "title":[],
                "score":[],
                "id":[], "url":[],
                "comms_num": [],
                "created": [],
                "body":[]}

reddit = praw.Reddit(client_id=PERSONAL_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=APP_NAME,
                     username=USERNAME,
                     password=PASSWORD, check_for_async=False)

subreddit = reddit.subreddit('buildapcsales')
new_subreddit = subreddit.new(limit=REQUEST)

def last_deal():
    all_deals_list = []
    for submission in new_subreddit:
        one_deal = [submission.title, submission.url, minutes_ago(submission.created)]
        all_deals_list.append(one_deal)
    return all_deals_list

def minutes_ago(post_in_unix):
    current_time = datetime.datetime.now(datetime.timezone.utc)
    reddit_post_time = post_in_unix
    timedd = (current_time.timestamp() - reddit_post_time)
    return math.trunc(timedd/60)
