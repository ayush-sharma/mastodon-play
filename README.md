# Playing with Mastodon
A collection of helpful utilities for doing things with Mastodon. If you don't know what Mastodon is, [check it out](https://mastodon.technology/).

This project has a pretty simple file structure. The files that start with `do-` do things, and the ones that start with `common_` contain things that are shared between all the `do-` files. You can run the `do-` files directly, or add them to a cronjob.

# Requirements
- `pip install requests`

# How To Run
- `do-save-instance-metadata`: Run this file, and it will download the instance metadata, like user count and server count, from `instances.json` and save it to a local SqLite database called `data.db`. You can change the database name in `common_config.py`.

# Common Files
- `common_config.py`: Contains configuration items.
- `common_db.py`: Contains database functions and commands.
- `common_network.py`: Contains things related to making HTTP calls and working with remote resources.