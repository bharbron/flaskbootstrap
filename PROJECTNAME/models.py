import datetime
from flask.ext.login import UserMixin

from sqlalchemy import Column, Integer, Boolean, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base, engine

class User(Base, UserMixin):
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True)
  name = Column(String(128))
  email = Column(String(256), unique=True, nullable=False)
  password = Column(String(128), nullable=False)

  items = relationship("Item", backref="user")

class Item(Base):
	__tablename__ = "items"

	id = Column(Integer, primary_key=True)
	name = Column(String(512), nullable=False)

	user_id = Column(ForeignKey('users.id'), nullable=False)