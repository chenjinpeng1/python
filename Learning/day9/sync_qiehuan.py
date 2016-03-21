from gevent import monkey; monkey.patch_all()
import gevent,time
from  urllib.request import urlopen
 
def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    time.sleep(1)
    print('%d bytes received from %s.' % (len(data), url))
 
gevent.joinall([
        gevent.spawn(f, 'http://51cto.com/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://baidu.com/'),
])
