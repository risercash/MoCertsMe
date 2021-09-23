#!/bin/bash
source /home/linux/github/MoCertsMe/venv/bin/activate
exec gunicorn  -c "/home/linux/github/MoCertsMe/MoCerts/gunicorn_config.py" MoCerts.wsgi