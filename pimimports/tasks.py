from __future__ import absolute_import
import yaml
from pimimports.celery import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@app.task
def play_all():
    stream = file('imports.yaml', 'r')
    imports = yaml.load(stream)
    while imports:
        key, value = imports.popitem()
        imports = play_import(key, value, imports)
    return True

def play_import(key, value, imports):
    play_one.apply_async(('produit',), link=[play_one.si('cat'), play_one.si('pneu')])
    return imports

@app.task
def play_one(name):
    logger.info(name)
