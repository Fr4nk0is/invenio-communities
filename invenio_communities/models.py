from invenio_records.models import RecordMetadata


class Community(RecordMetadata):
    """Represent a community."""

    __tablename__ = 'community_metadata'
    __versioned__ = {'versioning': False}
