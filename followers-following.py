'''
This program returns the usernames of the people who you follow but don't follow you back on IG
(yeah they are big celebs na)
note: it will not return the users who are verified
    to get the followers and following used IGimport chrome extension

not sure if fool proof
'''

import pandas as pd
import os
from dotenv import load_dotenv
from automation_part import InstaHandle


username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

followers_file_path = os.getenv('FOLLOWERS_FILE')
following_file_path = os.getenv('FOLLOWING_FILE')

def remove_verified_user():
    for not_follower in not_followers:
        t=following_df.loc[following_df['User ID'] == not_follower]["Is verified"]
        if t.values[0]=='YES':
            not_followers.remove(not_follower) 

followers = pd.read_csv(followers_file_path)
followers_df = pd.DataFrame(followers)
followers_id = followers_df["User ID"].values.tolist()


following = pd.read_csv(following_file_path)
following_df = pd.DataFrame(following)
following_id = following_df["User ID"].values.tolist()


not_followers = []
for me_following in following_id:
    if me_following not in followers_id:
        not_followers.append(me_following)

remove_verified_user()

not_followers_names = []
for not_follower in not_followers:
    t = following_df.loc[following_df['User ID'] == not_follower]["Username"]
    not_followers_names.append(t.values[0])
    
print(not_followers_names)

if(not_followers_names):
    handler = InstaHandle()
    handler.login_to_ig(username, password)
    handler.dont_save_info()
    handler.turn_off_notifications()

    for poser in not_followers_names:
        handler.search_user(poser)
        handler.follow()



