from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

user = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)

color = Table('color', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)
engine = create_engine("mysql+pymysql://root:chen27@localhost:3306/chen", max_overflow=5)

# metadata.create_all(engine)
class aa(object):
    def aa(self):
        print("aaaa")

