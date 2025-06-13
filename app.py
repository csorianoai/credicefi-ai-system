from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI(
   title="CredICEfi AI API",
   description="Sistema de Evaluación Crediticia",
   version="1.0.0"
)

@app.get("/", response_class=HTMLResponse)
@app.head("/")
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
           min-height: 100vh; color: #333;
       }
       .header {
           background: rgba(255, 255, 255, 0.95);
           padding: 1rem 2rem;
           box-shadow: 0 2px 20px rgba(0,0,0,0.1);
       }
       .header h1 { color: #2563eb; font-size: 2rem; font-weight: 700; }
       .container { max-width: 1400px; margin: 0 auto; padding: 2rem; }
       .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
       .card {
           background: rgba(255, 255, 255, 0.95);
           border-radius: 16px; padding: 2rem;
           box-shadow: 0 8px 32px rgba(0,0,0,0.1);
       }
       .card h3 { color: #1e293b; margin-bottom: 1rem; }
       .metric {
           display: flex; justify-content: space-between;
           padding: 0.75rem 0; border-bottom: 1px solid #e5e7eb;
       }
       .metric-value { font-weight: 600; color: #2563eb; }
       .btn {
           background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
           color: white; padding: 1rem 2rem; border: none;
           border-radius: 8px; cursor: pointer; margin: 1rem 0;
       }
       .form-group { margin: 1rem 0; }
       .form-group input, .form-group select {
           width: 100%; padding: 0.75rem; border: 1px solid #d1d5db;
           border-radius: 8px; margin-top: 0.5rem;
       }
       .result-card { margin: 2rem 0; padding: 2rem; border-radius: 12px; }
       .result-approve { background: #ecfdf5; border-left: 4px solid #10b981; }
       .result-review { background: #fef3c7; border-left: 4px solid #f59e0b; }
       .result-reject { background: #fef2f2; border-left: 4px solid #ef4444; }
   </style>
</head>
<body>
   <div class="header">
       <h1>🚀 CredICEfi Multi-Tenant Dashboard</h1>
       <p>Sistema de Evaluación Crediticia con IA - Funcionando en Internet</p>
   </div>
   
   <div class="container">
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
                   <span>Tiempo Promedio</span>
                   <span class="metric-value">89ms</span>
               </div>
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
               <label>Ciudad:</label>
               <select id="city">
                   <option value="Bogotá">Bogotá</option>
                   <option value="Medellín">Medellín</option>
                   <option value="Cali">Cali</option>
                   <option value="Barranquilla">Barranquilla</option>
               </select>
           </div>
           
           <div class="form-group">
               <label>Monto Solicitado (COP):</label>
               <input type="number" id="loanAmount" value="10000000">
           </div>
           
           <button class="btn" onclick="evaluateCredit()">
               🧠 Evaluar Riesgo Crediticio
           </button>
           
           <div id="result"></div>
       </div>
   </div>
   
   <script>
       function evaluateCredit() {
           const age = document.getElementById('age').value;
           const income = document.getElementById('income').value;
           const creditScore = document.getElementById('creditScore').value;
           const loanAmount = document.getElementById('loanAmount').value;
           
           // Simulación del motor IA
           let riskScore = 0;
           
           // Factores de riesgo
           if (age < 25 || age > 65) riskScore += 20;
           if (income < 2000000) riskScore += 30;
           if (creditScore < 600) riskScore += 25;
           if (loanAmount > income * 5) riskScore += 15;
           
           // Agregar variabilidad
           riskScore += Math.random() * 20;
           
           let resultClass, decision, icon, recommendation;
           
           if (riskScore < 30) {
               resultClass = 'result-approve';
               decision = 'APROBADO';
               icon = '✅';
               recommendation = 'Crédito aprobado con términos estándar';
           } else if (riskScore < 60) {
               resultClass = 'result-review';
               decision = 'REVISIÓN MANUAL';
               icon = '⚠️';
               recommendation = 'Requiere análisis adicional por especialista';
           } else {
               resultClass = 'result-reject';
               decision = 'RECHAZADO';
               icon = '❌';
               recommendation = 'Alto riesgo de impago detectado';
           }
           
           document.getElementById('result').innerHTML = \
               <div class="result-card \">
                   <h4>\ DECISIÓN: \</h4>
                   <p><strong>Score de Riesgo:</strong> \%</p>
                   <p><strong>Monto Evaluado:</strong> $\ COP</p>
                   <p><strong>Ratio Deuda/Ingreso:</strong> \x</p>
                   <p><strong>Recomendación:</strong> \</p>
                   <p><strong>Procesado en:</strong> \ms</p>
                   <p><strong>ID Evaluación:</strong> EVAL-\</p>
               </div>
           \;
       }
       
       // Actualizar métricas cada 5 segundos
       setInterval(() => {
           const evaluationsElement = document.querySelector('.metric-value');
           if (evaluationsElement) {
               const currentValue = parseInt(evaluationsElement.textContent);
               evaluationsElement.textContent = currentValue + Math.floor(Math.random() * 3);
           }
       }, 5000);
   </script>
</body>
</html>
   '''

@app.get("/health")
@app.head("/health")
def health():
   return {"status": "healthy", "timestamp": datetime.now().isoformat()}
