from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base

BASE = declarative_base()

class Grammys(BASE):
    __tablename__ = 'grammys'
    id = Column(Integer, primary_key=True, autoincrement=True)
    year = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    published_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)
    category = Column(String, nullable=False)
    nominee = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    workers = Column(String, nullable=False)
    img = Column(String, nullable=False)
    winner = Column(Boolean, nullable=False)

class DataMusic(BASE):
    __tablename__ = 'data_music'
    id = Column(Integer, primary_key=True)
    track_id = Column(String, nullable=False)
    artists = Column(String, nullable=False)
    album_name = Column(String, nullable=False)
    track_name = Column(String, nullable=False)
    popularity = Column(Integer, nullable=False)
    explicit = Column(Boolean, nullable=False)
    speechiness = Column(Integer, nullable=False)
    track_genre = Column(String, nullable=False)
    popularity_level = Column(String, nullable=False)
    duration_min_sec = Column(String, nullable=False)
    danceability_category = Column(String, nullable=False)
    speechiness_category = Column(String, nullable=False)
    valence_category = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    nominated = Column(Integer, nullable=False)