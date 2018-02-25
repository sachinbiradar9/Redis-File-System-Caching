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
#x.myset('motasim', 'mohammad', y, z)
x.myget('qw', a)
#x.my_delete('foo', c)
print x.get_info()
