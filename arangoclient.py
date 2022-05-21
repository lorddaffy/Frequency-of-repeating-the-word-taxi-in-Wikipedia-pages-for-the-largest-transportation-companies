from arango import ArangoClient, exceptions
import os
hostname = os.environ["ARANGO_HOSTNAME"]
port = os.environ["ARANGO_PORT"]
host = hostname + ":" + port
client = ArangoClient(hosts=host)


def setup_db():
    sys_db = client.db("_system", username="root", password="1234")
    try:
        sys_db.create_database("free-now")
    except exceptions.DatabaseCreateError:
        pass 