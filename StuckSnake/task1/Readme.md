# 瞬间掉头的贪吃蛇

在本**贪吃蛇游戏**实例中，有一个奇怪的地方：在游戏后期或者遇到需要突然急转弯的时候，特别容易撞到边界或者自身而游戏结束。请仔细阅读代码，判断是否是代码实现的问题？如果是，请编辑代码解决故障。

## 环境重现

在命令行中执行以下指令，以安装依赖并运行游戏。

```bash
# 切换目录
## Bash (Linux/macOS/Git Bash/WSL)
if [ "$(basename $(pwd))" = "task2" ]; then cd ../task1; else cd StuckSnake/task1; fi
## Windows PowerShell
if ((Split-Path -Leaf (Get-Location)) -eq "task2") { cd ../task1 } else { cd StuckSnake/task1 }

# 运行游戏
python Snake_instant_move.py
```

## 你的任务

- 在不影响功能的前提下，调试、检查代码中的可能Bug
- 在检查代码过程中，如果发现其他代码问题或潜在风险，修复并报告

## 参考文档

[Pygame Front Page pygame v2.6.0 documentation](https://www.pygame.org/docs/)

[PYGAME主页 pygame v2.1.3 documentation](https://www.osgeo.cn/pygame/) （版本稍早）
