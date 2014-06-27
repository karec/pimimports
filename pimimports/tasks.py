from __future__ import absolute_import
from pimimports.celery import app
from celery.utils.log import get_task_logger
from subprocess import call
import os
from pimimports import settings
from celery import chain

logger = get_task_logger(__name__)


def play_all(jobs):
    """
    This function will add all jobs in the jobs dict to queue
    It will pop all items of the dict
    :param jobs: dict of all jobs to play
    :return: the jobs dict, if all the process is good, it must be empty
    """
    logger.info('start jobs')
    while jobs:
        key, value = jobs.popitem()
        jobs = play_import(key, value, jobs)
    return jobs


def play_import(key, value, jobs):
    """
    This function will play an import.
    If the import has an after key, a chain will be generate and play.
    In other case, it just use the task play_one the start the import, passing the key parameter
    :param key: string key of the job in dict
    :param value: string the value of this key
    :param jobs: dict the whole dictionary
    :return: dict the dictionary jobs
    """
    if value.get('after', None):
        subtasks = list()
        subtasks.append(play_one.si(key))
        for name in value.get('after'):
            subtasks.append(play_one.si(name))
        workflow = chain(*subtasks)
        workflow.delay()
    else:
        play_one.delay(key)
    return jobs


@app.task
def play_one(name):
    """
    This function is used for playing async job.
    It will play one job using user parameters
    :param name: string name of the job
    :return: None
    """
    console_path = os.path.join(settings.PIM_ABS_PATH, 'app/console')
    exec_path = "%s %s akeneo:batch:job %s --env=%s" % (settings.PHP_PATH, console_path, name, settings.ENV)
    logger.info(exec_path)
    call([exec_path], shell=True)
