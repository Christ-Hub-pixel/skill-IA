# 🧠 Skills IA — Collection de Compétences pour Agents IA

Ce dépôt regroupe une collection de **21 compétences standardisées (Agent Skills)** conçues pour les assistants et agents de code IA (Claude Code, Gemini, Cursor, Copilot, etc.), spécialisées dans l'écosystème **Google Cloud Platform (GCP)**, le **Data Engineering**, le **Big Data**, le **Machine Learning** et la **Gouvernance de données**.

---

## 📊 Répartition Méthodologique (21 Skills au total)

Les 21 compétences sont structurées en **5 grands domaines méthodologiques** couvrant l'intégralité du cycle de vie de la donnée :

```
                                  SKILLS IA (21)
  ┌───────────────────────┬──────────────┴───────────────┬────────────────────────┐
  │                       │                              │                        │
1. Data Warehousing    2. Pipelines & ETL/Streaming   3. Orchestration & IaC   4. Gouvernance & Qualité   5. Data Apps, ML & Dev
   (3 skills)             (4 skills)                     (3 skills)               (4 skills)                 (7 skills)
```

---

### 1. 🗄️ Data Warehousing & SQL Analytics (3 skills)
Méthodes de requêtage, de modélisation analytique et d'optimisation de coûts sur les entrepôts de données modernes.

| Compétence | Méthode & Rôle |
| :--- | :--- |
| [`bigquery-sql`](skills/bigquery-sql/SKILL.md) | **Optimisation SQL & Coûts** : Bonnes pratiques de partitionnement, clustering, réduction des octets scannés et optimisation des requêtes analytiques sur Google BigQuery. |
| [`dbt-bigquery`](skills/dbt-bigquery/SKILL.md) | **Modélisation Modulaire (dbt)** : Transformations SQL déclaratives, lignage de données (*lineage*), tests automatisés et documentation dbt Core / dbt Cloud sur BigQuery. |
| [`dataform-bigquery`](skills/dataform-bigquery/SKILL.md) | **Pipelines SQLX Natifs** : Développement, assertions de qualité de données et gestion des dépendances via Dataform pour BigQuery. |

---

### 2. ⚡ Pipelines de Données & Traitement Distribué (4 skills)
Méthodes d'ingestion, d'ETL/ELT et de calcul distribué (Batch & Temps réel).

| Compétence | Méthode & Rôle |
| :--- | :--- |
| [`gcp-data-pipelines`](skills/gcp-data-pipelines/SKILL.md) | **Architecture ETL/ELT** : Conception et mise en œuvre globale de flux de données résilients et évolutifs sur GCP. |
| [`gcp-dataflow`](skills/gcp-dataflow/SKILL.md) | **Calcul Streaming & Batch (Apache Beam)** : Écriture, packaging en Flex Templates (Cloud Build), exécution et tuning de performance/autoscaling sur Dataflow. |
| [`gcp-spark`](skills/gcp-spark/SKILL.md) | **Big Data Distribué (PySpark)** : Développement et exécution de traitements massifs sur Dataproc (clusters managés et Dataproc Serverless). |
| [`bigquery-data-transfer-service`](skills/bigquery-data-transfer-service/SKILL.md) | **Ingestion Automatisée (DTS)** : Planification et automatisation des transferts récurrents depuis Cloud Storage, AWS S3 ou applications SaaS vers BigQuery. |

---

### 3. ⚙️ Orchestration, Infrastructure & FinOps (3 skills)
Méthodes d'automatisation des flux, de déploiement déclaratif (IaC) et de contrôle financier du cloud.

| Compétence | Méthode & Rôle |
| :--- | :--- |
| [`gcp-pipeline-orchestration`](skills/gcp-pipeline-orchestration/SKILL.md) | **Orchestration de Workflows (Airflow)** : Création et déclenchement de DAGs Google Cloud Composer / Airflow pour chaîner Spark, dbt, SQL et scripts Python. |
| [`gcp-pipeline-resource-provisioning`](skills/gcp-pipeline-resource-provisioning/SKILL.md) | **Provisionnement Déclaratif (IaC)** : Déploiement standardisé d'infrastructures de données (datasets, tables, DTS) via configuration `deployment.yaml` multi-environnements (dev, staging, prod). |
| [`enforcing-resource-attribution`](skills/enforcing-resource-attribution/SKILL.md) | **FinOps & Gouvernance Budgétaire** : Étiquetage obligatoire (*tagging/labeling*), traçabilité des ressources et attribution précise des coûts cloud. |

---

### 4. 🛡️ Gouvernance, Sécurité & Qualité des Données (4 skills)
Méthodes d'intégrité, de prévention des incidents et de cartographie des métadonnées.

| Compétence | Méthode & Rôle |
| :--- | :--- |
| [`accidental-data-loss-prevention`](skills/accidental-data-loss-prevention/SKILL.md) | **Protection Anti-Perte** : Garde-fous et procédures strictes pour prévenir la suppression accidentelle ou l'écrasement de tables et datasets de production. |
| [`data-autocleaning`](skills/data-autocleaning/SKILL.md) | **Qualité & Nettoyage Automatisé** : Détection des valeurs aberrantes, profiling et assainissement des données avec les scanners Dataplex. |
| [`discovering-gcp-data-assets`](skills/discovering-gcp-data-assets/SKILL.md) | **Découverte & Catalogue** : Exploration, inventaire et recherche sémantique des actifs de données via Dataplex Catalog. |
| [`schema-mapping`](skills/schema-mapping/SKILL.md) | **Alignement de Schémas** : Élaboration du *Mapping Manifesto* (plan rigoureux de correspondance entre schémas sources et cibles) avant tout développement d'intégration. |

---

### 5. 🚀 Data Applications, Machine Learning & Environnements (7 skills)
Méthodes de restitution interactive, de modélisation prédictive, de diagnostic et de gestion de l'environnement de travail.

| Compétence | Méthode & Rôle |
| :--- | :--- |
| [`building-data-apps`](skills/building-data-apps/SKILL.md) | **Applications Data & IA** : Construction d'interfaces complètes (Streamlit, FastAPI, React Chat Panels) pour exploiter les données. |
| [`ml-best-practices`](skills/ml-best-practices/SKILL.md) | **Ingénierie Machine Learning** : Standards rigoureux pour la modélisation (classification, régression, clustering, séries temporelles, tests statistiques). |
| [`notebook-guidance`](skills/notebook-guidance/SKILL.md) | **Analyse Exploratoire (Jupyter)** : Bonnes pratiques d'organisation de notebooks, visualisation de données et requêtage BigQuery via magics `%%bqsql`. |
| [`gcp-spark-troubleshooting`](skills/gcp-spark-troubleshooting/SKILL.md) | **Diagnostic & RCA (Root Cause Analysis)** : Analyse des logs Cloud Storage, streaming des traces Spark et résolution des erreurs mémoires/OOM sur Dataproc. |
| [`google-cloud-auth-verification`](skills/google-cloud-auth-verification/SKILL.md) | **Sécurité Pré-vol (Auth)** : Étape zéro obligatoire vérifiant les identifiants ADC (Application Default Credentials), gcloud CLI et les permissions IAM. |
| [`managing-python-dependencies`](skills/managing-python-dependencies/SKILL.md) | **Gestion des Runtimes Python** : Isolation stricte des environnements virtuels, gestion reproductible des versions (uv, poetry, pip-tools). |
| [`skill-repair`](skills/skill-repair/SKILL.md) | **Auto-Maintenance de l'Agent** : Procédures de correction et réinstallation des compétences défectueuses au sein du manifest de l'agent. |

---

## 🛠️ Structure d'une Compétence

Chaque dossier dans `skills/` contient :
1. **`SKILL.md`** : Définition YAML standardisée (métadonnées, déclencheurs d'activation, conditions d'exclusion) suivie du guide pas-à-pas pour l'agent IA.
2. **`scripts/`** *(le cas échéant)* : Scripts d'automatisation Python / Shell pour l'exécution directe des tâches.
3. **`references/`** *(le cas échéant)* : Guides d'architecture, matrices de diagnostic et gabarits de spécification.
4. **`examples/`** *(le cas échéant)* : Exemples concrets de code prêt à l'emploi.
