import sqlite3
import time

from common_config import *


def get_db_keys():
    return ['name', 'uptime', 'up', 'https_score', 'https_rank', 'ipv6', 'openRegistrations', 'users', 'statuses',
            'connections']


def create_db():
    """ Check if DB exists and the tables are there. Create it if not found. """

    database_file = get_config('local_db_file_name')
    connection = sqlite3.connect(database=database_file)
    cursor = connection.cursor()

    # Sample data:
    # {'name': 'mastodon.social', 'uptime': 99.43823093815433, 'up': True, 'https_score': 60, 'https_rank': 'B',
    #  'ipv6': False, 'openRegistrations': False, 'users': 47254, 'statuses': 1261466, 'connections': 1273}

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS mastodon_users (`name`, `up_time`, `up`, `https_score`'
        ', `https_rank`, `ipv6`, `open_registrations`, `users`, `statuses`,'
        '`connections`, `timestamp`)')

    connection.commit()
    connection.close()


def insert_instance_metadata_in_db(name, up_time, up, https_score, https_rank, ipv6, open_registrations, users,
                                   statuses,
                                   connections):
    """ Insert values in database """

    database_file = get_config('local_db_file_name')
    connection = sqlite3.connect(database=database_file)
    cursor = connection.cursor()

    cursor.execute('INSERT INTO mastodon_users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   [name, up_time, up, https_score, https_rank, ipv6, open_registrations, users, statuses, connections,
                    int(time.time())])

    connection.commit()
    connection.close()
