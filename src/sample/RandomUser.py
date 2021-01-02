import requests

class RandomUser:
    def __init__(self):
        self.url = "https://randomuser.me/api/"

    def get_random_user(self):
        r = requests.get(self.url)
        return r.json()['results'][0]

    def get_multiple_users(self, number):
        if type(number) != int:
            raise TypeError("Number of users must be an integer")
        params = {'results': number}
        r = requests.get(self.url, params=params)
        return r.json()['results']

    def get_random_male_user(self):
        params = {'gender': 'male'}
        r = requests.get(self.url, params=params)
        return r.json()['results'][0]

# u = RandomUser()
# print(u.get_random_user())