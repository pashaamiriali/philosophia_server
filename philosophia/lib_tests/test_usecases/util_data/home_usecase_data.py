import json


def get_json_string():
    return json.dumps({
        "user": {
            "username": "me",
            "rooms": [],
            "debates": [],
            "observations": [],
        },

        "rooms": [
            {
                "id": "",
                "name": "My Room",
                "ownerships": [],
                "debates": [],
                "observations": [],
            }
        ],
        "debates": [
            {"id": '',
             'participants': [],
             'topic': "Some Topic",
             'time': 45345624,
             },
                       ],
        'references': [{"id": '',
                        'name': 'Some Book',
                        'links': [],
                        }]

    }, separators=(',', ':')
    )
