from __future__ import absolute_import
import yaml
from pimimports.celery import app
from celery.utils.log import get_task_logger
from subprocess import call
import os
from pimimports import settings

logger = get_task_logger(__name__)

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
    console_path = os.path.join(settings.PIM_ABS_PATH, 'app/console')
    exec_path = "%s %s akeneo:batch:job %s" % (settings.PHP_PATH, console_path, name)
    logger.info(exec_path)
    call([exec_path], shell=True)
