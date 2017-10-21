# 树莓派＋墨水屏 添加网站统计功能
在原作者的基础上引入了百度统计功能，利用百度统计API将网站的访问情况显示在墨水屏上

原作者的代码：[emptyhua/epaper_clock](https://github.com/emptyhua/epaper_clock) 

这个功能是利用百度统计API实现的，并对统计SDK做了一些小调整，使其可以自动获取当日和前一日的pv和uv。
## 获取百度统计API
1.首先要获取百度统计的API，登录百度统计->管理->其它设置->数据导出服务，启用数据导出功能，启用后你会获得一个TOKEN：
 ![image](https://raw.githubusercontent.com/OGRLEAF/epaper_clock_baidutongji/master/get_baidutongji_api/get-baidutongjiapi.png)
 
2.编辑/tongjiapi/Config.inc.php，将其中的TOKEN、登录百度统计用的账号密码改为你自己的：
```php
<?php
/**
 * Demo of Tongji API
 * set your information such as USERNAME, PASSWORD ... before use
 */
//*
//preLogin,doLogin URL
define('LOGIN_URL', 'https://api.baidu.com/sem/common/HolmesLoginService');
//Tongji API URL
define('API_URL', 'https://api.baidu.com/json/tongji/v1/ReportService');
//USERNAME
define('USERNAME', '百度统计用户名');
//PASSWORD
define('PASSWORD', '密码');
//TOKEN
define('TOKEN', '从百度统计获得的TOKEN');
//UUID, used to identify your device, for instance: MAC address
define('UUID', '******');
//ACCOUNT_TYPE
define('ACCOUNT_TYPE', 1); //ZhanZhang:1,FengChao:2,Union:3,Columbus:4
//*/
```
3.安装环境
因为个人水平有限，而百度统计只提供了php的SDK，所以…………需要先安装php环境
```bash
sudo apt-get install php curl -y
```
4.尝试获取统计数据
```bash
php /tongjiapi/demo.php
```
如果输出类似下面的结果，说明获取成功：
```json
{"header":{"desc":"success","failures":[],"oprs":1,"succ":1,"oprtime":0,"quota":1,"rquota":49925,"status":0},"body":{"data":[{"result":{"total":2,"items":[[["2017/10/21"],["2017/10/20"]],[[419,156],[600,242]],[],[]],"timeSpan":["2017/10/20 - 2017/10/21"],"sum":[[1019,398],[]],"offset":0,"pageSum":[[1019,398],[],[]],"fields":["simple_date_title","pv_count","visitor_count"]}}]}}
```
## 开始运行吧
执行以下命令：
```bash
php /tongjiapi/demo.php > statistics.json  #将统计数据导入到本地的statistics.json文件中
sudo ./home_air_sensor.py
./weather_fetcher.py
./weather_time_render.py
```
## 运行结果
（我没插温湿传感器）
![images](https://raw.githubusercontent.com/OGRLEAF/epaper_clock_baidutongji/master/epaper_clock.jpg)

CREATE BY [橙叶博客](https://www.orgleaf.com)
