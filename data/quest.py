import sqlalchemy
from data.db_session import SqlAlchemyBase


class Quest(SqlAlchemyBase):
    __tablename__ = 'quests'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    json = sqlalchemy.Column(sqlalchemy.String)
