Flask Example - MediaCloud Client App
=====================================

Small example Flask applicaton for the MAS.500 course.

Installation
------------

Make sure you havy Python 2.7 (and the pip package manager).

You also need to install some requirements:

```
pip install -r requirements.pip
```

Copy `settings.config.template` to `settings.config` and edit it.

Use
---

Run this command and then visit `localhost:5000` with a web browser

```
python mcserver.py
```

You will be able to monitor progress in the `logs/mcserver.log` log file.

Deploying
---------

First, prep your Ubuntu machine:
```
sudo aptitude install python
sudo aptitude install libapache2-mod-wsgi
sudo pip install -r requirements
```

And make the `logs` folder writable by your web-user (ie. `www-data`).

Now follow the instructions for Configuring Apache:
  http://flask.pocoo.org/docs/deploying/mod_wsgi/

