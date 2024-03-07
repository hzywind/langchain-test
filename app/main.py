# 导入FastAPI
from fastapi import FastAPI

# 创建一个FastAPI实例
app = FastAPI()

# 定义一个路由
@app.get("/")
async def read_root(name: str = None):
    if name:
        message = f"Hello World, {name}!"
    else:
        message = "Hello World"
    return {"message": message}
