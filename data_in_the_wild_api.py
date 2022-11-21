import requests

import pandas as pd
from pathlib import Path
from datetime import datetime
import time

influencer_post_id = 1


class instagram_post:
    def __init__(self, url, date_time, caption, likes, user_id, insta_handle, post_id):
        self.url = url
        self.date_time = date_time
        self.caption = caption
        self.likes = likes
        self.user_id = user_id
        self.insta_handle = insta_handle
        self.post_id = post_id

    def __str__(self):
        return f"url: {self.url}, date_time: {self.date_time}, caption: {self.caption}, likes: {self.likes}"


class influencer:
    def __init__(self, name, user_id, insta_handle, follow_count):
        self.name = name
        self.user_id = user_id
        self.insta_handle = insta_handle
        self.follow_count = follow_count


def get_influencers_user_ids(influencers):
    # https://www.instagram.com/web/search/topsearch/?query=<username>
    # influencers = [inf.lower() for inf in influencers]
    influencers_ids = [202803290, 342594072, 2193977, 43561023713, 14592268, 447499606, 54517270, 228768371, 622407402,
                       5780713, 25983225, 328945925, 54013717, 7933735, ]

    # response = requests.request("GET", url)

    return influencers_ids


def get_influencers_user_ids(influencers):
    print("Fetching user ids, it will take a few seconds...")
    base = "https://instagram188.p.rapidapi.com/userid/"

    influencers_ids = []
    #influencers_ids = [202803290, 342594072, 2193977, 43561023713, 14592268, 447499606, 54517270, 228768371, 622407402, 5780713, 25983225, 328945925, 54013717, 7933735,]
    headers = {
        "X-RapidAPI-Key": "6b130ce03bmshe9b1c5345b5fd64p151030jsn429f30217f89",
	    "X-RapidAPI-Host": "instagram188.p.rapidapi.com"}
    
    for influencer in influencers:
        url = base + influencer
        response = requests.request("GET", url, headers=headers).json()
        influencers_ids.append(response["data"])
        print(response["data"])
        time.sleep(1)
    
    print("Yay, i am finished!")
    return influencers_ids


def get_user_posts(influencer_id):
    print("starting getting user posts")
    user_posts = []
    is_finished = False
    end_cursor = ""
    influencer = get_user_contact_info(influencer_id)

    while is_finished == False:
        posts, is_finished, end_cursor = get_user_posts_from_api(end_cursor, influencer_id)
        for item in posts:
            print("adding a post to list")
            user_posts.append(item)
        is_finished = True
    print("after getting user posts")
    return user_posts, influencer

def get_user_contact_info(influencer_id):
    print("start to get contact info")
    url = "https://instagram188.p.rapidapi.com/usercontact/" + str(influencer_id)

    headers = {
        "X-RapidAPI-Key": "6b130ce03bmshe9b1c5345b5fd64p151030jsn429f30217f89",
        "X-RapidAPI-Host": "instagram188.p.rapidapi.com"
    }
    time.sleep(2)
    response = requests.request("GET", url, headers=headers)
    response_dict = response.json()
    print(response_dict)
    user = response_dict.get('data').get('user')
    user_name = user.get('username')
    full_name = user.get('full_name')
    follower_count = user.get('follower_count')
    current_influencer = influencer(full_name, influencer_id, user_name, follower_count)
    print("after getting contact info")
    return current_influencer

def get_user_posts_from_api(end_cursor, user_id):
    print("start getting posts from api")
    ending = end_cursor
    if (not end_cursor):
        ending = "%7Bend_cursor%7D"
    url = "https://instagram188.p.rapidapi.com/userpost/" + str(user_id) + "/50/" + str(ending)

    headers = {
        "X-RapidAPI-Key": "6b130ce03bmshe9b1c5345b5fd64p151030jsn429f30217f89",
        "X-RapidAPI-Host": "instagram188.p.rapidapi.com"
    }
    time.sleep(2)
    response = requests.request("GET", url, headers=headers)
    responce_dict = response.json()
    posts, end_cursor = retrieve_information_needed(responce_dict, user_id)
    print("after getting post cycle")
    return posts, False, end_cursor


def retrieve_information_needed(responce_dict, user_id):
    print("starting to get info needed about posts from request")
    ig_posts = responce_dict.get('data').get('edges')
    end_cursor = responce_dict.get('data').get('end_cursor')
    short_codes = []
    posts = []
    for post in ig_posts:
        short_codes.append(post.get('node').get('shortcode'))
    #for sc in short_codes:
    #    post = get_single_post_info(sc, user_id)
    #    posts.append(post)
    post = get_single_post_info(short_codes[1], user_id)
    posts.append(post)
    end_cursor = ""
    print("finished getting info about posts from request")
    return posts, end_cursor


def get_single_post_info(short_code, user_id):
    print("start getting single post info from request")
    url = "https://instagram188.p.rapidapi.com/postinfo/" + short_code

    headers = {
        "X-RapidAPI-Key": "6b130ce03bmshe9b1c5345b5fd64p151030jsn429f30217f89",
        "X-RapidAPI-Host": "instagram188.p.rapidapi.com"
    }
    time.sleep(2)
    global influencer_post_id
    response = requests.request("GET", url, headers=headers)
    response_dict = response.json()
    print("got response")
    data = response_dict.get('data')
    if data is None:
        return None
    media_type = data.get('media_type')
    if media_type != 1:
        return None
    url = data.get('image_versions2').get('candidates')[0].get('url')
    likes = data.get('like_count')
    caption = data.get('image_versions2').get('caption')
    if caption is None:
        caption = ""
    else:
        caption = caption
    post_id = influencer_post_id
    date_time = datetime.fromtimestamp(data.get('taken_at'))
    print(date_time)
    influencer_post_id += 1
    user_id = user_id
    ig_post = instagram_post(url, date_time, caption, likes, user_id, "harpa96", post_id)
    print(ig_post)
    print("ended getting single post info")
    return ig_post

def add_posts_to_dataframe(posts):
    posts_list = []
    posts_dataframe = pd.DataFrame()

    cols = ['url', 'date_time', 'caption', 'likes', 'user_id', 'insta_handle']

    for post in posts:
        posts_list.append(post)

    posts_dataframe = pd.DataFrame(posts_list, columns=cols)


    filepath = Path('data.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    posts_dataframe.to_csv(filepath)


def main():
    demo_user_id = 177682273
    posts, influencer_info = get_user_posts(demo_user_id)
    result_dataframe = add_posts_to_dataframe(posts)

    #influencers_handles = ['herdisathena', 'mathilde_roien', 'Josefinehj', 'Birtahlin', 'Katarinakrebs',
    #                       'Kristinetrinkjaer',
    #                       'Chloemonchamp', 'Emiliemalou', 'Emmamoldt', 'Barbaraegholm', 'Annasarlvit', 'Filippajuhler',
    #                       'Karla_alajdi',
    #                       'Ellakarberg', 'Annakatrinkafehr', 'Annabjorkjohansson', 'Pernilleteisbaek', 'Emilisindlev',
    #                       'Madsdamind',
    #                       'Simonenoa', 'Mathildegoehler', 'Sarahdahll', 'Tommyleewinkworth', 'kennethnguyen']
    #influencers_ids = get_influencers_user_ids(influencers_handles)
    #for influencer in influencers_ids:
    #    user_posts = get_user_posts(influencer)  # user_posts is of type List<instagram_post>
    #    add_posts_to_dataframe(user_posts)


if __name__ == "__main__":
    main()






























