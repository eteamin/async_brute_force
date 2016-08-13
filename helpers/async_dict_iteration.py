

class AsyncDictIteration(object):
    def __init__(self, dictionary):
        self.keys = dictionary.keys()
        self.dict = dictionary

    def __aiter__(self):
        return self

    def __anext__(self):
        pair = self.keys[0]
