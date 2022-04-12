from sqlalchemy import create_engine, inspect, text
from sqlalchemy.engine import url

TRIKINET_CONNECTION = {
    'username':'root',
    'password':'root',
    'host':'127.0.0.1',
    'database':'trikinet_cms_wp',
    'drivername':'mysql'
}

DAILYSOCIAL_CONNECTION = {
    'username':'root',
    'password':'root',
    'host':'127.0.0.1',
    'database':'cms',
    'drivername':'mysql'
}

DsConn = url.URL.create(**DAILYSOCIAL_CONNECTION)
TrikiConn = url.URL.create(**TRIKINET_CONNECTION)

DSEngine = create_engine(DsConn)
DSEngine.connect()

TrikiEngine = create_engine(TrikiConn)
TrikiEngine.connect()


# to inspectdb: sqlacodegen mysql://yohanes:12345@127.0.0.1/cmsdb > libs/models.py