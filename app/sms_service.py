import asyncio

async def send_sms(to, message, metadata):
    await asyncio.sleep(0.3)
    print(f"[SMS] to={to} message={message[:40]}")
    return {"status":"sent"}