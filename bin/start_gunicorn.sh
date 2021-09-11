#!/bin/bash
exec gunicorn  -c "/home/linux/github/MoCertsMe/MoCerts/gunicorn_config.py" MoCerts.wsgi