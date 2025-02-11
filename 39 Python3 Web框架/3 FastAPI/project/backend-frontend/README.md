# Python3 + FastAPI + SQLite + Vue3

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

### 安装Node.js和npm

确保你已经安装了Node.js和npm。你可以从Node.js官方网站下载并安装。

构建前端

```shell
cd example-frontend/frontend
npm install
```

构建前端项目

```shell
npm run build
```

## 项目结构

> 通过启动main.py即可实现统一端口访问前后端程序，我们可以使用FastAPI的静态文件服务功能来提供前端文件。

```text
project/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI应用入口
│   │   ├── models.py        # 数据库模型定义
│   │   ├── schemas.py       # 数据验证和序列化模式
│   │   ├── crud.py          # CRUD操作
│   │   ├── database.py      # 数据库配置
│   │   ├── routers/         # API路由
│   │   │   ├── __init__.py
│   │   │   ├── users.py     # 用户相关的API路由
│   │   │   ├── files.py     # 文件相关的API路由
│   │   ├── tests/           # 单元测试
│   │   │   ├── __init__.py
│   │   │   ├── test_main.py # 测试用例
│   ├── frontend/
│   │   ├── public/          # 公共静态文件
│   │   ├── src/
│   │   │   ├── assets/      # 静态资源（如图片、字体等）
│   │   │   ├── components/  # Vue组件
│   │   │   ├── views/       # 页面视图
│   │   │   ├── router/      # Vue路由配置
│   │   │   ├── store/       # Vuex状态管理（如果有）
│   │   │   ├── App.vue      # 根组件
│   │   │   ├── main.js      # Vue应用入口
│   │   ├── package.json     # 项目依赖和脚本
│   ├── requirements.txt     # Python依赖
```

## 代码实现

### 后端部分

```python
# example-frontend/app/main.py
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from . import models, database
from .routers import users, files

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(files.router)

# Mount the frontend static files
app.mount("/static", StaticFiles(directory="example-frontend/frontend/dist"), name="static")


# Serve the frontend index.html for all other routes
@app.get("/{full_path:path}", response_class=HTMLResponse)
async def read_index(request: Request, full_path: str):
    with open("example-frontend/frontend/dist/index.html") as f:
        return HTMLResponse(content=f.read())
```

requirements.txt

```text
fastapi
uvicorn
sqlalchemy
sqlite3
pydantic
python-multipart
```

### 前端部分

安装依赖并构建前端

```shell
cd example-frontend/frontend
npm install vue@^3.0.0 vue-router@^4.0.0 axios

npm run build
```

main.js

```javascript
// example-frontend/frontend/src/main.js
import {createApp} from 'vue'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app')
```

router/index.js

```javascript
// example-frontend/frontend/src/router/index.js
import {createRouter, createWebHistory} from 'vue-router'
import Users from '../views/Users.vue'
import Files from '../views/Files.vue'

const routes = [
    {
        path: '/',
        name: 'Users',
        component: Users
    },
    {
        path: '/files',
        name: 'Files',
        component: Files
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router

```

views/Users.vue

```javascript
<!-- example-frontend/frontend/src/views/Users.vue -->
<template>
    <div>
        <h1>Users</h1>
        <ul>
            <li v-for="user in users"
            :key="user.id">{{user.username}} - {{user.email}}
        </li>
    </ul>
</div>
</template>

<script>
    import axios from 'axios'

    export default {
    data() {
    return {
    users: []
}
},
    async created() {
    const response = await axios.get('/users/')
    this.users = response.data
}
}
</script>

```

views/Files.vue

```javascript
<!-- example-frontend/frontend/src/views/Files.vue -->
<template>
    <div>
        <h1>Files</h1>
        <ul>
            <li v-for="file in files"
            :key="file.id">{{file.filename}}
        </li>
    </ul>
    <input type="file"
    @change="uploadFile">
</div>
</template>

<script>
    import axios from 'axios'

    export default {
    data() {
    return {
    files: []
}
},
    async created() {
    const response = await axios.get('/files/')
    this.files = response.data
},
    methods: {
    async uploadFile(event) {
    const file = event.target.files[0]
    const formData = new FormData()
    formData.append('file', file)
    await axios.post('/files/', formData, {
    headers: {
    'Content-Type': 'multipart/form-data'
}
})
    this.files = (await axios.get('/files/')).data
}
}
}
</script>

```

package.json

```json
{
  "name": "frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "serve": "vue-cli-service serve",
    "build": "vue-cli-service build",
    "lint": "vue-cli-service lint",
    "test:unit": "vue-cli-service test:unit"
  },
  "dependencies": {
    "axios": "^0.21.1",
    "core-js": "^3.6.5",
    "vue": "^3.0.0",
    "vue-router": "^4.0.0"
  },
  "devDependencies": {
    "@vue/cli-plugin-babel": "~4.5.0",
    "@vue/cli-plugin-eslint": "~4.5.0",
    "@vue/cli-plugin-unit-jest": "~4.5.0",
    "@vue/cli-service": "~4.5.0",
    "@vue/compiler-sfc": "^3.0.0",
    "babel-eslint": "^10.1.0",
    "eslint": "^6.7.2",
    "eslint-plugin-vue": "^7.0.0",
    "jest": "^24.9.0"
  }
}

```

重新安装依赖

```shell
cd example-frontend/frontend
rm -rf node_modules package-lock.json
npm install

```

## 运行项目

1.构建前端

```shell
   cd example-frontend/frontend
   npm run build
```

2.启动后端

```shell
   cd example-frontend/app
   uvicorn main:app --reload
```

3.访问应用

```text
打开浏览器，访问 http://localhost:8000，你应该能够看到前端页面，并且能够通过API与后端进行交互。
```

这样，通过启动main.py，你就可以在同一个端口（默认是8000）上访问前后端程序。前端文件会被FastAPI的静态文件服务提供，而API请求会由FastAPI处理。