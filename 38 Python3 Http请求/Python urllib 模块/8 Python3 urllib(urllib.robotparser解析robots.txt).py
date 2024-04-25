# Python urllib 模块.robotparser 用于解析 robots.txt 文件。


import urllib.robotparser
rp = urllib.robotparser.RobotFileParser()
rp.set_url("http://www.musi-cal.com/robots.txt")
rp.read()
rrate = rp.request_rate("*")
print(rrate.requests) # 3
print(rrate.seconds) # 20
print(rp.crawl_delay("*")) # 6
print(rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco")) # False
print(rp.can_fetch("*", "http://www.musi-cal.com/")) # True









