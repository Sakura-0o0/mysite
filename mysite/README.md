# mysite

基于 **Django 5.2** 的一个学习型 Web 项目，用来练习 Django 的路由、视图、模板渲染、表单提交、ORM 增删改查，以及调用第三方天气 API。项目里还附带一个 **B 站爬虫脚本**，用于演示 `requests` 会话与带 Cookie 的接口请求。

> 本项目为学习练习用途，部分页面和代码保留了实验痕迹。

## 功能概览

| 路由 | 功能 | 说明 |
| --- | --- | --- |
| `/index/` | 欢迎页 | 返回纯文本“欢迎使用” |
| `/user/list/` / `/user/add/` | 用户页 | 静态模板练习 |
| `/login/` | 登录 | POST 表单校验（`root` / `123`），成功跳转 |
| `/info/list/` | 用户信息列表 | 展示数据库中 `UserInfo` 数据 |
| `/info/add/` | 添加用户 | 表单提交写入数据库 |
| `/info/delete/` | 删除用户 | 按 `nid` 删除记录 |
| `/weather/` | 成都实时天气 | 调用 Open-Meteo API 获取并展示 |
| `/orm/` | ORM 练习 | 展示 ORM 增删改查用法（部分为注释示例） |
| `/tpl/` / `/something/` | 模板 / 跳转 | 模板语法练习与重定向演示 |

### 爬虫脚本 `001.py`

使用 `requests.Session` 保持会话，携带自定义请求头与 Cookie，依次请求 B 站三个接口：

1. `nav` — 验证登录状态
2. `space/myinfo` — 获取个人基础信息
3. `relation/stat` — 获取关注 / 粉丝数据

## 技术栈

- **后端框架**：Django 5.2.3
- **数据库**：MySQL（经 Django ORM 访问）
- **外部 API**：Open-Meteo（天气）、Bilibili（爬虫脚本）
- **爬虫库**：requests

## 项目结构

```
mysite/
├── manage.py              # Django 管理入口
├── mysite/                # 项目配置
│   ├── settings.py        # 配置（数据库、应用等）
│   ├── urls.py            # 总路由
│   └── wsgi.py / asgi.py  # 部署入口
├── myapp/                 # 应用
│   ├── views.py           # 视图函数（页面逻辑）
│   ├── models.py          # 数据模型（UserInfo / Department）
│   ├── templates/         # HTML 模板
│   ├── static/            # 静态资源（css/js/img）
│   └── migrations/        # 数据库迁移文件
├── 001.py                 # B 站爬虫脚本
└── db.sqlite3             # SQLite 数据库（当前为空）
```

## 快速开始

### 1. 环境要求

- Python 3.10+
- MySQL（本地或远程）
- pip

### 2. 安装依赖

```bash
pip install django requests
```

### 3. 配置数据库

`mysite/settings.py` 中已配置为 MySQL，请按本机环境修改（注意文件里有一处被覆盖的 SQLite 配置，以 MySQL 为准）：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite2',        # 数据库名，需先在 MySQL 中创建
        'USER': 'root',
        'PASSWORD': '123456',     # 请改成你自己的密码
        'HOST': 'localhost',
        'PORT': 3306,
    }
}
```

> 若本地没有 MySQL，可改回 SQLite：
> ```python
> DATABASES = {
>     'default': {
>         'ENGINE': 'django.db.backends.sqlite3',
>         'NAME': BASE_DIR / 'db.sqlite3',
>     }
> }
> ```

### 4. 执行数据库迁移

```bash
python manage.py makemigrations myapp
python manage.py migrate
```

### 5. 启动服务

```bash
python manage.py runserver
```

浏览器访问 http://127.0.0.1:8000/index/

## 使用说明

- 登录账号：`root`，密码：`123`（见 `views.py` 的 `login` 函数）
- 天气功能依赖外网访问 `api.open-meteo.com`，首次使用请确认网络可达并已安装 `requests`
- `/info/*` 系列页面读写的是 `UserInfo` 表，可通过页面直接增删数据

## 数据库模型

`myapp/models.py` 定义了两个模型：

- **UserInfo**：`name`（用户名）、`password`（密码）、`age`（年龄，默认 2）
- **Department**：`title`（部门名称）

## ⚠️ 重要安全提醒

- **`settings.py` 中的数据库密码（root / 123456）是明文写死的，上传 GitHub 前请务必修改或改用环境变量读取。**
- **`001.py` 中包含真实的 B 站登录 Cookie（SESSDATA、bili_jct 等）和个人 UID，属敏感凭据，强烈建议上传前删除该 Cookie 信息或整个文件，以免泄露账号相关信息。**
- `SECRET_KEY` 为开发密钥，生产环境需更换。

## License

本项目仅供学习交流使用。
