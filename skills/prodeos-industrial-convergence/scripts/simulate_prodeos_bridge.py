#!/usr/bin/env python3
"""
Simulateur de Convergence Prodeos OT/IT :
Automate/SCADA (FUXA/UMH) -> Détection IA -> Génération Ticket GMAO (Atlas CMMS).
"""

import json
import datetime
import uuid

def simulate_scada_alarm():
    """Simule une alarme provenant d'un automate Siemens S7 via FUXA / MQTT UNS."""
    return {
        "event_id": str(uuid.uuid4())[:8],
        "uns_topic": "prodeos-demo/usine-paris/usinage/ligne1/cnc-01/alarms/thermal",
        "timestamp": datetime.datetime.now().isoformat(),
        "source": "Siemens_S7_1500_PLC4X",
        "asset_code": "EQ-CNC-01",
        "asset_name": "Centre d'usinage 5 axes DMG Mori",
        "tag_name": "Broche_Temperature_C",
        "value": 78.4,
        "threshold": 70.0,
        "unit": "°C",
        "severity": "CRITICAL"
    }

def analyze_and_triage(alarm):
    """Analyse par l'Agent IA : corrélation historique et pièces de rechange."""
    print(f"\n[1. OT Ingestion] Alarme reçue via UNS Topic : {alarm['uns_topic']}")
    print(f"    Capteur : {alarm['tag_name']} = {alarm['value']}{alarm['unit']} (Seuil max : {alarm['threshold']}{alarm['unit']})")
    
    # Base de connaissances simulée
    knowledge_base = {
        "EQ-CNC-01": {
            "criticality": "CRITICAL",
            "probable_cause": "Défaut de lubrification du palier principal de broche ou obstruction circuit de refroidissement",
            "recommended_part_sku": "SKU-ROUL-6205",
            "recommended_part_name": "Roulement à billes céramique haute vitesse",
            "stock_available": 4,
            "assigned_technician": "Marc Dupont (Spécialiste Mécanique Précision)",
            "estimated_intervention_hours": 2.5
        }
    }
    
    asset_info = knowledge_base.get(alarm["asset_code"], {
        "criticality": "MEDIUM",
        "probable_cause": "Anomalie générique",
        "recommended_part_sku": "SKU-GEN-01",
        "recommended_part_name": "Pièce générique",
        "stock_available": 0,
        "assigned_technician": "Équipe Maintenance Générale",
        "estimated_intervention_hours": 1.0
    })
    
    print("\n[2. Triage IA & Diagnostic]")
    print(f"    Équipement cible : {alarm['asset_name']} ({alarm['asset_code']})")
    print(f"    Diagnostic automatique : {asset_info['probable_cause']}")
    print(f"    Pièce requise : {asset_info['recommended_part_name']} [{asset_info['recommended_part_sku']}]")
    print(f"    Stock magasin : {asset_info['stock_available']} unités en stock (Statut : DISPONIBLE)")
    
    # 3. Création automatique du Work Order GMAO
    work_order = {
        "ticket_number": f"WO-{datetime.datetime.now().year}-{str(uuid.uuid4())[:4].upper()}",
        "asset_code": alarm["asset_code"],
        "title": f"Intervention d'urgence : Surchauffe broche ({alarm['value']}°C)",
        "type": "CORRECTIVE_URGENT",
        "priority": "HIGH",
        "status": "ASSIGNED",
        "assigned_to": asset_info["assigned_technician"],
        "trigger_source": f"SCADA_ALARM_EVENT_{alarm['event_id']}",
        "diagnostic_summary": asset_info["probable_cause"],
        "parts_allocated": [
            {
                "sku": asset_info["recommended_part_sku"],
                "name": asset_info["recommended_part_name"],
                "quantity": 1
            }
        ],
        "estimated_hours": asset_info["estimated_intervention_hours"],
        "created_at": datetime.datetime.now().isoformat()
    }
    
    print("\n[3. Action IT / GMAO]")
    print(f"    Génération du Bon de Travail : {work_order['ticket_number']}")
    print(f"    Technicien notifié : {work_order['assigned_to']}")
    print(f"    Payload JSON API GMAO (Atlas CMMS / CMMS-OEE) :\n")
    print(json.dumps(work_order, indent=2, ensure_ascii=False))
    
    return work_order

if __name__ == "__main__":
    alarm = simulate_scada_alarm()
    analyze_and_triage(alarm)
