from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def read_root():
    container_id = socket.gethostname()
    return {
        "message": "Halo! Aplikasi FastAPI merespons.",
        "container_id": container_id
    }
