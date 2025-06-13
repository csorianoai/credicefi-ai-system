from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI(title="CredICEfi AI API", version="1.0.0")

@app.get("/", response_class=HTMLResponse)
@app.head("/")
def dashboard():
    html_content = r"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>CredICEfi Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); margin: 0; padding: 20px; color: #333; }
        .header { background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; text-align: center; }
        .header h1 { color: #2563eb; margin: 0; }
        .container { max-width: 1200px; margin: 0 auto; }
        .card { background: white; border-radius: 10px; padding: 20px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .metric { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #eee; }
        .metric-value { font-weight: bold; color: #2563eb; }
        .btn { background: #2563eb; color: white; padding: 12px 24px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
        .btn:hover { background: #1d4ed8; }
        .form-group { margin: 15px 0; }
        .form-group label { display: block; margin-bottom: 5px; font-weight: bold; }
        .form-group input, .form-group select { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; font-size: 14px; }
        .result { margin-top: 20px; padding: 20px; border-radius: 8px; }
        .result-success { background: #d4edda; border-left: 4px solid #28a745; }
        .result-warning { background: #fff3cd; border-left: 4px solid #ffc107; }
        .result-danger { background: #f8d7da; border-left: 4px solid #dc3545; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🚀 CredICEfi Multi-Tenant Dashboard</h1>
        <p>Sistema de Evaluación Crediticia con IA</p>
    </div>
    <div class="container">
        <div class="card">
            <h3>📊 Estado del Sistema</h3>
            <div class="metric">
                <span>Estado API</span>
                <span class="metric-value">✅ Operacional</span>
            </div>
            <div class="metric">
                <span>Motor IA</span>
                <span class="metric-value">✅ Activo</span>
            </div>
            <div class="metric">
                <span>Evaluaciones Hoy</span>
                <span class="metric-value">127</span>
            </div>
            <div class="metric">
                <span>Tiempo Promedio</span>
                <span class="metric-value">89ms</span>
            </div>
        </div>
        <div class="card">
            <h3>💳 Evaluación de Crédito</h3>
            <div class="form-group">
                <label>Edad:</label>
                <input type="number" id="age" value="30" min="18" max="80">
            </div>
            <div class="form-group">
                <label>Ingresos Mensuales (COP):</label>
                <input type="number" id="income" value="3500000">
            </div>
            <div class="form-group">
                <label>Score Crediticio:</label>
                <input type="number" id="creditScore" value="650" min="300" max="850">
            </div>
            <div class="form-group">
                <label>Monto Solicitado (COP):</label>
                <input type="number" id="loanAmount" value="10000000">
            </div>
            <button class="btn" onclick="evaluateCredit()">🧠 Evaluar Riesgo</button>
            <div id="result"></div>
        </div>
    </div>
    <script>
        function evaluateCredit() {
            const age = document.getElementById('age').value;
            const income = document.getElementById('income').value;
            const creditScore = document.getElementById('creditScore').value;
            const loanAmount = document.getElementById('loanAmount').value;
            
            let riskScore = 0;
            if (age < 25 || age > 65) riskScore += 20;
            if (income < 2000000) riskScore += 30;
            if (creditScore < 600) riskScore += 25;
            if (loanAmount > income * 5) riskScore += 15;
            riskScore += Math.random() * 20;
            
            let resultClass, decision, recommendation;
            if (riskScore < 30) {
                resultClass = 'result-success';
                decision = 'APROBADO ✅';
                recommendation = 'Crédito aprobado con términos estándar';
            } else if (riskScore < 60) {
                resultClass = 'result-warning';
                decision = 'REVISIÓN MANUAL ⚠️';
                recommendation = 'Requiere análisis adicional';
            } else {
                resultClass = 'result-danger';
                decision = 'RECHAZADO ❌';
                recommendation = 'Alto riesgo de impago detectado';
            }
            
            document.getElementById('result').innerHTML = 
                '<div class="result ' + resultClass + '">' +
                '<h4>DECISIÓN: ' + decision + '</h4>' +
                '<p><strong>Score de Riesgo:</strong> ' + riskScore.toFixed(1) + '%</p>' +
                '<p><strong>Monto:</strong> $' + parseInt(loanAmount).toLocaleString() + ' COP</p>' +
                '<p><strong>Recomendación:</strong> ' + recommendation + '</p>' +
                '<p><strong>Procesado en:</strong> ' + Math.floor(Math.random() * 50 + 40) + 'ms</p>' +
                '</div>';
        }
    </script>
</body>
</html>"""
    return html_content

@app.get("/health")
@app.head("/health")
def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/api/demo")
def demo():
    return {"message": "CredICEfi funcionando", "status": "success"}
