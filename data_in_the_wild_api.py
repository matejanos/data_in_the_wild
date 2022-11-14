import requests

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
    influencers_ids = []
    return influencers_ids

def get_user_posts(influencer):
    user_posts = []
    return user_posts

def add_posts_to_dataframe():
    posts_dataframe = []
    return posts_dataframe


def main():
    influencers_handles = []

    influencers_ids = get_influencers_user_ids(influencers_handles)

    for influencer in influencers_ids:
        user_posts = get_user_posts(influencer)
        add_posts_to_dataframe(user_posts)

    #JUST FOR TESTING
    url = "https://instagram188.p.rapidapi.com/userpost/25025320/12/%7Bend_cursor%7D"

    headers = {
        "X-RapidAPI-Key": "6b130ce03bmshe9b1c5345b5fd64p151030jsn429f30217f89",
        "X-RapidAPI-Host": "instagram188.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

if __name__ == "__main__":
    main()