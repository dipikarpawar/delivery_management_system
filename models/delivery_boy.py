from extensions.db import db
from datetime import datetime

class DeliveryBoy(db.Model):
    __tablename__ = "delivery_boys"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, unique=True)
    
    status = db.Column(db.String(20), default="offline")  # available, busy, offline, suspended
    current_lat = db.Column(db.Float)
    current_lng = db.Column(db.Float)
    last_active = db.Column(db.DateTime, default=datetime.utcnow)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship to User
    user = db.relationship("User", backref="delivery_profile", uselist=False)
