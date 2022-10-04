from gendiff.get_data import get_data
from operator import itemgetter


def generate_diff(file_path1, file_path2):
    result = []
    s1 = get_data(file_path1)
    s2 = get_data(file_path2)
    unic_keys = s1.keys() | s2.keys()
    for key in unic_keys:
        if key in s1 and key in s2:
            if s1.get(key) == s2.get(key):
                values = s1.get(key)
                result.append({'name': key, 'value': '   ' + key + ': ' + str(values)})
            else:
                values = s1.get(key)
                values2 = s2.get(key)
                result.append({'name': key, 'value': ' - ' + key + ': ' + str(values)})
                result.append({'name': key, 'value': ' + ' + key + ': ' + str(values2)})
        elif key in s1:
            values = s1.get(key)
            result.append({'name': key, 'value': ' - ' + key + ': ' + str(values)})
        else:
            values2 = s2.get(key)
            result.append({'name': key, 'value': ' + ' + key + ': ' + str(values2)})

    result.sort(key=itemgetter('name'))
    res = [dct['value'].lower() for dct in result]

    return '{\n' + '\n'.join(res) + '\n}'
