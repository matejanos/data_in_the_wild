import requests
import time
import pandas as pd
from pathlib import Path

class instagram_post:
    def __init__(self, url, date_time, caption, likes, user_id, insta_handle, post_id):
        self.url = url,
        self.date_time = date_time,
        self.caption = caption,
        self.likes = likes,
        self.user_id = user_id,
        self.insta_handle = insta_handle,
        self.post_id = post_id

class influencer:
    def __init__(self, name, user_id, insta_handle, follow_count):
        self.name = name,
        self.user_id = user_id,
        self.insta_handle = insta_handle,
        self.follow_count = follow_count

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
    user_posts = []
    is_finished = False
    end_cursor = ""
    while not is_finished:
        posts, is_finished, end_cursor = get_user_posts_from_api(end_cursor, user_id)
        user_posts.append(posts)
    return user_posts

def get_user_posts_from_api(end_cursor, user_id):
    url = "https://instagram188.p.rapidapi.com/userpost/25025320/50/%7Bend_cursor%7D"

    headers = {
        "X-RapidAPI-Key": "6b130ce03bmshe9b1c5345b5fd64p151030jsn429f30217f89",
        "X-RapidAPI-Host": "instagram188.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    posts = retrieve_information_needed(response.text)
    return end_date, posts

def retrieve_information_needed(response_text):
    posts = []
    # appending instances to list
    posts.append(instagram_post(url, date_time, caption, likes, user_id, insta_handle, post_id))
    return posts

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
    influencers_handles = ['herdisathena', 'mathilde_roien', 'Josefinehj', 'Birtahlin', 'Katarinakrebs', 'Kristinetrinkjaer',
                        'Chloemonchamp', 'Emiliemalou', 'Emmamoldt', 'Barbaraegholm', 'Annasarlvit', 'Filippajuhler', 'Karla_alajdi',
                         'Ellakarberg', 'Annakatinkafehr', 'Annabjorkjohansson', 'Pernilleteisbaek', 'Emilisindlev', 'Madsdamind',
                         'Simonenoa', 'Mathildegoehler', 'Sarahdahll', 'Tommyleewinkworth', 'kennethnguyen']
    influencers_ids = get_influencers_user_ids(influencers_handles)
    print(influencers_ids)
    for influencer in influencers_ids:
        user_posts = get_user_posts(influencer)   #user_posts is of type List<instagram_post>
        add_posts_to_dataframe(user_posts)

if __name__ == "__main__":
    main()