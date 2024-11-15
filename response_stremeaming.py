import asyncio
from fastapi import FastAPI
app = FastAPI()
from fastapi.responses import StreamingResponse
async def generate_data():
    for i in range(1, 6):
        yield f"data: Parte {i} \n\n".encode()
        await asyncio.sleep(1)  

@app.post("/stream")
async def stream_data():
    return StreamingResponse(generate_data(),media_type='text/event-stream')



