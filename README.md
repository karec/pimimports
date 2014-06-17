# PIM Celery-imports #

## Introduction ##

This project has for goal to allow you to configure your imports in queue mod, always waiting for somes to end for pass to the other

At the same time, imports that do not required any other imports will be lunch in other worker

## Installation ##


```
#!sh

pip install -r requirements.txt
```

## Configure your application ##

You can configure the application for your need, you only add to update the file 


```
#!sh

pimimports/celery.py
```

For more information about the configuration, please refer to the [celery docs](http://celery.readthedocs.org/en/latest/configuration.html)

