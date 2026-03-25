from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy

# initialize Cloud SQL Connector
connector = Connector()

# SQLAlchemy database connection creator function
def getconn():
    conn = connector.connect(
        "project:region:instance-name", # Cloud SQL Instance Connection Name
        "pg8000",
        user="my-user",
        password="my-password",
        db="my-db-name",
        ip_type=IPTypes.PUBLIC # IPTypes.PRIVATE for private IP
    )
    return conn

# create SQLAlchemy connection pool
pool = sqlalchemy.create_engine(
    "postgresql+pg8000://",
    creator=getconn,
)

# interact with Cloud SQL database using connection pool
with pool.connect() as db_conn:
    # query database
    result = db_conn.execute("SELECT * from my_table").fetchall()

    # Do something with the results
    for row in result:
        print(row)

# close Cloud SQL Connector
connector.close()
