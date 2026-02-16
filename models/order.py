from extensions.db import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"), nullable=False)
    delivery_boy_id = db.Column(db.Integer, db.ForeignKey("delivery_boys.id"), nullable=True)


    status = db.Column(db.String(20), nullable=False, default="ready_for_pickup")
    total_amount = db.Column(db.Float, nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship - delivery
    delivery = db.relationship("Delivery", backref="order", uselist=False)
    
