'''import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


async def index(request):  # 参考aiohttp的文档
    # 与老师的源码相比，最重要的是要加content_type这个参数，否则会变成下载文件
    return web.Response(body='<h1>Awesome</h1>'.encode('utf-8'), content_type='text/html')

def init():
    app = web.Application()
    app.add_routes([web.get('/', index)])  # 多看看官方文档，aiohttp和asyncio都要看
    logging.info('Server started at http://127.0.0.1:8080')
    web.run_app(app, host='127.0.0.1', port=8080)


init()'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()