import os

import biothings, config
biothings.config_for_app(config)
from config import DATA_ARCHIVE_ROOT

import biothings.hub.dataload.dumper


class AnnouncementDumper(biothings.hub.dataload.dumper.DummyDumper):

    SRC_NAME = "covid19_announcements"
    __metadata__ = {
        "src_meta": {
            "author":{
                "name": "Ginger Tsueng",
                "url": "https://github.com/gtsueng"
            },
            "code":{
                "branch": "main",
                "repo": "https://github.com/gtsueng/announceTest.git"
            },
            "url": "https://github.com/gtsueng/announceTest",
            "license": "http://creativecommons.org/licenses/by-nc-sa/4.0/"
        }
    }
    # override in subclass accordingly
    SRC_ROOT_FOLDER = os.path.join(DATA_ARCHIVE_ROOT, SRC_NAME)
    
    SCHEDULE = None #"15 14 * * 1"  # mondays at 14:15UTC/7:15PT
