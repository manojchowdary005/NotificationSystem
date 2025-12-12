import asyncio

async def send_push(to, message, metadata):
    await asyncio.sleep(0.4)
    print(f"[PUSH] to={to} message={message[:40]}")
    return {"status":"sent"}