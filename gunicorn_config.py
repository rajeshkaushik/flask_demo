""" Settings added as specified in following link
http://docs.gunicorn.org/en/stable/settings.html
"""

import multiprocessing
from project.instance import config

bind = '{}:{}'.format(config.HOST, config.PORT)
workers = 2 if config.DEBUG else (multiprocessing.cpu_count() * 2) + 1


