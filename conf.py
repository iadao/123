# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "iadao/123@gh-pages"
}

# 站点设置
site_name = "阿道"  # 标题
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "阿道博客" # 页脚
email = "adao.me"
author_homepage = "https://adao.me"
description = "将生活带给你的如柠檬的酸楚，酿成犹如柠檬汽水般的甘甜。"
key_words = ['阿道博客', 'blog', '', '']
language = 'zh-CN'
external_links = [
#    {
#        "name": "Maverick",
#        "url": "https://github.com/AlanDecode/Maverick",
#       "brief": "🏄‍ Go My Own Way."
#    },
    {
        "name": "阿道",
        "url": "https://adao.me",
        "brief": "阿道博客。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
