# Database BugSpot 之 SQLite锁冲突

在这个任务中，你的任务是找出一个**基于Flask和SQLite3的数据库系统**的漏洞，该系统在初始化时报错“sqlite3.OperationalError: database is locked”。

In this task your mission is to spot the bugs of a database system based on the Flask and SQLite3 architecture. The system, when initiates, encounters Operational Error that the database is locked.

## 问题重现

请在终端中执行如下代码，以部署页面并检查问题。

```bash
# 切换目录
## Bash (Linux/macOS/Git Bash/WSL)
if [ "$(basename $(pwd))" = "task1" ]; then cd ../task2; else cd Database/task2; fi
## Windows PowerShell
if ((Split-Path -Leaf (Get-Location)) -eq "task1") { cd ../task2 } else { cd Database/task2 }

python main.py
```

## 你的任务

- 在不影响功能的前提下，修复代码中的Bug
- 在检查代码过程中，如果发现其他代码问题或潜在风险，修复并报告

## 参考文档

关于python依赖包的文档，请访问以下网页：

Documentation of the python packages:

| 依赖         | 中文/Chinese                                                                           | 英文/English                                                                 |
| ---------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| sqlalchemy | [SQLAlchemy 2.0 文档 - SQLAlchemy 中文](https://docs.sqlalchemy.org.cn/en/20/intro.html) | [SQLAlchemy Documentation 2.0](https://docs.sqlalchemy.org/en/20/)         |
| SQLite     | [SQLite中文 文档分类导航](https://www.sqlite.cn/docs.html)                                   | [SQLite Documentation](https://sqlite.org/docs.html)                       |
| Flask      | [Flask文档-中文版（3.1.x）](https://flask.org.cn/en/stable/)                                | [Flask documentation(3.1.x)](https://flask.palletsprojects.com/en/stable/) |
