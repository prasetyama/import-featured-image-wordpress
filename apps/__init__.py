from sqlalchemy import select, desc
from libs.connection import DSEngine
from libs.models import WpPost


def get_latestpost():
    data = DSEngine.execute(select(WpPost).order_by(WpPost.ID.desc()).limit(10))
    
    for item in data:
        print(item)


"""
source venv/bin/activate
cd project
python

> from apps import get_latestpost
> get_latestpost
"""