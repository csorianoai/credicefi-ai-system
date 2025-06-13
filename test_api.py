#!/usr/bin/env python3
"""
Script de testing completo para CredICEfi Multi-Tenant API
Ejecutar con: python test_api.py
"""

import requests
import json
import time
from datetime import datetime

# Configuración
BASE_URL = "http://localhost:8000"
TENANT_ID = "banco_demo"

def print_section(title):
    """Imprime una sección del test"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def test_request(method, endpoint, data=None, headers=None, description=""):
    """Ejecuta un request y muestra el resultado"""
    url = f"{BASE_URL}{endpoint}"
    
    print(f"\n🔍 {description}")
    print(f"   {method} {endpoint}")
    
    if headers:
        print(f"   Headers: {headers}")
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, json=data, headers=headers)
        else:
            print(f"❌ Método {method} no soportado")
            return None
        
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"   ✅ Success")
            
            # Mostrar algunos campos clave
            if isinstance(result, dict):
                if "status" in result:
                    print(f"   📊 Status: {result['status']}")
                if "count" in result:
                    print(f"   📊 Count: {result['count']}")
                if "decision" in result.get("risk_assessment", {}):
                    print(f"   📊 Decision: {result['risk_assessment']['decision']}")
                if "risk_level" in result.get("risk_assessment", {}):
                    print(f"   📊 Risk Level: {result['risk_assessment']['risk_level']}")
                if "similarity_score" in result:
                    print(f"   📊 Similarity: {result['similarity_score']:.1f}%")
            
            return result
        else:
            print(f"   ❌ Error: {response.text}")
            return None
            
    except requests.exceptions.ConnectionError:
        print(f"   ❌ Connection Error - ¿Está corriendo el servidor en {BASE_URL}?")
        return None
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")
        return None

def main():
    """Ejecutar todos los tests"""
    
    print("🚀 CredICEfi Multi-Tenant API - Test Suite")
    print(f"   Base URL: {BASE_URL}")
    print(f"   Tenant: {TENANT_ID}")
    print(f"   Timestamp: {datetime.now().isoformat()}")
    
    # Test básico
    print_section("TESTS BÁSICOS")
    test_request("GET", "/", description="Test del endpoint raíz")
    test_request("GET", "/health", description="Verificación de salud")
    
    # Setup
    print_section("SETUP DEL SISTEMA")
    test_request("GET", "/setup/complete-setup", description="Setup completo")
    
    time.sleep(1)
    
    # Multi-tenant
    print_section("TESTS MULTI-TENANT")
    tenant_headers = {"X-Tenant-ID": TENANT_ID}
    
    test_request("GET", "/tenant/config", headers=tenant_headers, description="Config del tenant")
    test_request("GET", "/ai/performance", headers=tenant_headers, description="Performance IA")
    
    # Evaluaciones
    print_section("EVALUACIONES DE CRÉDITO")
    
    # Bajo riesgo
    bajo_riesgo = {
        "applicant": {
            "age": 35,
            "monthly_income": 8000000,
            "credit_score": 780,
            "city": "Bogotá",
            "debt_to_income_ratio": 0.2,
            "late_payments": 0
        },
        "loan_amount": 15000000,
        "loan_term_months": 36,
        "loan_purpose": "vivienda"
    }
    
    result_bajo = test_request("POST", "/assess-credit", data=bajo_riesgo, headers=tenant_headers, description="BAJO RIESGO")
    
    # Alto riesgo
    alto_riesgo = {
        "applicant": {
            "age": 24,
            "monthly_income": 1400000,
            "credit_score": 540,
            "city": "Pereira",
            "debt_to_income_ratio": 0.8,
            "late_payments": 8
        },
        "loan_amount": 20000000,
        "loan_term_months": 60,
        "loan_purpose": "consumo"
    }
    
    result_alto = test_request("POST", "/assess-credit", data=alto_riesgo, headers=tenant_headers, description="ALTO RIESGO")
    
    # Resumen
    print_section("RESUMEN")
    if result_bajo:
        print(f"🟢 Bajo Riesgo: {result_bajo.get('risk_assessment', {}).get('decision', 'N/A')}")
        print(f"   Similitud: {result_bajo.get('similarity_score', 0):.1f}%")
    
    if result_alto:
        print(f"🔴 Alto Riesgo: {result_alto.get('risk_assessment', {}).get('decision', 'N/A')}")
        print(f"   Similitud: {result_alto.get('similarity_score', 0):.1f}%")
    
    print("\n✅ TESTING COMPLETADO!")

if __name__ == "__main__":
    main()