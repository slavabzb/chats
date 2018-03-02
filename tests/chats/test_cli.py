from aiohttp import web

from chats.cli import index


class TestIndex:
    async def test_get__return_text(self, aiohttp_client):
        app = web.Application()
        app.router.add_get('/', index)
        client = await aiohttp_client(app)
        resp = await client.get('/')
        assert resp.status == 200
        text = await resp.text()
        assert 'index' in text
