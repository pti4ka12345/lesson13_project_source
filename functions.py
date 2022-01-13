import json
import pprint


def read_json(filename):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)


def get_tags(data):
    results = set()

    for record in data:
        content = record['content']
        words = content.split()
        for word in words:
            if word.startswith('#'):
                results.add(word[1:])
    return results


def get_posts_by_tag(data, tag):
    results = []
    for record in data:
        if f'#{tag}' in record['content']:
            results.append(record)
    return results


# pprint.pprint(read_json('posts.json'))
# print(get_tags(read_json('posts.json')))
# pprint.pprint(get_posts_by_tag(read_json('posts.json'), 'пирог'))