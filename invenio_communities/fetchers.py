from __future__ import absolute_import, print_function

from collections import namedtuple

from flask import current_app


FetchedPID = namedtuple('FetchedPID', ['provider', 'pid_type', 'pid_value'])
"""A pid fetcher."""


def comid_fetcher(record_uuid, data):
    """Fetch a record's identifiers.
    :param record_uuid: The record UUID.
    :param data: The record metadata.
    :returns: A :data:`invenio_pidstore.fetchers.FetchedPID` instance.
    """
    pid_field = current_app.config['COMMUNITIES_PIDSTORE_COMID_FIELD']
    return FetchedPID(
        provider=None,
        pid_type='comid',
        pid_value=data[pid_field]
    )
