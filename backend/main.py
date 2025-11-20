from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.db import init_db
from core.auth.routes import router as auth_router
from lottery.routes import router as lottery_router
from football.routes import router as football_router
from markets.crypto.routes import router as crypto_router
from markets.stocks.routes import router as stocks_router
from casino.routes import router as casino_router
from alerts.service import router as alerts_router
from notifications.service import router as notifications_router
from notifications.service_settings import router as notification_settings_router
from suite.routes import router as suite_router
from chat.ws_chat import router as chat_router

app = FastAPI(title="OracleSuite API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api")
app.include_router(lottery_router, prefix="/api")
app.include_router(football_router, prefix="/api")
app.include_router(crypto_router, prefix="/api")
app.include_router(stocks_router, prefix="/api")
app.include_router(casino_router, prefix="/api")
app.include_router(alerts_router, prefix="/api")
app.include_router(notifications_router, prefix="/api")
app.include_router(notification_settings_router, prefix="/api")
app.include_router(suite_router, prefix="/api")
app.include_router(chat_router)

@app.on_event("startup")
async def on_startup():
    init_db()
