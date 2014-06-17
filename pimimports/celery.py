from __future__ import absolute_import

from celery import Celery

app = Celery('pimimports',
             broker='amqp://',
             backend='amqp://',
             include=['pimimports.tasks'])

if __name__ == '__main__':
    app.start()
