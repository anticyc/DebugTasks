# 确认requirements.txt中的包是否已安装
import subprocess

with open('requirements.txt', 'r') as f:
    packages = [line.strip() for line in f]
    not_installed = []
    
    for package in packages:
        try:
            subprocess.check_output(['pip', 'show', package])
        except subprocess.CalledProcessError:
            not_installed.append(package)
    
    if not not_installed:
        print("所有依赖均已成功安装！")
    else:
        print("以下依赖未成功安装：")
        for package in not_installed:
            print(f"- {package}")
