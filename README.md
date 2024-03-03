# xytb
一个python进度条工具，可以方便的使用进度条。

### 使用方法
使用pip安装xytb
``` 
pip install xytb
````
导入xytb
```  python
from xytb import xytb
```
使用xytb
``` python

for i in xytb(iter,total,desc,out):
    pass

```
参数说明：  
1. iter: 迭代次数
2. total: 总次数
3. desc: 进度条描述
4. out: 进度条输出位置，默认是标准输出

### 示例
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

### 更新日志
#### v1.0.0
1. 初始化版本



