from datetime import datetime

import sqlalchemy as sa


class Timestamp(object):
    created_at = sa.Column(sa.DateTime, default=datetime.utcnow)
    updated_at = sa.Column(sa.DateTime, onupdate=datetime.utcnow)
