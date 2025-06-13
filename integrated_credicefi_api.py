from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI(title="CredICEfi AI API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "message": "🚀 CredICEfi Multi-Tenant AI API - FUNCIONANDO!",
        "status": "✅ OPERATIONAL", 
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0-deployment"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "api": "✅ Active",
        "system": "✅ Ready"
    }

@app.get("/demo")
def demo_evaluation():
    return {
        "applicant": "Demo User",
        "risk_level": "LOW", 
        "decision": "APPROVE",
        "similarity": 25.5,
        "message": "🎉 CredICEfi funcionando en internet!"
    }
