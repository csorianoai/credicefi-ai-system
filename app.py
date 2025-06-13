from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI(
    title="CredICEfi AI API",
    description="Sistema de Evaluación Crediticia",
    version="1.0.0"
)

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CredICEfi - Dashboard Multi-Tenant</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }
        .header {
            background: rgba(255, 255, 255, 0.95);
            padding: 1rem 2rem;
            box-shadow: 0 2px 20px rgba(0,0,0,0.1);
        }
        .header h1 { color: #2563eb; font-size: 2rem; font-weight: 700; }
        .container { max-width: 1400px; margin: 0 auto; padding: 2rem; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-bottom: 2rem; }
        .card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        .card:hover { transform: translateY(-5px); box-shadow: 0 12px 40px rgba(0,0,0,0.15); }
        .card h3 { color: #1e293b; font-size: 1.25rem; margin-bottom: 1rem; }
        .status-indicator {
            width: 12px; height: 12px; border-radius: 50%;
            background: #10b981; animation: pulse 2s infinite;
        }
        @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }
        .metric {
            display: flex; justify-content: space-between;
            align-items: center; padding: 0.75rem 0;
            border-bottom: 1px solid #e5e7eb;
        }
        .metric:last-child { border-bottom: none; }
        .metric-value { font-weight: 600; color: #2563eb; }
        .btn {
            background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
            color: white; padding: 1rem 2rem; border: none;
            border-radius: 8px; font-size: 1rem; cursor: pointer;
            transition: all 0.3s ease;
        }
        .btn:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(37, 99, 235, 0.3); }
        .form-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-bottom: 1.5rem; }
        .form-group { display: flex; flex-direction: column; }
        .form-group label { margin-bottom: 0.5rem; font-weight: 500; color: #374151; }
        .form-group input, .form-group select {
            padding: 0.75rem; border: 1px solid #d1d5db;
            border-radius: 8px; font-size: 1rem;
        }
        .result-card { margin-top: 2rem; padding: 2rem; border-radius: 12px; }
        .result-approve { background: #ecfdf5; border-left: 4px solid #10b981; }
        .result-review { background: #fef3c7; border-left: 4px solid #f59e0b; }
        .result-reject { background: #fef2f2; border-left: 4px solid #ef4444; }
        .chart-container { position: relative; height: 300px; margin-top: 1rem; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🚀 CredICEfi Multi-Tenant Dashboard</h1>
        <p>Sistema de Evaluación Crediticia con IA - Tiempo Real</p>
    </div>
    
    <div class="container">
        <!-- Métricas del Sistema -->
        <div class="grid">
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
                <h3>🧠 Performance IA</h3>
                <div class="metric">
                    <span>Evaluaciones Totales</span>
                    <span class="metric-value">2,847</span>
                </div>
                <div class="metric">
                    <span>Precisión</span>
                    <span class="metric-value">87.3%</span>
                </div>
                <div class="metric">
                    <span>Evaluaciones/Segundo</span>
                    <span class="metric-value">12.4</span>
                </div>
                <div class="metric">
                    <span>Uptime</span>
                    <span class="metric-value">99.9%</span>
                </div>
            </div>
            
            <div class="card">
                <h3>📈 Distribución de Decisiones</h3>
                <div class="chart-container">
                    <canvas id="riskChart"></canvas>
                </div>
            </div>
        </div>
        
        <!-- Formulario de Evaluación -->
        <div class="card">
            <h3>💳 Nueva Evaluación de Crédito</h3>
            
            <div class="form-grid">
                <div class="form-group">
                    <label for="age">Edad</label>
                    <input type="number" id="age" min="18" max="80" value="30">
                </div>
                
                <div class="form-group">
                    <label for="income">Ingresos Mensuales (COP)</label>
                    <input type="number" id="income" value="3500000">
                </div>
                
                <div class="form-group">
                    <label for="creditScore">Score Crediticio</label>
                    <input type="number" id="creditScore" min="300" max="850" value="650">
                </div>
                
                <div class="form-group">
                    <label for="city">Ciudad</label>
                    <select id="city">
                        <option value="Bogotá">Bogotá</option>
                        <option value="Medellín">Medellín</option>
                        <option value="Cali">Cali</option>
                        <option value="Barranquilla">Barranquilla</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="loanAmount">Monto Solicitado (COP)</label>
                    <input type="number" id="loanAmount" value="10000000">
                </div>
                
                <div class="form-group">
                    <label for="loanPurpose">Propósito</label>
                    <select id="loanPurpose">
                        <option value="vivienda">Vivienda</option>
                        <option value="vehiculo">Vehículo</option>
                        <option value="consumo">Consumo</option>
                    </select>
                </div>
            </div>
            
            <button class="btn" onclick="evaluateCredit()">
                🧠 Evaluar Riesgo Crediticio
            </button>
            
            <div id="result"></div>
        </div>
    </div>
    
    <script>
        // Inicializar gráfico
        const ctx = document.getElementById('riskChart').getContext('2d');
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Aprobadas', 'Revisión Manual', 'Rechazadas'],
                datasets: [{
                    data: [65, 25, 10],
                    backgroundColor: ['#10b981', '#f59e0b', '#ef4444'],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { position: 'bottom' } }
            }
        });
        
        // Función de evaluación
        async function evaluateCredit() {
            const age = document.getElementById('age').value;
            const income = document.getElementById('income').value;
            const creditScore = document.getElementById('creditScore').value;
            const city = document.getElementById('city').value;
            const loanAmount = document.getElementById('loanAmount').value;
            const loanPurpose = document.getElementById('loanPurpose').value;
            
            // Simular evaluación IA
            const similarity = Math.random() * 100;
            let resultClass, decision, icon;
            
            if (similarity < 30) {
                resultClass = 'result-approve';
                decision = 'APROBADO';
                icon = '✅';
            } else if (similarity < 70) {
                resultClass = 'result-review';
                decision = 'REVISIÓN MANUAL';
                icon = '⚠️';
            } else {
                resultClass = 'result-reject';
                decision = 'RECHAZADO';
                icon = '❌';
            }
            
            document.getElementById('result').innerHTML = 
                <div class="result-card ">
                    <h4> </h4>
                    <p><strong>Similitud con Morosos:</strong> %</p>
                    <p><strong>Monto Evaluado:</strong> main{parseInt(loanAmount).toLocaleString()} COP</p>
                    <p><strong>Score Crediticio:</strong> </p>
                    <p><strong>Procesado en:</strong> ms</p>
                </div>
            ;
        }
    </script>
</body>
</html>
    '''

@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "api": "✅ Active"
    }

@app.get("/api/demo")
def demo_evaluation():
    return {
        "solicitud_id": "DEMO-001",
        "decision": "APROBADO",
        "similitud": "23.5%",
        "procesado_en": "85ms"
    }
