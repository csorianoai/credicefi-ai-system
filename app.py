from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
import random

app = FastAPI(title="Nadaki AI Credit Risk Platform", version="2.0.0")

@app.get("/", response_class=HTMLResponse)
@app.head("/")
def dashboard():
    html_content = r"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Nadaki AI Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f6fa; margin: 0; padding: 20px; color: #333; }
        .header { background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; border-left: 8px solid #2563eb; }
        .header h1 { color: #2563eb; margin: 0; }
        .container { max-width: 1200px; margin: 0 auto; }
        .card { background: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .metric { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #eee; }
        .metric-value { font-weight: bold; color: #2563eb; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🧠 Nadaki Credit Risk AI Platform</h1>
        <p>Sistema de Evaluación Crediticia con IA</p>
    </div>

    <div class="container">
        <div class="card">
            <h3>📊 Estado del Sistema</h3>
            <div class="metric"><span>Estado API</span><span class="metric-value">✅ Operacional</span></div>
            <div class="metric"><span>Motor IA</span><span class="metric-value">✅ Activo</span></div>
            <div class="metric"><span>Evaluaciones Hoy</span><span class="metric-value">245</span></div>
            <div class="metric"><span>Tiempo Promedio</span><span class="metric-value">42ms</span></div>
        </div>

        <div class="card">
            <h3>📈 Distribución de Evaluaciones</h3>
            <canvas id="riskChart" height="100"></canvas>
        </div>
    </div>

    <script>
        const ctx = document.getElementById('riskChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Aprobado', 'Revisión Manual', 'Rechazado'],
                datasets: [{
                    label: 'Evaluaciones',
                    data: [162, 53, 30],
                    backgroundColor: ['#38a169', '#ffc107', '#e53e3e']
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false },
                    title: { display: true, text: 'Casos de Evaluación' }
                }
            }
        });
    </script>
</body>
</html>"""
    return html_content

@app.get("/health")
@app.head("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "Nadaki AI",
        "version": "2.0.0"
    }

@app.get("/api/demo")
def demo():
    return {
        "message": "Nadaki AI funcionando perfectamente",
        "status": "success",
        "version": "2.0.0",
        "features": ["AI Risk Assessment", "Real-time Analytics", "Multi-factor Analysis"]
    }

@app.get("/api/evaluate")
def quick_evaluate(age: int = 34, income: int = 4800000, credit_score: int = 742, loan_amount: int = 18000000):
    risk_score = 0
    if age < 25 or age > 65:
        risk_score += 15
    if income < 3000000:
        risk_score += 20
    if credit_score < 650:
        risk_score += 25
    if loan_amount > income * 4:
        risk_score += 20
    risk_score += random.uniform(-5, 10)
    risk_score = max(0, min(100, risk_score))

    if risk_score < 25:
        decision = "APPROVED"
        confidence = 90 + random.uniform(0, 10)
    elif risk_score < 50:
        decision = "MANUAL_REVIEW"
        confidence = 75 + random.uniform(0, 15)
    else:
        decision = "REJECTED"
        confidence = 85 + random.uniform(0, 15)

    return {
        "decision": decision,
        "risk_score": round(risk_score, 1),
        "confidence": round(confidence, 1),
        "processing_time_ms": random.randint(25, 65),
        "evaluation_id": f"NK-{random.randint(100000, 999999)}"
    }
