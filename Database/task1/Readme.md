# Database BugSpot 之 消失的用户数据

在这个任务中，你的任务是找出一个**在线用户管理系统**的漏洞，该系统可以创建用户并列出用户。然而，系统出现了一些问题，创建的用户都会消失……

In this task your mission is to spot the bugs of an **online user management system**, which enables creating users as well as listing users. However, somethings went wrong and the users created would disappear ...

## 问题重现

请在终端中执行如下代码，以部署页面并检查问题。

```bash
# 切换目录
## Bash (Linux/macOS/Git Bash/WSL)
if [ "$(basename $(pwd))" = "task2" ]; then cd ../task1; else cd Database/task1; fi
## Windows PowerShell
if ((Split-Path -Leaf (Get-Location)) -eq "task2") { cd ../task1 } else { cd Database/task1 }

streamlit run demo.py
# 如果以上任务执行失败，也可尝试
python -m streamlit run demo.py
```

开启成功后，你将能够在 `http://localhost:8501`访问你的页面。

## 你的任务

- 在不影响功能的前提下，修复代码中的Bug
- 在检查代码过程中，如果发现其他代码问题或潜在风险，修复并报告

## 参考文档

关于python依赖包的文档，请访问以下网页：

Documentation of the python packages:

中文：[概述 — SQLAlchemy 2.0 文档 - SQLAlchemy 中文](https://docs.sqlalchemy.org.cn/en/20/intro.html)

英文：[SQLAlchemy Documentation 2.0](https://docs.sqlalchemy.org/en/20/)

[Streamlit Documentation](https://docs.streamlit.io/)
