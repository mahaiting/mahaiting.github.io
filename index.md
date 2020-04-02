
## LinuxONE Chart v1.0
> 用于解析nmon, hyptop, cpumf并生成图形html报告直接在线查看.  
> 该工具处于开发阶段,暂未对外公布.  

cpuplugd测试数据DEMO地址(IBM内部访问): [http://chart.linuxone.cn/cpuplugd](http://chart.linuxone.cn/cpuplugd)

## cpuplugd测试数据说明
进入目录后会出现10个G开头的目录，G01-G10对应的是10个测试场景，点击某个场景名可以查看。
注：coremap里面保存的是每个场景的coremap和LPAR weight。
![](index/5DA0DEA9-F0E1-4A90-83F1-784752803D28%202.png)

进入某个场景后，里面会显示该场景下全部LPAR的数据，比如红框内代表的是G01的LPAR10的全部性能数据。
主要关注如下类似的两个文件名：
1. G01_LPAR10.linuxonechart.html
这里面包含的是LPAR的性能数据图形报表，直接点击查看。
页面打开后，最上面有一排按钮，点击后即可生成对应的图形。
2. G01_LPAR10_jmeter_html_report/
这里面包含的是Jmeter客户端的性能数据，比如TPS/Response Time等。
![](index/B3B07561-78C4-4807-92BE-CD1C0FFCD5F5%202.png)

### 原始数据说明
1. G01_LPAR10.20200323204553.cpumf
cpumf的原始数据
2. G01_LPAR10.20200323204553.csv.tar.gz
发压工具Jmeter作为客户端收集到的数据，TPS/Response Time等原始数据都打包放到了这里
3. G01_LPAR10.20200323204553.hyptop
hyptop的原始数据
4. G01_LPAR10.20200323204553.nmon
nmon的原始数据
5. G01_LPAR10.20200323204553.top
top的原始数据
6. G01_LPAR10.conf.txt
Jmeter发压时的配置文件，记录了初始线程，目标线程等基础信息
7. G01_LPAR10.jmeter.log
Jmeter的压力日志，里面每6秒会汇总一次TPS/Response Time和Active Thread


