import orm
from orm import create_pool,destory_pool
from models import User, Blog, Comment
import asyncio


'''
async def test(loop):
    await orm.create_pool(loop=loop,user='root', password='password', db='awesome')
    u = User(name='Test3', email='test3@example.com', password='12345678902', image='about:blank')
    await u.save()
    await destory_pool()

if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait([test(loop)]))
        loop.close()
'''
        
        
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html', charset='UTF-8')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


