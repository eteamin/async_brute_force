import asyncio

dsn = "..."

class Foo(object):
    @classmethod
    async def create(cls, settings):
        self = Foo()
        self.settings = settings
        self.pool = await create_pool(dsn)
        return self

async def main(settings):
    settings = "..."
    foo = await Foo.create(settings)
