from fastapi import FastAPI, HTTPException from pydantic import BaseModel import openai import os import requests

app = FastAPI()

Configuration

N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL") openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatRequest(BaseModel): message: str user_id: str

@app.post("/chat") async def chat_endpoint(request: ChatRequest): try: # 1. Process with GPT response = openai.chat.completions.create( model="gpt-4o", messages=[ {"role": "system", "content": "You are a helpful business assistant. Identify if the user wants to book a demo."}, {"role": "user", "content": request.message} ] ) ai_message = response.choices[0].message.content

    # 2. Check for Lead Intent and trigger n8n
    if "demo" in ai_message.lower() or "book" in ai_message.lower():
        requests.post(N8N_WEBHOOK_URL, json={
            "user_id": request.user_id,
            "intent": "demo_request",
            "raw_query": request.message
        })

    return {"reply": ai_message}
except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))


if name == "main": import uvicorn uvicorn.run(app, host="0.0.0.0", port=8000)