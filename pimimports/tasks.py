from __future__ import absolute_import
import yaml
from pimimports.celery import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@app.task
def play_all(imports):
    logger.info('start import')
    while imports:
        key, value = imports.popitem()
        imports = play_import(key, value, imports)
    return True

def play_import(key, value, imports):
    if value.get('after', None):
        play_one.apply_async((key,), link=[play_one.si(name) for name in value.get('after')])
    else:
        play_one.delay(key)
    return imports

@app.task
def play_one(name):
    logger.info(name)
