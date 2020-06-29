# Shop run tutorial

## 创建项目
```shell script
django-admin.py startproject Shop
django-admin.py startapp common
django-admin.py startapp goods 
django-admin.py startapp users
```
## 创建后台管理员
```shell script
python3 manage.py createsuperuser
python3 manage.py runserver
```

## 数据库初始化
```sql
create database Shop character set utf8mb4;
use Shop;

-- 会员信息表(后台管理员信息也在此标准，通过状态区分)
CREATE TABLE `users`(
`id` int(11) unsigned NOT NULL AUTO_INCREMENT, `username` varchar(32) NOT NULL,
`name` varchar(16) DEFAULT NULL,
`password` char(32) NOT NULL,
`sex` tinyint(1) unsigned NOT NULL DEFAULT '1', `address` varchar(255) DEFAULT NULL,
 `code` char(6) DEFAULT NULL,
`phone` varchar(16) DEFAULT NULL,
`email` varchar(50) DEFAULT NULL,
`state` tinyint(1) unsigned NOT NULL DEFAULT '1', `addtime` datetime DEFAULT NULL,
PRIMARY KEY (`id`),
UNIQUE KEY `username` (`username`)
)ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
-- 商品类别表
CREATE TABLE `type`(
`id` int(11) unsigned NOT NULL AUTO_INCREMENT, `name` varchar(32) DEFAULT NULL,
`pid` int(11) unsigned DEFAULT '0',
`path` varchar(255) DEFAULT NULL,
PRIMARY KEY (`id`)
)ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
-- 商品信息表
CREATE TABLE `goods`(
`id` int(11) unsigned NOT NULL AUTO_INCREMENT, `typeid` int(11) unsigned NOT NULL,
`goods` varchar(32) NOT NULL,
`company` varchar(50) DEFAULT NULL,
`content` text,
`price` double(6,2) unsigned NOT NULL,
`picname` varchar(255) DEFAULT NULL,
`store` int(11) unsigned NOT NULL DEFAULT '0', `num` int(11) unsigned NOT NULL DEFAULT '0', `clicknum` int(11) unsigned NOT NULL DEFAULT '0', `state` tinyint(1) unsigned NOT NULL DEFAULT '1', `addtime` datetime DEFAULT NULL,
PRIMARY KEY (`id`),
KEY `typeid` (`typeid`)
)ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
-- 订单信息表
CREATE TABLE `orders`(
`id` int(11) unsigned NOT NULL AUTO_INCREMENT, `uid` int(11) unsigned DEFAULT NULL,
`linkman` varchar(32) DEFAULT NULL,
`address` varchar(255) DEFAULT NULL,
`code` char(6) DEFAULT NULL,
`phone` varchar(16) DEFAULT NULL, `addtime` datetime DEFAULT NULL,
`total` double(8,2) unsigned DEFAULT NULL, `state` tinyint(1) unsigned DEFAULT NULL, PRIMARY KEY (`id`)
)ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
-- 订单信息详情表
CREATE TABLE `detail`(
`id` int(11) unsigned NOT NULL AUTO_INCREMENT, `orderid` int(11) unsigned DEFAULT NULL, `goodsid` int(11) unsigned DEFAULT NULL, `name` varchar(32) DEFAULT NULL,
`price` double(6,2) DEFAULT NULL, `num` int(11) unsigned DEFAULT NULL,
 
 PRIMARY KEY (`id`)
)ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
 
```

## 生成迁移脚本并作用于数据库

```shell script
python3 manage.py makemigrations
python3 manage.py migrate
```

## 测试数据

```sql
商品分类
INSERT INTO `common_types` VALUES (1,'女装'),(2,'男装'),(3,'童装');

商品列表
INSERT INTO `common_goods` VALUES (1,'友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休','妈妈裤','友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4',200.6,'upload/2020/06/a1717971f87b3d86.jpg',14,12,98,0,'2020-06-29 12:45:00.000000',1),(2,'友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休','妈妈裤','友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4',100,'upload/2020/06/a1717971f87b3d86.jpg',14,12,98,0,'2020-06-29 12:45:00.000000',1),(3,'友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休','妈妈裤','友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4',29,'upload/2020/06/a1717971f87b3d86.jpg',14,12,97,0,'2020-06-29 12:45:00.000000',1),(4,'友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休','妈妈裤','友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4',1432,'upload/2020/06/a1717971f87b3d86.jpg',14,12,97,0,'2020-06-29 12:45:00.000000',1),(5,'友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休','妈妈裤','友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4',200.6,'upload/2020/06/a1717971f87b3d86.jpg',14,12,97,0,'2020-06-29 12:45:00.000000',1),(6,'友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休','妈妈裤','友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4',200.6,'upload/2020/06/a1717971f87b3d86.jpg',14,12,97,0,'2020-06-29 12:45:00.000000',1),(7,'友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休','妈妈裤','友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4',200.6,'upload/2020/06/a1717971f87b3d86.jpg',14,12,97,0,'2020-06-29 12:45:00.000000',1),(8,'友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休','妈妈裤','友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4',200.6,'upload/2020/06/a1717971f87b3d86.jpg',14,12,97,0,'2020-06-29 12:45:00.000000',1),(9,'友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休','妈妈裤','友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4',200.6,'upload/2020/06/a1717971f87b3d86.jpg',14,12,97,0,'2020-06-29 12:45:00.000000',1),(10,'友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休','妈妈裤','友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4友家坊 九分裤女亚麻宽松直筒松紧腰中老年女裤大码妈妈裤夏季薄款休闲裤女九分裤 灰色 2XL（腰围2尺3-2尺4',200.6,'upload/2020/06/a1717971f87b3d86.jpg',14,12,97,0,'2020-06-29 12:45:00.000000',1);
```