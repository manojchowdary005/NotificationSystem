import asyncio

async def send_email(to, subject, message, metadata):
    await asyncio.sleep(0.5)         #It doesn't block the worker,other tasks can run
    print(f"[EMAIL] to={to} subject={subject} message={message[:40]}")
    return {"status": "sent"}