# Just a test python pro.

## begin
cd 当前工程目录

### 虚拟环境
````
virtualenv .venv           # 安装名为.venv的虚拟环境
source .venv/bin/activate  # 进入虚拟环境
```

### 安装依赖
```
pip install pip==8.1.1     # 更新pip到8.1.1版本
pip install -r requirements.txt --trusted-host pypi.doubanio.com -i http://pypi.doubanio.com/simple/ # 从指定源(豆瓣)安装依赖

python setup.py install
```

### 运行
```
gunicorn --paste=etc/development/app.conf
```

### 访问
```
127.0.0.1:8000
```
