"""调用功能一般看import后面词加功能名
import 模块名1,模块名2 /模块名.功能名-   /后为调用方式  (导入语句放在代码最上面)
import random

for i in range(100):
    print(random.randint(1, 100))

import 模块名 as 别名 /别名.功能名
import random as rd

for i in range(20):
    print(rd.randint(0, 10))

from 模块名 import 功能名 /功能名
from random import randint
for i in range(20):
    print(randint(0, 10))

from 模块名 import 功能名 as 别名 / 别名
from random import randint as rint
for i in range(20):
    print(rint(1,20))
"""

# from 模块名 import * / 功能名 调用全部功能
from random import *
for i in range(30):# 遍历个数
    print(randint(1, 20)) #遍历元素的数字范围

