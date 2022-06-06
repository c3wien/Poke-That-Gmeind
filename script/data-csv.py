import json
import unicodecsv as csv


# see: https://stackoverflow.com/a/28246154
def flatten_json(b, delim):
    val = {}
    for i in b.keys():
        if isinstance(b[i], dict):
            get = flatten_json(b[i], delim)
            for j in get.keys():
                val[i + delim + j] = get[j]
        else:
            val[i] = b[i]
    return val


def json_file_to_csv_file(in_path, out_path):
    f = open(in_path)
    data = json.load(f)

    f = csv.writer(open(out_path, "wb+"))
    first_line = flatten_json(data.get("91501"), '.')
    f.writerow(first_line.keys())

    for line in iter(data.items()):
        line = flatten_json(line[1], '.')
        f.writerow(line.values())


# paths without extension
paths = {
    'luftfilterbegehren/data/cities.json':
    'luftfilterbegehren/static/data/cities.csv'
    }
for in_path, out_path in iter(paths.items()):
    json_file_to_csv_file(in_path, out_path)
