import unittest
from src.sample.RandomUser import RandomUser
from hamcrest import *


class TestRandomUser(unittest.TestCase):
    def setUp(self):
        self.user = RandomUser()

    def test_get_random_user_is_dict(self):
        res = self.user.get_random_user()
        assert_that(res, instance_of(dict))

    def test_get_multiple_users_is_proper_length_and_contains_dictionaries(self):
        res = self.user.get_multiple_users(3)
        assert_that(res, all_of(has_length(3), only_contains(instance_of(dict))))

    def test_get_multiple_users_number_not_an_int(self):
        assert_that(calling(self.user.get_multiple_users).with_args('Asdsa'),
                    raises(TypeError))

    def test_get_random_male_user_gender_is_male(self):
        res = self.user.get_random_male_user()
        assert_that(res, has_entries({'gender': 'male'}))

    def tearDown(self):
        self.user = None
