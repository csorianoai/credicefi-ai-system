from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI(title="Nadaki AI API", version="1.0.0")

@app.get("/", response_class=HTMLResponse)
@app.head("/")
def dashboard():
    try:
        with open("nadaki_dashboard.html", "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"<h1>Error cargando dashboard</h1><p>{e}</p>"

@app.get("/health")
@app.head("/health")
def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/api/demo")
def demo():
    return {"message": "Nadaki funcionando", "status": "success"}
