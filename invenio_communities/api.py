# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Records API."""

from __future__ import absolute_import, print_function

from invenio_db import db
from invenio_records.api import Record

from .models import Community as CommunityModel

class Community(Record):
    """Custom record."""

    model_cls = CommunityModel

    schema = 'dasdasdas' or config
