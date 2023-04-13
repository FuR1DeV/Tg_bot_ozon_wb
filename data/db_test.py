import asyncio
from datetime import datetime

from sqlalchemy import and_, or_

from settings import config
from data.db_gino import db


async def db_test():
    pass
    # performers = await Performers.query.where(and_(Performers.auto_send == 1,
    #                                                Performers.performer_money > 49,
    #                                                or_(Performers.performer_category == "car",
    #                                                    Performers.performer_category == "scooter",
    #                                                    Performers.performer_category == "pedestrian", ))).gino.all()
    # print(performers)
loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())
