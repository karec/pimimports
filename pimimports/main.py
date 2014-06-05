import yaml


stream = file('imports.yaml', 'r')
imports = yaml.load(stream)


def play_import(name, value, imports):
    after = value.get('after', None)
    if after is not None  and after in imports:
        play_import(after, imports.get(after), imports)
    print "playing %s..." % (name)
    if name in imports:
        imports.pop(name)
    return imports

if __name__ == '__main__':
    while imports:
        key, value = imports.popitem()
        imports = play_import(key, value, imports)
