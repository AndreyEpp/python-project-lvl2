import json, os
from operator import itemgetter


def generate_diff(file_path1, file_path2):
    result = []
    basedir_f1 = os.path.abspath('..' + '/' + '/python-project-lvl2/tests/fixtures/' + file_path1)
    basedir_f2 = os.path.abspath('..' + '/' + '/python-project-lvl2/tests/fixtures/' + file_path2)
    with open(basedir_f1, "r", encoding='utf-8') as source1, \
         open(basedir_f2, "r", encoding='utf-8') as source2:
        s1 = json.load(source1)
        s2 = json.load(source2)
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

