
## LinuxONE Chart v1.0
> 用于解析nmon, hyptop, cpumf并生成图形html报告直接在线查看.  
> 该工具处于开发阶段,暂未对外公布.  
> HTML Report Demo地址(IBM内部访问): [http://chart.linuxone.cn/output](http://chart.linuxone.cn/output)  

## 总览
![](index/A4291159-169A-4CE9-A5E3-77CB410D5352%205.png)

## 基于Hyptop提取的数据
### 指定LPAR的Core使用量(1颗物理IFL=100)
![](index/6B637D83-9583-47D8-9788-2F4D64CDF8D7%205.png)

### 指定LPAR的Core MGM使用量(1颗物理IFL=100)
![](index/DC637938-099F-4DFA-930E-EF71A80921D0%204.png)

### 指定LPAR的Core Thread使用量(开启SMT2,每颗物理IFL包含2个线程, 1个线程=100)
![](index/D4848946-37CA-44B8-97A3-47D2A43EC344%204.png)

- - - -

### 整机Core的使用量(1IFL=100)
![](index/FEF6B79D-55B8-4871-891D-B0CA9E3C221F%204.png)

### 整机Core Thread使用量(开启SMT2,每颗物理IFL包含2个线程, 1个线程=100)
![](index/D1215A35-6303-4177-941C-B4970720C95D%204.png)

### 整机Core vs Core Thread
![](index/251AFF6B-B003-4C3C-B22B-41CBF7B94012%204.png)

- - - -

## 基于CPUMF提取的数据

### CPUMF : L2P L3P L4LP L4RP MEMP
![](index/A7F5B881-41DE-4D32-AC1A-452955858C43%205.png)

### CPUMF: CPI L1MP
![](index/ECC11D35-565A-4044-BC8D-66A36D5933F9%205.png)

- - - -
## 基于nmon提取的数据
### CPU
![](index/EF509C3F-D97D-46B5-8E91-1A14EC41820F.png)


### 网络
![](index/3BD4D6ED-A0C1-429A-8D5B-52F291F2C726%203.png)

### 磁盘
![](index/3F5ABB25-B32A-47AC-892A-298E641B9BA8%203.png)

