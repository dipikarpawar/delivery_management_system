from extensions.db import db
from models import User
from extensions.logger import logger
from sqlalchemy.exc import SQLAlchemyError

class UserDao:

    @staticmethod
    def get_by_id(user_id):
        try:
            return User.query.get(user_id)
        except SQLAlchemyError as e:
            logger.error(f"Error fetching user by id {user_id}: {e}")
            return None

    @staticmethod
    def get_by_email(email):
        try:
            return User.query.filter_by(email=email).first()
        except SQLAlchemyError as e:
            logger.error(f"Error fetching user by email {email}: {e}")
            return None

    @staticmethod
    def create_user(username, email, password, role):
        try:
            user = User(username=username, email=email, password=password, role=role)
            db.session.add(user)
            db.session.commit()
            logger.info(f"Created user: {username}")
            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            logger.error(f"Error creating user {username}: {e}")
            return None

    @staticmethod
    def update_user(user_id, **kwargs):
        try:
            user = UserDao.get_by_id(user_id)
            if not user:
                logger.warning(f"User {user_id} not found")
                return None
            for key, value in kwargs.items():
                setattr(user, key, value)
            db.session.commit()
            logger.info(f"Updated user {user_id}")
            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            logger.error(f"Error updating user {user_id}: {e}")
            return None
