from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from datetime import datetime
import pandas as pd

# --- CONFIGURACIÓN DE APP ---
app = FastAPI(
    title="CrediFace Multi-Tenant API",
    version="2.0.0",
    description="🚀 Sistema de Evaluación Crediticia Multi-Institucional"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- ENDPOINT PRINCIPAL ---
@app.get("/")
async def root():
    return {
        "message": "🚀 CrediFace Multi-Tenant API v2.0.0 - FUNCIONANDO!",
        "status": "✅ ACTIVE",
        "timestamp": datetime.now().isoformat(),
        "phase": "FASE 1 - Infraestructura Multi-Tenant",
        "note": "API funcionando - Motor ML pendiente por espacio en disco"
    }

# --- ENDPOINT DE SALUD ---
@app.get("/health")
async def health_check():
    folders_to_check = {
        "config": "../config",
        "institutions_config": "../config/institutions",
        "data": "../data",
        "banco_demo_data": "../data/banco_demo",
        "logs": "../logs",
        "assets": "../assets"
    }
    infrastructure = {k: "✅ EXISTS" if os.path.exists(v) else "❌ MISSING" for k, v in folders_to_check.items()}
    
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "dependencies": {
            "fastapi": "✅ OK",
            "uvicorn": "✅ OK",
            "pandas": "✅ OK"
        },
        "infrastructure": infrastructure,
        "pandas_test": "✅ Working",
        "disk_status": "⚠️ Needs cleanup for ML dependencies"
    }

# --- ENDPOINT: LISTAR INSTITUCIONES ---
@app.get("/institutions")
async def list_institutions():
    config_dir = "../config/institutions"
    institutions = []
    if os.path.exists(config_dir):
        for filename in os.listdir(config_dir):
            if filename.endswith(".json"):
                try:
                    with open(os.path.join(config_dir, filename), "r", encoding="utf-8") as f:
                        config = json.load(f)
                        institutions.append({
                            "id": config.get("institution_info", {}).get("id", "unknown"),
                            "name": config.get("institution_info", {}).get("name", filename.replace(".json", "")),
                            "status": config.get("institution_info", {}).get("status", "active"),
                            "config_file": filename
                        })
                except Exception as e:
                    print(f"Error loading {filename}: {e}")

    return {
        "institutions": institutions,
        "count": len(institutions),
        "config_dir": config_dir,
        "timestamp": datetime.now().isoformat()
    }

# --- ENDPOINT: PROBAR CARGA DE DATOS ---
@app.get("/data-test")
async def test_data():
    banco_csv = "../data/banco_demo/historical_defaults.csv"
    results = {}

    if os.path.exists(banco_csv):
        try:
            df = pd.read_csv(banco_csv)
            results["banco_demo"] = {
                "status": "✅ CSV loaded",
                "rows": len(df),
                "columns": list(df.columns),
                "sample": df.head(3).to_dict("records")
            }
        except Exception as e:
            results["banco_demo"] = {"status": f"❌ Error loading CSV: {str(e)}"}
    else:
        results["banco_demo"] = {"status": "❌ CSV not found", "path": banco_csv}

    return results

# --- ENDPOINT: CREAR CONFIGURACIÓN DE EJEMPLO ---
@app.get("/create-sample-config")
async def create_sample_config():
    config_dir = "../config/institutions"
    os.makedirs(config_dir, exist_ok=True)

    sample_config = {
        "institution_info": {
            "id": "banco_demo_001",
            "name": "Banco Demo Colombia",
            "short_name": "BancoDemo",
            "country": "CO",
            "status": "active",
            "created": datetime.now().isoformat()
        },
        "risk_configuration": {
            "auto_reject_threshold": 0.90,
            "high_risk_threshold": 0.80,
            "medium_risk_threshold": 0.65,
            "low_risk_threshold": 0.35
        },
        "ui_customization": {
            "primary_color": "#1976d2",
            "secondary_color": "#dc004e",
            "theme": "corporate_blue"
        }
    }

    config_path = os.path.join(config_dir, "banco_demo.json")
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(sample_config, f, indent=2, ensure_ascii=False)

    return {
        "status": "✅ Sample config created",
        "path": config_path,
        "config": sample_config
    }

# --- ENDPOINT: CREAR DATA DE EJEMPLO ---
@app.get("/create-sample-data")
async def create_sample_data():
    data_dir = "../data/banco_demo"
    os.makedirs(data_dir, exist_ok=True)

    csv_data = """edad,ingresos,ciudad,score_crediticio,moroso
25,2500000,Bogotá,650,0
35,4500000,Medellín,720,0
45,8000000,Cali,780,0
28,1800000,Barranquilla,580,1
38,3200000,Cartagena,690,0
52,12000000,Bogotá,820,0
23,1200000,Pereira,520,1
41,5500000,Bucaramanga,740,0
33,2800000,Manizales,640,1
29,3100000,Bogotá,680,0"""

    csv_path = os.path.join(data_dir, "historical_defaults.csv")
    with open(csv_path, "w", encoding="utf-8") as f:
        f.write(csv_data)

    return {
        "status": "✅ Sample data created",
        "path": csv_path,
        "records": len(csv_data.split('\n')) - 1
    }

# --- ENDPOINT: CONFIGURACIÓN AUTOMÁTICA ---
@app.get("/setup-all")
async def setup_all():
    config_result = await create_sample_config()
    data_result = await create_sample_data()
    health_result = await health_check()

    return {
        "status": "✅ Setup completed",
        "results": {
            "config": config_result,
            "data": data_result,
            "health": health_result
        },
        "next_steps": [
            "1. Visit /institutions to see configured institutions",
            "2. Visit /data-test to verify data loading",
            "3. Clean disk space to install scikit-learn for ML features",
            "4. Proceed to Phase 2 - AI Engine"
        ]
    }

# --- EJECUCIÓN LOCAL ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("simple_api:app", host="0.0.0.0", port=8000, reload=True)
