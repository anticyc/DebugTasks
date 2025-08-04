# 贪吃蛇之重玩错误

在本**贪吃蛇游戏**实例中，有一个致命的错误：预设的 **“按C重玩”** 并不能起到预期效果。请仔细阅读代码，找到错误的根源并编辑代码解决故障。

## 故障重现

在命令行中执行以下指令，以安装依赖并运行游戏。

```bash
# 切换目录
## Bash (Linux/macOS/Git Bash/WSL)
if [ "$(basename $(pwd))" = "task1" ]; then cd ../task2; else cd StuckSnake/task2; fi
## Windows PowerShell
if ((Split-Path -Leaf (Get-Location)) -eq "task1") { cd ../task2 } else { cd StuckSnake/task2 }

# 运行游戏
python ./Snake_retry_failure.py
```

## 你的任务

- 在不影响功能的前提下，修复代码中的Bug
- 在检查代码过程中，如果发现其他代码问题或潜在风险，修复并报告

## 参考文档

[Pygame Front Page pygame v2.6.0 documentation](https://www.pygame.org/docs/)

[PYGAME主页 pygame v2.1.3 documentation](https://www.osgeo.cn/pygame/) （版本稍早）
