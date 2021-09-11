#!/bin/bash
cd /home/linux/github/MoCertsMe/MoCerts
celery -A MoCerts worker -l INFO