from extensions.db import db
from datetime import datetime

class Delivery(db.Model):
    __tablename__ = "deliveries"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    pickup_time = db.Column(db.DateTime)
    delivered_time = db.Column(db.DateTime)

    pickup_photo = db.Column(db.String(255))      # path or URL
    delivered_photo = db.Column(db.String(255))   # path or URL

    current_lat = db.Column(db.Float)  # GPS tracking
    current_lng = db.Column(db.Float)
    estimated_delivery_time = db.Column(db.DateTime)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
