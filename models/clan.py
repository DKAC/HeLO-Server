"""
first level class
"""

import json
from datetime import datetime

from database.db import db, CustomQuerySet


class Clan(db.Document):
    # e.g. StDb for Stoßtrupp Donnerbalken
    tag = db.StringField(required=True, unique=True, max_length=10)
    # full name
    name = db.StringField()
    # discord icon flag, e.g. :flag_eu:, :flag_de:, ...
    flag = db.StringField()
    # discord invite link to a clan's discord server
    invite = db.StringField()
    # current HeLO Score
    score = db.IntField(default=600)
    # number of games
    num_matches = db.IntField(default=0)
    # confirmation, reserved ??
    conf = db.StringField()
    # alternative tags, if a clan was renamed, reserved
    alt_tags = db.ListField(db.StringField())
    # link to the icon of a clan
    icon = db.StringField(default="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_189144.png&f=1&nofb=1")
    # when the clan was last updated (e.g. the score)
    last_updated = db.DateTimeField(default=datetime.now())
    meta = {
        "indexes": [
            {
                "fields": ["$tag", "$name", "$alt_tags"]
            }
        ],
        "queryset_class": CustomQuerySet
    }


    def to_dict(self):
        return json.loads(self.to_json())

