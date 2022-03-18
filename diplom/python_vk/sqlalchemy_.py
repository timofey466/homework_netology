import sqlalchemy as sq
from sqlalchemy.orm import declarative_base
from vk_info import city, age, best_family, title, gender, vk_id

Base = declarative_base()


class People(Base):

    __tablename__ = 'people'

    id = sq.Column(sq.Integer, primary_key=True)

    name = sq.Column(sq.String)

    big_city = sq.Column(sq.String)

    date = sq.Column(sq.Integer)

    family = sq.Column(sq.String)

    sex = sq.Column(sq.String)

    vk = sq.Column(sq.String)


sql_city = People(big_city=city)

sql_age = People(date=age)

sql_family = People(family=best_family)

sql_name = People(name=title)

sql_sex = People(sex=gender)

sql_vk_id = People(vk=vk_id)






