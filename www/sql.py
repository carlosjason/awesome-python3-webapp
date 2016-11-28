import orm
import asyncio
import sys
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='password', db='awesome')
    u = User(name='test', email='test@qq.com', passwd='1234567', image='about:blank')
    await u.save()

if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait([test(loop)]))
        loop.close()