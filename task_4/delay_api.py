from fastapi import FastAPI, HTTPException
import asyncio
import time

app = FastAPI(title="Сервис задержек")

@app.get("/ping")
async def ping():
    return {"status": "ok"}

@app.get("/delay/{seconds}")
async def delay_path(seconds: float):
    if not (0 <= seconds <= 10):
        raise HTTPException(status_code=400, detail="Ошибка задержка от 0 до 10 сек")
    
    start = time.perf_counter()
    await asyncio.sleep(seconds)
    return {
        "seconds": seconds,
        "time": round(time.perf_counter() - start, 4)
    }

@app.get("/delay")
async def delay_query(seconds: float, label: str):
    if not (0 <= seconds <= 10):
        raise HTTPException(status_code=400, detail="Ошибка задержка от 0 до 10 сек")
    
    start = time.perf_counter()
    await asyncio.sleep(seconds)
    return {
        "label": label,
        "seconds": seconds,
        "time": round(time.perf_counter() - start, 4)
    }
