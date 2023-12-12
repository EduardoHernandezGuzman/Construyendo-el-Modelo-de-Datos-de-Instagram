import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er



Base = declarative_base()



class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    user_name =  Column(String(250), nullable=False)
    first_name =  Column(String(250), nullable=False)
    second_name =  Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

  
class Comment(Base):
    __tablename__ = "Comment"
    id = Column(Integer, primary_key=True)
    comment_text =  Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey("User.id"))
    post_id = Column(Integer, ForeignKey("Post.id"))
    comment_relationship = relationship("Post")


class Post(Base):
    __tablename__ = "Post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"))
    post_relationship = relationship("User")


class Media(Base):
    __tablename__ = "Media"
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey("Post.id"))
    post_relationship = relationship("Post")


class Follower(Base):
    __tablename__ = "Follower"
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("User.id"))
    user_to_id = Column(Integer, ForeignKey("User.id"))
    user_relationship_from = relationship("User", foreign_keys=[user_from_id])
    user_relationship_to = relationship("User", foreign_keys=[user_to_id])



render_er(Base, "diagram.png")
