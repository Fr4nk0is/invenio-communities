# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Default configuration."""

from __future__ import absolute_import, print_function

from invenio_indexer.api import RecordIndexer
from invenio_records_rest.facets import terms_filter
from invenio_records_rest.utils import allow_all, check_elasticsearch
from invenio_search import RecordsSearch


COMMUNITIES_PIDSTORE_COMID_FIELD = 'community_id'

#: Records REST API endpoints.
COMMUNITIES_REST_ENDPOINTS = dict(
    comid=dict(
        pid_type='comid',
        pid_minter='comid_minter',
        pid_fetcher='comid_fetcher',
        list_route='/communities/',
        item_route='/communities/<{0}:pid_value>'.format(
            'pid(comid,record_class="invenio_communities.api:Community",'
            'object_type="com")'
        ),
        search_index='communities',
        record_class='invenio_communities.api:Community',
        search_type=['record-v1.0.0'],
        record_serializers={
            'application/json': (
                'invenio_communities.serializers.json_v1_response'),
        },
        search_serializers={
            'application/json': (
                'invenio_communities.serializers:search_responsify'),
        },
        record_loaders={
            'application/json': ('invenio_communities.loaders:json_v1'),
        },
        default_media_type='application/json',
        read_permission_factory_imp=allow_all,
    ),
)
