# FlareAI后端代码

* Dockerfile 使用 poetry 进行 Python 依赖管理

## Poetry 完全入门指南

[Poetry 完全入门指南 链接](https://blog.kyomind.tw/python-poetry/)

## 本地开发环境安装

* 本地安装 poetry 及 python 3.10

* 创建poetry环境 
```shell
poetry env use python3.10
```

* 使用poetry环境
```shell
poetry shell
```

* 安装依赖
```shell
poetry install
```

* 运行 如果是第一次运行 先 退出 poetry，命令 exit。再重新进入poetry环境
```shell
uvicorn flareai.main:app --workers 2 --host 0.0.0.0 --port 7860
```