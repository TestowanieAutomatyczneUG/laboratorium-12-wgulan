import unittest
from unittest.mock import Mock, patch
from hamcrest import *
from src.sample.RandomUser import RandomUser


class TestRandomUser(unittest.TestCase):
    def setUp(self):
        self.temp = RandomUser()
        self.user = {
            "results": [
                {
                    "gender": "male",
                    "name": {
                        "title": "Mr",
                        "first": "Pablo",
                        "last": "Saez"
                    },
                    "location": {
                        "street": {
                            "number": 6981,
                            "name": "Avenida de Castilla"
                        },
                        "city": "Santiago de Compostela",
                        "state": "Castilla y León",
                        "country": "Spain",
                        "postcode": 80762,
                        "coordinates": {
                            "latitude": "-21.9262",
                            "longitude": "-16.4948"
                        },
                        "timezone": {
                            "offset": "+8:00",
                            "description": "Beijing, Perth, Singapore, Hong Kong"
                        }
                    },
                    "email": "pablo.saez@example.com",
                    "login": {
                        "uuid": "cddb1c5c-d93d-4533-a58d-e4243033925a",
                        "username": "orangesnake909",
                        "password": "free",
                        "salt": "YKnYwmmj",
                        "md5": "8a40dab134ac53ec5ad07cfbd59f10de",
                        "sha1": "191638194e19173e539fd13173d8a0f984231dea",
                        "sha256": "f60ad4b609daf2a447f3fe57854050023c1a963e0be3d7aa4ac806946e91d92d"
                    },
                    "dob": {
                        "date": "1960-07-28T16:30:07.584Z",
                        "age": 60
                    },
                    "registered": {
                        "date": "2005-01-18T08:49:28.399Z",
                        "age": 15
                    },
                    "phone": "910-125-136",
                    "cell": "606-313-497",
                    "id": {
                        "name": "DNI",
                        "value": "95367784-Y"
                    },
                    "picture": {
                        "large": "https://randomuser.me/api/portraits/men/25.jpg",
                        "medium": "https://randomuser.me/api/portraits/med/men/25.jpg",
                        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/25.jpg"
                    },
                    "nat": "ES"
                }
            ],
            "info": {
                "seed": "6ad2b66543410ebe",
                "results": 1,
                "page": 1,
                "version": "1.3"
            }
        }
        self.users = {
            "results": [
                {
                    "gender": "female",
                    "name": {
                        "title": "Mrs",
                        "first": "Clara",
                        "last": "Martin"
                    },
                    "location": {
                        "street": {
                            "number": 706,
                            "name": "Calle de Segovia"
                        },
                        "city": "Talavera de la Reina",
                        "state": "Comunidad Valenciana",
                        "country": "Spain",
                        "postcode": 27808,
                        "coordinates": {
                            "latitude": "-17.3643",
                            "longitude": "134.2421"
                        },
                        "timezone": {
                            "offset": "+8:00",
                            "description": "Beijing, Perth, Singapore, Hong Kong"
                        }
                    },
                    "email": "clara.martin@example.com",
                    "login": {
                        "uuid": "385d19d8-3001-4bb7-b599-df58b9415abc",
                        "username": "organicswan994",
                        "password": "mouse1",
                        "salt": "abfSTBRv",
                        "md5": "d7f79a8955581812172e2e1e32aeafe3",
                        "sha1": "7de1eab31cfa8bcb5071b0c4a267998691888edf",
                        "sha256": "2ab6320198061b826d69889f4a5894a2f10e79405f5ec371c66f3ee0d27f77c1"
                    },
                    "dob": {
                        "date": "1963-10-14T23:27:25.578Z",
                        "age": 57
                    },
                    "registered": {
                        "date": "2011-12-18T15:37:42.677Z",
                        "age": 9
                    },
                    "phone": "962-036-688",
                    "cell": "633-628-590",
                    "id": {
                        "name": "DNI",
                        "value": "92989346-V"
                    },
                    "picture": {
                        "large": "https://randomuser.me/api/portraits/women/67.jpg",
                        "medium": "https://randomuser.me/api/portraits/med/women/67.jpg",
                        "thumbnail": "https://randomuser.me/api/portraits/thumb/women/67.jpg"
                    },
                    "nat": "ES"
                },
                {
                    "gender": "female",
                    "name": {
                        "title": "Ms",
                        "first": "Marjella",
                        "last": "Kronenberg"
                    },
                    "location": {
                        "street": {
                            "number": 4371,
                            "name": "Jan van de Capellelaan"
                        },
                        "city": "Ginnum",
                        "state": "Utrecht",
                        "country": "Netherlands",
                        "postcode": 77755,
                        "coordinates": {
                            "latitude": "66.8684",
                            "longitude": "-37.4150"
                        },
                        "timezone": {
                            "offset": "+9:00",
                            "description": "Tokyo, Seoul, Osaka, Sapporo, Yakutsk"
                        }
                    },
                    "email": "marjella.kronenberg@example.com",
                    "login": {
                        "uuid": "493d8e0f-3fdf-456b-9bd9-6cd6d4cc8b65",
                        "username": "tinymeercat829",
                        "password": "4you",
                        "salt": "FRzvSrea",
                        "md5": "a339b4e6df0906c1b695ec0e58954cfd",
                        "sha1": "8271b0a43e3c7907889b0de39285a4a17c1c3023",
                        "sha256": "cb8b067a0358dd23512233995211df79a0d892a4709dbdcfeddfd18830f8fcd3"
                    },
                    "dob": {
                        "date": "1992-11-02T11:42:49.308Z",
                        "age": 28
                    },
                    "registered": {
                        "date": "2009-05-02T05:28:48.115Z",
                        "age": 11
                    },
                    "phone": "(666)-440-4382",
                    "cell": "(604)-357-2050",
                    "id": {
                        "name": "BSN",
                        "value": "45604461"
                    },
                    "picture": {
                        "large": "https://randomuser.me/api/portraits/women/33.jpg",
                        "medium": "https://randomuser.me/api/portraits/med/women/33.jpg",
                        "thumbnail": "https://randomuser.me/api/portraits/thumb/women/33.jpg"
                    },
                    "nat": "NL"
                },
                {
                    "gender": "female",
                    "name": {
                        "title": "Mrs",
                        "first": "Claraa",
                        "last": "Martin"
                    },
                    "location": {
                        "street": {
                            "number": 706,
                            "name": "Calle de Segovia"
                        },
                        "city": "Talavera de la Reina",
                        "state": "Comunidad Valenciana",
                        "country": "Spain",
                        "postcode": 27808,
                        "coordinates": {
                            "latitude": "-17.3643",
                            "longitude": "134.2421"
                        },
                        "timezone": {
                            "offset": "+8:00",
                            "description": "Beijing, Perth, Singapore, Hong Kong"
                        }
                    },
                    "email": "clara.martin@example.com",
                    "login": {
                        "uuid": "385d19d8-3001-4bb7-b599-df58b9415abc",
                        "username": "organicswan994",
                        "password": "mouse1",
                        "salt": "abfSTBRv",
                        "md5": "d7f79a8955581812172e2e1e32aeafe3",
                        "sha1": "7de1eab31cfa8bcb5071b0c4a267998691888edf",
                        "sha256": "2ab6320198061b826d69889f4a5894a2f10e79405f5ec371c66f3ee0d27f77c1"
                    },
                    "dob": {
                        "date": "1963-10-14T23:27:25.578Z",
                        "age": 57
                    },
                    "registered": {
                        "date": "2011-12-18T15:37:42.677Z",
                        "age": 9
                    },
                    "phone": "962-036-688",
                    "cell": "633-628-590",
                    "id": {
                        "name": "DNI",
                        "value": "92989346-V"
                    },
                    "picture": {
                        "large": "https://randomuser.me/api/portraits/women/67.jpg",
                        "medium": "https://randomuser.me/api/portraits/med/women/67.jpg",
                        "thumbnail": "https://randomuser.me/api/portraits/thumb/women/67.jpg"
                    },
                    "nat": "ES"
                }
            ],
            "info": {
                "seed": "732efaa5e5cae3cc",
                "results": 2,
                "page": 1,
                "version": "1.3"
            },

        }

    @patch('src.sample.RandomUser.requests.get')
    def test_get_random_user_is_dict(self, mock_get):
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = self.user
        result = self.temp.get_random_user()
        assert_that(result, instance_of(dict))

    @patch('src.sample.RandomUser.requests.get')
    def test_get_random_user_has_name_field(self, mock_get):
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = self.users
        result = self.temp.get_multiple_users(3)
        assert_that(result, all_of(has_length(3), only_contains(instance_of(dict))))

    @patch('src.sample.RandomUser.RandomUser.get_multiple_users')
    def test_get_multiple_users_number_not_an_int(self, mock_get_multiple_users):
        mock_get_multiple_users.side_effect = TypeError("Number of users must be an integer")
        assert_that(calling(self.temp.get_multiple_users).with_args("asdasd"), raises(TypeError, "Number of users must be an integer"))