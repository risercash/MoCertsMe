#!/bin/bash
source /home/linux/github/MoCertsMe/venv/bin/activate
cd /home/linux/github/MoCertsMe/MoCerts
exec celery -A MoCerts worker -l INFO