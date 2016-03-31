#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine,select, Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

user = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)

color = Table('color', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)
engine = create_engine("mysql+mysqldb://root:123@localhost:3306/test", max_overflow=5)

#metadata.create_all(engine)
conn = engine.connect()
#sql = user.insert().values(name='a')
#sql = user.insert().values(name='ab')
#conn.execute(sql)
#sql = user.delete().where(user.c.name == 'alex')
#conn.execute(sql)
# sql = user.update().values(fullname=user.c.name)

#sql = user.update().where(user.c.name == 'jack').values(name='ed')


sql = select([user, ])
res =conn.execute(sql)
print(res.fetchall() )
#sql = user.select([user.c.id, ])
sql = select([user.c.name, color.c.name]).where(user.c.id==color.c.id)
# sql = select([user.c.name]).order_by(user.c.name)
# sql = select([user]).group_by(user.c.name)

# result = conn.execute(sql)
# print result.fetchall()
# conn.close()
