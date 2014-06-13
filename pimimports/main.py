import yaml
from tasks import play_all


stream = file('imports.yaml', 'r')
imports = yaml.load(stream)


if __name__ == '__main__':
    play_all.delay(imports)
