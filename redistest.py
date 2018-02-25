from datetime import datetime
from myredis import MyRedis
########
def y():
    print "im prehook of set"
def z():
    print "im prehook of set"
def a():
    print "im prehook of get"
def b():
    print "im prehook of get"
def c():
    print "im prehook of delete"

x = MyRedis('localhost', 6379, '')
#x.my_set('motasim', 'mohammad', y, z)
x.my_get('qw', a)
#x.my_delete('foo', c)
d = str(datetime.utcnow())
x.delete_older(d)
print x.get_info()
