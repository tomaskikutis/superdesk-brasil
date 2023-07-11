#!/usr/bin/env python
# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013, 2014, 2015 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license

import os
from flask import json
from pathlib import Path


def env(variable, fallback_value=None):
    env_value = os.environ.get(variable, '')
    if len(env_value) == 0:
        return fallback_value
    else:
        if env_value == "__EMPTY__":
            return ''
        else:
            return env_value


ABS_PATH = str(Path(__file__).resolve().parent)

init_data = Path(ABS_PATH) / 'data'
if init_data.exists():
    INIT_DATA_PATH = init_data

INSTALLED_APPS = [
    "apps.languages"
]

RENDITIONS = {
    'picture': {
        'thumbnail': {'width': 220, 'height': 120},
        'viewImage': {'width': 640, 'height': 640},
        'baseImage': {'width': 1400, 'height': 1400},
    },
    'avatar': {
        'thumbnail': {'width': 60, 'height': 60},
        'viewImage': {'width': 200, 'height': 200},
    }
}

WS_HOST = env('WSHOST', '0.0.0.0')
WS_PORT = env('WSPORT', '5100')

LOG_CONFIG_FILE = env('LOG_CONFIG_FILE', 'logging_config.yml')

REDIS_URL = env('REDIS_URL', 'redis://localhost:6379')
if env('REDIS_PORT'):
    REDIS_URL = env('REDIS_PORT').replace('tcp:', 'redis:')
BROKER_URL = env('CELERY_BROKER_URL', REDIS_URL)

PUBLISH_ASSOCIATED_ITEMS = True

CONTENT_EXPIRY_MINUTES = 60 * 24 * 7  # 1w
PUBLISHED_CONTENT_EXPIRY_MINUTES = 60 * 24 * 30
AUDIT_EXPIRY_MINUTES = PUBLISHED_CONTENT_EXPIRY_MINUTES
CONTENT_API_EXPIRY_DAYS = 15

with open(os.path.join(os.path.dirname(__file__), 'picture-profile.json')) as profile_json:
    picture_profile = json.load(profile_json)

EDITOR = {
    "picture": picture_profile['editor'],
}

SCHEMA = {
    "picture": picture_profile['schema'],
}

# media required fields
VALIDATOR_MEDIA_METADATA = {
    "headline": {
        "required": False,
    },
    "alt_text": {
        "required": False,
    },
    "archive_description": {
        "required": False,
    },
    "description_text": {
        "required": False,
    },
    "copyrightholder": {
        "required": False,
    },
    "byline": {
        "required": False,
    },
    "usageterms": {
        "required": False,
    },
    "copyrightnotice": {
        "required": False,
    },

}

PUBLISH_QUEUE_EXPIRY_MINUTES = 60 * 24 * 15  # 15d
