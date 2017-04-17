# Playing with Mastodon
A collection of helpful utilities for doing things with Mastodon. If you don't know what Mastodon is, [check it out](https://mastodon.technology/).

# How To Run
You can just run the files that begin with `do-`. For example:
- `do-save-instance-metadata`: Run this file, and it will download the instance metadata, like user count and server count, from `instances.json` and save it to a local SqLite database called `data.db`. You can change the database name in `common_db.py`.