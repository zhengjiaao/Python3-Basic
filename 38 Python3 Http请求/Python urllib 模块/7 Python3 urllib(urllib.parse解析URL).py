from urllib.parse import urlparse

o = urlparse("https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B")
print(o)
# ParseResult(scheme='https', netloc='www.runoob.com', path='/', params='', query='s=python+%E6%95%99%E7%A8%8B', fragment='')

o = urlparse("https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B")
print(o.scheme)
# https
