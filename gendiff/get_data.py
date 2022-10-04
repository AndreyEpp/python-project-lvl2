import json
import yaml
import os


def get_data(file):
    basedir_file = os.path.abspath(file)
    if file.endswith('yaml') or file.endswith('yml'):
        with open(basedir_file, 'r') as f1:
            data_file = yaml.safe_load(f1)
            return data_file

    if file.endswith('json'):
        with open(basedir_file, "r", encoding='utf-8') as f1:
            data_file = json.load(f1)
            return data_file
