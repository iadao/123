---
layout: post
title: mac系统-亚马逊云EC2-密钥（免密码）登陆服务器
slug: mac-ec2-password
date: 2020/05/16 11:42:00
status: publish
author: 阿道
categories: 
  - 默认分类
tags: 
  - 博客
  - ec2
  -  亚马逊
excerpt: 海外版本亚马逊云，服务器所在
---

## 账号注册及服务器创建

海外版本亚马逊云，服务器所在机房可以选择新加坡或者日本，速度相对快一些

需要注意的是创建秘钥时选择创建新的秘钥并下载保存好。

## 本地操作
1. 移动文件
将下载好的秘钥保存到下载目录，并改好名字，我这里改成ec2，并移动秘钥文件
如果没有相关目录，自行创建即可

`mv ~/Downloads/ec2.pem ~/.ssh/ec2.pem`

2. 赋权限
`chmod 400 ec2.pem`

3. 连接
`ssh -i {您的 .pem 文件的完整路径} ec2-user@{实例 IP 地址}`

ssh -i ~/.ssh/ec2.pem centos@1.2.3.4
注意@前面的名称需要根据自己的服务器系统来修改，我这里是centos7，其他系统请自行修改!

![e](media/ec2.png)




