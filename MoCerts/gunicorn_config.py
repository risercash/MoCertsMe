command = '/root/MoCertsMe/venv/bin/gunicorn'
pythonpath = '/root/MoCertsMe/MoCertsMe/MoCerts'
bind = '0.0.0.0:8001'
workers = 3
user = 'root'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=MoCerts.settings'
