import locale

from common_network import *
from common_db import *

locale.setlocale(locale.LC_ALL, 'en_US')
data = get_mastodon_data_json()

create_db()
keys = get_db_keys()

for item in data:

    for key in keys:

        if ~(key in item):
            item[key] = None

    insert_instance_metadata_in_db(name=item['name'], up_time=item['uptime'], up=item['up'],
                                   https_score=item['https_score'],
                                   https_rank=item['https_rank'], ipv6=item['ipv6'],
                                   open_registrations=item['openRegistrations'],
                                   users=item['users'], statuses=item['statuses'], connections=item['connections'])
