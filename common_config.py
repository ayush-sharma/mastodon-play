def get_config(item):
    config = {'local_db_file_name': 'data.db'}

    if item in config:

        return config[item]
    else:

        return None
