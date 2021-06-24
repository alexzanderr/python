
import json
import requests

tinder_api_url = "https://api.gotinder.com"
headers = {
    'app_version': '6.9.4',
    'platform': 'ios',
    'content-type': 'application/json',
    'User-agent': 'Tinder/7.5.3 (iPohone; iOS 10.3.2; Scale/2.00)',
    'X-Auth-Token': "0314982b-a879-4b7a-92ac-b0f0661413f8",
}

def tinder_get(controller: str):
    complete_url = tinder_api_url + controller
    r = requests.get(complete_url, headers=headers)
    return r.json()

def tinder_post(controller: str, tinder_post_data):
    complete_url = tinder_api_url + controller
    r = requests.post(
        complete_url,
        headers=headers,
        data=json.dumps(tinder_post_data))
    return r.json()

def tinder_delete(controller: str):
    complete_url = tinder_api_url + controller
    r = requests.delete(complete_url, headers)
    return r

def tinder_put(controller: str, put_data):
    complete_url = tinder_api_url + controller
    r = requests.put(
        complete_url,
        headers=headers,
        data=json.dumps(put_data)
    )
    return r

from TinderAPIX import user as u

class Session:
    def __init__(self, xauth_token):
        self.xauth_token = xauth_token

        # headers is created every session because xauth token
        # changes very frequently
        global headers
        headers["X-Auth-Token"] = self.xauth_token

        self.id = tinder_get("/profile")["_id"]
        self.data = tinder_get('/profile')
        self.meta = tinder_get('/meta')
        self.metav2 = tinder_get('/v2/meta')

    def get_id(self):
        return tinder_get("/profile")["_id"]

    def me(self):
        """Returns a UserModel() for the Session"""
        return u.UserController(tinder_get('/profile')['_id']).get_user()

    def yield_users(self):
        """Returns a generator of nearby users as NormalUser()"""
        while True:
            resp = tinder_get('/user/recs')
            recs = resp['results'] if 'results' in resp else []
            for rec in recs:
                yield u.UserController(rec['_id'], self.xauth_token).get_user()

    def yield_usersv2(self):
        """Returns a generator of nearby users as NormalUser() and calculates location"""
        while True:
            resp = tinder_get('/v2/recs/core?locale=en-US')
            recs = resp['data']['results'] if 'data' in resp else []
            for rec in recs:
                if rec['type'] == 'user':
                    yield u.UserController(rec['user']['_id'], self.xauth_token).get_user()

    def yield_matches(self):
        """Returns a generator of matches as MatchUsers()"""
        resp = tinder_post('/updates', {"last_activity_date": ""})
        for match in reversed(resp['matches']):
            yield u.UserController(match['_id'], self.xauth_token).get_user()

    def list_matches(self):
        """Returns a [] of matches"""
        return tinder_post('/updates', {"last_activity_date": ""})['matches']

    def get_updates(self, date=''):
        """Returns the profile 'updates' since date
        Date formatting is specific:
            date = '2017-03-25T20:58:00.404z"
            if date='' then returns updates since profile was made
        """
        return tinder_post('/updates', {"last_activity_date": date})

    def update_profile(self, **kwargs):
        """Updates the session profile
        Kwargs - not all are known, type specific (int, str, dict, bool):
            age_filter_min=20
            age_filter_max=30
            bio='new bio who dis'
            distance_filter=100
            discoverable=true
            gender=1 <- seeking females
            {"photo_optimizer_enabled":false}
        """
        try:
            return tinder_post('/profile', kwargs)
        except Exception as e:
            print('Error in updating profile: ', e)

    def change_location(self, lat, lon):
        """Changes the session user's location for Tinder+"""
        resp = tinder_post('/passport/user/travel', {"lat": lat, "lon": lon})
        if 'error' in resp:
            return "Could not change location. Remeber +-=NS_lat and +-=EW_lon"
        return resp

    def reset_location(self):
        """Resets the session user's location to original location for Tinder+"""
        resp = tinder_post('/passport/user/reset', {})
        if 'error' in resp:
            return "Could not change location. Are you a tinder+ user?"
        return resp

    def change_username(self, uname):
        """Changes the session user's username. Not the same as Name"""
        if len(uname) > 20:
            return "Username max length = 20"
        resp = tinder_put(url, {"username": uname})
        if 'error' in resp.json():
            return resp.json()['error']
        else:
            return 'Username Updated'

    def reset_username(self):
        """Resets the session user's username"""
        return tinder_delete('/profile/username')

    def trending_gifs(self, limit=3):
        """Returns the trending gifs based on limit=int(amount)"""
        return tinder_get('/giphy/trending?limit={}'.format(limit))

    def search_gifs(self, query, limit=3):
        """Returns the limit=int(amount) of gifs based on the query -> see giphy docs"""
        return tinder_get('/giphy/search?limit={}&query={}'.format(limit, query))

    def fast_match_count(self):
        """Returns the number of like's the session user has received"""
        return tinder_get('/v2/fast-match/count')['data']['count']

    def fast_match_img(self):
        """Returns the blurred image thumbnails of users in fast-match, TinderGold"""
        return requests.get('/v2/fast-match/preview', headers=headers).content