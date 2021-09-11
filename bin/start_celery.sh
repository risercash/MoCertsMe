#!/bin/bash
cd /home/linux/github/MoCertsMe/MoCerts
exec celery -A MoCerts worker -l INFO