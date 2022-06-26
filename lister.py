import os
import json

arr = []
types = []
fintypes = []


def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path, x)) for x in os.listdir
        (path)]
    else:
        d['type'] = "file"
        mainDir = path.replace("\\", "/")[1:]
        obj = {'type': mainDir.split('/')[2], 'path': 'assets/data' + path.replace("\\", "/")[1:]}
        arr.append(obj)
        if mainDir.split('/')[2] not in types:
            types.append(mainDir.split('/')[2])
    return d


with open('projects.json', 'w') as outfile:
    path_to_dict('./projects')

    for type in types:
        fintypes.append({'label': type, 'value': type})
    outfile.write(json.dumps({'types': fintypes, 'files': arr}))
