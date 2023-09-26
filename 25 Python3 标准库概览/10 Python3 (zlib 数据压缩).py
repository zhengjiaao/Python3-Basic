# 数据压缩
# 以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。

import zlib

s = b'witch which has which witches wrist watch'
print(len(s))  # 41

t = zlib.compress(s)
print(len(t))  # 37

zlib.decompress(t)
print(zlib.crc32(s))  # 226805979

# 输出结果

# 41
# 37
# 226805979
