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

def get_user_posts(influencer_id):
    user_posts = []
    is_finished = false
    end_cursor = ""
    while is_finished == false:
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
    posts_dataframe = []
    return posts_dataframe


def main():
    influencers_handles = ['herdisathena', 'mathilde_roien', 'Josefinehj', 'Birtahlin', 'Katarinakrebs', 'Kristinetrinkjaer',
                        'Chloemonchamp', 'Emiliemalou', 'Emmamoldt', 'Barbaraegholm', 'Annasarlvit' 'Filippajuhler', 'Karla_alajdi',
                         'Ellakarberg', 'Annakatrinkafehr', 'Annabjorkjohansson', 'Pernilleteisbaek', 'Emilisindlev', 'Madsdamind',
                         'Simonenoa', 'Mathildegoehler', 'Sarahdahll', 'Tommyleewinkworth', 'kennethnguyen']
    influencers_ids = get_influencers_user_ids(influencers_handles)
    for influencer in influencers_ids:
        user_posts = get_user_posts(influencer)   #user_posts is of type List<instagram_post>
        add_posts_to_dataframe(user_posts)


if __name__ == "__main__":
    main()