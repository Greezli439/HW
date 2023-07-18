from src.routes import contacts
import redis.asyncio as redis
from fastapi_limiter import FastAPILimiter
from fastapi.middleware.cors import CORSMiddleware


from fastapi import FastAPI
from fastapi.security import HTTPBearer
from src.conf.config import settings
from src.routes import auth, users

origins = [
    "http://localhost:3000"
    ]


app = FastAPI()
app.include_router(contacts.router, prefix='/api')
app.include_router(auth.router, prefix='/api')
app.include_router(users.router, prefix='/api')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBearer()


@app.on_event("startup")
async def startup():
    """
    For start redis. Redis is started for limiting connection and protected DDOS.

    :return: None
    """
    r = await redis.Redis(host=settings.redis_host, port=settings.redis_port, db=0, encoding="utf-8",
                          decode_responses=True)
    await FastAPILimiter.init(r)
