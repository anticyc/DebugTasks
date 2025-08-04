# Debug Tasks

## 在开始之前：依赖安装

如果选择在python环境中直接安装：

```bash
pip install -r requirements.txt
# 检验环境配置成功
python PkgCheck.py
```

如果选择在conda环境下安装：

```bash
conda env create -f environment.yml
conda activate codeDebug
python PkgCheck.py
```

Package Check: 若所有依赖均已成功安装，会提示“所有依赖均已成功安装！”

在结束后如果需要删除conda环境，可以使用：

```bash
conda deactivate
conda env remove -n codeDebug -y
```
