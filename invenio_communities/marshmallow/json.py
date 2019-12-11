from __future__ import absolute_import, print_function
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""JSON Schemas."""


import uuid

from invenio_jsonschemas import current_jsonschemas
from invenio_records_rest.schemas import Nested, StrictKeysMixin
from invenio_records_rest.schemas.fields import DateString, GenFunction, \
    PersistentIdentifier, SanitizedUnicode
from marshmallow import fields, missing, validate

from invenio_communities.api import Community

def schema_from_context(_, context):
    """Get the record's schema from context."""
    record = (context or {}).get('record', {})
    return record.get(
        "_schema",
        current_jsonschemas.path_to_url(Record._schema)
    )

class CommunitySchemaV1(StrictKeysMixin):
    """Schema for the community metadata."""
    # TODO:
    # - required fields? (In both jsonschema and here)
    created = fields.Str(dump_only=True)
    revision = fields.Integer(dump_only=True)
    updated = fields.Str(dump_only=True)
    id = PersistentIdentifier()

    internal_id = fields.UUID(missing=uuid.uuid1, dump_only=True)
    title = SanitizedUnicode(required=True, validate=validate.Length(min=3))
    curation_policy = fields.Str(dump_only=True)
    page = fields.Str(dump_only=True)
    type_ = fields.Str(validate = validate.OneOf([
        'institution/organization',
        'event',
        'topic',
        'project']))
    alternate_identifiers = fields.List(fields.String())
    website = fields.Str(dump_only=True)
    funding = fields.List(fields.String())
    domain_discipline = fields.Str(dump_only=True)
    verified = fields.Boolean()
    visibility = fields.Str(validate =validate.OneOf([
        'public',
        'private',
        'hidden']))
    member_policy = fields.Str(validate =validate.OneOf([
        'open',
        'closed']))
    record_policy = fields.Str(validate =validate.OneOf([
        'open',
        'closed',
        'restricted']))
    archived = fields.Boolean()
    logo = fields.Str()
    _schema = GenFunction(
        attribute="$schema",
        data_key="$schema",
        deserialize=schema_from_context,  # to be added only when loading
    )
