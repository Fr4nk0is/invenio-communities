# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from flask import current_app

from invenio_pidstore.providers.base import BaseProvider
from invenio_pidstore.models import PIDStatus

def comid_minter(record_uuid, data):
    """Mint record identifiers with RecordIDProviderV2.
    This minter is recommended to be used when creating records to get
    PersistentIdentifier with ``object_type='rec'`` and the new random
    alphanumeric `pid_value`.
    Raises ``AssertionError`` if a ``PIDSTORE_RECID_FIELD`` entry is already in
    ``data``. The minted ``pid_value`` will be stored in that field.
    :param record_uuid: The object UUID of the record.
    :param data: The record metadata.
    :returns: A fresh `invenio_pidstore.models.PersistentIdentifier` instance.
    """
    pid_field = current_app.config['COMMUNITIES_PIDSTORE_COMID_FIELD']
    assert pid_field in data
    provider = BaseProvider.create(
        object_type='com', object_uuid=record_uuid, pid_value=data[pid_field],
        status=PIDStatus.REGISTERED, pid_type='comid')
    return provider.pid
