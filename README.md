# Python3 基础学习

- [python3 官网](https://www.python.org/)
- [python3 菜鸟教程](https://www.runoob.com/python3/python3-tutorial.html)
- [python3 廖雪峰教程](https://www.liaoxuefeng.com/wiki/1016959663602400)

**Python3 基础学习进展是根据[python3 菜鸟教程](https://www.runoob.com/python3/python3-tutorial.html)步骤进行的。**

## 基础环境

### 安装Python和虚拟环境

确保你已经安装了Python 3.8或更高版本。你可以从Python官方网站下载并安装。

1.创建虚拟环境

```shell
python -m venv .venv
```

2.激活虚拟环境

```shell
  # Windows:
  .venv\Scripts\activate
  # macOS/Linux:
  source .venv/bin/activate
```

3.安装Python依赖

```shell
cd example-frontend
pip install -r requirements.txt
```