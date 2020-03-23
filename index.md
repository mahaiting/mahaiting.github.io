
## LinuxONE Chart v1.0
> 该工具用于解析nmon, hyptop, cpumf并生成图形html报告直接在线查看.  

Demo地址(IBM内部访问): http://chart.linuxone.cn/output

### 总览
![](index/A4291159-169A-4CE9-A5E3-77CB410D5352%203.png)

### 指定LPAR的Hyptop Core使用量(1颗物理IFL=100)
![](index/6B637D83-9583-47D8-9788-2F4D64CDF8D7%203.png)

### 指定LPAR的Hyptop MGM使用量(1颗物理IFL=100)
![](index/DC637938-099F-4DFA-930E-EF71A80921D0%202.png)

### 指定LPAR的Hyptop Thread使用量(开启SMT2,每颗物理IFL包含2个线程, 1个线程=100)
![](index/D4848946-37CA-44B8-97A3-47D2A43EC344%202.png)

- - - -

### 整机Core的使用量(1IFL=100)
![](index/FEF6B79D-55B8-4871-891D-B0CA9E3C221F%202.png)

### 整机Core Thread使用量(开启SMT2,每颗物理IFL包含2个线程, 1个线程=100)
![](index/D1215A35-6303-4177-941C-B4970720C95D%202.png)

### 整机Core vs Thread
![](index/251AFF6B-B003-4C3C-B22B-41CBF7B94012%202.png)

- - - -

### CPUMF : L2P L3P L4LP L4RP MEMP
![](index/A7F5B881-41DE-4D32-AC1A-452955858C43%203.png)

### CPUMF: CPI L1MP
![](index/ECC11D35-565A-4044-BC8D-66A36D5933F9%203.png)

- - - -
## 其他nmon指标
### 网络
![](index/3BD4D6ED-A0C1-429A-8D5B-52F291F2C726.png)

### 磁盘
![](index/3F5ABB25-B32A-47AC-892A-298E641B9BA8.png)

