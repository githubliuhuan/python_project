工作交接

一.设备厂商

1.ornitela 谈判
	2.druid 开发完成。                 备注：等正式账号跑批，需要注意第一次要爬历史全部数据，不止6个月
	3.ecotone 开发完成。               备注：等正式账号跑批，数据少，两只鸟
	4.koeco 开发完成。                 备注：等正式账号跑批，定向设备爬取，后续可考虑抓取全部设备id号再遍历
	5.hqsx 开发完成。                  备注：已部署服务器，每天2:30跑批

二.观鸟网站

	1.ebird 开发完成。                 备注：已部署服务器，每天2:01跑批
	2.中国观鸟记录中心 开发完成。      备注：已部署服务器，每天1:01跑批
	3.gbif 开发完成。                  备注：已部署服务器，每天1:30跑批
4.movebank 开发中。                  备注：暂时无法用python爬取，且需翻墙，可提供java代码，只能定向下载某一文件，无法增量（后期是否考虑手动下载定时入库再去重...）
5.seamap 开发中。                    备注：暂时无法用python爬取，且需翻墙

三.相关账户密码

1.阿里云：https://account.aliyun.com/login/login.htm?oauth_callback=https%3A%2F%2Fhome.console.aliyun.com%2Fnew
  用户名：水鸟与湿地生态研究组
  密码：shidi2017

2.云数据库RDS华北3
  地址：rm-8vbqudhd5zy60sin3o.mysql.zhangbei.rds.aliyuncs.com
  数据库用户名：bird
  数据库名：birds_db
  密码：Bird@2017

3.云服务器ECS
  ip:47.92.64.101
  root密码：Bird@2017
  bird密码：123456
  hqxs密码（ftp账户）：111111

四.服务器相关路径

1.kettle作业 /home/bird/kettle_project
2.相关软件包 /home/bird/package
3.python脚本 /home/bird/python_project
4.hqxs文件路径 /data/sftp/hqxs/upload

