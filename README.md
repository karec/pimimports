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

## Using it as daemon ##

You can find in this repo an basic supervisor configuration, but feel free to deamonize the script in an other way. For more information about setting up celery worker as a daemon [here](http://celery.readthedocs.org/en/latest/tutorials/daemonizing.html)

## Configuring logs ##

The default path for the logs is :


```
#!sh

/var/log/celery/
```

you may need to create this folder

## Confirguring exports ##

The file imports.yaml is used for configuration, it's look like this :


```
#!yaml

import_marque:
    name: import_marque
    after: [import_pneu, import_options, import_produits]
import_categories:
    name: import_categories
```

### How it's work ###

You can simply configuring a job by setting up his name. If this job is needed by an other job you simply have to set a property "after" and setting up your job list. Every job in this list will wait for the previous to be ended for start, with this you can easly chainning your imports.
If a job is a standalone job, simply set the name property, it will run in an other process and don't be lock by others job.
The name of the import in the yaml file **must be the job code in your pim**

## Lunch the script ##

When your configuration is set, you juste have to run :



```
#!sh

./main.py
```

Since the script is not blocking you can run it one shot or set it in a crontab