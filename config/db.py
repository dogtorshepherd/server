from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:][p'@localhost:3306/sql_exam")
meta = MetaData()
conn = engine.connect()