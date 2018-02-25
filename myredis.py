import redis
from datetime import datetime

class MyRedis(redis.Redis):
    def __init__(self, *args, **kwargs):
        super(MyRedis, self).__init__(*args, **kwargs)

    def my_set(self, key, value, pre_hook=None, post_hook=None):
        if pre_hook:
            pre_hook()
        self.set(key, value)
        self.set(key+':time_created', datetime.utcnow())
        if post_hook:
            pre_hook()

    def my_get(self, key, pre_hook=None):
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

    def my_rename(self, old_key, new_key, pre_hook=None):
        if pre_hook:
            pre_hook()
        self.rename(old_key, new_key)
        self.rename(old_key+':time_created', new_key+':time_created')
        if self.get(old_key+':last_accessed'):
            self.rename(old_key+':last_accessed', new_key+':last_accessed')

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

    def delete_older(self, datetime_x, flag=0):
        info = self.get_info()
        if flag == 0:
            to_search = 'last_accessed'
        else:
            to_search = 'time_created'
        datetime_x = datetime.strptime(datetime_x,'%Y-%m-%d  %H:%M:%S.%f')
        for key in list(info.keys()):
            if info[key].get(to_search)!= None:
                values = datetime.strptime(info[key][to_search],'%Y-%m-%d  %H:%M:%S.%f')
                if values< datetime_x:
                    self.my_delete(key)
