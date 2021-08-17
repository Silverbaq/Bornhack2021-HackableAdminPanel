from . import db


class HackedBy(db.Model):
    """Data model for user accounts."""
    __tablename__ = 'hacked_by'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    ip = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=False
    )
    country = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=False
    )
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    password = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=False
    )

    def __repr__(self):
        return '<From {}>'.format(self.country)
