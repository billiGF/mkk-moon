import uvicorn
from fastapi import FastAPI
from src.api.routers import main_router
# from logger import logger



app = FastAPI()
app.include_router(main_router)




if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)