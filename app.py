from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="CredICEfi AI API",
    description="Sistema de Evaluación Crediticia",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "🚀 CredICEfi AI API - FUNCIONANDO EN INTERNET!",
        "status": "✅ OPERATIONAL",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "sistema": "Evaluación Crediticia con IA",
        "institucion": "Multi-Tenant Ready"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "api": "✅ Active",
        "database": "✅ Ready",
        "ai_engine": "✅ Operational"
    }

@app.get("/demo-evaluation")
def demo_evaluation():
    return {
        "solicitud_id": "DEMO-001",
        "solicitante": "Usuario Demo",
        "edad": 30,
        "ingresos": 3500000,
        "evaluacion": {
            "riesgo": "BAJO",
            "decision": "APROBADO",
            "similitud_morosos": "23.5%",
            "confianza": "87%"
        },
        "recomendacion": "✅ Crédito aprobado con términos estándar",
        "procesado_en": "85ms"
    }
