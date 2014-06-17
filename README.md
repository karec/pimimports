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

You can configure the application for your need, you only need to update the file 


```
#!sh

pimimports/celery.py
```

For more information about the app configuration, please refer to the [celery docs](http://celery.readthedocs.org/en/latest/configuration.html)

You also need to update your PIM_PATH config in the file


```
#!sh

pimimports/settings.py
```

This file only contains two settings :


```
#!python

PIM_ABS_PATH = '/home/evalette/Projets/FeuVert-PIM'
PHP_PATH = 'php'
```

Obviously you can use the os module to set your path, the script will only use this string to start jobs
