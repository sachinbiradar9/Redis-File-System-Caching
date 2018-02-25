import redis
from datetime import datetime
import re

class MyRedis(redis.Redis):
    def __init__(self, *args, **kwargs):
        super(MyRedis, self).__init__(*args, **kwargs)

    def myset(self, key, value, pre_hook=None, post_hook=None):
        if pre_hook:
            pre_hook()
        self.set(key, value)
        self.set(key+':time_created', datetime.utcnow())
        if post_hook:
            pre_hook()

    def myget(self, key, pre_hook=None):
        if pre_hook:
            pre_hook()
        self.set(key+':last_accessed', datetime.utcnow())
        return self.get(key)

    def my_delete(self, key, pre_hook=None):
        if pre_hook:
            pre_hook()
        self.delete(key)
        self.delete(key+':last_accessed')
        self.delete(key+':time_created')

    def get_info(self, pattern=''):
        data = {}
        for key in self.scan_iter():
            if ':time_created' in key:
                if key[:-13] not in data:
                    data[key[:-13]] = {}
                data[key[:-13]]['time_created'] = self.get(key)
            elif ':last_accessed' in key:
                if key[:-14] not in data:
                    data[key[:-14]] = {}
                data[key[:-14]]['last_accessed'] = self.get(key)
            else:
                if key not in data:
                    data[key] = {}
                data[key]['value'] = self.get(key)
        return data
