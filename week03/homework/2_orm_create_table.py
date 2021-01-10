'''
2. 使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:

用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
将 ORM、插入、查询语句作为作业内容提交
'''

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Student_table(Base):
    __tablename__ = 'student'

    uid = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(15), nullable=True)
    age = Column(Integer(), nullable=False)
    birthday = Column(DateTime())
    sex = Column(Boolean(), nullable=False)
    edu = Column(Enum("中学", "专科", "本科", "硕士", "博士"))
    create_on = Column(DateTime(), default=datetime.now)
    update_on = Column(DateTime(), default=datetime.now,
                       onupdate=datetime.now)

    def __repr__(self):
        return f'id={self.uid}, name={self.name}, age={self.age}, ' \
               f'birthday={self.birthday}, sex={self.sex}, edu={self.edu}, ' \
               f'create_on={self.create_on}, update_on={self.update_on}'


dburl = "mysql+pymysql://root:123456@localhost:3306/jove_class?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")

SessionClass = sessionmaker(bind=engine)
session = SessionClass()
# Base.metadata.create_all(engine)


student = Student_table(name='Jove',
                        age=18,
                        birthday=datetime(2002, 1, 1),
                        sex=True,
                        edu="本科",
                        )
# session.add(student)
result = session.query(Student_table).filter(
    Student_table.name == 'Jove').all()
print(result)
session.commit()
