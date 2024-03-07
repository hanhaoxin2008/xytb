# xytb
一个python进度条工具，可以方便的使用进度条。

### 使用方法
使用pip安装xytb
（因为国内无法注册pypi，所以只能通过whl安装）
``` 
pip install xytb-x.x.x-py3-none-any.whl
````
导入xytb
```  python
from xytb import xytb
```
使用xytb
``` python
#用法1
for i in xytb(iter,total,barLen,desc,out):
    pass

#用法2
for i in rxytb(100):
    #会使用默认参数
    pass

#用法3
c=cxytb(desc,total,barLen,out)

for i in c(100):
    pass

```
参数说明：  
1. iter: 迭代次数
2. total: 总次数 ，默认为None
3. desc: 进度条描述,默认为空
4. barLen:进度条长度，默认为10
5. out: 进度条输出位置，默认是标准输出

#### 示例1
``` python
from xytb import xytb
import time
for i in xytb(100,100,'下载进度',sys.stdout):
    time.sleep(1)

```
输出
``` 
下载进度:|##--------| 22/100 22% [已开始: 00:22 预计还需: 01:18, 1 任务/秒]

```

#### 示例2
``` python
for i in rxytb(10):
    time.sleep(1)
```
输出
```
|###-------| 3/10 30% [已开始: 00:03 预计还需: 00:07, 1 任务/秒]
```

#### 示例3
``` python
c=cxytb(desc="示例",barLen=20)
for i in c(100):
    time.sleep(1)

```

输出

```
示例:|##########----------| 51/100 51% [已开始: 00:51 预计还需: 00:49, 1 任务/秒]
```


### 更新日志
#### v1.0.0
1. 初始化版本
####  v1.0.1
1. 进度套长度可自定义
2. 新增rxytb函数
3. 新增cxytb函数
### v1.0.1
1. 事件循环



