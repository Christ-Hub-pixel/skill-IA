# 🧠 Skills IA — Grande Bibliothèque de Compétences pour Agents IA

Ce dépôt rassemble une bibliothèque exhaustive de **1201 compétences standardisées (Agent Skills)** pour les assistants et agents de code IA (Claude Code, Gemini CLI, Cursor, Copilot, Codex, etc.).

---

## 📊 Répartition par Domaine Méthodologique

| Domaine Méthodologique | Nombre de Skills | Description |
| :--- | :---: | :--- |
| **🛡️ Cybersécurité, Pentesting & Threat Intelligence** | **431** | Détection d'intrusions, forensic, rétro-ingénierie malware, audit AD/Cloud et techniques MITRE ATT&CK. |
| **☁️ Cloud, Kubernetes, DevOps & Infrastructure** | **95** | Déploiement IaC (Terraform), orchestration Kubernetes, pipelines CI/CD et gestion multi-cloud (GCP, AWS, Azure). |
| **📊 Data Engineering, Big Data & Analytics** | **49** | Pipelines BigQuery, Spark, dbt, Dataform, traitement distribué (Dataflow/Beam) et bases de données. |
| **🤖 Intelligence Artificielle, Agents & Machine Learning** | **243** | Ingénierie agentique, loops autonomes, évaluation de LLMs, optimisation de prompts et ML ops. |
| **💻 Développement Logiciel, Web & Langages** | **252** | Patrons de conception, frameworks (React, Vue, Next.js, Django, Spring Boot, Ktor) et langages (Python, Go, Rust, C#, Swift, etc.). |
| **🧪 Tests, QA & Validation Logicielle** | **69** | Stratégies de tests automatisés (TDD, Playwright E2E, tests unitaires, fuzzing et benchmarks). |
| **📋 Architecture, API, FinOps & Gouvernance** | **62** | Design d'API REST/GraphQL, conformité (HIPAA, ISO), suivi des coûts (FinOps) et ADRs. |
| **TOTAL** | **1201** | **Bibliothèque complète de skills agents** |

---

## 🛡️ Cybersécurité, Pentesting & Threat Intelligence (431 skills)

| Compétence | Description |
| :--- | :--- |
| [`acquiring-disk-image-with-dd-and-dcfldd`](skills/acquiring-disk-image-with-dd-and-dcfldd/SKILL.md) | Create forensically sound bit-for-bit disk images with dd or dcfldd on a Linux forensic workstation, preserving evidence integr... |
| [`analyzing-active-directory-acl-abuse`](skills/analyzing-active-directory-acl-abuse/SKILL.md) | Detect dangerous ACL misconfigurations in Active Directory using ldap3 |
| [`analyzing-android-malware-with-apktool`](skills/analyzing-android-malware-with-apktool/SKILL.md) | Perform static analysis of Android APK malware using apktool for resource decompilation, jadx for Java source recovery, and and... |
| [`analyzing-api-gateway-access-logs`](skills/analyzing-api-gateway-access-logs/SKILL.md) | Parses API Gateway access logs (AWS API Gateway, Kong, Nginx) to detect |
| [`analyzing-apt-group-with-mitre-navigator`](skills/analyzing-apt-group-with-mitre-navigator/SKILL.md) | Query ATT&CK data with attackcti, mitreattack-python, and stix2, then build MITRE ATT&CK Navigator layers and multi-layer heatm... |
| [`analyzing-azure-activity-logs-for-threats`](skills/analyzing-azure-activity-logs-for-threats/SKILL.md) | Queries Azure Monitor activity logs and sign-in logs via azure-monitor-query |
| [`analyzing-bootkit-and-rootkit-samples`](skills/analyzing-bootkit-and-rootkit-samples/SKILL.md) | Analyzes bootkit and advanced rootkit malware infecting the Master |
| [`analyzing-browser-forensics-with-hindsight`](skills/analyzing-browser-forensics-with-hindsight/SKILL.md) | Parse Chromium-based browser databases with Hindsight to extract and correlate browsing history, downloads, cookies, cached con... |
| [`analyzing-campaign-attribution-evidence`](skills/analyzing-campaign-attribution-evidence/SKILL.md) | Systematically evaluate cyber-campaign evidence to attribute an operation to a threat actor, using the Diamond Model and Analys... |
| [`analyzing-certificate-transparency-for-phishing`](skills/analyzing-certificate-transparency-for-phishing/SKILL.md) | Monitor Certificate Transparency logs using crt.sh and Certstream to |
| [`analyzing-cloud-storage-access-patterns`](skills/analyzing-cloud-storage-access-patterns/SKILL.md) | Detect abnormal access in AWS S3, GCS, and Azure Blob Storage by analyzing CloudTrail Data Events, GCS audit logs, and Azure St... |
| [`analyzing-cobalt-strike-beacon-configuration`](skills/analyzing-cobalt-strike-beacon-configuration/SKILL.md) | Extract and analyze Cobalt Strike beacon configuration from PE files |
| [`analyzing-cobaltstrike-malleable-c2-profiles`](skills/analyzing-cobaltstrike-malleable-c2-profiles/SKILL.md) | Parse and analyze Cobalt Strike Malleable C2 profiles with dissect.cobaltstrike (profiles and beacon-payload configs) and pyMal... |
| [`analyzing-command-and-control-communication`](skills/analyzing-command-and-control-communication/SKILL.md) | Analyzes malware C2 communication over HTTP, HTTPS, DNS, and custom |
| [`analyzing-cyber-kill-chain`](skills/analyzing-cyber-kill-chain/SKILL.md) | Analyzes intrusion activity against the Lockheed Martin Cyber Kill Chain |
| [`analyzing-disk-image-with-autopsy`](skills/analyzing-disk-image-with-autopsy/SKILL.md) | Perform comprehensive forensic analysis of raw (dd), E01, or AFF disk images with Autopsy and The Sleuth Kit, recovering delete... |
| [`analyzing-dns-logs-for-exfiltration`](skills/analyzing-dns-logs-for-exfiltration/SKILL.md) | Analyzes DNS query logs to detect data exfiltration via DNS tunneling, |
| [`analyzing-docker-container-forensics`](skills/analyzing-docker-container-forensics/SKILL.md) | Investigate compromised Docker containers by analyzing images, layers, |
| [`analyzing-email-headers-for-phishing-investigation`](skills/analyzing-email-headers-for-phishing-investigation/SKILL.md) | Parse and analyze email headers (Received chain, Return-Path, Message-ID) |
| [`analyzing-ethereum-smart-contract-vulnerabilities`](skills/analyzing-ethereum-smart-contract-vulnerabilities/SKILL.md) | Perform static and symbolic analysis of Solidity smart contracts using |
| [`analyzing-golang-malware-with-ghidra`](skills/analyzing-golang-malware-with-ghidra/SKILL.md) | Reverse engineer Go-compiled malware in Ghidra by parsing Go buildinfo |
| [`analyzing-heap-spray-exploitation`](skills/analyzing-heap-spray-exploitation/SKILL.md) | Detect and analyze heap spray attacks in memory dumps using Volatility3 |
| [`analyzing-indicators-of-compromise`](skills/analyzing-indicators-of-compromise/SKILL.md) | Analyzes indicators of compromise (IOCs) including IP addresses, domains, |
| [`analyzing-ios-app-security-with-objection`](skills/analyzing-ios-app-security-with-objection/SKILL.md) | >- |
| [`analyzing-kubernetes-audit-logs`](skills/analyzing-kubernetes-audit-logs/SKILL.md) | >- |
| [`analyzing-linux-audit-logs-for-intrusion`](skills/analyzing-linux-audit-logs-for-intrusion/SKILL.md) | Uses the Linux Audit framework (auditd) with ausearch and aureport utilities |
| [`analyzing-linux-elf-malware`](skills/analyzing-linux-elf-malware/SKILL.md) | Analyze malicious Linux ELF binaries — botnets, cryptominers, ransomware, |
| [`analyzing-linux-kernel-rootkits`](skills/analyzing-linux-kernel-rootkits/SKILL.md) | Detect kernel-level rootkits in Linux memory dumps using Volatility3 |
| [`analyzing-linux-system-artifacts`](skills/analyzing-linux-system-artifacts/SKILL.md) | Examine Linux system artifacts (auth logs, cron/systemd persistence, |
| [`analyzing-lnk-file-and-jump-list-artifacts`](skills/analyzing-lnk-file-and-jump-list-artifacts/SKILL.md) | Analyze Windows LNK shortcut files and Jump List artifacts with LECmd, |
| [`analyzing-macro-malware-in-office-documents`](skills/analyzing-macro-malware-in-office-documents/SKILL.md) | Analyzes malicious VBA macros embedded in Microsoft Office documents |
| [`analyzing-malicious-pdf-with-peepdf`](skills/analyzing-malicious-pdf-with-peepdf/SKILL.md) | Perform static analysis of malicious PDF documents using peepdf, pdfid, |
| [`analyzing-malicious-url-with-urlscan`](skills/analyzing-malicious-url-with-urlscan/SKILL.md) | URLScan.io is a free service for scanning and analyzing suspicious URLs. |
| [`analyzing-malware-behavior-with-cuckoo-sandbox`](skills/analyzing-malware-behavior-with-cuckoo-sandbox/SKILL.md) | Detonate malware samples in Cuckoo Sandbox to observe runtime behavior |
| [`analyzing-malware-family-relationships-with-malpedia`](skills/analyzing-malware-family-relationships-with-malpedia/SKILL.md) | Query the Malpedia API to look up malware family aliases and naming |
| [`analyzing-malware-persistence-with-autoruns`](skills/analyzing-malware-persistence-with-autoruns/SKILL.md) | Use Sysinternals Autoruns to systematically enumerate and analyze malware |
| [`analyzing-malware-sandbox-evasion-techniques`](skills/analyzing-malware-sandbox-evasion-techniques/SKILL.md) | Detect sandbox and VM evasion techniques in malware samples by analyzing |
| [`analyzing-memory-dumps-with-volatility`](skills/analyzing-memory-dumps-with-volatility/SKILL.md) | Analyzes RAM memory dumps from compromised systems using the Volatility framework to identify malicious processes, |
| [`analyzing-memory-forensics-with-lime-and-volatility`](skills/analyzing-memory-forensics-with-lime-and-volatility/SKILL.md) | Performs Linux memory acquisition using LiME (Linux Memory Extractor) |
| [`analyzing-mft-for-deleted-file-recovery`](skills/analyzing-mft-for-deleted-file-recovery/SKILL.md) | Analyze the NTFS Master File Table ($MFT) with MFTECmd, analyzeMFT, |
| [`analyzing-network-covert-channels-in-malware`](skills/analyzing-network-covert-channels-in-malware/SKILL.md) | Detect and analyze covert communication channels used by malware, including |
| [`analyzing-network-flow-data-with-netflow`](skills/analyzing-network-flow-data-with-netflow/SKILL.md) | Parse NetFlow v9 and IPFIX records to detect volumetric anomalies, port |
| [`analyzing-network-packets-with-scapy`](skills/analyzing-network-packets-with-scapy/SKILL.md) | Use Scapy to craft, send, sniff, and dissect TCP/UDP/ICMP/DNS packets, analyze pcap files, implement SYN scans, and detect anom... |
| [`analyzing-network-traffic-for-incidents`](skills/analyzing-network-traffic-for-incidents/SKILL.md) | Analyzes network traffic captures and flow data to identify adversary activity during security incidents, including |
| [`analyzing-network-traffic-of-malware`](skills/analyzing-network-traffic-of-malware/SKILL.md) | Analyzes network traffic generated by malware during sandbox execution |
| [`analyzing-network-traffic-with-wireshark`](skills/analyzing-network-traffic-with-wireshark/SKILL.md) | Captures and analyzes network packet data using Wireshark and tshark |
| [`analyzing-office365-audit-logs-for-compromise`](skills/analyzing-office365-audit-logs-for-compromise/SKILL.md) | Parse Office 365 Unified Audit Logs via Microsoft Graph API to detect |
| [`analyzing-outlook-pst-for-email-forensics`](skills/analyzing-outlook-pst-for-email-forensics/SKILL.md) | Parse Microsoft Outlook PST and OST files using libpff and pst-utils to extract message content, headers, attachments, deleted ... |
| [`analyzing-packed-malware-with-upx-unpacker`](skills/analyzing-packed-malware-with-upx-unpacker/SKILL.md) | Identifies and unpacks UPX-packed malware samples, including binaries with modified UPX magic bytes or headers that block autom... |
| [`analyzing-pdf-malware-with-pdfid`](skills/analyzing-pdf-malware-with-pdfid/SKILL.md) | Analyzes malicious PDF files using PDFiD, pdf-parser, and peepdf to |
| [`analyzing-persistence-mechanisms-in-linux`](skills/analyzing-persistence-mechanisms-in-linux/SKILL.md) | Scan Linux systems for persistence mechanisms including crontab/systemd entries, LD_PRELOAD injection, shell profile modificati... |
| [`analyzing-powershell-empire-artifacts`](skills/analyzing-powershell-empire-artifacts/SKILL.md) | Detect PowerShell Empire post-exploitation framework artifacts in Windows Script Block Logging (Event ID 4104) and Module Loggi... |
| [`analyzing-powershell-script-block-logging`](skills/analyzing-powershell-script-block-logging/SKILL.md) | Parse Windows PowerShell Script Block Logs (Event ID 4104) from EVTX |
| [`analyzing-prefetch-files-for-execution-history`](skills/analyzing-prefetch-files-for-execution-history/SKILL.md) | Parse Windows Prefetch files (versions 17, 23, 26, 30) with tools like PECmd, WinPrefetchView, or python-prefetch to determine ... |
| [`analyzing-ransomware-encryption-mechanisms`](skills/analyzing-ransomware-encryption-mechanisms/SKILL.md) | Analyzes encryption algorithms, key management, and file encryption |
| [`analyzing-ransomware-leak-site-intelligence`](skills/analyzing-ransomware-leak-site-intelligence/SKILL.md) | Safely monitor ransomware group Tor-hosted data leak sites (DLS) to collect and extract structured victim posting data, track g... |
| [`analyzing-ransomware-network-indicators`](skills/analyzing-ransomware-network-indicators/SKILL.md) | Identify ransomware-related network indicators, including C2 beaconing patterns, TOR exit node connections, data exfiltration f... |
| [`analyzing-ransomware-payment-wallets`](skills/analyzing-ransomware-payment-wallets/SKILL.md) | Traces ransomware cryptocurrency payment flows using blockchain analysis tools such as Chainalysis Reactor, WalletExplorer, and... |
| [`analyzing-sbom-for-supply-chain-vulnerabilities`](skills/analyzing-sbom-for-supply-chain-vulnerabilities/SKILL.md) | Parses Software Bill of Materials (SBOM) in CycloneDX and SPDX JSON |
| [`analyzing-security-logs-with-splunk`](skills/analyzing-security-logs-with-splunk/SKILL.md) | Leverages Splunk Enterprise Security and SPL (Search Processing Language) |
| [`analyzing-slack-space-and-file-system-artifacts`](skills/analyzing-slack-space-and-file-system-artifacts/SKILL.md) | Examine NTFS slack space, MFT entries, the USN Change Journal, and Alternate Data Streams (ADS) to recover hidden or residual d... |
| [`analyzing-supply-chain-malware-artifacts`](skills/analyzing-supply-chain-malware-artifacts/SKILL.md) | Investigate supply chain attack artifacts including trojanized software |
| [`analyzing-threat-actor-ttps-with-mitre-attack`](skills/analyzing-threat-actor-ttps-with-mitre-attack/SKILL.md) | Systematically map threat actor behavior and observed IOCs to the MITRE ATT&CK framework, build technique coverage heatmaps wit... |
| [`analyzing-threat-actor-ttps-with-mitre-navigator`](skills/analyzing-threat-actor-ttps-with-mitre-navigator/SKILL.md) | Map advanced persistent threat (APT) group TTPs to the MITRE ATT&CK framework using the attackcti Python library to query STIX/... |
| [`analyzing-threat-intelligence-feeds`](skills/analyzing-threat-intelligence-feeds/SKILL.md) | Analyzes structured and unstructured threat intelligence feeds to extract |
| [`analyzing-threat-landscape-with-misp`](skills/analyzing-threat-landscape-with-misp/SKILL.md) | Query a MISP (Malware Information Sharing Platform) instance via PyMISP |
| [`analyzing-tls-certificate-transparency-logs`](skills/analyzing-tls-certificate-transparency-logs/SKILL.md) | Queries Certificate Transparency logs via crt.sh and pycrtsh to detect |
| [`analyzing-typosquatting-domains-with-dnstwist`](skills/analyzing-typosquatting-domains-with-dnstwist/SKILL.md) | Generate domain permutations with dnstwist and check DNS resolution |
| [`analyzing-uefi-bootkit-persistence`](skills/analyzing-uefi-bootkit-persistence/SKILL.md) | Analyzes UEFI bootkit persistence (SPI flash implants, ESP modifications, |
| [`analyzing-usb-device-connection-history`](skills/analyzing-usb-device-connection-history/SKILL.md) | Correlate Windows registry keys (USBSTOR, MountedDevices), Event Logs, |
| [`analyzing-web-server-logs-for-intrusion`](skills/analyzing-web-server-logs-for-intrusion/SKILL.md) | Parse Apache and Nginx access logs to detect SQL injection attempts, |
| [`analyzing-windows-amcache-artifacts`](skills/analyzing-windows-amcache-artifacts/SKILL.md) | Parses the Windows Amcache.hve registry hive with Eric Zimmerman''s |
| [`analyzing-windows-event-logs-in-splunk`](skills/analyzing-windows-event-logs-in-splunk/SKILL.md) | Analyzes Windows Security, System, and Sysmon event logs in Splunk to |
| [`analyzing-windows-lnk-files-for-artifacts`](skills/analyzing-windows-lnk-files-for-artifacts/SKILL.md) | Parse Windows LNK shortcut files to extract target paths, MAC timestamps, |
| [`analyzing-windows-prefetch-with-python`](skills/analyzing-windows-prefetch-with-python/SKILL.md) | Parse Windows Prefetch (.pf) files with the windowsprefetch Python |
| [`analyzing-windows-registry-for-artifacts`](skills/analyzing-windows-registry-for-artifacts/SKILL.md) | Extract and analyze Windows Registry hives with tools like RegRipper |
| [`analyzing-windows-shellbag-artifacts`](skills/analyzing-windows-shellbag-artifacts/SKILL.md) | Analyze Windows Shellbag (BagMRU) registry artifacts with SBECmd and |
| [`attacking-oauth-with-device-code-phishing`](skills/attacking-oauth-with-device-code-phishing/SKILL.md) | Run OAuth 2.0 device-code and illicit-consent phishing attacks against |
| [`auditing-azure-active-directory-configuration`](skills/auditing-azure-active-directory-configuration/SKILL.md) | Auditing Microsoft Entra ID (Azure Active Directory) configuration to |
| [`auditing-uefi-firmware-with-chipsec`](skills/auditing-uefi-firmware-with-chipsec/SKILL.md) | Use Intel CHIPSEC to assess platform firmware configuration, SPI flash write protection, BIOS lock, SMM/SMRR, and Secure Boot v... |
| [`building-adversary-infrastructure-tracking-system`](skills/building-adversary-infrastructure-tracking-system/SKILL.md) | Build an automated adversary infrastructure tracking system in Python (dnspython, python-whois, shodan, networkx) that pivots a... |
| [`building-attack-pattern-library-from-cti-reports`](skills/building-attack-pattern-library-from-cti-reports/SKILL.md) | Parse cyber threat intelligence reports (Mandiant, CrowdStrike, Talos, Microsoft) with stix2, mitreattack-python, and spaCy to ... |
| [`building-automated-malware-submission-pipeline`](skills/building-automated-malware-submission-pipeline/SKILL.md) | Builds an automated malware submission and analysis pipeline that collects |
| [`building-c2-infrastructure-with-sliver-framework`](skills/building-c2-infrastructure-with-sliver-framework/SKILL.md) | Deploy and harden a Sliver C2 team server (BishopFox's Go-based adversary emulation framework) with multi-protocol listeners (m... |
| [`building-c2-redirector-infrastructure`](skills/building-c2-redirector-infrastructure/SKILL.md) | Build dumb-pipe and traffic-filtering C2 redirectors with nginx (proxy_pass) and Apache (mod_rewrite), deriving filter rules fr... |
| [`building-cloud-siem-with-sentinel`](skills/building-cloud-siem-with-sentinel/SKILL.md) | Deploy Microsoft Sentinel as a cloud-native SIEM/SOAR by configuring multi-cloud data connectors (AWS, Azure, GCP), writing KQL... |
| [`building-devsecops-pipeline-with-gitlab-ci`](skills/building-devsecops-pipeline-with-gitlab-ci/SKILL.md) | Configure a GitLab CI/CD pipeline that embeds SAST (Semgrep, SpotBugs, Gosec, Bandit, NodeJsScan), DAST, container scanning, de... |
| [`building-incident-timeline-with-timesketch`](skills/building-incident-timeline-with-timesketch/SKILL.md) | Build collaborative forensic incident timelines using Timesketch to ingest, |
| [`building-malware-incident-communication-template`](skills/building-malware-incident-communication-template/SKILL.md) | Build structured communication templates for malware incidents (ransomware, |
| [`building-phishing-reporting-button-workflow`](skills/building-phishing-reporting-button-workflow/SKILL.md) | Implement a phishing report button (Microsoft 365 built-in Report button |
| [`building-ransomware-playbook-with-cisa-framework`](skills/building-ransomware-playbook-with-cisa-framework/SKILL.md) | Builds a structured ransomware incident response playbook aligned with |
| [`building-red-team-c2-infrastructure-with-havoc`](skills/building-red-team-c2-infrastructure-with-havoc/SKILL.md) | Deploy and configure the Havoc C2 framework (teamserver, HTTPS/HTTP/SMB |
| [`building-soc-playbook-for-ransomware`](skills/building-soc-playbook-for-ransomware/SKILL.md) | Builds a structured SOC incident response playbook for ransomware attacks |
| [`building-super-timelines-with-plaso`](skills/building-super-timelines-with-plaso/SKILL.md) | Generate forensic super-timelines with Plaso's log2timeline.py, pinfo.py, |
| [`building-threat-actor-profile-from-osint`](skills/building-threat-actor-profile-from-osint/SKILL.md) | Build threat actor profiles by collecting OSINT from vendor reports, paste sites, dark web forums, social media, and code repos... |
| [`building-threat-feed-aggregation-with-misp`](skills/building-threat-feed-aggregation-with-misp/SKILL.md) | Deploy MISP via Docker and configure feeds from sources like abuse.ch, AlienVault OTX, and CIRCL to aggregate, correlate, and d... |
| [`building-threat-hunt-hypothesis-framework`](skills/building-threat-hunt-hypothesis-framework/SKILL.md) | Build a systematic threat-hunt workflow that turns threat intelligence and ATT&CK gap analysis into testable hypotheses, then e... |
| [`building-threat-intelligence-enrichment-in-splunk`](skills/building-threat-intelligence-enrichment-in-splunk/SKILL.md) | Build automated IOC enrichment pipelines in Splunk Enterprise Security by ingesting threat feeds into KV Store collections and ... |
| [`building-threat-intelligence-feed-integration`](skills/building-threat-intelligence-feed-integration/SKILL.md) | Builds automated threat intelligence feed integration pipelines connecting |
| [`building-threat-intelligence-platform`](skills/building-threat-intelligence-platform/SKILL.md) | Design and deploy a Threat Intelligence Platform (TIP) by integrating open-source CTI tools (MISP, OpenCTI, TheHive, Cortex) in... |
| [`building-vulnerability-aging-and-sla-tracking`](skills/building-vulnerability-aging-and-sla-tracking/SKILL.md) | Implement a vulnerability aging dashboard and SLA tracking system that measures time-to-remediation against severity-based dead... |
| [`building-vulnerability-dashboard-with-defectdojo`](skills/building-vulnerability-dashboard-with-defectdojo/SKILL.md) | Deploy DefectDojo as a centralized vulnerability management dashboard that ingests findings from 200+ security scanners, dedupl... |
| [`building-vulnerability-exception-tracking-system`](skills/building-vulnerability-exception-tracking-system/SKILL.md) | Build a vulnerability exception and risk acceptance tracking system covering approval workflows, compensating controls document... |
| [`building-vulnerability-scanning-workflow`](skills/building-vulnerability-scanning-workflow/SKILL.md) | Builds a structured vulnerability scanning workflow using tools like |
| [`collecting-open-source-intelligence`](skills/collecting-open-source-intelligence/SKILL.md) | Collects and synthesizes open-source intelligence (OSINT) about threat |
| [`collecting-threat-intelligence-with-misp`](skills/collecting-threat-intelligence-with-misp/SKILL.md) | Deploy MISP, configure threat feeds (MISP community, freetext, TAXII, CSV), and use the PyMISP API to programmatically fetch, a... |
| [`collecting-volatile-evidence-from-compromised-host`](skills/collecting-volatile-evidence-from-compromised-host/SKILL.md) | Collect volatile forensic evidence from a compromised host by following the order of volatility, preserving memory, network con... |
| [`conducting-cloud-incident-response`](skills/conducting-cloud-incident-response/SKILL.md) | Respond to security incidents in AWS, Azure, and GCP via identity-based containment, cloud-native log analysis (CloudTrail, Azu... |
| [`conducting-full-scope-red-team-engagement`](skills/conducting-full-scope-red-team-engagement/SKILL.md) | Plan and execute a comprehensive, MITRE ATT&CK-aligned red team engagement spanning threat modeling, reconnaissance, initial ac... |
| [`conducting-internal-network-penetration-test`](skills/conducting-internal-network-penetration-test/SKILL.md) | Execute an internal network penetration test simulating an insider threat |
| [`conducting-malware-incident-response`](skills/conducting-malware-incident-response/SKILL.md) | Respond to malware infections across enterprise endpoints by identifying the malware family, determining infection vectors, ass... |
| [`conducting-memory-forensics-with-volatility`](skills/conducting-memory-forensics-with-volatility/SKILL.md) | Performs memory forensics analysis using Volatility 3 to extract evidence |
| [`conducting-pass-the-ticket-attack`](skills/conducting-pass-the-ticket-attack/SKILL.md) | Perform Pass-the-Ticket (PtT) lateral movement by extracting Kerberos TGT/TGS tickets from LSASS memory on a compromised host a... |
| [`conducting-phishing-incident-response`](skills/conducting-phishing-incident-response/SKILL.md) | Respond to phishing incidents by analyzing reported emails, extracting indicators, sandboxing URLs/attachments, assessing crede... |
| [`conducting-social-engineering-penetration-test`](skills/conducting-social-engineering-penetration-test/SKILL.md) | Design and execute a social engineering penetration test combining OSINT-driven target profiling with phishing, vishing, smishi... |
| [`conducting-social-engineering-pretext-call`](skills/conducting-social-engineering-pretext-call/SKILL.md) | Plan and execute authorized vishing (voice phishing) pretext calls to |
| [`conducting-spearphishing-simulation-campaign`](skills/conducting-spearphishing-simulation-campaign/SKILL.md) | Run a targeted spearphishing simulation for initial access by developing OSINT-derived pretexts, building payloads (HTML smuggl... |
| [`configuring-active-directory-tiered-model`](skills/configuring-active-directory-tiered-model/SKILL.md) | Implement Microsoft's Enhanced Security Admin Environment (ESAE) tiered |
| [`configuring-suricata-for-network-monitoring`](skills/configuring-suricata-for-network-monitoring/SKILL.md) | Deploys and configures Suricata IDS/IPS with Emerging Threats rulesets, |
| [`continuous-llm-red-teaming-with-promptfoo`](skills/continuous-llm-red-teaming-with-promptfoo/SKILL.md) | Wires Promptfoo and DeepTeam into CI/CD for automated, repeatable red-teaming of LLM apps against OWASP LLM Top 10, OWASP Agent... |
| [`correlating-threat-campaigns`](skills/correlating-threat-campaigns/SKILL.md) | Correlates disparate security incidents, IOCs, and adversary behaviors |
| [`cybersecurity-ptes-methodology`](skills/cybersecurity-ptes-methodology/SKILL.md) | Comprehensive Penetration Testing Execution Standard (PTES) and OWASP offensive/defensive cybersecurity methodology based on Hi... |
| [`deobfuscating-javascript-malware`](skills/deobfuscating-javascript-malware/SKILL.md) | Deobfuscates malicious JavaScript found in phishing pages, web skimmers, and dropper scripts by reversing encoding layers, eval... |
| [`deobfuscating-powershell-obfuscated-malware`](skills/deobfuscating-powershell-obfuscated-malware/SKILL.md) | Systematically deobfuscates multi-layer PowerShell malware using AST analysis, dynamic tracing, and tools like PSDecode and Pow... |
| [`deploying-active-directory-honeytokens`](skills/deploying-active-directory-honeytokens/SKILL.md) | Deploys deception-based honeytokens in Active Directory including fake |
| [`deploying-decoy-files-for-ransomware-detection`](skills/deploying-decoy-files-for-ransomware-detection/SKILL.md) | Deploys canary files (honeytokens) across file systems to detect ransomware |
| [`deploying-ransomware-canary-files`](skills/deploying-ransomware-canary-files/SKILL.md) | Deploys and monitors ransomware canary files using Python's watchdog library, placing decoy files mimicking high-value targets ... |
| [`designing-adversary-engagement-with-mitre-engage`](skills/designing-adversary-engagement-with-mitre-engage/SKILL.md) | >- |
| [`detecting-ai-model-prompt-injection-attacks`](skills/detecting-ai-model-prompt-injection-attacks/SKILL.md) | Detects prompt injection using regex signature matching, heuristic scoring for structural anomalies, and DeBERTa-based transfor... |
| [`detecting-anomalies-in-industrial-control-systems`](skills/detecting-anomalies-in-industrial-control-systems/SKILL.md) | Deploys anomaly detection for OT/ICS environments using machine learning on OT network baselines, physics-based process models,... |
| [`detecting-anomalous-authentication-patterns`](skills/detecting-anomalous-authentication-patterns/SKILL.md) | Detects anomalous authentication patterns using UEBA analytics, statistical |
| [`detecting-api-enumeration-attacks`](skills/detecting-api-enumeration-attacks/SKILL.md) | Detect API enumeration attacks (BOLA/IDOR, OWASP API1:2023) by writing SIEM |
| [`detecting-arp-poisoning-in-network-traffic`](skills/detecting-arp-poisoning-in-network-traffic/SKILL.md) | Detect Layer 2 ARP poisoning/spoofing by deploying ARPWatch, Dynamic ARP |
| [`detecting-attacks-on-historian-servers`](skills/detecting-attacks-on-historian-servers/SKILL.md) | Detect cyber attacks on OT historian servers (OSIsoft PI, Ignition, GE |
| [`detecting-attacks-on-scada-systems`](skills/detecting-attacks-on-scada-systems/SKILL.md) | This skill covers detecting cyber attacks targeting Supervisory Control |
| [`detecting-aws-cloudtrail-anomalies`](skills/detecting-aws-cloudtrail-anomalies/SKILL.md) | Detect unusual API call patterns in AWS CloudTrail logs using boto3, |
| [`detecting-aws-credential-exposure-with-trufflehog`](skills/detecting-aws-credential-exposure-with-trufflehog/SKILL.md) | Scan source code repositories, CI/CD pipelines, and configuration files |
| [`detecting-aws-guardduty-findings-automation`](skills/detecting-aws-guardduty-findings-automation/SKILL.md) | Build automated AWS GuardDuty finding response pipelines using EventBridge |
| [`detecting-aws-iam-privilege-escalation`](skills/detecting-aws-iam-privilege-escalation/SKILL.md) | Detect AWS IAM privilege escalation paths using boto3 and Cloudsplaining |
| [`detecting-azure-lateral-movement`](skills/detecting-azure-lateral-movement/SKILL.md) | Detect lateral movement in Azure AD/Entra ID environments using Microsoft |
| [`detecting-azure-service-principal-abuse`](skills/detecting-azure-service-principal-abuse/SKILL.md) | Detect Azure service principal abuse in Microsoft Entra ID using KQL detection |
| [`detecting-azure-storage-account-misconfigurations`](skills/detecting-azure-storage-account-misconfigurations/SKILL.md) | Audit Azure Blob and ADLS storage accounts for public access exposure, weak |
| [`detecting-beaconing-patterns-with-zeek`](skills/detecting-beaconing-patterns-with-zeek/SKILL.md) | Performs statistical analysis of Zeek conn.log connection intervals |
| [`detecting-bluetooth-low-energy-attacks`](skills/detecting-bluetooth-low-energy-attacks/SKILL.md) | Detects and analyzes Bluetooth Low Energy (BLE) security attacks including |
| [`detecting-broken-object-property-level-authorization`](skills/detecting-broken-object-property-level-authorization/SKILL.md) | Detect and test for OWASP API3:2023 Broken Object Property Level Authorization |
| [`detecting-business-email-compromise`](skills/detecting-business-email-compromise/SKILL.md) | Detect Business Email Compromise (BEC) fraud, where attackers impersonate |
| [`detecting-business-email-compromise-with-ai`](skills/detecting-business-email-compromise-with-ai/SKILL.md) | Deploy AI and NLP-powered detection systems to identify business email |
| [`detecting-cloud-threats-with-guardduty`](skills/detecting-cloud-threats-with-guardduty/SKILL.md) | Deploy and operationalize Amazon GuardDuty, covering protection plans |
| [`detecting-command-and-control-over-dns`](skills/detecting-command-and-control-over-dns/SKILL.md) | Detect command-and-control (C2) traffic tunneled over DNS from tools like |
| [`detecting-compromised-cloud-credentials`](skills/detecting-compromised-cloud-credentials/SKILL.md) | Detect compromised cloud credentials across AWS, Azure, and GCP by analyzing |
| [`detecting-container-drift-at-runtime`](skills/detecting-container-drift-at-runtime/SKILL.md) | >- |
| [`detecting-container-escape-attempts`](skills/detecting-container-escape-attempts/SKILL.md) | >- |
| [`detecting-container-escape-with-falco-rules`](skills/detecting-container-escape-with-falco-rules/SKILL.md) | >- |
| [`detecting-container-runtime-threats-with-falco`](skills/detecting-container-runtime-threats-with-falco/SKILL.md) | >- |
| [`detecting-credential-dumping-techniques`](skills/detecting-credential-dumping-techniques/SKILL.md) | Detect LSASS credential dumping, SAM database extraction, and NTDS.dit theft (e.g. via Mimikatz) using Sysmon Event ID 10 proce... |
| [`detecting-cryptomining-in-cloud`](skills/detecting-cryptomining-in-cloud/SKILL.md) | This skill teaches security teams how to detect and respond to unauthorized |
| [`detecting-data-and-model-poisoning`](skills/detecting-data-and-model-poisoning/SKILL.md) | Identify poisoned training data and backdoored ML models across the pipeline using IBM's Adversarial Robustness Toolbox (activa... |
| [`detecting-dcsync-attack-in-active-directory`](skills/detecting-dcsync-attack-in-active-directory/SKILL.md) | Detect DCSync attacks (MITRE T1003.006) where adversaries abuse Active Directory replication privileges to extract password has... |
| [`detecting-deepfake-audio-in-vishing-attacks`](skills/detecting-deepfake-audio-in-vishing-attacks/SKILL.md) | Detect AI-generated deepfake audio used in voice phishing (vishing) by extracting spectral features (MFCC, spectral centroid, s... |
| [`detecting-dependency-confusion`](skills/detecting-dependency-confusion/SKILL.md) | Detect and prevent dependency confusion (public-over-private package name resolution) in npm, PyPI, and Maven by enumerating cl... |
| [`detecting-dll-sideloading-attacks`](skills/detecting-dll-sideloading-attacks/SKILL.md) | Detect DLL side-loading and search-order hijacking (MITRE T1574) where adversaries plant malicious DLLs for legitimate signed a... |
| [`detecting-dnp3-protocol-anomalies`](skills/detecting-dnp3-protocol-anomalies/SKILL.md) | Detect anomalies in DNP3 communications used in SCADA/ICS systems by monitoring unauthorized control commands, firmware update ... |
| [`detecting-dns-exfiltration-with-dns-query-analysis`](skills/detecting-dns-exfiltration-with-dns-query-analysis/SKILL.md) | Detect data exfiltration via DNS tunneling (tools like iodine, dnscat2, dns2tcp) by analyzing query entropy, subdomain length, ... |
| [`detecting-email-account-compromise`](skills/detecting-email-account-compromise/SKILL.md) | Detect compromised O365 and Google Workspace email accounts by analyzing Unified Audit Logs and Azure AD sign-in logs for impos... |
| [`detecting-email-forwarding-rules-attack`](skills/detecting-email-forwarding-rules-attack/SKILL.md) | Detect malicious inbox/mail-flow forwarding rules that adversaries create to maintain |
| [`detecting-entra-offensive-tools-in-graph-logs`](skills/detecting-entra-offensive-tools-in-graph-logs/SKILL.md) | Hunt AADGraphActivityLogs and MicrosoftGraphActivityLogs in Microsoft Sentinel/Log Analytics using KQL to fingerprint offensive... |
| [`detecting-evasion-techniques-in-endpoint-logs`](skills/detecting-evasion-techniques-in-endpoint-logs/SKILL.md) | Detects defense evasion techniques used by adversaries in endpoint logs |
| [`detecting-exfiltration-over-dns-with-zeek`](skills/detecting-exfiltration-over-dns-with-zeek/SKILL.md) | Detect DNS-based data exfiltration by analyzing Zeek dns.log for high-entropy |
| [`detecting-fileless-attacks-on-endpoints`](skills/detecting-fileless-attacks-on-endpoints/SKILL.md) | Detects fileless malware and in-memory attacks that execute entirely |
| [`detecting-fileless-malware-techniques`](skills/detecting-fileless-malware-techniques/SKILL.md) | Detects and analyzes fileless malware that operates entirely in memory |
| [`detecting-golden-ticket-attacks-in-kerberos-logs`](skills/detecting-golden-ticket-attacks-in-kerberos-logs/SKILL.md) | Detect Golden Ticket attacks in Active Directory using Splunk and KQL queries |
| [`detecting-golden-ticket-forgery`](skills/detecting-golden-ticket-forgery/SKILL.md) | Detect Kerberos Golden Ticket forgery (e.g. Mimikatz-forged tickets) by analyzing |
| [`detecting-indirect-prompt-injection`](skills/detecting-indirect-prompt-injection/SKILL.md) | Detect and defend against indirect prompt injection hidden in web pages, documents, |
| [`detecting-insider-data-exfiltration-via-dlp`](skills/detecting-insider-data-exfiltration-via-dlp/SKILL.md) | Detects insider data exfiltration by analyzing DLP policy violations, |
| [`detecting-insider-threat-behaviors`](skills/detecting-insider-threat-behaviors/SKILL.md) | Detect insider threat behavioral indicators including unusual data access, |
| [`detecting-insider-threat-with-ueba`](skills/detecting-insider-threat-with-ueba/SKILL.md) | Implement User and Entity Behavior Analytics (UEBA) using Elasticsearch/OpenSearch |
| [`detecting-kerberoasting-attacks`](skills/detecting-kerberoasting-attacks/SKILL.md) | Detect Kerberoasting attacks by monitoring for anomalous Kerberos TGS |
| [`detecting-lateral-movement-in-network`](skills/detecting-lateral-movement-in-network/SKILL.md) | Identifies lateral movement techniques in enterprise networks by analyzing |
| [`detecting-lateral-movement-with-splunk`](skills/detecting-lateral-movement-with-splunk/SKILL.md) | Detect adversary lateral movement across networks using Splunk SPL queries |
| [`detecting-lateral-movement-with-zeek`](skills/detecting-lateral-movement-with-zeek/SKILL.md) | Detect lateral movement in network traffic using Zeek (formerly Bro) |
| [`detecting-living-off-the-land-attacks`](skills/detecting-living-off-the-land-attacks/SKILL.md) | Detect abuse of legitimate Windows binaries (LOLBins) used for living |
| [`detecting-living-off-the-land-with-lolbas`](skills/detecting-living-off-the-land-with-lolbas/SKILL.md) | Detect Living Off the Land Binaries (LOLBins/LOLBAS) abuse including |
| [`detecting-malicious-npm-packages`](skills/detecting-malicious-npm-packages/SKILL.md) | Triage npm packages and lockfiles for install-script malware, credential exfiltration, and worming behavior using GuardDog, man... |
| [`detecting-malicious-scheduled-tasks-with-sysmon`](skills/detecting-malicious-scheduled-tasks-with-sysmon/SKILL.md) | Detect malicious scheduled task creation and modification using Sysmon |
| [`detecting-mimikatz-execution-patterns`](skills/detecting-mimikatz-execution-patterns/SKILL.md) | Detect Mimikatz credential-dumping activity via command-line pattern matching, LSASS access signatures, binary/hash indicators,... |
| [`detecting-misconfigured-azure-storage`](skills/detecting-misconfigured-azure-storage/SKILL.md) | Audit Azure Storage accounts for public blob containers, missing encryption, overly permissive SAS tokens, disabled logging, an... |
| [`detecting-mobile-malware-behavior`](skills/detecting-mobile-malware-behavior/SKILL.md) | Detects and analyzes malicious behavior in mobile applications through |
| [`detecting-modbus-command-injection-attacks`](skills/detecting-modbus-command-injection-attacks/SKILL.md) | Detect command injection against Modbus TCP/RTU in ICS/SCADA environments by monitoring unauthorized writes, anomalous function... |
| [`detecting-modbus-protocol-anomalies`](skills/detecting-modbus-protocol-anomalies/SKILL.md) | Detect anomalies in Modbus/TCP and Modbus RTU industrial traffic via function code monitoring, register range validation, timin... |
| [`detecting-model-extraction-attacks`](skills/detecting-model-extraction-attacks/SKILL.md) | Detect MITRE ATLAS AML.T0024 attacks (model stealing, inversion, membership inference) performed via inference-API abuse, by mo... |
| [`detecting-network-anomalies-with-zeek`](skills/detecting-network-anomalies-with-zeek/SKILL.md) | Deploy and configure Zeek (formerly Bro) to passively analyze network traffic, generate structured connection/DNS/HTTP/SSL/file... |
| [`detecting-network-scanning-with-ids-signatures`](skills/detecting-network-scanning-with-ids-signatures/SKILL.md) | Detect network reconnaissance and port scanning using Suricata and Snort |
| [`detecting-ntlm-relay-with-event-correlation`](skills/detecting-ntlm-relay-with-event-correlation/SKILL.md) | Detect NTLM relay attacks (T1557.001) by correlating Windows Event 4624 LogonType 3 for IP-to-hostname mismatches, identifying ... |
| [`detecting-oauth-token-theft`](skills/detecting-oauth-token-theft/SKILL.md) | Detect and respond to OAuth token theft and replay in Microsoft Entra ID (Azure AD), covering access token theft, refresh token... |
| [`detecting-pass-the-hash-attacks`](skills/detecting-pass-the-hash-attacks/SKILL.md) | Detect Pass-the-Hash (T1550.002) attacks by analyzing NTLM authentication patterns, flagging Type 3 logons using NTLM where Ker... |
| [`detecting-pass-the-ticket-attacks`](skills/detecting-pass-the-ticket-attacks/SKILL.md) | Detect Kerberos Pass-the-Ticket (PtT) attacks by analyzing Windows Event IDs 4768, 4769, and 4771 for anomalous ticket usage pa... |
| [`detecting-port-scanning-with-fail2ban`](skills/detecting-port-scanning-with-fail2ban/SKILL.md) | Configures Fail2ban with custom filters and actions to detect port scanning |
| [`detecting-privilege-escalation-attempts`](skills/detecting-privilege-escalation-attempts/SKILL.md) | Detect privilege escalation attempts across Windows and Linux, including access token manipulation, UAC bypass, unquoted servic... |
| [`detecting-privilege-escalation-in-kubernetes-pods`](skills/detecting-privilege-escalation-in-kubernetes-pods/SKILL.md) | >- |
| [`detecting-process-hollowing-technique`](skills/detecting-process-hollowing-technique/SKILL.md) | Detect process hollowing (MITRE T1055.012) by analyzing memory-mapped |
| [`detecting-process-injection-techniques`](skills/detecting-process-injection-techniques/SKILL.md) | Detects and analyzes process injection techniques used by malware including |
| [`detecting-qr-code-phishing-with-email-security`](skills/detecting-qr-code-phishing-with-email-security/SKILL.md) | Detect and prevent QR code phishing (quishing) attacks that embed |
| [`detecting-ransomware-encryption-behavior`](skills/detecting-ransomware-encryption-behavior/SKILL.md) | Detects ransomware encryption activity in real time using entropy |
| [`detecting-ransomware-precursors-in-network`](skills/detecting-ransomware-precursors-in-network/SKILL.md) | Detects early-stage ransomware indicators in network traffic before |
| [`detecting-rdp-brute-force-attacks`](skills/detecting-rdp-brute-force-attacks/SKILL.md) | Detect RDP brute force attacks by parsing Windows Security Event Logs |
| [`detecting-rootkit-activity`](skills/detecting-rootkit-activity/SKILL.md) | Detects rootkit presence on compromised systems by identifying hidden |
| [`detecting-s3-data-exfiltration-attempts`](skills/detecting-s3-data-exfiltration-attempts/SKILL.md) | Detecting data exfiltration attempts from AWS S3 buckets by analyzing |
| [`detecting-secure-boot-bypass`](skills/detecting-secure-boot-bypass/SKILL.md) | Detect UEFI Secure Boot bypasses and bootkits such as BlackLotus and |
| [`detecting-serverless-function-injection`](skills/detecting-serverless-function-injection/SKILL.md) | Detects and prevents code injection attacks targeting serverless functions |
| [`detecting-service-account-abuse`](skills/detecting-service-account-abuse/SKILL.md) | Detect abuse of service accounts by hunting for anomalous interactive |
| [`detecting-shadow-api-endpoints`](skills/detecting-shadow-api-endpoints/SKILL.md) | Discover and inventory shadow API endpoints that operate outside |
| [`detecting-shadow-it-cloud-usage`](skills/detecting-shadow-it-cloud-usage/SKILL.md) | Detect unauthorized SaaS and cloud service usage (shadow IT) by parsing |
| [`detecting-spearphishing-with-email-gateway`](skills/detecting-spearphishing-with-email-gateway/SKILL.md) | Detect and block spearphishing emails that use personalized, researched |
| [`detecting-sql-injection-via-waf-logs`](skills/detecting-sql-injection-via-waf-logs/SKILL.md) | Analyze WAF (ModSecurity/AWS WAF/Cloudflare) logs to detect SQL injection |
| [`detecting-stuxnet-style-attacks`](skills/detecting-stuxnet-style-attacks/SKILL.md) | Detects sophisticated cyber-physical attacks that follow the Stuxnet |
| [`detecting-supply-chain-attacks-in-ci-cd`](skills/detecting-supply-chain-attacks-in-ci-cd/SKILL.md) | Scans GitHub Actions workflows and CI/CD pipeline configurations for |
| [`detecting-suspicious-oauth-application-consent`](skills/detecting-suspicious-oauth-application-consent/SKILL.md) | Detect risky OAuth application consent grants in Azure AD / Microsoft |
| [`detecting-suspicious-powershell-execution`](skills/detecting-suspicious-powershell-execution/SKILL.md) | Hunt for suspicious PowerShell execution (T1059.001) such as encoded commands, |
| [`detecting-t1003-credential-dumping-with-edr`](skills/detecting-t1003-credential-dumping-with-edr/SKILL.md) | Detect OS credential dumping (MITRE T1003) targeting LSASS memory, the SAM |
| [`detecting-t1055-process-injection-with-sysmon`](skills/detecting-t1055-process-injection-with-sysmon/SKILL.md) | Detect process injection techniques (T1055) - including DLL injection, process |
| [`detecting-t1548-abuse-elevation-control-mechanism`](skills/detecting-t1548-abuse-elevation-control-mechanism/SKILL.md) | Detect abuse of elevation control mechanisms (T1548), including Windows UAC |
| [`detecting-typosquatting-packages`](skills/detecting-typosquatting-packages/SKILL.md) | Flag misspelled, brandjacked, and typosquatted package names across npm, PyPI, and crates.io before installation, using edit-di... |
| [`detecting-typosquatting-packages-in-npm-pypi`](skills/detecting-typosquatting-packages-in-npm-pypi/SKILL.md) | Detects typosquatting attacks in npm and PyPI package registries by |
| [`detecting-wmi-persistence`](skills/detecting-wmi-persistence/SKILL.md) | Detect WMI event subscription persistence (MITRE T1546.003) by analyzing Sysmon |
| [`emulating-cloud-attacks-with-stratus-red-team`](skills/emulating-cloud-attacks-with-stratus-red-team/SKILL.md) | Install and run Stratus Red Team to detonate granular, MITRE ATT&CK-mapped |
| [`eradicating-malware-from-infected-systems`](skills/eradicating-malware-from-infected-systems/SKILL.md) | Systematically map and remove malware, backdoors, and attacker persistence |
| [`evaluating-threat-intelligence-platforms`](skills/evaluating-threat-intelligence-platforms/SKILL.md) | Evaluates and selects Threat Intelligence Platform (TIP) products based |
| [`executing-active-directory-attack-simulation`](skills/executing-active-directory-attack-simulation/SKILL.md) | Executes authorized attack simulations against Active Directory environments |
| [`executing-phishing-simulation-campaign`](skills/executing-phishing-simulation-campaign/SKILL.md) | Executes authorized phishing simulation campaigns to assess an organization''s |
| [`executing-red-team-exercise`](skills/executing-red-team-exercise/SKILL.md) | Run a stealthy, MITRE ATT&CK-mapped adversary emulation against an organization''s |
| [`exploiting-active-directory-certificate-services-esc1`](skills/exploiting-active-directory-certificate-services-esc1/SKILL.md) | Exploit misconfigured Active Directory Certificate Services (AD CS) ESC1 |
| [`exploiting-active-directory-with-bloodhound`](skills/exploiting-active-directory-with-bloodhound/SKILL.md) | BloodHound is a graph-based Active Directory reconnaissance tool that |
| [`exploiting-adcs-with-certipy`](skills/exploiting-adcs-with-certipy/SKILL.md) | Use Certipy to enumerate AD CS certificate authorities and templates over LDAP/RPC, then exploit ESC1-ESC16 misconfigurations -... |
| [`exploiting-api-injection-vulnerabilities`](skills/exploiting-api-injection-vulnerabilities/SKILL.md) | >- |
| [`exploiting-aws-with-pacu`](skills/exploiting-aws-with-pacu/SKILL.md) | >- |
| [`exploiting-bgp-hijacking-vulnerabilities`](skills/exploiting-bgp-hijacking-vulnerabilities/SKILL.md) | Analyzes and simulates BGP hijacking scenarios in authorized lab environments |
| [`exploiting-broken-function-level-authorization`](skills/exploiting-broken-function-level-authorization/SKILL.md) | >- |
| [`exploiting-broken-link-hijacking`](skills/exploiting-broken-link-hijacking/SKILL.md) | >- |
| [`exploiting-constrained-delegation-abuse`](skills/exploiting-constrained-delegation-abuse/SKILL.md) | >- |
| [`exploiting-deeplink-vulnerabilities`](skills/exploiting-deeplink-vulnerabilities/SKILL.md) | Tests and exploits deep link (URL scheme and App Link) vulnerabilities |
| [`exploiting-excessive-data-exposure-in-api`](skills/exploiting-excessive-data-exposure-in-api/SKILL.md) | >- |
| [`exploiting-http-request-smuggling`](skills/exploiting-http-request-smuggling/SKILL.md) | >- |
| [`exploiting-idor-vulnerabilities`](skills/exploiting-idor-vulnerabilities/SKILL.md) | >- |
| [`exploiting-insecure-data-storage-in-mobile`](skills/exploiting-insecure-data-storage-in-mobile/SKILL.md) | Identifies and exploits insecure local data storage vulnerabilities |
| [`exploiting-insecure-deserialization`](skills/exploiting-insecure-deserialization/SKILL.md) | Identifying and exploiting insecure deserialization vulnerabilities in |
| [`exploiting-ipv6-vulnerabilities`](skills/exploiting-ipv6-vulnerabilities/SKILL.md) | Identifies and exploits IPv6-specific vulnerabilities including SLAAC |
| [`exploiting-jwt-algorithm-confusion-attack`](skills/exploiting-jwt-algorithm-confusion-attack/SKILL.md) | >- |
| [`exploiting-kerberoasting-with-impacket`](skills/exploiting-kerberoasting-with-impacket/SKILL.md) | >- |
| [`exploiting-mass-assignment-in-rest-apis`](skills/exploiting-mass-assignment-in-rest-apis/SKILL.md) | >- |
| [`exploiting-ms17-010-eternalblue-vulnerability`](skills/exploiting-ms17-010-eternalblue-vulnerability/SKILL.md) | >- |
| [`exploiting-nopac-cve-2021-42278-42287`](skills/exploiting-nopac-cve-2021-42278-42287/SKILL.md) | Exploits the noPac Active Directory privilege-escalation chain (CVE-2021-42278 |
| [`exploiting-nosql-injection-vulnerabilities`](skills/exploiting-nosql-injection-vulnerabilities/SKILL.md) | Detects and exploits NoSQL injection vulnerabilities in MongoDB, CouchDB, |
| [`exploiting-oauth-misconfiguration`](skills/exploiting-oauth-misconfiguration/SKILL.md) | Identifying and exploiting OAuth 2.0 and OpenID Connect misconfigurations |
| [`exploiting-prototype-pollution-in-javascript`](skills/exploiting-prototype-pollution-in-javascript/SKILL.md) | Detects and exploits JavaScript prototype pollution vulnerabilities |
| [`exploiting-race-condition-vulnerabilities`](skills/exploiting-race-condition-vulnerabilities/SKILL.md) | Detects and exploits race condition (TOCTOU) vulnerabilities in web |
| [`exploiting-server-side-request-forgery`](skills/exploiting-server-side-request-forgery/SKILL.md) | Identifying and exploiting SSRF vulnerabilities to access internal services, |
| [`exploiting-smb-vulnerabilities-with-metasploit`](skills/exploiting-smb-vulnerabilities-with-metasploit/SKILL.md) | Identifies and exploits SMB protocol vulnerabilities using Metasploit |
| [`exploiting-sql-injection-vulnerabilities`](skills/exploiting-sql-injection-vulnerabilities/SKILL.md) | Identifies and exploits SQL injection vulnerabilities in web applications |
| [`exploiting-sql-injection-with-sqlmap`](skills/exploiting-sql-injection-with-sqlmap/SKILL.md) | Detecting and exploiting SQL injection vulnerabilities using sqlmap to |
| [`exploiting-template-injection-vulnerabilities`](skills/exploiting-template-injection-vulnerabilities/SKILL.md) | Detects and exploits Server-Side Template Injection (SSTI) vulnerabilities |
| [`exploiting-type-juggling-vulnerabilities`](skills/exploiting-type-juggling-vulnerabilities/SKILL.md) | Exploits PHP type juggling vulnerabilities caused by loose (==) comparison |
| [`exploiting-vulnerabilities-with-metasploit-framework`](skills/exploiting-vulnerabilities-with-metasploit-framework/SKILL.md) | Uses the Metasploit Framework (msfconsole and its exploit, auxiliary, |
| [`exploiting-websocket-vulnerabilities`](skills/exploiting-websocket-vulnerabilities/SKILL.md) | Testing WebSocket implementations for authentication bypass, cross-site |
| [`exploiting-zerologon-vulnerability-cve-2020-1472`](skills/exploiting-zerologon-vulnerability-cve-2020-1472/SKILL.md) | Exploits the Zerologon vulnerability (CVE-2020-1472) in the Netlogon |
| [`extracting-iocs-from-malware-samples`](skills/extracting-iocs-from-malware-samples/SKILL.md) | Extracts indicators of compromise (IOCs) from malware samples, including |
| [`extracting-memory-artifacts-with-rekall`](skills/extracting-memory-artifacts-with-rekall/SKILL.md) | Uses Rekall memory forensics framework to analyze memory dumps for process |
| [`fleet-hunting-with-velociraptor`](skills/fleet-hunting-with-velociraptor/SKILL.md) | Deploy a Velociraptor server and agents, then author VQL (Velociraptor Query Language) artifacts and run them as fleet-wide hun... |
| [`generating-and-analyzing-sboms`](skills/generating-and-analyzing-sboms/SKILL.md) | Generate CycloneDX and SPDX SBOMs from container images and filesystems with Syft, correlate them to CVEs with Grype, and sign/... |
| [`generating-forensic-timelines-with-hayabusa`](skills/generating-forensic-timelines-with-hayabusa/SKILL.md) | Run Hayabusa against collected Windows EVTX files to apply Sigma detection rules and produce a prioritized, chronological CSV/J... |
| [`generating-threat-intelligence-reports`](skills/generating-threat-intelligence-reports/SKILL.md) | Generates structured cyber threat intelligence reports at strategic, |
| [`hunting-advanced-persistent-threats`](skills/hunting-advanced-persistent-threats/SKILL.md) | Proactively hunts for Advanced Persistent Threat (APT) activity within |
| [`hunting-bootkits-in-efi-system-partition`](skills/hunting-bootkits-in-efi-system-partition/SKILL.md) | Baseline the EFI System Partition and hunt malicious EFI binaries such as ESPecter, BlackLotus, Bootkitty, and Glupteba by moun... |
| [`hunting-credential-stuffing-attacks`](skills/hunting-credential-stuffing-attacks/SKILL.md) | Detects credential stuffing attacks by analyzing authentication logs |
| [`hunting-evtx-with-chainsaw`](skills/hunting-evtx-with-chainsaw/SKILL.md) | Run Chainsaw against collected Windows EVTX files to hunt with the SigmaHQ rule corpus, built-in detection rules, and high-spee... |
| [`hunting-for-anomalous-powershell-execution`](skills/hunting-for-anomalous-powershell-execution/SKILL.md) | Hunt for malicious PowerShell activity by analyzing Script Block Logging |
| [`hunting-for-beaconing-with-frequency-analysis`](skills/hunting-for-beaconing-with-frequency-analysis/SKILL.md) | Identify command-and-control beaconing patterns in network traffic by |
| [`hunting-for-cobalt-strike-beacons`](skills/hunting-for-cobalt-strike-beacons/SKILL.md) | Detect Cobalt Strike beacon command-and-control traffic using default TLS certificate signatures (serial 8BB00EE), JA3/JA3S/JAR... |
| [`hunting-for-command-and-control-beaconing`](skills/hunting-for-command-and-control-beaconing/SKILL.md) | Detect C2 beaconing patterns in network traffic using frequency analysis, |
| [`hunting-for-data-exfiltration-indicators`](skills/hunting-for-data-exfiltration-indicators/SKILL.md) | Hunt for data exfiltration by analyzing Zeek and Suricata network telemetry for unusual data flows, DNS tunneling via large/fre... |
| [`hunting-for-data-staging-before-exfiltration`](skills/hunting-for-data-staging-before-exfiltration/SKILL.md) | Detect data-staging activity (MITRE ATT&CK T1074) by analyzing EDR/Sysmon process-creation and file-system telemetry (Event ID ... |
| [`hunting-for-dcom-lateral-movement`](skills/hunting-for-dcom-lateral-movement/SKILL.md) | Hunt for DCOM-based lateral movement (MITRE ATT&CK T1021.003) by detecting |
| [`hunting-for-dcsync-attacks`](skills/hunting-for-dcsync-attacks/SKILL.md) | Detect DCSync attacks (MITRE ATT&CK T1003.006) by analyzing Windows Event ID 4662 (AccessMask 0x100) for DS-Replication-Get-Cha... |
| [`hunting-for-defense-evasion-via-timestomping`](skills/hunting-for-defense-evasion-via-timestomping/SKILL.md) | Detect NTFS timestamp manipulation (MITRE T1070.006) by comparing $STANDARD_INFORMATION |
| [`hunting-for-dns-based-persistence`](skills/hunting-for-dns-based-persistence/SKILL.md) | Hunts for DNS-based persistence mechanisms such as DNS hijacking, dangling |
| [`hunting-for-dns-tunneling-with-zeek`](skills/hunting-for-dns-tunneling-with-zeek/SKILL.md) | Detects DNS tunneling and covert-channel data exfiltration by analyzing |
| [`hunting-for-domain-fronting-c2-traffic`](skills/hunting-for-domain-fronting-c2-traffic/SKILL.md) | Detects domain fronting C2 traffic by analyzing SNI-vs-HTTP-Host-header |
| [`hunting-for-lateral-movement-via-wmi`](skills/hunting-for-lateral-movement-via-wmi/SKILL.md) | Detects WMI-based lateral movement (e.g. wmic process call create, |
| [`hunting-for-living-off-the-cloud-techniques`](skills/hunting-for-living-off-the-cloud-techniques/SKILL.md) | Hunts for adversary abuse of legitimate cloud services (Azure, AWS, GCP, |
| [`hunting-for-living-off-the-land-binaries`](skills/hunting-for-living-off-the-land-binaries/SKILL.md) | Proactively hunts for adversary abuse of legitimate, signed system binaries |
| [`hunting-for-lolbins-execution-in-endpoint-logs`](skills/hunting-for-lolbins-execution-in-endpoint-logs/SKILL.md) | Hunts for LOLBins (Living Off the Land Binaries) abuse, mapped to MITRE |
| [`hunting-for-ntlm-relay-attacks`](skills/hunting-for-ntlm-relay-attacks/SKILL.md) | Detects NTLM relay attacks (MITRE T1557.001) by analyzing Windows Event |
| [`hunting-for-persistence-mechanisms-in-windows`](skills/hunting-for-persistence-mechanisms-in-windows/SKILL.md) | Systematically hunts for adversary persistence mechanisms across Windows |
| [`hunting-for-persistence-via-wmi-subscriptions`](skills/hunting-for-persistence-via-wmi-subscriptions/SKILL.md) | Hunts for adversary persistence via WMI event subscriptions (MITRE T1546.003) |
| [`hunting-for-process-injection-techniques`](skills/hunting-for-process-injection-techniques/SKILL.md) | Detects process injection techniques (MITRE T1055) — including |
| [`hunting-for-registry-persistence-mechanisms`](skills/hunting-for-registry-persistence-mechanisms/SKILL.md) | Hunts for registry-based persistence mechanisms (MITRE T1547) in Windows |
| [`hunting-for-registry-run-key-persistence`](skills/hunting-for-registry-run-key-persistence/SKILL.md) | Detect MITRE ATT&CK T1547.001 registry Run key persistence by analyzing |
| [`hunting-for-scheduled-task-persistence`](skills/hunting-for-scheduled-task-persistence/SKILL.md) | Runs a hypothesis-driven threat hunt for Windows Scheduled Task persistence (T1053), guiding SIEM/EDR queries against task crea... |
| [`hunting-for-shadow-copy-deletion`](skills/hunting-for-shadow-copy-deletion/SKILL.md) | Runs a hypothesis-driven threat hunt for Volume Shadow Copy deletion (T1490) by querying SIEM/EDR telemetry for vssadmin, wmic ... |
| [`hunting-for-spearphishing-indicators`](skills/hunting-for-spearphishing-indicators/SKILL.md) | Hunt for spearphishing campaign indicators across email logs, endpoint |
| [`hunting-for-startup-folder-persistence`](skills/hunting-for-startup-folder-persistence/SKILL.md) | Detects T1547.001 startup folder persistence by monitoring Windows startup directories for suspicious file creation, cross-refe... |
| [`hunting-for-supply-chain-compromise`](skills/hunting-for-supply-chain-compromise/SKILL.md) | Runs a hypothesis-driven threat hunt for supply-chain compromise (T1195) by querying SIEM/EDR logs for trojanized software upda... |
| [`hunting-for-suspicious-scheduled-tasks`](skills/hunting-for-suspicious-scheduled-tasks/SKILL.md) | Hunts for adversary persistence and execution via Windows scheduled tasks (T1053.005) by analyzing Security Event ID 4698 task-... |
| [`hunting-for-t1098-account-manipulation`](skills/hunting-for-t1098-account-manipulation/SKILL.md) | Hunts for MITRE ATT&CK T1098 account manipulation - shadow admin creation, SID history injection, group membership changes, and... |
| [`hunting-for-unusual-network-connections`](skills/hunting-for-unusual-network-connections/SKILL.md) | Runs a hypothesis-driven threat hunt for command-and-control activity (T1071) by querying SIEM/EDR network telemetry for anomal... |
| [`hunting-for-unusual-service-installations`](skills/hunting-for-unusual-service-installations/SKILL.md) | Detects suspicious Windows service installations (MITRE ATT&CK T1543.003) by parsing System event log Event ID 7045, analyzing ... |
| [`hunting-for-webshell-activity`](skills/hunting-for-webshell-activity/SKILL.md) | Runs a hypothesis-driven threat hunt for web shell deployment (T1505.003) on internet-facing servers by analyzing file creation... |
| [`hunting-saas-sso-token-abuse`](skills/hunting-saas-sso-token-abuse/SKILL.md) | Hunts for stolen-session and OAuth/PRT token replay (T1550.001) by correlating Microsoft Entra ID SigninLogs SessionId/UniqueTo... |
| [`implementing-anti-phishing-training-program`](skills/implementing-anti-phishing-training-program/SKILL.md) | Guides designing, deploying, and measuring an anti-phishing security awareness program - baseline phishing simulations, interac... |
| [`implementing-anti-ransomware-group-policy`](skills/implementing-anti-ransomware-group-policy/SKILL.md) | Configures Windows Group Policy Objects to block ransomware execution |
| [`implementing-api-threat-protection-with-apigee`](skills/implementing-api-threat-protection-with-apigee/SKILL.md) | Implements API threat protection using Google Apigee reverse-proxy |
| [`implementing-cloud-trail-log-analysis`](skills/implementing-cloud-trail-log-analysis/SKILL.md) | Implementing AWS CloudTrail log analysis for security monitoring, threat |
| [`implementing-cloud-vulnerability-posture-management`](skills/implementing-cloud-vulnerability-posture-management/SKILL.md) | Implement multi-cloud CSPM to detect cloud-native misconfigurations |
| [`implementing-dmarc-dkim-spf-email-security`](skills/implementing-dmarc-dkim-spf-email-security/SKILL.md) | Configures SPF, DKIM, and DMARC DNS TXT records to authenticate outbound email, prevent domain spoofing, and enforce a rejectio... |
| [`implementing-dragos-platform-for-ot-monitoring`](skills/implementing-dragos-platform-for-ot-monitoring/SKILL.md) | Deploys and configures Dragos Platform sensors and detection analytics for OT/ICS network monitoring, using industrial protocol... |
| [`implementing-epss-score-for-vulnerability-prioritization`](skills/implementing-epss-score-for-vulnerability-prioritization/SKILL.md) | Queries FIRST's Exploit Prediction Scoring System (EPSS) API to fetch exploitation-probability and percentile scores for CVEs, ... |
| [`implementing-fuzz-testing-in-cicd-with-aflplusplus`](skills/implementing-fuzz-testing-in-cicd-with-aflplusplus/SKILL.md) | Integrates AFL++ coverage-guided fuzzing into CI/CD pipelines, covering harness construction, AFL++/AddressSanitizer/CmpLog ins... |
| [`implementing-github-advanced-security-for-code-scanning`](skills/implementing-github-advanced-security-for-code-scanning/SKILL.md) | Configures GitHub Advanced Security (code scanning with CodeQL, secret scanning, dependency review, and Dependabot alerts) to p... |
| [`implementing-google-workspace-phishing-protection`](skills/implementing-google-workspace-phishing-protection/SKILL.md) | Configures Google Workspace advanced phishing and malware protection settings in the Admin Console — pre-delivery message scann... |
| [`implementing-honeypot-for-ransomware-detection`](skills/implementing-honeypot-for-ransomware-detection/SKILL.md) | Deploys canary files, honeypot shares, and decoy systems to detect ransomware |
| [`implementing-immutable-backup-with-restic`](skills/implementing-immutable-backup-with-restic/SKILL.md) | Implements ransomware-resistant backups using restic with S3-compatible |
| [`implementing-mitre-attack-coverage-mapping`](skills/implementing-mitre-attack-coverage-mapping/SKILL.md) | Implement MITRE ATT&CK coverage mapping to identify detection gaps, prioritize |
| [`implementing-ransomware-backup-strategy`](skills/implementing-ransomware-backup-strategy/SKILL.md) | Designs a ransomware-resilient backup strategy using the 3-2-1-1-0 |
| [`implementing-ransomware-kill-switch-detection`](skills/implementing-ransomware-kill-switch-detection/SKILL.md) | Analyzes ransomware kill switch mechanisms, including mutex-based execution |
| [`implementing-security-information-sharing-with-stix2`](skills/implementing-security-information-sharing-with-stix2/SKILL.md) | Create, validate, and share STIX 2.1 threat intelligence objects (indicators, |
| [`implementing-soar-playbook-for-phishing`](skills/implementing-soar-playbook-for-phishing/SKILL.md) | Automates phishing incident response by calling the Splunk SOAR (Phantom) |
| [`implementing-stix-taxii-feed-integration`](skills/implementing-stix-taxii-feed-integration/SKILL.md) | Implements a STIX 2.1/TAXII 2.1 threat-intelligence feed consumer and |
| [`implementing-threat-intelligence-lifecycle-management`](skills/implementing-threat-intelligence-lifecycle-management/SKILL.md) | Build out a full CTI program around the six-phase threat intelligence |
| [`implementing-threat-modeling-with-mitre-attack`](skills/implementing-threat-modeling-with-mitre-attack/SKILL.md) | Implements threat modeling using the MITRE ATT&CK framework to map adversary |
| [`implementing-velociraptor-for-ir-collection`](skills/implementing-velociraptor-for-ir-collection/SKILL.md) | Deploy and configure Velociraptor for scalable endpoint forensic artifact |
| [`implementing-vulnerability-management-with-greenbone`](skills/implementing-vulnerability-management-with-greenbone/SKILL.md) | Deploy and operate Greenbone/OpenVAS vulnerability management using the |
| [`implementing-vulnerability-remediation-sla`](skills/implementing-vulnerability-remediation-sla/SKILL.md) | Design a vulnerability remediation SLA program covering asset tiering, |
| [`implementing-vulnerability-sla-breach-alerting`](skills/implementing-vulnerability-sla-breach-alerting/SKILL.md) | Build an automated SLA breach alerting system for vulnerability remediation, |
| [`implementing-zero-trust-dns-with-nextdns`](skills/implementing-zero-trust-dns-with-nextdns/SKILL.md) | Configure NextDNS as an encrypted (DoH/DoT) zero trust DNS resolver that blocks malicious, phishing, and cryptojacking domains ... |
| [`integrating-sast-into-github-actions-pipeline`](skills/integrating-sast-into-github-actions-pipeline/SKILL.md) | Integrates CodeQL and Semgrep SAST scanning into GitHub Actions, covering scans on pull requests/pushes, rule tuning to cut fal... |
| [`investigating-insider-threat-indicators`](skills/investigating-insider-threat-indicators/SKILL.md) | Investigates insider threat indicators including data exfiltration attempts, |
| [`investigating-phishing-email-incident`](skills/investigating-phishing-email-incident/SKILL.md) | Investigates phishing email incidents from initial user report through |
| [`investigating-ransomware-attack-artifacts`](skills/investigating-ransomware-attack-artifacts/SKILL.md) | Forensically preserve memory and disk, collect ransom notes and encrypted file samples, and identify the ransomware variant usi... |
| [`managing-intelligence-lifecycle`](skills/managing-intelligence-lifecycle/SKILL.md) | Manages the end-to-end cyber threat intelligence lifecycle from planning |
| [`mapping-mitre-attack-techniques`](skills/mapping-mitre-attack-techniques/SKILL.md) | Maps observed adversary behaviors, security alerts, and detection rules |
| [`modeling-threats-with-opencti`](skills/modeling-threats-with-opencti/SKILL.md) | Deploy OpenCTI (Filigran) via Docker Compose and use the pycti Python client to model threat actors, intrusion sets, campaigns,... |
| [`monitoring-darkweb-sources`](skills/monitoring-darkweb-sources/SKILL.md) | Monitors dark web forums, marketplaces, paste sites, and ransomware |
| [`moving-laterally-with-netexec`](skills/moving-laterally-with-netexec/SKILL.md) | Use NetExec (nxc) to validate credentials, enumerate SMB shares/users/policy, password-spray safely across lockout thresholds, ... |
| [`operating-havoc-c2`](skills/operating-havoc-c2/SKILL.md) | Deploy a Havoc C2 team server with Yaotl malleable profiles, generate evasive Demon agents using indirect syscalls and sleep ob... |
| [`operating-sliver-c2`](skills/operating-sliver-c2/SKILL.md) | Stand up a Sliver C2 server and mTLS listeners, generate cross-platform implants and beacons, and run post-exploitation, pivoti... |
| [`operationalizing-misp-threat-feeds`](skills/operationalizing-misp-threat-feeds/SKILL.md) | Stand up MISP, enable and cache curated threat feeds (CIRCL, abuse.ch, Feodo Tracker), apply warninglists to suppress false pos... |
| [`parsing-artifacts-with-eric-zimmerman-tools`](skills/parsing-artifacts-with-eric-zimmerman-tools/SKILL.md) | Parse Windows forensic artifacts—$MFT/$J (MFTECmd), Prefetch (PECmd), registry hives (RECmd), shellbags, and Amcache—into norma... |
| [`performing-active-directory-bloodhound-analysis`](skills/performing-active-directory-bloodhound-analysis/SKILL.md) | Use BloodHound and SharpHound (or AzureHound) to enumerate Active Directory |
| [`performing-active-directory-compromise-investigation`](skills/performing-active-directory-compromise-investigation/SKILL.md) | Investigate Active Directory compromise by analyzing authentication logs, |
| [`performing-active-directory-forest-trust-attack`](skills/performing-active-directory-forest-trust-attack/SKILL.md) | Enumerate and audit Active Directory forest trust relationships using |
| [`performing-active-directory-penetration-test`](skills/performing-active-directory-penetration-test/SKILL.md) | Conduct a focused Active Directory penetration test using BloodHound, |
| [`performing-active-directory-vulnerability-assessment`](skills/performing-active-directory-vulnerability-assessment/SKILL.md) | Assess Active Directory security posture using PingCastle, BloodHound, |
| [`performing-adversary-in-the-middle-phishing-detection`](skills/performing-adversary-in-the-middle-phishing-detection/SKILL.md) | Detect and respond to Adversary-in-the-Middle (AiTM) phishing attacks |
| [`performing-agentless-vulnerability-scanning`](skills/performing-agentless-vulnerability-scanning/SKILL.md) | Configure and execute agentless vulnerability scanning using network |
| [`performing-authenticated-scan-with-openvas`](skills/performing-authenticated-scan-with-openvas/SKILL.md) | Configure and execute authenticated (credentialed) vulnerability scans using OpenVAS/Greenbone |
| [`performing-authenticated-vulnerability-scan`](skills/performing-authenticated-vulnerability-scan/SKILL.md) | Plan and run authenticated (credentialed) vulnerability scans with scanners such as |
| [`performing-automated-malware-analysis-with-cape`](skills/performing-automated-malware-analysis-with-cape/SKILL.md) | Deploy and operate the CAPEv2 malware sandbox (a Cuckoo derivative) to run samples in a |
| [`performing-binary-exploitation-analysis`](skills/performing-binary-exploitation-analysis/SKILL.md) | Analyze ELF binaries for memory-corruption vulnerabilities and build proof-of-concept |
| [`performing-blind-ssrf-exploitation`](skills/performing-blind-ssrf-exploitation/SKILL.md) | Detect and exploit blind Server-Side Request Forgery (SSRF) using out-of-band |
| [`performing-cloud-forensics-investigation`](skills/performing-cloud-forensics-investigation/SKILL.md) | Collect and analyze cloud forensic evidence using AWS CLI, Azure CLI, or gcloud |
| [`performing-cloud-forensics-with-aws-cloudtrail`](skills/performing-cloud-forensics-with-aws-cloudtrail/SKILL.md) | Investigate AWS account compromise by querying CloudTrail with boto3's LookupEvents |
| [`performing-cloud-log-forensics-with-athena`](skills/performing-cloud-log-forensics-with-athena/SKILL.md) | Uses AWS Athena to query CloudTrail, VPC Flow Logs, S3 access logs, |
| [`performing-cloud-native-forensics-with-falco`](skills/performing-cloud-native-forensics-with-falco/SKILL.md) | Uses Falco YAML rules for runtime threat detection in containers and |
| [`performing-cloud-native-threat-hunting-with-aws-detective`](skills/performing-cloud-native-threat-hunting-with-aws-detective/SKILL.md) | Investigate AWS security incidents using Amazon Detective's behavior graphs, |
| [`performing-cloud-penetration-testing-with-pacu`](skills/performing-cloud-penetration-testing-with-pacu/SKILL.md) | Run authorized AWS penetration tests with Pacu, the open-source AWS exploitation |
| [`performing-cloud-storage-forensic-acquisition`](skills/performing-cloud-storage-forensic-acquisition/SKILL.md) | Perform forensic acquisition of cloud storage services including Google |
| [`performing-cve-prioritization-with-kev-catalog`](skills/performing-cve-prioritization-with-kev-catalog/SKILL.md) | Fetch and parse the CISA Known Exploited Vulnerabilities (KEV) catalog, |
| [`performing-dark-web-monitoring-for-threats`](skills/performing-dark-web-monitoring-for-threats/SKILL.md) | Dark web monitoring involves systematically scanning Tor hidden services, |
| [`performing-disk-forensics-investigation`](skills/performing-disk-forensics-investigation/SKILL.md) | Conduct disk forensics investigations using forensic imaging, file system |
| [`performing-dynamic-analysis-with-any-run`](skills/performing-dynamic-analysis-with-any-run/SKILL.md) | Perform interactive dynamic malware analysis using the ANY.RUN cloud sandbox |
| [`performing-endpoint-forensics-investigation`](skills/performing-endpoint-forensics-investigation/SKILL.md) | Performs digital forensics investigation on compromised endpoints including |
| [`performing-endpoint-vulnerability-remediation`](skills/performing-endpoint-vulnerability-remediation/SKILL.md) | Performs vulnerability remediation on endpoints by prioritizing CVEs |
| [`performing-firmware-malware-analysis`](skills/performing-firmware-malware-analysis/SKILL.md) | Analyzes firmware images for embedded malware, backdoors, and unauthorized |
| [`performing-insider-threat-investigation`](skills/performing-insider-threat-investigation/SKILL.md) | Investigates insider threat incidents involving employees, contractors, |
| [`performing-kerberoasting-attack`](skills/performing-kerberoasting-attack/SKILL.md) | Perform Kerberoasting, a post-exploitation technique that enumerates |
| [`performing-linux-log-forensics-investigation`](skills/performing-linux-log-forensics-investigation/SKILL.md) | Perform forensic investigation of Linux system logs including syslog, |
| [`performing-log-analysis-for-forensic-investigation`](skills/performing-log-analysis-for-forensic-investigation/SKILL.md) | Collect, parse, and correlate system, application, and security logs |
| [`performing-malware-hash-enrichment-with-virustotal`](skills/performing-malware-hash-enrichment-with-virustotal/SKILL.md) | Enrich malware file hashes (MD5, SHA-1, SHA-256) using the VirusTotal |
| [`performing-malware-ioc-extraction`](skills/performing-malware-ioc-extraction/SKILL.md) | Malware IOC extraction is the process of analyzing malicious software |
| [`performing-malware-persistence-investigation`](skills/performing-malware-persistence-investigation/SKILL.md) | Systematically investigate all persistence mechanisms on Windows and |
| [`performing-malware-triage-with-yara`](skills/performing-malware-triage-with-yara/SKILL.md) | Performs rapid malware triage and classification using YARA rules that |
| [`performing-memory-forensics-with-volatility3`](skills/performing-memory-forensics-with-volatility3/SKILL.md) | Analyze volatile memory (RAM) dumps using the Volatility 3 framework |
| [`performing-memory-forensics-with-volatility3-plugins`](skills/performing-memory-forensics-with-volatility3-plugins/SKILL.md) | Analyze memory dumps using Volatility3 plugins to detect injected code, |
| [`performing-mobile-device-forensics-with-cellebrite`](skills/performing-mobile-device-forensics-with-cellebrite/SKILL.md) | Acquire and analyze mobile device data using Cellebrite UFED Touch/4PC, UFED Physical Analyzer, and open-source alternatives (A... |
| [`performing-network-forensics-with-wireshark`](skills/performing-network-forensics-with-wireshark/SKILL.md) | Capture and analyze network traffic using Wireshark and tshark to reconstruct network events from PCAP/PCAPNG files, extract tr... |
| [`performing-network-packet-capture-analysis`](skills/performing-network-packet-capture-analysis/SKILL.md) | Perform forensic analysis of network packet captures (PCAP/PCAPNG) using Wireshark, tshark, and tcpdump to reconstruct network ... |
| [`performing-network-traffic-analysis-with-zeek`](skills/performing-network-traffic-analysis-with-zeek/SKILL.md) | Deploy Zeek (formerly Bro) as a passive network security monitor to generate structured logs of protocol metadata (HTTP, DNS, T... |
| [`performing-osint-with-spiderfoot`](skills/performing-osint-with-spiderfoot/SKILL.md) | Automate OSINT collection with the SpiderFoot REST API and CLI (sf.py/spiderfoot-cli) across 200+ modules, selecting scan modes... |
| [`performing-ot-vulnerability-assessment-with-claroty`](skills/performing-ot-vulnerability-assessment-with-claroty/SKILL.md) | Perform OT vulnerability assessments using the Claroty xDome platform for asset discovery, risk scoring, and vulnerability corr... |
| [`performing-ot-vulnerability-scanning-safely`](skills/performing-ot-vulnerability-scanning-safely/SKILL.md) | Perform vulnerability scanning in OT/ICS environments safely using passive |
| [`performing-phishing-simulation-with-gophish`](skills/performing-phishing-simulation-with-gophish/SKILL.md) | Deploy and run authorized phishing awareness campaigns with GoPhish, covering admin panel setup, SMTP sending profiles, email t... |
| [`performing-power-grid-cybersecurity-assessment`](skills/performing-power-grid-cybersecurity-assessment/SKILL.md) | Conduct cybersecurity assessments of power grid infrastructure spanning generation, transmission substations, distribution, and... |
| [`performing-purple-team-atomic-testing`](skills/performing-purple-team-atomic-testing/SKILL.md) | Executes Atomic Red Team tests mapped to MITRE ATT&CK via Invoke-AtomicRedTeam |
| [`performing-ransomware-response`](skills/performing-ransomware-response/SKILL.md) | Executes a structured ransomware incident response from detection through |
| [`performing-ransomware-tabletop-exercise`](skills/performing-ransomware-tabletop-exercise/SKILL.md) | Plans and facilitates tabletop exercises simulating ransomware incidents, |
| [`performing-red-team-phishing-with-gophish`](skills/performing-red-team-phishing-with-gophish/SKILL.md) | Automates GoPhish phishing simulation campaigns using the Python gophish |
| [`performing-red-team-with-covenant`](skills/performing-red-team-with-covenant/SKILL.md) | Conducts red team operations using the Covenant C2 framework for authorized |
| [`performing-second-order-sql-injection`](skills/performing-second-order-sql-injection/SKILL.md) | Detect and exploit second-order SQL injection vulnerabilities where malicious |
| [`performing-soc2-type2-audit-preparation`](skills/performing-soc2-type2-audit-preparation/SKILL.md) | Automates SOC 2 Type II audit preparation including gap assessment against |
| [`performing-sqlite-database-forensics`](skills/performing-sqlite-database-forensics/SKILL.md) | Performs forensic analysis of SQLite databases by examining B-tree page |
| [`performing-ssrf-vulnerability-exploitation`](skills/performing-ssrf-vulnerability-exploitation/SKILL.md) | >- |
| [`performing-static-malware-analysis-with-pe-studio`](skills/performing-static-malware-analysis-with-pe-studio/SKILL.md) | >- |
| [`performing-threat-emulation-with-atomic-red-team`](skills/performing-threat-emulation-with-atomic-red-team/SKILL.md) | Executes Atomic Red Team tests for MITRE ATT&CK technique validation |
| [`performing-threat-hunting-with-elastic-siem`](skills/performing-threat-hunting-with-elastic-siem/SKILL.md) | Performs proactive threat hunting in Elastic Security SIEM using KQL/EQL |
| [`performing-threat-hunting-with-yara-rules`](skills/performing-threat-hunting-with-yara-rules/SKILL.md) | Use YARA pattern-matching rules to hunt for malware, suspicious files, |
| [`performing-threat-intelligence-sharing-with-misp`](skills/performing-threat-intelligence-sharing-with-misp/SKILL.md) | >- |
| [`performing-threat-landscape-assessment-for-sector`](skills/performing-threat-landscape-assessment-for-sector/SKILL.md) | >- |
| [`performing-threat-modeling-with-owasp-threat-dragon`](skills/performing-threat-modeling-with-owasp-threat-dragon/SKILL.md) | >- |
| [`performing-vulnerability-scanning-with-nessus`](skills/performing-vulnerability-scanning-with-nessus/SKILL.md) | Performs authenticated and unauthenticated vulnerability scanning using |
| [`performing-web-application-vulnerability-triage`](skills/performing-web-application-vulnerability-triage/SKILL.md) | Triages web application vulnerability findings from DAST/SAST scanners |
| [`performing-web-cache-deception-attack`](skills/performing-web-cache-deception-attack/SKILL.md) | Executes web cache deception attacks by exploiting path normalization |
| [`performing-web-cache-poisoning-attack`](skills/performing-web-cache-poisoning-attack/SKILL.md) | Exploiting web cache mechanisms to serve malicious content to other users |
| [`performing-windows-artifact-analysis-with-eric-zimmerman-tools`](skills/performing-windows-artifact-analysis-with-eric-zimmerman-tools/SKILL.md) | Performs comprehensive Windows forensic artifact analysis using Eric |
| [`performing-yara-rule-development-for-detection`](skills/performing-yara-rule-development-for-detection/SKILL.md) | Develops precise YARA and YARA-X rules for malware detection by identifying |
| [`post-exploiting-microsoft-graph-with-graphrunner`](skills/post-exploiting-microsoft-graph-with-graphrunner/SKILL.md) | Runs GraphRunner, a PowerShell post-exploitation toolset built on |
| [`prioritizing-vulnerabilities-with-cvss-scoring`](skills/prioritizing-vulnerabilities-with-cvss-scoring/SKILL.md) | The Common Vulnerability Scoring System (CVSS) is the industry standard |
| [`processing-stix-taxii-feeds`](skills/processing-stix-taxii-feeds/SKILL.md) | Processes STIX 2.1 threat intelligence bundles delivered via TAXII 2.1 |
| [`profiling-threat-actor-groups`](skills/profiling-threat-actor-groups/SKILL.md) | Develops comprehensive threat actor profiles for APT groups, criminal |
| [`recovering-from-ransomware-attack`](skills/recovering-from-ransomware-attack/SKILL.md) | Executes structured ransomware incident recovery following NIST/CISA |
| [`reverse-engineering-android-malware-with-jadx`](skills/reverse-engineering-android-malware-with-jadx/SKILL.md) | Reverse engineers malicious Android APK files using the JADX decompiler |
| [`reverse-engineering-dotnet-malware-with-dnspy`](skills/reverse-engineering-dotnet-malware-with-dnspy/SKILL.md) | Reverse engineers .NET malware samples using the dnSpy decompiler and |
| [`reverse-engineering-malware-with-ghidra`](skills/reverse-engineering-malware-with-ghidra/SKILL.md) | Reverse engineers malware binaries using NSA''s Ghidra disassembler and |
| [`reverse-engineering-ransomware-encryption-routine`](skills/reverse-engineering-ransomware-encryption-routine/SKILL.md) | Reverse engineer ransomware encryption routines to identify cryptographic |
| [`reverse-engineering-rust-malware`](skills/reverse-engineering-rust-malware/SKILL.md) | Reverse engineers Rust-compiled malware using IDA Pro and Ghidra, covering |
| [`scanning-infrastructure-with-nessus`](skills/scanning-infrastructure-with-nessus/SKILL.md) | Tenable Nessus is the industry-leading vulnerability scanner used to |
| [`security-bounty-hunter`](skills/security-bounty-hunter/SKILL.md) | Hunt for exploitable, bounty-worthy security issues in repositories. Focuses on remotely reachable vulnerabilities that qualify... |
| [`testing-api-for-mass-assignment-vulnerability`](skills/testing-api-for-mass-assignment-vulnerability/SKILL.md) | Tests APIs for mass assignment (auto-binding), OWASP API3:2023, by identifying |
| [`testing-cors-misconfiguration`](skills/testing-cors-misconfiguration/SKILL.md) | Identifying and exploiting Cross-Origin Resource Sharing misconfigurations |
| [`testing-for-open-redirect-vulnerabilities`](skills/testing-for-open-redirect-vulnerabilities/SKILL.md) | Identifies and exploits open redirect vulnerabilities by analyzing URL |
| [`testing-for-xxe-injection-vulnerabilities`](skills/testing-for-xxe-injection-vulnerabilities/SKILL.md) | Discovering and exploiting XML External Entity injection vulnerabilities |
| [`testing-ransomware-recovery-procedures`](skills/testing-ransomware-recovery-procedures/SKILL.md) | Tests and validates ransomware recovery procedures - backup restore operations |
| [`tracking-threat-actor-infrastructure`](skills/tracking-threat-actor-infrastructure/SKILL.md) | Discovers and maps adversary-controlled infrastructure (C2 servers, |

---

## ☁️ Cloud, Kubernetes, DevOps & Infrastructure (95 skills)

| Compétence | Description |
| :--- | :--- |
| [`attacking-entra-id-with-roadtools`](skills/attacking-entra-id-with-roadtools/SKILL.md) | Enumerate Microsoft Entra ID (Azure AD) tenants with ROADrecon and |
| [`auditing-aws-s3-bucket-permissions`](skills/auditing-aws-s3-bucket-permissions/SKILL.md) | Systematically audit AWS S3 bucket permissions to identify publicly |
| [`auditing-cloud-with-cis-benchmarks`](skills/auditing-cloud-with-cis-benchmarks/SKILL.md) | Audit AWS, Azure, and GCP environments against the CIS Foundations Benchmarks by running automated scans with tools like Prowle... |
| [`auditing-gcp-iam-permissions`](skills/auditing-gcp-iam-permissions/SKILL.md) | Auditing Google Cloud Platform IAM permissions to identify overly permissive |
| [`auditing-kubernetes-cluster-rbac`](skills/auditing-kubernetes-cluster-rbac/SKILL.md) | Auditing Kubernetes cluster RBAC configurations to identify overly permissive |
| [`auditing-kubernetes-rbac-privilege-escalation`](skills/auditing-kubernetes-rbac-privilege-escalation/SKILL.md) | >- |
| [`auditing-terraform-infrastructure-for-security`](skills/auditing-terraform-infrastructure-for-security/SKILL.md) | Auditing Terraform infrastructure-as-code for security misconfigurations |
| [`benchmarking-kubernetes-with-kube-bench`](skills/benchmarking-kubernetes-with-kube-bench/SKILL.md) | >- |
| [`building-identity-federation-with-saml-azure-ad`](skills/building-identity-federation-with-saml-azure-ad/SKILL.md) | Configure SAML 2.0 identity federation between on-premises Active Directory (via AD FS or a third-party IdP) and Microsoft Entr... |
| [`ci-cd-and-automation`](skills/ci-cd-and-automation/SKILL.md) | Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines. Use when you need to automate ... |
| [`conducting-cloud-penetration-testing`](skills/conducting-cloud-penetration-testing/SKILL.md) | This skill outlines methodologies for performing authorized penetration |
| [`conducting-internal-reconnaissance-with-bloodhound-ce`](skills/conducting-internal-reconnaissance-with-bloodhound-ce/SKILL.md) | Conduct internal Active Directory reconnaissance using BloodHound Community Edition's graph database with the SharpHound (AD) a... |
| [`configuring-aws-verified-access-for-ztna`](skills/configuring-aws-verified-access-for-ztna/SKILL.md) | Configure AWS Verified Access to provide VPN-less zero trust network |
| [`configuring-identity-aware-proxy-with-google-iap`](skills/configuring-identity-aware-proxy-with-google-iap/SKILL.md) | Configures Google Cloud Identity-Aware Proxy (IAP) via gcloud to enforce |
| [`deploying-cloud-deception-with-decoy-resources`](skills/deploying-cloud-deception-with-decoy-resources/SKILL.md) | >- |
| [`deploying-cloudflare-access-for-zero-trust`](skills/deploying-cloudflare-access-for-zero-trust/SKILL.md) | Deploys Cloudflare Access with Cloudflare Tunnel for zero trust access to self-hosted apps, configuring identity-aware policies... |
| [`deploying-honeytokens-and-canarytokens`](skills/deploying-honeytokens-and-canarytokens/SKILL.md) | Plants Canarytokens-based decoy artifacts (honey credentials, DNS tokens, web-bug URLs, AWS keys, documents, kubeconfigs) using... |
| [`deploying-palo-alto-prisma-access-zero-trust`](skills/deploying-palo-alto-prisma-access-zero-trust/SKILL.md) | Deploys Palo Alto Networks Prisma Access for SASE-based zero trust network access, configuring GlobalProtect agents, ZTNA Conne... |
| [`deployment-patterns`](skills/deployment-patterns/SKILL.md) | Deployment workflows, CI/CD pipeline patterns, Docker containerization, health checks, rollback strategies, and production read... |
| [`discovering-gcp-data-assets`](skills/discovering-gcp-data-assets/SKILL.md) | Guide de compétences et procédures d'agent. |
| [`docker-patterns`](skills/docker-patterns/SKILL.md) | Docker and Docker Compose patterns for local development, hardened CLI installer harnesses, container security, networking, vol... |
| [`enterprise-agent-ops`](skills/enterprise-agent-ops/SKILL.md) | Operational controls for long-lived or cloud-hosted agent systems — runtime lifecycle (start, pause, stop, restart), observabil... |
| [`enumerating-cloud-with-cloudfox`](skills/enumerating-cloud-with-cloudfox/SKILL.md) | Run CloudFox's read-only Describe/List/Get enumeration (all-checks, |
| [`gcp-data-pipelines`](skills/gcp-data-pipelines/SKILL.md) | Primary entry point for building, managing, and orchestrating data pipelines |
| [`gcp-dataflow`](skills/gcp-dataflow/SKILL.md) | Guide de compétences et procédures d'agent. |
| [`gcp-pipeline-orchestration`](skills/gcp-pipeline-orchestration/SKILL.md) | This skill helps the agent generate or update orchestration pipeline |
| [`gcp-pipeline-resource-provisioning`](skills/gcp-pipeline-resource-provisioning/SKILL.md) | Guide de compétences et procédures d'agent. |
| [`gcp-spark`](skills/gcp-spark/SKILL.md) | Guide de compétences et procédures d'agent. |
| [`gcp-spark-troubleshooting`](skills/gcp-spark-troubleshooting/SKILL.md) | Provides expert guidance for troubleshooting Google Cloud Spark and Dataproc |
| [`google-cloud-auth-verification`](skills/google-cloud-auth-verification/SKILL.md) | Mandatory Step 0 pre-flight execution order and authentication verification |
| [`hardening-docker-containers-for-production`](skills/hardening-docker-containers-for-production/SKILL.md) | >- |
| [`hardening-docker-daemon-configuration`](skills/hardening-docker-daemon-configuration/SKILL.md) | >- |
| [`implementing-api-gateway-security-controls`](skills/implementing-api-gateway-security-controls/SKILL.md) | Configures API gateways such as Kong, AWS API Gateway, Azure APIM, |
| [`implementing-aws-config-rules-for-compliance`](skills/implementing-aws-config-rules-for-compliance/SKILL.md) | Implements AWS Config managed and custom rules for continuous compliance |
| [`implementing-aws-iam-permission-boundaries`](skills/implementing-aws-iam-permission-boundaries/SKILL.md) | Configures AWS IAM permission boundaries that cap the maximum permissions |
| [`implementing-aws-macie-for-data-classification`](skills/implementing-aws-macie-for-data-classification/SKILL.md) | Enable and configure Amazon Macie via AWS CLI/Terraform to discover, classify, and protect sensitive data (PII, financial data,... |
| [`implementing-aws-nitro-enclave-security`](skills/implementing-aws-nitro-enclave-security/SKILL.md) | Build AWS Nitro Enclave confidential computing environments using nitro-cli |
| [`implementing-aws-security-hub`](skills/implementing-aws-security-hub/SKILL.md) | Deploy AWS Security Hub as a centralized CSPM platform, backed by AWS |
| [`implementing-aws-security-hub-compliance`](skills/implementing-aws-security-hub-compliance/SKILL.md) | Deploy AWS Security Hub, backed by AWS Config, to aggregate findings |
| [`implementing-azure-ad-privileged-identity-management`](skills/implementing-azure-ad-privileged-identity-management/SKILL.md) | Configure Microsoft Entra Privileged Identity Management (PIM) to convert |
| [`implementing-azure-defender-for-cloud`](skills/implementing-azure-defender-for-cloud/SKILL.md) | Enable Microsoft Defender for Cloud (CSPM + CWPP) across VMs, containers, |
| [`implementing-beyondcorp-zero-trust-access-model`](skills/implementing-beyondcorp-zero-trust-access-model/SKILL.md) | Implement Google''s BeyondCorp zero trust access model using Cloud |
| [`implementing-canary-tokens-for-network-intrusion`](skills/implementing-canary-tokens-for-network-intrusion/SKILL.md) | Deploys DNS, HTTP, and AWS API key canary tokens across network infrastructure |
| [`implementing-cloud-dlp-for-data-protection`](skills/implementing-cloud-dlp-for-data-protection/SKILL.md) | Implement cloud DLP using Amazon Macie, Google Cloud DLP API, Microsoft |
| [`implementing-cloud-security-posture-management`](skills/implementing-cloud-security-posture-management/SKILL.md) | Continuously monitor multi-cloud environments (AWS, Azure, GCP) for |
| [`implementing-cloud-waf-rules`](skills/implementing-cloud-waf-rules/SKILL.md) | Deploys and tunes Web Application Firewall rules on AWS WAF, Azure WAF, |
| [`implementing-cloud-workload-protection`](skills/implementing-cloud-workload-protection/SKILL.md) | Implements cloud workload protection using boto3 and google-cloud APIs |
| [`implementing-conditional-access-policies-azure-ad`](skills/implementing-conditional-access-policies-azure-ad/SKILL.md) | Configures Microsoft Entra ID (Azure AD) Conditional Access policies for |
| [`implementing-ddos-mitigation-with-cloudflare`](skills/implementing-ddos-mitigation-with-cloudflare/SKILL.md) | Configure Cloudflare DDoS protection with managed rulesets, rate limiting, |
| [`implementing-envelope-encryption-with-aws-kms`](skills/implementing-envelope-encryption-with-aws-kms/SKILL.md) | Implements envelope encryption with AWS KMS, encrypting data locally with a data encryption key (DEK) and protecting that DEK w... |
| [`implementing-gcp-binary-authorization`](skills/implementing-gcp-binary-authorization/SKILL.md) | Implements GCP Binary Authorization end to end, including creating KMS-backed attestors, Container Analysis notes, deploy-time ... |
| [`implementing-gcp-organization-policy-constraints`](skills/implementing-gcp-organization-policy-constraints/SKILL.md) | Implements GCP Organization Policy constraints via gcloud and Terraform, such as restricting external IPs, resource locations, ... |
| [`implementing-gcp-vpc-firewall-rules`](skills/implementing-gcp-vpc-firewall-rules/SKILL.md) | Implements and audits GCP VPC firewall rules using gcloud, covering auditing overly permissive rules, creating restrictive ingr... |
| [`implementing-honeytokens-for-breach-detection`](skills/implementing-honeytokens-for-breach-detection/SKILL.md) | Deploys canary tokens and honeytokens (fake AWS credentials, DNS canaries, |
| [`implementing-kubernetes-network-policy-with-calico`](skills/implementing-kubernetes-network-policy-with-calico/SKILL.md) | >- |
| [`implementing-kubernetes-pod-security-standards`](skills/implementing-kubernetes-pod-security-standards/SKILL.md) | >- |
| [`implementing-network-policies-for-kubernetes`](skills/implementing-network-policies-for-kubernetes/SKILL.md) | >- |
| [`implementing-privileged-access-workstation`](skills/implementing-privileged-access-workstation/SKILL.md) | Design and implement Privileged Access Workstations (PAWs) using the |
| [`implementing-rbac-hardening-for-kubernetes`](skills/implementing-rbac-hardening-for-kubernetes/SKILL.md) | >- |
| [`implementing-secrets-scanning-in-ci-cd`](skills/implementing-secrets-scanning-in-ci-cd/SKILL.md) | Integrate gitleaks and trufflehog into CI/CD pipelines to detect leaked |
| [`implementing-security-monitoring-with-datadog`](skills/implementing-security-monitoring-with-datadog/SKILL.md) | Implements security monitoring using Datadog Cloud SIEM, Cloud Security |
| [`implementing-taxii-server-with-opentaxii`](skills/implementing-taxii-server-with-opentaxii/SKILL.md) | Deploy and configure a TAXII 2.1 server (Medallion) with Docker, publish |
| [`implementing-zero-standing-privilege-with-cyberark`](skills/implementing-zero-standing-privilege-with-cyberark/SKILL.md) | Deploy CyberArk Secure Cloud Access (SCA) to eliminate standing privileges in AWS, Azure, and GCP by provisioning ephemeral, sc... |
| [`implementing-zero-trust-in-cloud`](skills/implementing-zero-trust-in-cloud/SKILL.md) | Guides zero trust implementation across AWS, Azure, and GCP per NIST SP 800-207 and BeyondCorp principles, covering identity-ce... |
| [`implementing-zero-trust-network-access`](skills/implementing-zero-trust-network-access/SKILL.md) | Configures Zero Trust Network Access (ZTNA) in AWS, Azure, and GCP using identity-aware proxies, micro-segmentation, and contin... |
| [`implementing-zero-trust-with-beyondcorp`](skills/implementing-zero-trust-with-beyondcorp/SKILL.md) | Configures Google BeyondCorp Enterprise Identity-Aware Proxy (IAP) as the access enforcement point for web applications, defini... |
| [`integrating-dast-with-owasp-zap-in-pipeline`](skills/integrating-dast-with-owasp-zap-in-pipeline/SKILL.md) | Integrates OWASP ZAP (Zed Attack Proxy) into GitHub Actions and GitLab CI pipelines, covering baseline, full, and API scan conf... |
| [`kubernetes-patterns`](skills/kubernetes-patterns/SKILL.md) | Kubernetes workload patterns, resource management, RBAC, probes, autoscaling, ConfigMap/Secret handling, and kubectl debugging ... |
| [`managing-cloud-identity-with-okta`](skills/managing-cloud-identity-with-okta/SKILL.md) | >- |
| [`mapping-attack-paths-with-bloodhound-ce`](skills/mapping-attack-paths-with-bloodhound-ce/SKILL.md) | Collect Active Directory data with SharpHound and Entra ID data with AzureHound, ingest into BloodHound Community Edition, and ... |
| [`performing-aws-account-enumeration-with-scout-suite`](skills/performing-aws-account-enumeration-with-scout-suite/SKILL.md) | Run the agentless, open-source ScoutSuite tool (via pip install and the `scout` CLI) |
| [`performing-aws-privilege-escalation-assessment`](skills/performing-aws-privilege-escalation-assessment/SKILL.md) | Performing authorized privilege escalation assessments in AWS environments |
| [`performing-cloud-asset-inventory-with-cartography`](skills/performing-cloud-asset-inventory-with-cartography/SKILL.md) | Run Cartography to sync AWS, GCP, or Azure resources into a Neo4j graph database, |
| [`performing-cloud-incident-containment-procedures`](skills/performing-cloud-incident-containment-procedures/SKILL.md) | Execute cloud-native incident containment across AWS, Azure, and GCP using platform |
| [`performing-docker-bench-security-assessment`](skills/performing-docker-bench-security-assessment/SKILL.md) | >- |
| [`performing-gcp-penetration-testing-with-gcpbucketbrute`](skills/performing-gcp-penetration-testing-with-gcpbucketbrute/SKILL.md) | Performs authorized GCP security testing using GCPBucketBrute to enumerate |
| [`performing-gcp-security-assessment-with-forseti`](skills/performing-gcp-security-assessment-with-forseti/SKILL.md) | Performing comprehensive security assessments of Google Cloud Platform |
| [`performing-kubernetes-cis-benchmark-with-kube-bench`](skills/performing-kubernetes-cis-benchmark-with-kube-bench/SKILL.md) | >- |
| [`performing-kubernetes-etcd-security-assessment`](skills/performing-kubernetes-etcd-security-assessment/SKILL.md) | >- |
| [`performing-kubernetes-penetration-testing`](skills/performing-kubernetes-penetration-testing/SKILL.md) | >- |
| [`performing-serverless-function-security-review`](skills/performing-serverless-function-security-review/SKILL.md) | Performing security reviews of serverless functions across AWS Lambda, |
| [`scanning-docker-images-with-trivy`](skills/scanning-docker-images-with-trivy/SKILL.md) | >- |
| [`scanning-iac-and-images-with-trivy`](skills/scanning-iac-and-images-with-trivy/SKILL.md) | Scans container images, Infrastructure-as-Code (Terraform, CloudFormation, |
| [`scanning-kubernetes-manifests-with-kubesec`](skills/scanning-kubernetes-manifests-with-kubesec/SKILL.md) | >- |
| [`securing-api-gateway-with-aws-waf`](skills/securing-api-gateway-with-aws-waf/SKILL.md) | Secures AWS API Gateway endpoints with AWS WAF by configuring managed |
| [`securing-aws-iam-permissions`](skills/securing-aws-iam-permissions/SKILL.md) | Hardens AWS IAM configurations to enforce least-privilege access, covering |
| [`securing-aws-lambda-execution-roles`](skills/securing-aws-lambda-execution-roles/SKILL.md) | Hardens AWS Lambda execution roles by writing least-privilege IAM policies, |
| [`securing-azure-with-microsoft-defender`](skills/securing-azure-with-microsoft-defender/SKILL.md) | Deploys and configures Microsoft Defender for Cloud as a CNAPP for |
| [`securing-container-registry-images`](skills/securing-container-registry-images/SKILL.md) | Secures container registry images (ECR, ACR, GCR, Docker Hub) by scanning |
| [`securing-kubernetes-on-cloud`](skills/securing-kubernetes-on-cloud/SKILL.md) | Hardens managed Kubernetes clusters on EKS, AKS, and GKE by implementing |
| [`securing-serverless-functions`](skills/securing-serverless-functions/SKILL.md) | Hardens serverless compute platforms (AWS Lambda, Azure Functions, Google |
| [`taste`](skills/taste/SKILL.md) | Creative-direction layer for music videos and short-form edits in the angelcore / cloud-trance / hyperpop family — a named-genr... |
| [`testing-for-business-logic-vulnerabilities`](skills/testing-for-business-logic-vulnerabilities/SKILL.md) | Manually identifies flaws in application business logic - price manipulation, |
| [`testing-oauth2-implementation-flaws`](skills/testing-oauth2-implementation-flaws/SKILL.md) | Tests OAuth 2.0 and OpenID Connect implementations for authorization code |
| [`uncloud`](skills/uncloud/SKILL.md) | Use when managing an Uncloud cluster — deploying services, configuring Caddy ingress, adding static proxy routes for non-cluste... |

---

## 📊 Data Engineering, Big Data & Analytics (49 skills)

| Compétence | Description |
| :--- | :--- |
| [`accidental-data-loss-prevention`](skills/accidental-data-loss-prevention/SKILL.md) | Guide de compétences et procédures d'agent. |
| [`agentic-os`](skills/agentic-os/SKILL.md) | Build persistent multi-agent operating systems on Claude Code. Covers kernel architecture, specialist agents, slash commands, f... |
| [`ai-regression-testing`](skills/ai-regression-testing/SKILL.md) | Regression testing strategies for AI-assisted development. Sandbox-mode API testing without database dependencies, automated bu... |
| [`architecture-decision-records`](skills/architecture-decision-records/SKILL.md) | Capture architectural decisions as numbered ADR markdown files in docs/adr/ with context, alternatives considered, consequences... |
| [`backend-patterns`](skills/backend-patterns/SKILL.md) | Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next... |
| [`bigquery-data-transfer-service`](skills/bigquery-data-transfer-service/SKILL.md) | Discovers and inspects BigQuery Data Transfer Service (DTS) configurations. |
| [`bigquery-sql`](skills/bigquery-sql/SKILL.md) | Provides BigQuery SQL query optimization techniques, execution best practices, |
| [`building-data-apps`](skills/building-data-apps/SKILL.md) | Guide de compétences et procédures d'agent. |
| [`clickhouse-io`](skills/clickhouse-io/SKILL.md) | ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytica... |
| [`conducting-external-reconnaissance-with-osint`](skills/conducting-external-reconnaissance-with-osint/SKILL.md) | Conduct external recon using OSINT techniques to map an organization's external attack surface without touching target systems,... |
| [`constraint-driven-development`](skills/constraint-driven-development/SKILL.md) | Establishes a project's quality bar as a written contract and stops agents quietly lowering it. Interviews the user on which di... |
| [`contract-first`](skills/contract-first/SKILL.md) | Coordinate frontend/backend or service-to-service work through one authoritative machine-checkable contract (OpenAPI, AsyncAPI,... |
| [`data-autocleaning`](skills/data-autocleaning/SKILL.md) | Automated data quality and transformation capabilities for Dataform/dbt/BigQuery |
| [`data-scraper-agent`](skills/data-scraper-agent/SKILL.md) | Build a fully automated AI-powered data collection agent for any public source — job boards, prices, news, GitHub, sports, anyt... |
| [`data-throughput-accelerator`](skills/data-throughput-accelerator/SKILL.md) | Diagnose and accelerate large data movement — ingestion, backfill, export, ETL, warehouse loading, manifest catch-up, and table... |
| [`database-migrations`](skills/database-migrations/SKILL.md) | Safe, reversible database migration patterns: forward-only production changes, expand-contract zero-downtime renames, concurren... |
| [`dataform-bigquery`](skills/dataform-bigquery/SKILL.md) | Expertise in generating clean, correct, and efficient Dataform pipeline |
| [`dbt-bigquery`](skills/dbt-bigquery/SKILL.md) | Expert guidance for creating, modifying, and optimizing dbt pipelines |
| [`deprecation-and-migration`](skills/deprecation-and-migration/SKILL.md) | Manages deprecation and migration. Use when removing old systems, APIs, or features. Use when migrating users from one implemen... |
| [`django-security`](skills/django-security/SKILL.md) | Django security best practices, authentication, authorization, CSRF protection, SQL injection prevention, XSS prevention, and s... |
| [`fastapi-patterns`](skills/fastapi-patterns/SKILL.md) | FastAPI best practices covering project structure, Pydantic v2 schemas, dependency injection, async handlers, authentication, a... |
| [`flox-environments`](skills/flox-environments/SKILL.md) | Create reproducible, cross-platform (macOS/Linux) development environments with Flox, a declarative Nix-based environment manag... |
| [`gateguard`](skills/gateguard/SKILL.md) | PreToolUse fact-forcing gate that denies the first Edit/Write/Bash (including MultiEdit and NotebookEdit) attempt until the age... |
| [`gmao-cmms-patterns`](skills/gmao-cmms-patterns/SKILL.md) | Architecture patterns, database schemas, REST API design, and OT/IT convergence workflows for Computerized Maintenance Manageme... |
| [`healthcare-phi-compliance`](skills/healthcare-phi-compliance/SKILL.md) | Protected Health Information (PHI) and PII compliance patterns for healthcare applications: data classification, row-level acce... |
| [`implementing-aes-encryption-for-data-at-rest`](skills/implementing-aes-encryption-for-data-at-rest/SKILL.md) | Guides implementing AES-256 encryption in GCM mode (FIPS 197) for files and data stores at rest, covering key derivation, IV/no... |
| [`implementing-api-schema-validation-security`](skills/implementing-api-schema-validation-security/SKILL.md) | Implements API schema validation using OpenAPI Specification and JSON |
| [`implementing-data-loss-prevention-with-microsoft-purview`](skills/implementing-data-loss-prevention-with-microsoft-purview/SKILL.md) | Implements DLP policies using Microsoft Purview PowerShell cmdlets and |
| [`implementing-file-integrity-monitoring-with-aide`](skills/implementing-file-integrity-monitoring-with-aide/SKILL.md) | Configures AIDE (Advanced Intrusion Detection Environment) for file integrity monitoring on Linux, covering baseline database c... |
| [`implementing-gdpr-data-protection-controls`](skills/implementing-gdpr-data-protection-controls/SKILL.md) | Implements GDPR (EU 2016/679) technical and organizational measures — privacy by design/default, DPIAs, data subject rights man... |
| [`implementing-gdpr-data-subject-access-request`](skills/implementing-gdpr-data-subject-access-request/SKILL.md) | Automates GDPR Data Subject Access Request (DSAR) workflows including |
| [`implementing-hashicorp-vault-dynamic-secrets`](skills/implementing-hashicorp-vault-dynamic-secrets/SKILL.md) | Configures HashiCorp Vault dynamic secrets engines for database credentials, |
| [`implementing-pam-for-database-access`](skills/implementing-pam-for-database-access/SKILL.md) | Deploy privileged access management for database systems including Oracle, |
| [`mybatis-patterns`](skills/mybatis-patterns/SKILL.md) | MyBatis and MyBatis-Spring patterns for mapper design, XML and annotation SQL, result mapping, dynamic SQL safety, transactions... |
| [`mysql-patterns`](skills/mysql-patterns/SKILL.md) | MySQL and MariaDB schema, query, indexing, transaction, replication, and connection-pool patterns for production backends. Use ... |
| [`performance-optimization`](skills/performance-optimization/SKILL.md) | Optimizes application performance across frontend, backend, queries, and databases. Use when performance requirements exist, wh... |
| [`performing-graphql-introspection-attack`](skills/performing-graphql-introspection-attack/SKILL.md) | Performs GraphQL introspection attacks that extract the full API schema |
| [`perl-security`](skills/perl-security/SKILL.md) | Comprehensive Perl security covering taint mode, input validation, safe process execution, DBI parameterized queries, web secur... |
| [`postgres-patterns`](skills/postgres-patterns/SKILL.md) | PostgreSQL database patterns for query optimization, schema design, indexing, and security. Based on Supabase best practices. U... |
| [`prediction-market-risk-review`](skills/prediction-market-risk-review/SKILL.md) | Review prediction-market, basket, oracle, and trading-agent workflows for compliance, safety, data-quality, privacy, and execut... |
| [`prisma-patterns`](skills/prisma-patterns/SKILL.md) | Prisma ORM patterns for TypeScript backends — schema design, query optimization, transactions, pagination, and critical traps l... |
| [`schema-mapping`](skills/schema-mapping/SKILL.md) | Guides the process of analyzing, mapping, and documenting transformations |
| [`scientific-db-pubmed-database`](skills/scientific-db-pubmed-database/SKILL.md) | Direct PubMed and NCBI E-utilities search workflows for biomedical literature, MeSH queries, PMID lookup, citation retrieval, a... |
| [`scientific-db-uspto-database`](skills/scientific-db-uspto-database/SKILL.md) | USPTO patent and trademark data workflow for official record lookup, PatentSearch queries, TSDR checks, assignment data, and re... |
| [`scientific-pkg-gget`](skills/scientific-pkg-gget/SKILL.md) | gget CLI and Python workflow for quick genomic database queries, sequence lookup, BLAST-style searches, enrichment checks, and ... |
| [`seo`](skills/seo/SKILL.md) | Audit, plan, and implement SEO improvements across technical SEO, on-page optimization, structured data, Core Web Vitals, and c... |
| [`testing-for-sensitive-data-exposure`](skills/testing-for-sensitive-data-exposure/SKILL.md) | Identifying sensitive data exposure vulnerabilities including API key |
| [`tinystruct-patterns`](skills/tinystruct-patterns/SKILL.md) | Expert guidance for developing with the tinystruct Java framework. Use when working on the tinystruct codebase or any project b... |
| [`xlsx`](skills/xlsx/SKILL.md) | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, r... |

---

## 🤖 Intelligence Artificielle, Agents & Machine Learning (243 skills)

| Compétence | Description |
| :--- | :--- |
| [`abusing-dpapi-for-credential-access`](skills/abusing-dpapi-for-credential-access/SKILL.md) | Extract and decrypt Windows DPAPI-protected secrets (Credential Manager, browser logins/cookies, Wi-Fi credentials, KeePass key... |
| [`accessibility`](skills/accessibility/SKILL.md) | Design, implement, and audit accessible UI to WCAG 2.2 Level AA across Web, iOS, and Android — semantic ARIA roles and labels, ... |
| [`agent-architecture-audit`](skills/agent-architecture-audit/SKILL.md) | Full-stack diagnostic for agent and LLM applications. Audits the 12-layer agent stack for wrapper regression, memory pollution,... |
| [`agent-eval`](skills/agent-eval/SKILL.md) | Head-to-head comparison of coding agents (Claude Code, Aider, Codex, etc.) on custom tasks with pass rate, cost, time, and cons... |
| [`agent-harness-construction`](skills/agent-harness-construction/SKILL.md) | Design and optimize AI agent action spaces, tool definitions, and observation formatting for higher completion rates. Use when ... |
| [`agent-introspection-debugging`](skills/agent-introspection-debugging/SKILL.md) | Structured self-debugging workflow for AI agent failures using capture, diagnosis, contained recovery, and introspection report... |
| [`agent-payment-x402`](skills/agent-payment-x402/SKILL.md) | Add x402 payment execution to AI agents with per-task budgets, spending controls, and non-custodial wallets. Supports Base thro... |
| [`agent-runtime-gateway-smoke-test`](skills/agent-runtime-gateway-smoke-test/SKILL.md) | Verify a local agent API, temporary gateway tunnel, and remote sandbox callback with a tool-free task, then restore the origina... |
| [`agent-security-hardening`](skills/agent-security-hardening/SKILL.md) | Security hardening guidance for AI agent frameworks that process untrusted content, invoke tools, write workspace files, manage... |
| [`agent-self-evaluation`](skills/agent-self-evaluation/SKILL.md) | Use after completing any non-trivial task. The agent self-rates its output on 5 axes — accuracy, completeness, clarity, actiona... |
| [`agent-sort`](skills/agent-sort/SKILL.md) | Build an evidence-backed ECC install plan for a specific repo by sorting skills, commands, rules, hooks, and extras into DAILY ... |
| [`agentic-engineering`](skills/agentic-engineering/SKILL.md) | Operate as an agentic engineer using eval-first execution, decomposition, and cost-aware model routing. Use when planning or ex... |
| [`ai-first-engineering`](skills/ai-first-engineering/SKILL.md) | Engineering operating model for teams where AI agents generate a large share of implementation output. Use when setting team pr... |
| [`angular-developer`](skills/angular-developer/SKILL.md) | Generates Angular code and provides architectural guidance. Trigger when creating projects, components, or services, or for bes... |
| [`auditing-entra-id-with-aadinternals`](skills/auditing-entra-id-with-aadinternals/SKILL.md) | Drive the AADInternals PowerShell toolkit to perform Microsoft Entra ID tenant reconnaissance, access-token acquisition across ... |
| [`auditing-mcp-servers-for-tool-poisoning`](skills/auditing-mcp-servers-for-tool-poisoning/SKILL.md) | Audit MCP servers for tool poisoning, tool shadowing, rug pulls, SSRF, and unauthenticated exposure using Invariant Labs' mcp-s... |
| [`autonomous-agent-harness`](skills/autonomous-agent-harness/SKILL.md) | Transform Claude Code into a fully autonomous agent system with persistent memory, scheduled operations, computer use, and task... |
| [`autonomous-loops`](skills/autonomous-loops/SKILL.md) | Patterns and architectures for autonomous Claude Code loops — from simple sequential pipelines to RFC-driven multi-agent DAG sy... |
| [`benchmark-optimization-loop`](skills/benchmark-optimization-loop/SKILL.md) | Convert 'make it faster' requests into a bounded measured optimization loop — baseline first, generate one-hypothesis variants,... |
| [`bengali-nlp`](skills/bengali-nlp/SKILL.md) | Bengali (Bangla) text processing patterns including Unicode normalization, script detection, tokenization, conjunct handling, a... |
| [`blender-motion-state-inspection`](skills/blender-motion-state-inspection/SKILL.md) | Use this skill when inspecting Blender characters, rigs, poses, animation retargeting, ground contact, facing direction, or mod... |
| [`blueprint`](skills/blueprint/SKILL.md) | Turn a one-line objective into a step-by-step construction plan for multi-session, multi-agent engineering projects: one-PR-siz... |
| [`brand-voice`](skills/brand-voice/SKILL.md) | Build a source-derived writing style profile from real posts, essays, launch notes, docs, or site copy, then reuse that profile... |
| [`brownfield-retrospective`](skills/brownfield-retrospective/SKILL.md) | Run the ECC engineering process retroactively against an existing project slice. Audit current state, reconstruct past decision... |
| [`building-identity-governance-lifecycle-process`](skills/building-identity-governance-lifecycle-process/SKILL.md) | Design identity governance and lifecycle (IGA) programs on platforms like SailPoint, Saviynt, or Entra ID Governance, covering ... |
| [`building-ioc-defanging-and-sharing-pipeline`](skills/building-ioc-defanging-and-sharing-pipeline/SKILL.md) | Build an automated pipeline that ingests raw IOCs (URLs, IPs, domains, |
| [`carrier-relationship-management`](skills/carrier-relationship-management/SKILL.md) | Manage truckload, LTL, and intermodal carrier portfolios: sourcing and FMCSA vetting, freight rate and fuel-surcharge negotiati... |
| [`ck`](skills/ck/SKILL.md) | Persistent per-project memory for Claude Code (Context Keeper) driven by deterministic Node.js /ck commands: init, save, resume... |
| [`claude-devfleet`](skills/claude-devfleet/SKILL.md) | Orchestrate multi-agent coding tasks via Claude DevFleet — plan projects, dispatch parallel agents in isolated worktrees, monit... |
| [`code-review-and-quality`](skills/code-review-and-quality/SKILL.md) | Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or ... |
| [`code-simplification`](skills/code-simplification/SKILL.md) | Simplifies code for clarity. Use when refactoring code for clarity without changing behavior. Use when code works but is harder... |
| [`code-tour`](skills/code-tour/SKILL.md) | Create CodeTour `.tour` files — persona-targeted, step-by-step walkthroughs with real file and line anchors. Use for onboarding... |
| [`codehealth-mcp`](skills/codehealth-mcp/SKILL.md) | Real-time structural Code Health via CodeScene MCP — review before edits, verify score deltas after changes, gate commits and P... |
| [`coding-standards`](skills/coding-standards/SKILL.md) | Baseline cross-project coding conventions for naming, readability, immutability, and code-quality review. Use detailed frontend... |
| [`coercing-authentication-with-coercer-petitpotam`](skills/coercing-authentication-with-coercer-petitpotam/SKILL.md) | Trigger machine account authentication with PetitPotam (MS-EFSR) and Coercer (MS-RPRN, MS-DFSNM, MS-FSRVP, MS-EVEN) via Coercer... |
| [`conducting-domain-persistence-with-dcsync`](skills/conducting-domain-persistence-with-dcsync/SKILL.md) | Perform DCSync attacks by abusing MS-DRSR replication rights (DS-Replication-Get-Changes/-All) to impersonate a Domain Controll... |
| [`conducting-network-penetration-test`](skills/conducting-network-penetration-test/SKILL.md) | Conducts comprehensive network penetration tests against authorized |
| [`configure-ecc`](skills/configure-ecc/SKILL.md) | Run the conversational ECC setup wizard inside the current harness: inventory the install, collect scope (user/project/local) a... |
| [`configuring-ldap-security-hardening`](skills/configuring-ldap-security-hardening/SKILL.md) | Hardens LDAP directory services against credential harvesting, LDAP |
| [`containing-active-breach`](skills/containing-active-breach/SKILL.md) | Executes containment strategies to stop active adversary operations |
| [`content-engine`](skills/content-engine/SKILL.md) | Create platform-native content systems for X, LinkedIn, TikTok, YouTube, newsletters, and repurposed multi-platform campaigns. ... |
| [`context-budget`](skills/context-budget/SKILL.md) | Routes live context checks to the native Codex or Claude Code meter without scanning files, and performs a bounded static compo... |
| [`context-engineering`](skills/context-engineering/SKILL.md) | Optimizes agent context setup. Use when starting a new session, when agent output quality degrades, when switching between task... |
| [`continuous-agent-loop`](skills/continuous-agent-loop/SKILL.md) | Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls. Use when running an agent loop... |
| [`continuous-learning-v2`](skills/continuous-learning-v2/SKILL.md) | Instinct-based learning system that observes sessions via hooks, creates atomic instincts with confidence scoring, and evolves ... |
| [`cost-aware-llm-pipeline`](skills/cost-aware-llm-pipeline/SKILL.md) | Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic, and prompt cachi... |
| [`cost-tracking`](skills/cost-tracking/SKILL.md) | Track and report Claude Code token usage, spending, and budgets from the local ECC cost-tracker metrics log. Use when the user ... |
| [`council-multi-model`](skills/council-multi-model/SKILL.md) | Add one optional external Codex critique after the existing council has produced a decision draft. Use when an ambiguous, high-... |
| [`counterparty-channel-discipline`](skills/counterparty-channel-discipline/SKILL.md) | Per-channel strict prompts, mention gating, silent observation, and a communication autonomy policy for agents that sit in shar... |
| [`cpp-testing`](skills/cpp-testing/SKILL.md) | Use only when writing/updating/fixing C++ tests, configuring GoogleTest/CTest, diagnosing failing or flaky tests, or adding cov... |
| [`debugging-and-error-recovery`](skills/debugging-and-error-recovery/SKILL.md) | Guides systematic root-cause debugging. Use when tests fail, builds break, something that worked yesterday broke, behavior does... |
| [`deep-research`](skills/deep-research/SKILL.md) | Produce cited research reports from multiple web sources using firecrawl and exa MCP tools — plan sub-questions, search and dee... |
| [`deepseek-harness-setup`](skills/deepseek-harness-setup/SKILL.md) | Install and operate Everything Claude Code (ECC) on the DeepSeek Harness (DSH): native skill roots (~/.dsh/skills, .agents/skil... |
| [`defending-llms-with-guardrails`](skills/defending-llms-with-guardrails/SKILL.md) | Deploys Llama Guard 3 safety classification, NeMo Guardrails programmable dialogue rails, and LLM Guard input/output scanner pi... |
| [`deploying-edr-agent-with-crowdstrike`](skills/deploying-edr-agent-with-crowdstrike/SKILL.md) | Deploys and configures CrowdStrike Falcon EDR agents across enterprise |
| [`deploying-tailscale-for-zero-trust-vpn`](skills/deploying-tailscale-for-zero-trust-vpn/SKILL.md) | Deploys and configures Tailscale (or self-hosted Headscale) as a WireGuard-based zero trust mesh VPN, setting up identity-aware... |
| [`design-system`](skills/design-system/SKILL.md) | Generate a design system from an existing codebase or audit one for visual consistency: extract tokens (colors, typography, spa... |
| [`dev-team`](skills/dev-team/SKILL.md) | Simulate a collaborative dev team session where multiple role-based personas (PM, Architect, Developer, QA) respond to the same... |
| [`django-verification`](skills/django-verification/SKILL.md) | Run the full Django verification loop — environment check, mypy/ruff/black linting, migration safety, pytest with coverage targ... |
| [`dmux-workflows`](skills/dmux-workflows/SKILL.md) | Multi-agent orchestration using dmux (tmux pane manager for AI agents). Patterns for parallel agent workflows across Claude Cod... |
| [`documentation-and-adrs`](skills/documentation-and-adrs/SKILL.md) | Records decisions and documentation. Use when you need to document an architecture decision (ADR) or the reasoning behind a des... |
| [`documentation-lookup`](skills/documentation-lookup/SKILL.md) | Use up-to-date library and framework docs via Context7 MCP instead of training data. Activates for setup questions, API referen... |
| [`dotnet-patterns`](skills/dotnet-patterns/SKILL.md) | Idiomatic C# and .NET patterns, conventions, dependency injection, async/await, and best practices for building robust, maintai... |
| [`doubt-driven-development`](skills/doubt-driven-development/SKILL.md) | Subjects every non-trivial decision to a fresh-context adversarial review before it stands. Use when you want every assumption ... |
| [`dynamic-workflow-mode`](skills/dynamic-workflow-mode/SKILL.md) | Design task-local harnesses, eval gates, and reusable skill extraction for Claude dynamic workflow mode and other adaptive agen... |
| [`e2e-testing`](skills/e2e-testing/SKILL.md) | Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and flaky test strat... |
| [`ecc-guide`](skills/ecc-guide/SKILL.md) | Answer questions about ECC by reading the live repo surface — agents, skills, commands, hooks, rules, install profiles, and doc... |
| [`ecc-recipes`](skills/ecc-recipes/SKILL.md) | Map a described workflow to the right ECC command group with run-order and stop condition, or browse all command-group recipe f... |
| [`ecc-tools-cost-audit`](skills/ecc-tools-cost-audit/SKILL.md) | Evidence-first ECC Tools burn and billing audit workflow. Use when investigating runaway PR creation, quota bypass, premium-mod... |
| [`email-ops`](skills/email-ops/SKILL.md) | Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow for ECC. Use when the user wa... |
| [`energy-procurement`](skills/energy-procurement/SKILL.md) | Procure electricity and natural gas for commercial and industrial facilities: tariff and rate-schedule optimization, demand-cha... |
| [`error-handling`](skills/error-handling/SKILL.md) | Patterns for robust error handling across TypeScript, Python, and Go. Covers typed errors, error boundaries, retries, circuit b... |
| [`escaping-containers-to-host`](skills/escaping-containers-to-host/SKILL.md) | >- |
| [`eval-harness`](skills/eval-harness/SKILL.md) | Eval-driven development (EDD) framework for AI coding sessions — define capability and regression evals before coding, grade wi... |
| [`evm-token-decimals`](skills/evm-token-decimals/SKILL.md) | Prevent silent decimal mismatch bugs across EVM chains. Covers runtime decimal lookup, chain-aware caching, bridged-token preci... |
| [`exa-search`](skills/exa-search/SKILL.md) | Neural search via Exa MCP for web, code, and company research. Use when the user needs web search, code examples, company intel... |
| [`extracting-config-from-agent-tesla-rat`](skills/extracting-config-from-agent-tesla-rat/SKILL.md) | Extracts embedded configuration from Agent Tesla RAT samples, including |
| [`extracting-windows-event-logs-artifacts`](skills/extracting-windows-event-logs-artifacts/SKILL.md) | Extract, parse, and analyze Windows Event Logs (EVTX) using Chainsaw, |
| [`fal-ai-media`](skills/fal-ai-media/SKILL.md) | Unified media generation via fal.ai MCP — image, video, and audio. Covers text-to-image (Nano Banana), text/image-to-video (See... |
| [`finance-billing-ops`](skills/finance-billing-ops/SKILL.md) | Evidence-first revenue, pricing, refunds, team-billing, and billing-model truth workflow for ECC. Use when the user wants a sal... |
| [`foundation-models-on-device`](skills/foundation-models-on-device/SKILL.md) | Apple FoundationModels framework for on-device LLM — text generation, guided generation with @Generable, tool calling, and snap... |
| [`frontend-a11y`](skills/frontend-a11y/SKILL.md) | Accessibility patterns for React and Next.js — semantic HTML, ARIA attributes, form labeling, keyboard navigation, focus manage... |
| [`frontend-slides`](skills/frontend-slides/SKILL.md) | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. Use when the user wants to b... |
| [`frontend-ui-engineering`](skills/frontend-ui-engineering/SKILL.md) | Builds production-quality, accessible, responsive user-facing UIs. Use when building or modifying interfaces and pages, creatin... |
| [`gan-style-harness`](skills/gan-style-harness/SKILL.md) | GAN-inspired Generator-Evaluator agent harness for building high-quality applications autonomously. Based on Anthropic's March ... |
| [`golang-patterns`](skills/golang-patterns/SKILL.md) | Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and maintainable Go applications. Use wh... |
| [`growth-log`](skills/growth-log/SKILL.md) | Write growth log entries that extract reusable patterns from completed work — root cause, transferable rule, and a recognizable... |
| [`healthcare-eval-harness`](skills/healthcare-eval-harness/SKILL.md) | Patient safety evaluation harness for healthcare application deployments. Automated test suites for CDSS accuracy, PHI exposure... |
| [`hexagonal-architecture`](skills/hexagonal-architecture/SKILL.md) | Design, implement, and refactor Ports & Adapters systems with clear domain boundaries, dependency inversion, and testable use-c... |
| [`hookify-rules`](skills/hookify-rules/SKILL.md) | Create and configure hookify rules — markdown files with YAML frontmatter that match bash, file, prompt, or stop events by rege... |
| [`implementing-aqua-security-for-container-scanning`](skills/implementing-aqua-security-for-container-scanning/SKILL.md) | Deploy Aqua Security's Trivy scanner to detect vulnerabilities, misconfigurations, |
| [`implementing-cisa-zero-trust-maturity-model`](skills/implementing-cisa-zero-trust-maturity-model/SKILL.md) | Assess, gap-analyze, and progressively implement the CISA Zero Trust |
| [`implementing-code-signing-for-artifacts`](skills/implementing-code-signing-for-artifacts/SKILL.md) | Implements code signing for build artifacts (binaries, packages, containers) |
| [`implementing-container-image-minimal-base-with-distroless`](skills/implementing-container-image-minimal-base-with-distroless/SKILL.md) | >- |
| [`implementing-container-network-policies-with-calico`](skills/implementing-container-network-policies-with-calico/SKILL.md) | >- |
| [`implementing-diamond-model-analysis`](skills/implementing-diamond-model-analysis/SKILL.md) | The Diamond Model of Intrusion Analysis provides a structured framework |
| [`implementing-digital-signatures-with-ed25519`](skills/implementing-digital-signatures-with-ed25519/SKILL.md) | Implements digital signatures using the Ed25519 algorithm (Curve25519), covering key-pair generation, signing, signature verifi... |
| [`implementing-email-sandboxing-with-proofpoint`](skills/implementing-email-sandboxing-with-proofpoint/SKILL.md) | Email sandboxing detonates suspicious attachments and URLs in isolated |
| [`implementing-end-to-end-encryption-for-messaging`](skills/implementing-end-to-end-encryption-for-messaging/SKILL.md) | Implements a simplified Signal Protocol-style end-to-end encryption scheme for messaging, covering key exchange, forward secrec... |
| [`implementing-endpoint-detection-with-wazuh`](skills/implementing-endpoint-detection-with-wazuh/SKILL.md) | Deploys and configures Wazuh SIEM/XDR for endpoint detection, covering agent authentication and management, custom decoder and ... |
| [`implementing-google-workspace-sso-configuration`](skills/implementing-google-workspace-sso-configuration/SKILL.md) | Configures SAML 2.0 single sign-on for Google Workspace against a third-party |
| [`implementing-identity-governance-with-sailpoint`](skills/implementing-identity-governance-with-sailpoint/SKILL.md) | Deploys SailPoint IdentityNow or IdentityIQ for identity governance and |
| [`implementing-llm-guardrails-for-security`](skills/implementing-llm-guardrails-for-security/SKILL.md) | Implements input/output validation guardrails for LLM applications using |
| [`implementing-log-integrity-with-blockchain`](skills/implementing-log-integrity-with-blockchain/SKILL.md) | >- |
| [`implementing-microsegmentation-with-guardicore`](skills/implementing-microsegmentation-with-guardicore/SKILL.md) | Implements microsegmentation with Akamai Guardicore Segmentation to map |
| [`implementing-policy-as-code-with-open-policy-agent`](skills/implementing-policy-as-code-with-open-policy-agent/SKILL.md) | Implements policy-as-code enforcement with Open Policy Agent (OPA) |
| [`implementing-proofpoint-email-security-gateway`](skills/implementing-proofpoint-email-security-gateway/SKILL.md) | Deploy and configure Proofpoint Email Protection as a secure email gateway |
| [`implementing-purdue-model-network-segmentation`](skills/implementing-purdue-model-network-segmentation/SKILL.md) | Implement network segmentation based on the Purdue Enterprise Reference |
| [`implementing-rsa-key-pair-management`](skills/implementing-rsa-key-pair-management/SKILL.md) | Generates, stores, rotates, and manages RSA key pairs following NIST |
| [`implementing-runtime-application-self-protection`](skills/implementing-runtime-application-self-protection/SKILL.md) | Deploy Runtime Application Self-Protection (RASP) agents to detect and |
| [`implementing-saml-sso-with-okta`](skills/implementing-saml-sso-with-okta/SKILL.md) | Implement SAML 2.0 Single Sign-On using Okta as the Identity Provider, |
| [`implementing-semgrep-for-custom-sast-rules`](skills/implementing-semgrep-for-custom-sast-rules/SKILL.md) | Write custom Semgrep SAST rules in YAML to detect application-specific |
| [`implementing-supply-chain-security-with-in-toto`](skills/implementing-supply-chain-security-with-in-toto/SKILL.md) | >- |
| [`inherit-legacy-style`](skills/inherit-legacy-style/SKILL.md) | Prevent AI style drift on legacy projects by scanning the codebase for implicit conventions, resolving conflicts with the opera... |
| [`intent-driven-development`](skills/intent-driven-development/SKILL.md) | Turn ambiguous or high-impact product and engineering changes into scoped, verifiable acceptance criteria before or alongside i... |
| [`inventory-demand-planning`](skills/inventory-demand-planning/SKILL.md) | Codified demand planning expertise for multi-location retailers: demand forecasting method selection, ABC/XYZ segmentation, saf... |
| [`investor-materials`](skills/investor-materials/SKILL.md) | Create and update pitch decks, one-pagers, investor memos, accelerator applications, financial models, and fundraising material... |
| [`investor-outreach`](skills/investor-outreach/SKILL.md) | Draft cold emails, warm intro blurbs, follow-ups, update emails, and investor communications for fundraising. Use when the user... |
| [`iterative-retrieval`](skills/iterative-retrieval/SKILL.md) | Pattern for progressively refining context retrieval to solve the subagent context problem. Use when a subagent lacks the conte... |
| [`ito-baskets`](skills/ito-baskets/SKILL.md) | Read-only Itô basket and prediction-market data skill. Index the live basket catalog, compare a basket against user-supplied re... |
| [`ito-compute`](skills/ito-compute/SKILL.md) | Query live GPU inventory, submit an authenticated Itô fixed-rate RFQ, inspect RFQ or procurement status, revoke device credenti... |
| [`ito-inference`](skills/ito-inference/SKILL.md) | Inspect the availability of model serving on a completed Itô compute booking and, when the canonical backend becomes available,... |
| [`ito-training`](skills/ito-training/SKILL.md) | Inspect the availability of ML training on a completed Itô compute booking and, when the canonical backend becomes available, h... |
| [`knowledge-ops`](skills/knowledge-ops/SKILL.md) | Knowledge base management, ingestion, sync, and retrieval across multiple storage layers (local files, MCP memory, vector store... |
| [`kotlin-exposed-patterns`](skills/kotlin-exposed-patterns/SKILL.md) | JetBrains Exposed ORM patterns including DSL queries, DAO pattern, transactions, HikariCP connection pooling, Flyway migrations... |
| [`kotlin-patterns`](skills/kotlin-patterns/SKILL.md) | Idiomatic Kotlin patterns, best practices, and conventions for building robust, efficient, and maintainable Kotlin applications... |
| [`laravel-plugin-discovery`](skills/laravel-plugin-discovery/SKILL.md) | Discover and evaluate Laravel packages via LaraPlugins.io MCP. Use when the user wants to find plugins, check package health, o... |
| [`laravel-tdd`](skills/laravel-tdd/SKILL.md) | Laravel testing strategies with PHPUnit, Pest, model factories, HTTP tests, Sanctum authentication testing, mocking, and covera... |
| [`latency-critical-systems`](skills/latency-critical-systems/SKILL.md) | Optimize and verify latency-sensitive systems — realtime dashboards, market data feeds, streaming agents, execution gateways, q... |
| [`lead-intelligence`](skills/lead-intelligence/SKILL.md) | AI-native lead intelligence and outreach pipeline. Replaces Apollo, Clay, and ZoomInfo with agent-powered signal scoring, mutua... |
| [`living-docs-governance`](skills/living-docs-governance/SKILL.md) | Keep a long-lived project's documentation from rotting by assigning existing project docs clear constitution, map, status, and ... |
| [`llm-trading-agent-security`](skills/llm-trading-agent-security/SKILL.md) | Security patterns for autonomous trading agents with wallet or transaction authority. Covers prompt injection, spend limits, pr... |
| [`logistics-exception-management`](skills/logistics-exception-management/SKILL.md) | Codified freight-exception handling expertise for shipment delays, damages, losses, shortages, and carrier disputes, with escal... |
| [`loop-design-check`](skills/loop-design-check/SKILL.md) | Design a goal-oriented agent loop or review one for failure modes: spinning, Goodhart-gaming the verifier, or running a wrong a... |
| [`mailtrap-email-integration`](skills/mailtrap-email-integration/SKILL.md) | Guides agents through integrating transactional email sending via Mailtrap's Email API, including sandbox testing, domain verif... |
| [`make-interfaces-feel-better`](skills/make-interfaces-feel-better/SKILL.md) | Apply concrete design-engineering details that make interfaces feel polished. Use when reviewing or improving UI spacing, typog... |
| [`manim-video`](skills/manim-video/SKILL.md) | Build reusable Manim explainers for technical concepts, graphs, system diagrams, and product walkthroughs, then hand off to the... |
| [`marketing-campaign`](skills/marketing-campaign/SKILL.md) | End-to-end marketing campaign planning and execution. Covers audience research, positioning, campaign angle definition, landing... |
| [`mcp-builder`](skills/mcp-builder/SKILL.md) | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services throug... |
| [`mcp-server-patterns`](skills/mcp-server-patterns/SKILL.md) | Build MCP servers with Node/TypeScript SDK — tools, resources, prompts, Zod validation, stdio vs Streamable HTTP. Use Context7 ... |
| [`migrating-to-post-quantum-cryptography`](skills/migrating-to-post-quantum-cryptography/SKILL.md) | Build a cryptographic inventory/CBOM with OpenSSL 3.5+, deploy hybrid post-quantum key exchange (X25519MLKEM768) on TLS/VPN/SSH... |
| [`ml-adoption-playbook`](skills/ml-adoption-playbook/SKILL.md) | End-to-end methodology for AI agents and software engineers to add machine learning algorithms to existing non-ML codebases. Co... |
| [`ml-best-practices`](skills/ml-best-practices/SKILL.md) | Guide de compétences et procédures d'agent. |
| [`mle-workflow`](skills/mle-workflow/SKILL.md) | Production machine-learning engineering workflow for data contracts, reproducible training, model evaluation, deployment, monit... |
| [`nanoclaw-repl`](skills/nanoclaw-repl/SKILL.md) | Operate and extend NanoClaw, ECC's zero-dependency session-aware REPL, with persistent markdown-backed sessions and slash comma... |
| [`nutrient-document-processing`](skills/nutrient-document-processing/SKILL.md) | Process, convert, OCR, extract, redact, sign, and fill documents using the Nutrient DWS API. Works with PDFs, DOCX, XLSX, PPTX,... |
| [`observability-and-instrumentation`](skills/observability-and-instrumentation/SKILL.md) | Instruments code so production behavior is visible and diagnosable. Use when adding logging, metrics, tracing, or alerting. Use... |
| [`openclaw-persona-forge`](skills/openclaw-persona-forge/SKILL.md) | 为 OpenClaw AI Agent 锻造完整的龙虾灵魂方案。根据用户偏好或随机抽卡， 输出身份定位、灵魂描述(SOUL.md)、角色化底线规则、名字和头像生图提示词。 如当前环境提供已审核的生图 skill，可自动生成统一风格头像图片。 当用户需要创... |
| [`opensource-pipeline`](skills/opensource-pipeline/SKILL.md) | Open-source pipeline: fork, sanitize, and package private projects for safe public release. Chains 3 agents (forker, sanitizer,... |
| [`operator-approval-loop`](skills/operator-approval-loop/SKILL.md) | Operator approval contract with internal filing notices for agent-drafted outbound messages, hashed drafts, epoch-keyed decisio... |
| [`orch-add-feature`](skills/orch-add-feature/SKILL.md) | Orchestrate building a brand-new feature end to end — research, plan, TDD implementation, review, and gated commit — by delegat... |
| [`orch-build-mvp`](skills/orch-build-mvp/SKILL.md) | Orchestrate bootstrapping a working MVP from a design or spec document — ingest the SDD/PRD, plan thin vertical slices, scaffol... |
| [`orch-fix-defect`](skills/orch-fix-defect/SKILL.md) | Orchestrate fixing a bug — reproduce it as a failing regression test, fix to green, review, and gated commit — by delegating ea... |
| [`orch-pipeline`](skills/orch-pipeline/SKILL.md) | Shared orchestration engine behind the orch-* skill family — the gated Research-Plan-TDD-Review-Commit pipeline, size classifie... |
| [`orchestrating-llm-attacks-with-pyrit`](skills/orchestrating-llm-attacks-with-pyrit/SKILL.md) | Build automated multi-turn adversarial attacks against conversational LLM targets using Microsoft PyRIT's RedTeamingOrchestrato... |
| [`parallel-execution-optimizer`](skills/parallel-execution-optimizer/SKILL.md) | Speed up a task by turning it into a dependency graph of parallel lanes with a lane matrix, batched reads and checks, write sur... |
| [`performing-access-recertification-with-saviynt`](skills/performing-access-recertification-with-saviynt/SKILL.md) | Configure and execute access recertification campaigns in Saviynt Enterprise |
| [`performing-access-review-and-certification`](skills/performing-access-review-and-certification/SKILL.md) | Designs and runs access review and certification campaigns-scoping, |
| [`performing-ai-driven-osint-correlation`](skills/performing-ai-driven-osint-correlation/SKILL.md) | Use AI/LLM-based reasoning with Sherlock, theHarvester, and SpiderFoot |
| [`performing-api-rate-limiting-bypass`](skills/performing-api-rate-limiting-bypass/SKILL.md) | Tests API rate limiting for bypass vulnerabilities using Python (requests/aiohttp) |
| [`performing-asset-criticality-scoring-for-vulns`](skills/performing-asset-criticality-scoring-for-vulns/SKILL.md) | Build a multi-factor asset criticality scoring model—incorporating data |
| [`performing-brand-monitoring-for-impersonation`](skills/performing-brand-monitoring-for-impersonation/SKILL.md) | Monitor for brand impersonation attacks across domains, social media, |
| [`performing-container-escape-detection`](skills/performing-container-escape-detection/SKILL.md) | >- |
| [`performing-container-image-hardening`](skills/performing-container-image-hardening/SKILL.md) | Harden container images by minimizing attack surface, stripping unnecessary |
| [`performing-container-security-scanning-with-trivy`](skills/performing-container-security-scanning-with-trivy/SKILL.md) | >- |
| [`performing-dns-enumeration-and-zone-transfer`](skills/performing-dns-enumeration-and-zone-transfer/SKILL.md) | Enumerates DNS records, attempts zone transfers, brute-forces subdomains, |
| [`performing-entitlement-review-with-sailpoint-iiq`](skills/performing-entitlement-review-with-sailpoint-iiq/SKILL.md) | Runs entitlement review and access certification campaigns in SailPoint |
| [`performing-network-traffic-analysis-with-tshark`](skills/performing-network-traffic-analysis-with-tshark/SKILL.md) | Automate network traffic analysis using tshark (Wireshark CLI) and pyshark to compute protocol distribution statistics, detect ... |
| [`performing-nist-csf-maturity-assessment`](skills/performing-nist-csf-maturity-assessment/SKILL.md) | Conduct a NIST Cybersecurity Framework (CSF) 2.0 maturity assessment across the six core Functions (Govern, Identify, Protect, ... |
| [`performing-oil-gas-cybersecurity-assessment`](skills/performing-oil-gas-cybersecurity-assessment/SKILL.md) | Conduct cybersecurity assessments of upstream, midstream, and downstream oil and gas operations, covering pipeline SCADA, refin... |
| [`performing-physical-intrusion-assessment`](skills/performing-physical-intrusion-assessment/SKILL.md) | Conduct authorized physical penetration testing against facilities, server rooms, and restricted areas using tailgating, RFID b... |
| [`performing-subdomain-enumeration-with-subfinder`](skills/performing-subdomain-enumeration-with-subfinder/SKILL.md) | Enumerate subdomains of target domains using ProjectDiscovery's Subfinder |
| [`performing-supply-chain-attack-simulation`](skills/performing-supply-chain-attack-simulation/SKILL.md) | >- |
| [`performing-wifi-password-cracking-with-aircrack`](skills/performing-wifi-password-cracking-with-aircrack/SKILL.md) | Captures WPA/WPA2 handshakes and performs offline password cracking |
| [`perl-patterns`](skills/perl-patterns/SKILL.md) | Modern Perl 5.36+ idioms, best practices, and conventions for building robust, maintainable Perl applications. Use when writing... |
| [`plan-canvas`](skills/plan-canvas/SKILL.md) | Open plans and HTML artifacts in a local browser canvas where the human annotates elements, chats, and approves or requests cha... |
| [`plan-orchestrate`](skills/plan-orchestrate/SKILL.md) | Read a plan document, decompose it into steps, classify each step, and emit the ready-to-paste ECC slash command for that step,... |
| [`pptx`](skills/pptx/SKILL.md) | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide... |
| [`prediction-market-oracle-research`](skills/prediction-market-oracle-research/SKILL.md) | Research prediction markets as data sources or oracle signals for products, agents, dashboards, and corporate decision intellig... |
| [`prodeos-industrial-convergence`](skills/prodeos-industrial-convergence/SKILL.md) | Industrial engineering and OT/IT convergence skill modeled after Prodeos industrial solutions. Use when designing, integrating,... |
| [`product-capability`](skills/product-capability/SKILL.md) | Translate PRD intent, roadmap asks, or product discussions into an implementation-ready capability plan that exposes constraint... |
| [`project-flow-ops`](skills/project-flow-ops/SKILL.md) | Operate execution flow across GitHub and Linear by triaging issues and pull requests, linking active work, and keeping GitHub p... |
| [`prompt-caching-strategy`](skills/prompt-caching-strategy/SKILL.md) | >- |
| [`prompt-optimizer`](skills/prompt-optimizer/SKILL.md) | Analyze draft prompts, detect intent and missing context, match ECC commands, skills, and agents, and output a ready-to-paste o... |
| [`python-patterns`](skills/python-patterns/SKILL.md) | Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and maintainable Python applic... |
| [`pytorch-patterns`](skills/pytorch-patterns/SKILL.md) | PyTorch deep learning patterns and best practices for building robust, efficient, and reproducible training pipelines, model ar... |
| [`quarkus-verification`](skills/quarkus-verification/SKILL.md) | Verification loop for Quarkus projects: build, static analysis (Checkstyle, PMD, SpotBugs), tests with JaCoCo coverage, OWASP d... |
| [`rails-patterns`](skills/rails-patterns/SKILL.md) | Ruby on Rails framework patterns for Rails 7.1+ and 8.x apps. Covers the directory contract, skinny controllers with service ob... |
| [`ralphinho-rfc-pipeline`](skills/ralphinho-rfc-pipeline/SKILL.md) | Split an RFC into a multi-agent execution DAG — decompose into work units with dependencies and acceptance tests, run research,... |
| [`react-performance`](skills/react-performance/SKILL.md) | React and Next.js performance optimization patterns adapted from Vercel Engineering's React Best Practices (https://github.com/... |
| [`recsys-pipeline-architect`](skills/recsys-pipeline-architect/SKILL.md) | Design composable recommendation, ranking, and feed pipelines using the six-stage Source→Hydrator→Filter→Scorer→Selector→SideEf... |
| [`recursive-decision-ledger`](skills/recursive-decision-ledger/SKILL.md) | Run repeated rollouts ("Prime Gauss" style recursive prompting) while keeping an append-only decision ledger of trials, marks, ... |
| [`red-teaming-llms-with-garak`](skills/red-teaming-llms-with-garak/SKILL.md) | Runs NVIDIA garak probe suites (jailbreak, prompt injection, data |
| [`regex-vs-llm-structured-text`](skills/regex-vs-llm-structured-text/SKILL.md) | Decision framework for parsing structured text (quizzes, forms, invoices, receipts, tables) with a hybrid regex-first pipeline ... |
| [`remotion-video-creation`](skills/remotion-video-creation/SKILL.md) | Best practices for Remotion - Video creation in React. 29 domain-specific rules covering 3D, animations, audio, captions, chart... |
| [`returns-reverse-logistics`](skills/returns-reverse-logistics/SKILL.md) | Codified expertise for returns authorization, receipt and inspection, disposition decisions, refund processing, fraud detection... |
| [`rust-patterns`](skills/rust-patterns/SKILL.md) | Idiomatic Rust patterns, ownership, error handling, traits, concurrency, and best practices for building safe, performant appli... |
| [`safety-guard`](skills/safety-guard/SKILL.md) | Guard against destructive operations with three modes: Careful intercepts dangerous commands (rm -rf, git push --force, DROP TA... |
| [`santa-method`](skills/santa-method/SKILL.md) | Multi-agent adversarial verification: two independent reviewers with the same rubric must both pass before output ships, with a... |
| [`scanning-container-images-with-grype`](skills/scanning-container-images-with-grype/SKILL.md) | >- |
| [`scanning-containers-with-trivy-in-cicd`](skills/scanning-containers-with-trivy-in-cicd/SKILL.md) | Integrates Aqua Security''s Trivy scanner into CI/CD pipelines to detect |
| [`scientific-thinking-scholar-evaluation`](skills/scientific-thinking-scholar-evaluation/SKILL.md) | Structured scholarly-work evaluation for papers, proposals, literature reviews, methods sections, evidence quality, citation su... |
| [`search-first`](skills/search-first/SKILL.md) | Research-before-coding workflow: search npm/PyPI, MCP servers, skills, and GitHub for existing tools before writing custom code... |
| [`securing-agentic-ai-tool-invocation`](skills/securing-agentic-ai-tool-invocation/SKILL.md) | Implements defense-in-depth controls at an AI agent's tool-invocation |
| [`securing-container-registry-with-harbor`](skills/securing-container-registry-with-harbor/SKILL.md) | >- |
| [`securing-github-actions-workflows`](skills/securing-github-actions-workflows/SKILL.md) | Hardens GitHub Actions workflows against supply chain attacks, credential |
| [`security-and-hardening`](skills/security-and-hardening/SKILL.md) | Hardens code against vulnerabilities. Use when auditing an input handler for vulnerabilities, when handling user input, authent... |
| [`security-scan`](skills/security-scan/SKILL.md) | Scan your Claude Code configuration (.claude/ directory) for security vulnerabilities, misconfigurations, and injection risks u... |
| [`skill-comply`](skills/skill-comply/SKILL.md) | Visualize whether skills, rules, and agent definitions are actually followed — auto-generates scenarios at 3 prompt strictness ... |
| [`skill-creator`](skills/skill-creator/SKILL.md) | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill fro... |
| [`skill-repair`](skills/skill-repair/SKILL.md) | Guide de compétences et procédures d'agent. |
| [`skill-stocktake`](skills/skill-stocktake/SKILL.md) | Use when auditing Claude skills and commands for quality. Supports Quick Scan (changed skills only) and Full Stocktake modes wi... |
| [`slack-gif-creator`](skills/slack-gif-creator/SKILL.md) | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation c... |
| [`social-graph-ranker`](skills/social-graph-ranker/SKILL.md) | Weighted social-graph ranking for warm intro discovery, bridge scoring, and network gap analysis across X and LinkedIn. Use whe... |
| [`social-publisher`](skills/social-publisher/SKILL.md) | Agent-driven scheduling and publishing of social media posts across 13 platforms via SocialClaw. Use when the user wants to pub... |
| [`source-driven-development`](skills/source-driven-development/SKILL.md) | Grounds every implementation decision in official documentation. Use when you want to verify an approach against the official d... |
| [`springboot-tdd`](skills/springboot-tdd/SKILL.md) | Test-driven development for Spring Boot using JUnit 5, Mockito, MockMvc, Testcontainers, and JaCoCo. Use when adding features, ... |
| [`springboot-verification`](skills/springboot-verification/SKILL.md) | Run the full Spring Boot verification loop — Maven or Gradle build, SpotBugs, PMD, and Checkstyle static analysis, unit and Tes... |
| [`story-lifecycle`](skills/story-lifecycle/SKILL.md) | Manage a file-based epic → story → sprint development loop without requiring an external project management tool. Creates and t... |
| [`swift-concurrency-6-2`](skills/swift-concurrency-6-2/SKILL.md) | Swift 6.2 Approachable Concurrency — single-threaded by default, @concurrent for explicit background offloading, isolated confo... |
| [`taste-application`](skills/taste-application/SKILL.md) | Generate new video against a distilled style pack and cut it into a finished piece - plan takes from the reference's cut rhythm... |
| [`taste-distillation`](skills/taste-distillation/SKILL.md) | Measure a set of reference videos into a reusable style pack - colour grade as a 3D LUT, cut rhythm as a shot-length distributi... |
| [`tasteforge-video`](skills/tasteforge-video/SKILL.md) | Use for file-driven multimodal image, video, and 3D-asset discovery; taste interviews; distill or apply workflows; style-pack v... |
| [`tdd-workflow`](skills/tdd-workflow/SKILL.md) | Test-driven development workflow: write a failing test first, watch it fail, implement the smallest change to green, then refac... |
| [`team-agent-orchestration`](skills/team-agent-orchestration/SKILL.md) | Run team-based orchestration for agent squads: work items with owners and scope, agent Kanban state, branch isolation, control ... |
| [`team-builder`](skills/team-builder/SKILL.md) | Interactive picker that discovers available agent personas via the claude agents command and agents/ markdown globs, groups the... |
| [`terminal-opener`](skills/terminal-opener/SKILL.md) | Open an executable and its argument array in a visible terminal window through a reusable, shell-free launch plan with dry-run,... |
| [`terminal-ops`](skills/terminal-ops/SKILL.md) | Evidence-first repo execution workflow for ECC. Use when the user wants a command run, a repo checked, a CI failure debugged, o... |
| [`testing-api-security-with-owasp-top-10`](skills/testing-api-security-with-owasp-top-10/SKILL.md) | Systematically assesses REST, GraphQL, and gRPC API endpoints against the OWASP |
| [`testing-for-email-header-injection`](skills/testing-for-email-header-injection/SKILL.md) | Tests web application email functionality (contact forms, password reset, |
| [`testing-for-system-prompt-leakage`](skills/testing-for-system-prompt-leakage/SKILL.md) | Extracts LLM system prompts using direct requests, jailbreak/instruction-override |
| [`testing-for-xml-injection-vulnerabilities`](skills/testing-for-xml-injection-vulnerabilities/SKILL.md) | Test web applications for XML injection vulnerabilities including XXE, |
| [`testing-prompt-injection-in-rag-pipelines`](skills/testing-prompt-injection-in-rag-pipelines/SKILL.md) | Probes Retrieval-Augmented Generation pipelines for indirect prompt injection |
| [`theme-factory`](skills/theme-factory/SKILL.md) | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are... |
| [`token-card`](skills/token-card/SKILL.md) | Render a token-usage stat card from local Claude Code, Codex, Gemini CLI, and OpenCode session logs and commit it into the repo... |
| [`ui-ux-pro-max`](skills/ui-ux-pro-max/SKILL.md) | UI/UX design intelligence for web, mobile, and desktop. This skill should be used when designing, building, reviewing, or fixin... |
| [`unified-memory`](skills/unified-memory/SKILL.md) | Share durable, inspectable context and handoffs between Claude, Codex, Hermes, Cursor, OpenCode, and other agents through the l... |
| [`using-agent-skills`](skills/using-agent-skills/SKILL.md) | Discovers and invokes agent skills. Use when starting a session, or when you need to decide which skill or workflow applies to ... |
| [`verification-loop`](skills/verification-loop/SKILL.md) | Run a six-phase verification of a Claude Code session's work — build, type check, lint, tests with coverage, security grep, and... |
| [`video-editing`](skills/video-editing/SKILL.md) | AI-assisted video editing workflows for cutting, structuring, and augmenting real footage. Covers the full pipeline from raw ca... |
| [`visa-doc-translate`](skills/visa-doc-translate/SKILL.md) | Translate visa document images (bank deposit, employment, income, and retirement certificates; HEIC, PNG, or JPG) into English ... |
| [`web-artifacts-builder`](skills/web-artifacts-builder/SKILL.md) | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, ... |
| [`workspace-surface-audit`](skills/workspace-surface-audit/SKILL.md) | Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the highest-value ECC-... |

---

## 💻 Développement Logiciel, Web & Langages (252 skills)

| Compétence | Description |
| :--- | :--- |
| [`abusing-shadow-credentials-for-privesc`](skills/abusing-shadow-credentials-for-privesc/SKILL.md) | Take over Active Directory accounts by writing attacker-controlled public keys to msDS-KeyCredentialLink (Shadow Credentials) w... |
| [`academy-guide`](skills/academy-guide/SKILL.md) | > |
| [`algorithmic-art`](skills/algorithmic-art/SKILL.md) | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request ... |
| [`auditing-foundry-smart-contract-security`](skills/auditing-foundry-smart-contract-security/SKILL.md) | >- |
| [`auditing-tls-certificate-transparency-logs`](skills/auditing-tls-certificate-transparency-logs/SKILL.md) | Monitors Certificate Transparency (CT) logs to detect unauthorized certificate |
| [`automating-ioc-enrichment`](skills/automating-ioc-enrichment/SKILL.md) | Automates the enrichment of raw indicators of compromise with multi-source |
| [`automation-audit-ops`](skills/automation-audit-ops/SKILL.md) | Evidence-first automation inventory and overlap audit workflow for ECC. Use when the user wants to know which jobs, hooks, conn... |
| [`brand-discovery`](skills/brand-discovery/SKILL.md) | Run a structured, resumable multi-session brand identity interview across 8 modules (purpose, positioning, audience, personalit... |
| [`brand-guidelines`](skills/brand-guidelines/SKILL.md) | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-... |
| [`building-detection-rule-with-splunk-spl`](skills/building-detection-rule-with-splunk-spl/SKILL.md) | Build effective detection rules using Splunk Search Processing Language |
| [`building-detection-rules-with-sigma`](skills/building-detection-rules-with-sigma/SKILL.md) | Builds vendor-agnostic detection rules using the Sigma rule format for |
| [`building-incident-response-dashboard`](skills/building-incident-response-dashboard/SKILL.md) | Builds real-time incident response dashboards in Splunk, Elastic, or |
| [`building-incident-response-playbook`](skills/building-incident-response-playbook/SKILL.md) | Designs and documents structured incident response playbooks with step-by-step |
| [`building-ioc-enrichment-pipeline-with-opencti`](skills/building-ioc-enrichment-pipeline-with-opencti/SKILL.md) | Build an automated IOC enrichment pipeline on OpenCTI (STIX 2.1 native |
| [`building-role-mining-for-rbac-optimization`](skills/building-role-mining-for-rbac-optimization/SKILL.md) | Apply bottom-up and top-down role mining techniques, including clustering |
| [`building-soc-escalation-matrix`](skills/building-soc-escalation-matrix/SKILL.md) | Build a structured SOC escalation matrix defining severity tiers, response |
| [`building-soc-metrics-and-kpi-tracking`](skills/building-soc-metrics-and-kpi-tracking/SKILL.md) | Builds SOC performance metrics and KPI tracking dashboards measuring |
| [`canary-watch`](skills/canary-watch/SKILL.md) | Use this skill to monitor and verify a deployed URL after releases — checks HTTP endpoints, SSE streams, static assets, console... |
| [`canvas-design`](skills/canvas-design/SKILL.md) | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to... |
| [`change-impact`](skills/change-impact/SKILL.md) | >- |
| [`cisco-ios-patterns`](skills/cisco-ios-patterns/SKILL.md) | Cisco IOS and IOS-XE review patterns for show commands, config hierarchy, wildcard masks, ACL placement, interface hygiene, and... |
| [`click-path-audit`](skills/click-path-audit/SKILL.md) | Trace every user-facing button/touchpoint through its full state change sequence to find bugs where functions individually work... |
| [`collecting-indicators-of-compromise`](skills/collecting-indicators-of-compromise/SKILL.md) | Systematically collects, categorizes, and distributes indicators of |
| [`conducting-cyber-risk-assessment-with-nist-800-30`](skills/conducting-cyber-risk-assessment-with-nist-800-30/SKILL.md) | >- |
| [`conducting-man-in-the-middle-attack-simulation`](skills/conducting-man-in-the-middle-attack-simulation/SKILL.md) | Simulates man-in-the-middle attacks using Ettercap, mitmproxy, and Bettercap |
| [`conducting-post-incident-lessons-learned`](skills/conducting-post-incident-lessons-learned/SKILL.md) | Facilitate structured post-incident reviews to identify root causes, |
| [`config-gc`](skills/config-gc/SKILL.md) | Garbage collection for your Claude Code configuration. Periodically scans ~/.claude (skills, memory, hooks, permissions, MCP se... |
| [`configuring-certificate-authority-with-openssl`](skills/configuring-certificate-authority-with-openssl/SKILL.md) | Build a two-tier PKI Certificate Authority hierarchy (offline Root CA |
| [`configuring-host-based-intrusion-detection`](skills/configuring-host-based-intrusion-detection/SKILL.md) | Configures host-based intrusion detection systems (HIDS) to monitor |
| [`configuring-hsm-for-key-storage`](skills/configuring-hsm-for-key-storage/SKILL.md) | Configures Hardware Security Modules for cryptographic key storage |
| [`configuring-microsegmentation-for-zero-trust`](skills/configuring-microsegmentation-for-zero-trust/SKILL.md) | Configures microsegmentation policies to enforce least-privilege workload-to-workload |
| [`configuring-multi-factor-authentication-with-duo`](skills/configuring-multi-factor-authentication-with-duo/SKILL.md) | Deploys Cisco Duo multi-factor authentication across enterprise applications, |
| [`configuring-network-segmentation-with-vlans`](skills/configuring-network-segmentation-with-vlans/SKILL.md) | Designs and implements VLAN-based (802.1Q) network segmentation on |
| [`configuring-oauth2-authorization-flow`](skills/configuring-oauth2-authorization-flow/SKILL.md) | Configures secure OAuth 2.0 authorization flows, including Authorization |
| [`configuring-pfsense-firewall-rules`](skills/configuring-pfsense-firewall-rules/SKILL.md) | Configures pfSense firewall rules, NAT policies, IPsec/OpenVPN tunnels, |
| [`configuring-snort-ids-for-intrusion-detection`](skills/configuring-snort-ids-for-intrusion-detection/SKILL.md) | Installs, configures, and tunes Snort 3 to monitor network traffic |
| [`configuring-tls-1-3-for-secure-communications`](skills/configuring-tls-1-3-for-secure-communications/SKILL.md) | Configures TLS 1.3 (RFC 8446) on servers, covering cipher suite and |
| [`configuring-windows-defender-advanced-settings`](skills/configuring-windows-defender-advanced-settings/SKILL.md) | Configures Microsoft Defender for Endpoint (MDE) advanced protection |
| [`configuring-windows-event-logging-for-detection`](skills/configuring-windows-event-logging-for-detection/SKILL.md) | Configures Windows Event Logging with advanced audit policies to generate |
| [`configuring-zscaler-private-access-for-ztna`](skills/configuring-zscaler-private-access-for-ztna/SKILL.md) | Configures Zscaler Private Access (ZPA) to replace traditional VPN |
| [`content-hash-cache-pattern`](skills/content-hash-cache-pattern/SKILL.md) | Cache expensive file processing results using SHA-256 content hashes — path-independent, auto-invalidating, with service layer ... |
| [`context-and-decisions`](skills/context-and-decisions/SKILL.md) | >- |
| [`continuous-learning`](skills/continuous-learning/SKILL.md) | [DEPRECATED - use continuous-learning-v2] Legacy v1 stop-hook skill extractor. v2 is a strict superset with instinct-based, pro... |
| [`conventional-commit-review`](skills/conventional-commit-review/SKILL.md) | Reviews staged changes and drafts a Conventional Commits-compliant commit message with the right type, scope, and length. Use b... |
| [`correlating-security-events-in-qradar`](skills/correlating-security-events-in-qradar/SKILL.md) | Correlates security events in IBM QRadar SIEM using AQL (Ariel Query |
| [`council`](skills/council/SKILL.md) | Convene a four-voice council for ambiguous decisions, tradeoffs, and go/no-go calls. Use when multiple valid paths exist and yo... |
| [`cpp-coding-standards`](skills/cpp-coding-standards/SKILL.md) | C++ coding standards based on the C++ Core Guidelines (isocpp.github.io). Use when writing, reviewing, or refactoring C++ code ... |
| [`crosspost`](skills/crosspost/SKILL.md) | Multi-platform content distribution across X, LinkedIn, Threads, and Bluesky. Adapts content per platform using content-engine ... |
| [`dashboard-builder`](skills/dashboard-builder/SKILL.md) | Build monitoring dashboards that answer real operator questions for Grafana, SigNoz, and similar platforms. Use when turning me... |
| [`defi-amm-security`](skills/defi-amm-security/SKILL.md) | Security checklist for Solidity AMM contracts, liquidity pools, and swap flows. Covers reentrancy, CEI ordering, donation or in... |
| [`delivery-gate`](skills/delivery-gate/SKILL.md) | Stop hook that blocks Claude from finishing until quality checks pass. Detects rationalization patterns (surface text heuristic... |
| [`deploying-osquery-for-endpoint-monitoring`](skills/deploying-osquery-for-endpoint-monitoring/SKILL.md) | Deploys and configures osquery for real-time endpoint monitoring using |
| [`discernment-nudge`](skills/discernment-nudge/SKILL.md) | > |
| [`docx`](skills/docx/SKILL.md) | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.do... |
| [`enforcing-resource-attribution`](skills/enforcing-resource-attribution/SKILL.md) | Enforces resource attribution for CLI commands. Use this skill whenever |
| [`esign-field-placement`](skills/esign-field-placement/SKILL.md) | Deterministic method for placing signature, date, and text fields in a web e-signature composer through a browser automation se... |
| [`executing-nist-rmf-authorization-to-operate`](skills/executing-nist-rmf-authorization-to-operate/SKILL.md) | >- |
| [`executing-red-team-engagement-planning`](skills/executing-red-team-engagement-planning/SKILL.md) | Build the foundational red team engagement plan - scope definition, Rules |
| [`extracting-browser-history-artifacts`](skills/extracting-browser-history-artifacts/SKILL.md) | Extracts and analyzes browser history, cookies, cache, downloads, and |
| [`extracting-credentials-from-memory-dump`](skills/extracting-credentials-from-memory-dump/SKILL.md) | Extracts cached credentials, password hashes, Kerberos tickets, and |
| [`frontend-patterns`](skills/frontend-patterns/SKILL.md) | Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices. Use when b... |
| [`git-workflow`](skills/git-workflow/SKILL.md) | Git workflow patterns including branching strategies, commit conventions, keeping history clean and readable, tidying local com... |
| [`git-workflow-and-versioning`](skills/git-workflow-and-versioning/SKILL.md) | Structures git workflow practices. Use when making any code change. Use when committing, branching, resolving conflicts, splitt... |
| [`github-ops`](skills/github-ops/SKILL.md) | GitHub repository operations, automation, and management. Issue triage, PR management, CI/CD operations, release management, an... |
| [`google-workspace-ops`](skills/google-workspace-ops/SKILL.md) | Operate across Google Drive, Docs, Sheets, and Slides as one workflow surface for plans, trackers, decks, and shared documents.... |
| [`healthcare-cdss-patterns`](skills/healthcare-cdss-patterns/SKILL.md) | Clinical Decision Support System (CDSS) development patterns. Drug interaction checking, dose validation, clinical scoring (NEW... |
| [`healthcare-emr-patterns`](skills/healthcare-emr-patterns/SKILL.md) | EMR/EHR development patterns for healthcare applications. Clinical safety, encounter workflows, prescription generation, clinic... |
| [`hermes-imports`](skills/hermes-imports/SKILL.md) | Convert local Hermes operator workflows into sanitized ECC skills and release-pack artifacts. Use when preparing a Hermes workf... |
| [`homelab-network-readiness`](skills/homelab-network-readiness/SKILL.md) | Readiness checklist for homelab VLAN segmentation, local DNS filtering (Pi-hole, AdGuard Home), and WireGuard-style remote acce... |
| [`homelab-network-setup`](skills/homelab-network-setup/SKILL.md) | Practical home and homelab network planning for gateways, switches, access points, IP ranges, DHCP reservations, DNS, cabling, ... |
| [`homelab-pihole-dns`](skills/homelab-pihole-dns/SKILL.md) | Pi-hole installation, blocklist management, DNS-over-HTTPS setup, DHCP integration, local DNS records, and troubleshooting brok... |
| [`homelab-vlan-segmentation`](skills/homelab-vlan-segmentation/SKILL.md) | Segmenting home networks into VLANs for IoT, guest, trusted, and server traffic using UniFi, pfSense/OPNsense, and MikroTik — i... |
| [`homelab-wireguard-vpn`](skills/homelab-wireguard-vpn/SKILL.md) | WireGuard VPN server setup, peer configuration, key generation, split tunneling vs full tunnel routing, and remote access to a ... |
| [`i18n-sync`](skills/i18n-sync/SKILL.md) | Translate and synchronize application JSON locale files using source-key usage, project terminology, and focused validation. Us... |
| [`implementing-alert-fatigue-reduction`](skills/implementing-alert-fatigue-reduction/SKILL.md) | Implements strategies to reduce SOC alert fatigue by tuning detection |
| [`implementing-application-whitelisting-with-applocker`](skills/implementing-application-whitelisting-with-applocker/SKILL.md) | Implements application whitelisting using Windows AppLocker to restrict |
| [`implementing-attack-path-analysis-with-xm-cyber`](skills/implementing-attack-path-analysis-with-xm-cyber/SKILL.md) | Deploys XM Cyber's continuous exposure management platform to build |
| [`implementing-attack-surface-management`](skills/implementing-attack-surface-management/SKILL.md) | Implements external attack surface management (EASM) using Shodan, Censys, |
| [`implementing-bgp-security-with-rpki`](skills/implementing-bgp-security-with-rpki/SKILL.md) | Implement RPKI-based BGP route origin validation by creating Route Origin |
| [`implementing-browser-isolation-for-zero-trust`](skills/implementing-browser-isolation-for-zero-trust/SKILL.md) | Deploys remote browser isolation (RBI) as a core component of a Zero |
| [`implementing-continuous-security-validation-with-bas`](skills/implementing-continuous-security-validation-with-bas/SKILL.md) | Deploys Breach and Attack Simulation (BAS) platforms such as SafeBreach, |
| [`implementing-delinea-secret-server-for-pam`](skills/implementing-delinea-secret-server-for-pam/SKILL.md) | Implements Delinea Secret Server for privileged access management, |
| [`implementing-device-posture-assessment-in-zero-trust`](skills/implementing-device-posture-assessment-in-zero-trust/SKILL.md) | Implements device posture assessment as a zero trust access control |
| [`implementing-devsecops-security-scanning`](skills/implementing-devsecops-security-scanning/SKILL.md) | Integrates SAST, DAST, and SCA into CI/CD pipelines using Semgrep for |
| [`implementing-disk-encryption-with-bitlocker`](skills/implementing-disk-encryption-with-bitlocker/SKILL.md) | Implements full disk encryption using Microsoft BitLocker on Windows |
| [`implementing-ebpf-security-monitoring`](skills/implementing-ebpf-security-monitoring/SKILL.md) | Implements eBPF-based security monitoring using Cilium Tetragon for |
| [`implementing-endpoint-dlp-controls`](skills/implementing-endpoint-dlp-controls/SKILL.md) | Implements endpoint Data Loss Prevention (DLP) controls to detect and |
| [`implementing-google-workspace-admin-security`](skills/implementing-google-workspace-admin-security/SKILL.md) | Hardens a Google Workspace tenant via Admin Console configuration: |
| [`implementing-hardware-security-key-authentication`](skills/implementing-hardware-security-key-authentication/SKILL.md) | Builds a FIDO2/WebAuthn relying party server with the python-fido2 |
| [`implementing-hipaa-security-rule-safeguards`](skills/implementing-hipaa-security-rule-safeguards/SKILL.md) | >- |
| [`implementing-ics-firewall-with-tofino`](skills/implementing-ics-firewall-with-tofino/SKILL.md) | Deploys and configures Tofino industrial firewalls (Belden/Hirschmann) |
| [`implementing-identity-verification-for-zero-trust`](skills/implementing-identity-verification-for-zero-trust/SKILL.md) | Implements continuous, risk-adaptive identity verification for zero trust |
| [`implementing-iec-62443-security-zones`](skills/implementing-iec-62443-security-zones/SKILL.md) | Designs security zones and conduits for industrial control systems |
| [`implementing-image-provenance-verification-with-cosign`](skills/implementing-image-provenance-verification-with-cosign/SKILL.md) | >- |
| [`implementing-infrastructure-as-code-security-scanning`](skills/implementing-infrastructure-as-code-security-scanning/SKILL.md) | Implements automated security scanning for Infrastructure as Code using |
| [`implementing-iso-27001-information-security-management`](skills/implementing-iso-27001-information-security-management/SKILL.md) | >- |
| [`implementing-just-in-time-access-provisioning`](skills/implementing-just-in-time-access-provisioning/SKILL.md) | >- |
| [`implementing-jwt-signing-and-verification`](skills/implementing-jwt-signing-and-verification/SKILL.md) | >- |
| [`implementing-log-forwarding-with-fluentd`](skills/implementing-log-forwarding-with-fluentd/SKILL.md) | >- |
| [`implementing-memory-protection-with-dep-aslr`](skills/implementing-memory-protection-with-dep-aslr/SKILL.md) | Implements memory protection mechanisms including DEP (Data Execution |
| [`implementing-mimecast-targeted-attack-protection`](skills/implementing-mimecast-targeted-attack-protection/SKILL.md) | >- |
| [`implementing-mobile-application-management`](skills/implementing-mobile-application-management/SKILL.md) | Implements Mobile Application Management (MAM) policies to protect enterprise |
| [`implementing-mtls-for-zero-trust-services`](skills/implementing-mtls-for-zero-trust-services/SKILL.md) | Configures mutual TLS (mTLS) authentication between microservices using |
| [`implementing-network-access-control`](skills/implementing-network-access-control/SKILL.md) | Implements 802.1X port-based network access control using RADIUS authentication, |
| [`implementing-network-access-control-with-cisco-ise`](skills/implementing-network-access-control-with-cisco-ise/SKILL.md) | Deploys Cisco Identity Services Engine (ISE) as a RADIUS policy server for 802.1X |
| [`implementing-network-deception-with-honeypots`](skills/implementing-network-deception-with-honeypots/SKILL.md) | Deploy and manage network honeypots using OpenCanary, T-Pot, or Cowrie |
| [`implementing-network-intrusion-prevention-with-suricata`](skills/implementing-network-intrusion-prevention-with-suricata/SKILL.md) | Deploys and configures Suricata as an inline network intrusion prevention system, |
| [`implementing-network-segmentation-for-ot`](skills/implementing-network-segmentation-for-ot/SKILL.md) | Implements OT network segmentation using VLANs, OT-aware firewalls, data diodes, |
| [`implementing-network-segmentation-with-firewall-zones`](skills/implementing-network-segmentation-with-firewall-zones/SKILL.md) | Designs and implements network segmentation using firewall security zones, VLANs, |
| [`implementing-network-traffic-baselining`](skills/implementing-network-traffic-baselining/SKILL.md) | Builds network traffic baselines from NetFlow/IPFIX CSV or JSON exports using Python |
| [`implementing-next-generation-firewall-with-palo-alto`](skills/implementing-next-generation-firewall-with-palo-alto/SKILL.md) | Configures and deploys Palo Alto Networks next-generation firewalls end-to-end, |
| [`implementing-opa-gatekeeper-for-policy-enforcement`](skills/implementing-opa-gatekeeper-for-policy-enforcement/SKILL.md) | >- |
| [`implementing-ot-network-traffic-analysis-with-nozomi`](skills/implementing-ot-network-traffic-analysis-with-nozomi/SKILL.md) | Deploy Nozomi Networks Guardian sensors for passive OT network traffic |
| [`implementing-passwordless-auth-with-microsoft-entra`](skills/implementing-passwordless-auth-with-microsoft-entra/SKILL.md) | Implements passwordless authentication using Microsoft Entra ID with |
| [`implementing-passwordless-authentication-with-fido2`](skills/implementing-passwordless-authentication-with-fido2/SKILL.md) | Deploy FIDO2/WebAuthn passwordless authentication using security keys |
| [`implementing-patch-management-for-ot-systems`](skills/implementing-patch-management-for-ot-systems/SKILL.md) | Implements a structured patch management program for OT/ICS environments |
| [`implementing-pod-security-admission-controller`](skills/implementing-pod-security-admission-controller/SKILL.md) | >- |
| [`implementing-privileged-access-management-with-cyberark`](skills/implementing-privileged-access-management-with-cyberark/SKILL.md) | Deploy CyberArk Privileged Access Management to discover, vault, rotate, |
| [`implementing-privileged-session-monitoring`](skills/implementing-privileged-session-monitoring/SKILL.md) | Implements privileged session monitoring and recording using PAM |
| [`implementing-runtime-security-with-tetragon`](skills/implementing-runtime-security-with-tetragon/SKILL.md) | >- |
| [`implementing-scim-provisioning-with-okta`](skills/implementing-scim-provisioning-with-okta/SKILL.md) | Implement automated user lifecycle provisioning and deprovisioning using |
| [`implementing-secret-scanning-with-gitleaks`](skills/implementing-secret-scanning-with-gitleaks/SKILL.md) | This skill covers implementing Gitleaks for detecting and preventing |
| [`implementing-secrets-management-with-vault`](skills/implementing-secrets-management-with-vault/SKILL.md) | Deploy HashiCorp Vault for centralized secrets management, covering dynamic |
| [`implementing-security-chaos-engineering`](skills/implementing-security-chaos-engineering/SKILL.md) | Implements security chaos engineering experiments that deliberately |
| [`implementing-siem-correlation-rules-for-apt`](skills/implementing-siem-correlation-rules-for-apt/SKILL.md) | Write multi-event correlation rules in Splunk SPL and Sigma format that |
| [`implementing-siem-use-case-tuning`](skills/implementing-siem-use-case-tuning/SKILL.md) | Tune SIEM detection rules in Splunk and Elastic to reduce false positives |
| [`implementing-siem-use-cases-for-detection`](skills/implementing-siem-use-cases-for-detection/SKILL.md) | Implements SIEM detection use cases by designing correlation rules, |
| [`implementing-sigstore-for-software-signing`](skills/implementing-sigstore-for-software-signing/SKILL.md) | Implements Sigstore-based software signing and verification using Cosign |
| [`implementing-soar-automation-with-phantom`](skills/implementing-soar-automation-with-phantom/SKILL.md) | Implements Security Orchestration, Automation, and Response (SOAR) workflows |
| [`implementing-soar-playbook-with-palo-alto-xsoar`](skills/implementing-soar-playbook-with-palo-alto-xsoar/SKILL.md) | Build automated incident response playbooks in Cortex XSOAR (Demisto) |
| [`implementing-syslog-centralization-with-rsyslog`](skills/implementing-syslog-centralization-with-rsyslog/SKILL.md) | Configure rsyslog for centralized log collection with TLS encryption, |
| [`implementing-ticketing-system-for-incidents`](skills/implementing-ticketing-system-for-incidents/SKILL.md) | Implements an integrated incident ticketing system connecting SIEM alerts |
| [`implementing-usb-device-control-policy`](skills/implementing-usb-device-control-policy/SKILL.md) | Implements USB device control policies to restrict unauthorized removable |
| [`implementing-web-application-logging-with-modsecurity`](skills/implementing-web-application-logging-with-modsecurity/SKILL.md) | Configure ModSecurity WAF with the OWASP Core Rule Set (CRS) for web |
| [`implementing-zero-knowledge-proof-for-authentication`](skills/implementing-zero-knowledge-proof-for-authentication/SKILL.md) | Implements the Schnorr identification protocol and a simplified Zero-Knowledge Password Proof (ZKPP) over the discrete logarith... |
| [`implementing-zero-trust-with-hashicorp-boundary`](skills/implementing-zero-trust-with-hashicorp-boundary/SKILL.md) | Installs and configures HashiCorp Boundary as a default-deny, identity-aware proxy for infrastructure access, including control... |
| [`incremental-implementation`](skills/incremental-implementation/SKILL.md) | Delivers changes incrementally in thin, verifiable slices. Use when implementing any feature or change that touches more than o... |
| [`intercepting-mobile-traffic-with-burpsuite`](skills/intercepting-mobile-traffic-with-burpsuite/SKILL.md) | Intercepts and analyzes HTTP/HTTPS traffic from mobile applications |
| [`internal-comms`](skills/internal-comms/SKILL.md) | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claud... |
| [`jpa-patterns`](skills/jpa-patterns/SKILL.md) | JPA/Hibernate patterns for entity design, relationships, query optimization, transactions, auditing, indexing, pagination, and ... |
| [`liquid-glass-design`](skills/liquid-glass-design/SKILL.md) | iOS 26 Liquid Glass design system — dynamic glass material with blur, reflection, and interactive morphing for SwiftUI, UIKit, ... |
| [`managing-python-dependencies`](skills/managing-python-dependencies/SKILL.md) | Guide de compétences et procédures d'agent. |
| [`managing-third-party-vendor-risk`](skills/managing-third-party-vendor-risk/SKILL.md) | >- |
| [`market-research`](skills/market-research/SKILL.md) | Conduct market research, competitive analysis, investor due diligence, and industry intelligence with source attribution and de... |
| [`mcp-dependency-review`](skills/mcp-dependency-review/SKILL.md) | Statically review MCP configuration for mutable package references before approval or CI, without executing discovered MCP serv... |
| [`module-regression`](skills/module-regression/SKILL.md) | >- |
| [`monitoring-scada-modbus-traffic-anomalies`](skills/monitoring-scada-modbus-traffic-anomalies/SKILL.md) | Monitors Modbus TCP traffic on SCADA and ICS networks to detect anomalous |
| [`motion-foundations`](skills/motion-foundations/SKILL.md) | Motion tokens, spring presets, performance rules, device adaptation, accessibility enforcement, and SSR safety for React / Next... |
| [`netmiko-ssh-automation`](skills/netmiko-ssh-automation/SKILL.md) | Safe Python Netmiko patterns for read-only collection, bounded batch SSH, TextFSM parsing, guarded config changes, timeouts, an... |
| [`network-config-validation`](skills/network-config-validation/SKILL.md) | Pre-deployment checks for router and switch configuration, including dangerous commands, duplicate addresses, subnet overlaps, ... |
| [`network-interface-health`](skills/network-interface-health/SKILL.md) | Diagnose interface errors, drops, CRCs, duplex mismatches, flapping, speed negotiation issues, and counter trends on routers, s... |
| [`nextjs-turbopack`](skills/nextjs-turbopack/SKILL.md) | Next.js 16+ and Turbopack guidance — incremental Rust bundling, file-system caching, faster dev startup and HMR, Turbopack vs w... |
| [`nodejs-keccak256`](skills/nodejs-keccak256/SKILL.md) | Prevent Ethereum hashing bugs in JavaScript and TypeScript. Node's sha3-256 is NIST SHA3, not Ethereum Keccak-256, and silently... |
| [`notebook-guidance`](skills/notebook-guidance/SKILL.md) | - |
| [`nuxt4-patterns`](skills/nuxt4-patterns/SKILL.md) | Nuxt 4 app patterns for hydration safety, performance, route rules, lazy loading, and SSR-safe data fetching with useFetch and ... |
| [`pdf`](skills/pdf/SKILL.md) | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs... |
| [`performing-alert-triage-with-elastic-siem`](skills/performing-alert-triage-with-elastic-siem/SKILL.md) | Perform systematic alert triage in Elastic Security SIEM—classifying, |
| [`performing-android-app-static-analysis-with-mobsf`](skills/performing-android-app-static-analysis-with-mobsf/SKILL.md) | Performs automated static analysis of Android applications using Mobile |
| [`performing-arp-spoofing-attack-simulation`](skills/performing-arp-spoofing-attack-simulation/SKILL.md) | Simulates ARP spoofing/cache-poisoning attacks in authorized lab or |
| [`performing-bandwidth-throttling-attack-simulation`](skills/performing-bandwidth-throttling-attack-simulation/SKILL.md) | Simulate bandwidth throttling and network degradation attacks using tc, |
| [`performing-bluetooth-security-assessment`](skills/performing-bluetooth-security-assessment/SKILL.md) | Assess Bluetooth Low Energy (BLE) device security using Python's bleak asyncio |
| [`performing-content-security-policy-bypass`](skills/performing-content-security-policy-bypass/SKILL.md) | Analyze Content-Security-Policy headers and bypass them to achieve cross-site |
| [`performing-credential-access-with-lazagne`](skills/performing-credential-access-with-lazagne/SKILL.md) | Extract stored credentials from compromised endpoints using the LaZagne |
| [`performing-cryptographic-audit-of-application`](skills/performing-cryptographic-audit-of-application/SKILL.md) | A cryptographic audit systematically reviews an application's use of |
| [`performing-deception-technology-deployment`](skills/performing-deception-technology-deployment/SKILL.md) | Deploys deception technology including honeypots, honeytokens, and decoy |
| [`performing-dmarc-policy-enforcement-rollout`](skills/performing-dmarc-policy-enforcement-rollout/SKILL.md) | Execute a phased DMARC rollout by inventorying sending sources, configuring |
| [`performing-dns-tunneling-detection`](skills/performing-dns-tunneling-detection/SKILL.md) | Detects DNS tunneling by computing Shannon entropy of DNS query names, |
| [`performing-dynamic-analysis-of-android-app`](skills/performing-dynamic-analysis-of-android-app/SKILL.md) | Performs runtime dynamic analysis of Android applications using Frida, |
| [`performing-false-positive-reduction-in-siem`](skills/performing-false-positive-reduction-in-siem/SKILL.md) | Reduces SIEM false positives through systematic rule tuning, threshold |
| [`performing-file-carving-with-foremost`](skills/performing-file-carving-with-foremost/SKILL.md) | Recovers files from disk images and unallocated space using Foremost's |
| [`performing-firmware-extraction-with-binwalk`](skills/performing-firmware-extraction-with-binwalk/SKILL.md) | Performs firmware image extraction and analysis using binwalk to identify |
| [`performing-fuzzing-with-aflplusplus`](skills/performing-fuzzing-with-aflplusplus/SKILL.md) | Performs coverage-guided fuzzing of compiled binaries with AFL++, instrumenting |
| [`performing-hardware-security-module-integration`](skills/performing-hardware-security-module-integration/SKILL.md) | Integrates Hardware Security Modules (HSMs) via the PKCS#11 interface |
| [`performing-hash-cracking-with-hashcat`](skills/performing-hash-cracking-with-hashcat/SKILL.md) | Cracks password hashes with Hashcat, covering hash-type identification, |
| [`performing-http-parameter-pollution-attack`](skills/performing-http-parameter-pollution-attack/SKILL.md) | Executes HTTP Parameter Pollution attacks that inject duplicate request |
| [`performing-ics-asset-discovery-with-claroty`](skills/performing-ics-asset-discovery-with-claroty/SKILL.md) | Performs ICS/OT asset discovery with Claroty xDome, combining passive |
| [`performing-indicator-lifecycle-management`](skills/performing-indicator-lifecycle-management/SKILL.md) | Tracks IOCs through discovery, enrichment/validation (VirusTotal, Shodan, |
| [`performing-initial-access-with-evilginx3`](skills/performing-initial-access-with-evilginx3/SKILL.md) | Perform authorized initial access using EvilGinx3 adversary-in-the-middle |
| [`performing-ioc-enrichment-automation`](skills/performing-ioc-enrichment-automation/SKILL.md) | Automates Indicator of Compromise (IOC) enrichment by orchestrating |
| [`performing-ios-app-security-assessment`](skills/performing-ios-app-security-assessment/SKILL.md) | Performs comprehensive iOS application security assessments using Frida |
| [`performing-iot-security-assessment`](skills/performing-iot-security-assessment/SKILL.md) | Performs comprehensive security assessments of IoT devices and their |
| [`performing-lateral-movement-detection`](skills/performing-lateral-movement-detection/SKILL.md) | Detects lateral movement techniques including Pass-the-Hash, PsExec, |
| [`performing-lateral-movement-with-wmiexec`](skills/performing-lateral-movement-with-wmiexec/SKILL.md) | Perform lateral movement across Windows networks using WMI-based remote |
| [`performing-log-source-onboarding-in-siem`](skills/performing-log-source-onboarding-in-siem/SKILL.md) | Perform structured log source onboarding into SIEM platforms (Splunk, |
| [`performing-mobile-app-certificate-pinning-bypass`](skills/performing-mobile-app-certificate-pinning-bypass/SKILL.md) | Bypasses SSL/TLS certificate pinning implementations in Android and |
| [`performing-oauth-scope-minimization-review`](skills/performing-oauth-scope-minimization-review/SKILL.md) | Performs OAuth 2.0 scope minimization review to identify over-permissioned |
| [`performing-open-source-intelligence-gathering`](skills/performing-open-source-intelligence-gathering/SKILL.md) | Open Source Intelligence (OSINT) gathering is the first active phase |
| [`performing-ot-network-security-assessment`](skills/performing-ot-network-security-assessment/SKILL.md) | This skill covers conducting comprehensive security assessments of Operational |
| [`performing-packet-injection-attack`](skills/performing-packet-injection-attack/SKILL.md) | Crafts and injects custom network packets using Scapy, hping3, and Nemesis |
| [`performing-paste-site-monitoring-for-credentials`](skills/performing-paste-site-monitoring-for-credentials/SKILL.md) | Monitor paste sites like Pastebin and GitHub Gists for leaked credentials, |
| [`performing-plc-firmware-security-analysis`](skills/performing-plc-firmware-security-analysis/SKILL.md) | This skill covers analyzing Programmable Logic Controller (PLC) firmware |
| [`performing-post-quantum-cryptography-migration`](skills/performing-post-quantum-cryptography-migration/SKILL.md) | Assesses organizational readiness for post-quantum cryptography migration |
| [`performing-privacy-impact-assessment`](skills/performing-privacy-impact-assessment/SKILL.md) | Automates the Privacy Impact Assessment (PIA) workflow including data |
| [`performing-privilege-escalation-assessment`](skills/performing-privilege-escalation-assessment/SKILL.md) | Performs privilege escalation assessments on compromised Linux and Windows |
| [`performing-privilege-escalation-on-linux`](skills/performing-privilege-escalation-on-linux/SKILL.md) | Guides manual enumeration and automated tooling to escalate from a low-privilege |
| [`performing-privileged-account-access-review`](skills/performing-privileged-account-access-review/SKILL.md) | Conducts systematic reviews of privileged accounts to validate access |
| [`performing-privileged-account-discovery`](skills/performing-privileged-account-discovery/SKILL.md) | Discovers and inventories privileged accounts across enterprise infrastructure, |
| [`performing-purple-team-exercise`](skills/performing-purple-team-exercise/SKILL.md) | Performs purple team exercises by coordinating red team adversary emulation |
| [`performing-s7comm-protocol-security-analysis`](skills/performing-s7comm-protocol-security-analysis/SKILL.md) | Perform security analysis of Siemens S7comm and S7CommPlus protocols |
| [`performing-sca-dependency-scanning-with-snyk`](skills/performing-sca-dependency-scanning-with-snyk/SKILL.md) | This skill covers implementing Software Composition Analysis (SCA) using |
| [`performing-scada-hmi-security-assessment`](skills/performing-scada-hmi-security-assessment/SKILL.md) | Perform security assessments of SCADA Human-Machine Interface (HMI) |
| [`performing-security-headers-audit`](skills/performing-security-headers-audit/SKILL.md) | Auditing HTTP security headers including CSP, HSTS, X-Frame-Options, |
| [`performing-service-account-audit`](skills/performing-service-account-audit/SKILL.md) | Audit service accounts across enterprise infrastructure to identify orphaned, |
| [`performing-service-account-credential-rotation`](skills/performing-service-account-credential-rotation/SKILL.md) | Automates credential rotation for service accounts across Active Directory, |
| [`performing-soc-tabletop-exercise`](skills/performing-soc-tabletop-exercise/SKILL.md) | Performs tabletop exercises for SOC teams simulating security incidents |
| [`performing-ssl-certificate-lifecycle-management`](skills/performing-ssl-certificate-lifecycle-management/SKILL.md) | Automates the full SSL/TLS certificate lifecycle, including generating |
| [`performing-ssl-stripping-attack`](skills/performing-ssl-stripping-attack/SKILL.md) | >- |
| [`performing-ssl-tls-security-assessment`](skills/performing-ssl-tls-security-assessment/SKILL.md) | >- |
| [`performing-steganography-detection`](skills/performing-steganography-detection/SKILL.md) | >- |
| [`performing-timeline-reconstruction-with-plaso`](skills/performing-timeline-reconstruction-with-plaso/SKILL.md) | >- |
| [`performing-user-behavior-analytics`](skills/performing-user-behavior-analytics/SKILL.md) | Performs User and Entity Behavior Analytics (UEBA) to detect anomalous |
| [`performing-vlan-hopping-attack`](skills/performing-vlan-hopping-attack/SKILL.md) | >- |
| [`performing-web-application-firewall-bypass`](skills/performing-web-application-firewall-bypass/SKILL.md) | Bypasses Web Application Firewall protections using encoding tricks, |
| [`performing-web-application-scanning-with-nikto`](skills/performing-web-application-scanning-with-nikto/SKILL.md) | Runs Nikto, an open-source web server and web application scanner, |
| [`performing-wireless-security-assessment-with-kismet`](skills/performing-wireless-security-assessment-with-kismet/SKILL.md) | Conduct wireless network security assessments using Kismet to detect |
| [`plankton-code-quality`](skills/plankton-code-quality/SKILL.md) | Write-time code quality enforcement using Plankton — auto-formatting, linting, and Claude-powered fixes on every file edit via ... |
| [`production-audit`](skills/production-audit/SKILL.md) | Local-evidence production readiness audit for shipped apps, pre-launch reviews, post-merge checks, and "what breaks in prod?" q... |
| [`production-scheduling`](skills/production-scheduling/SKILL.md) | Codified expertise for production scheduling, job sequencing, line balancing, changeover optimization, and bottleneck resolutio... |
| [`quality-nonconformance`](skills/quality-nonconformance/SKILL.md) | Quality control and non-conformance management for regulated manufacturing (FDA 21 CFR 820, IATF 16949, AS9100): NCR lifecycle ... |
| [`quarkus-security`](skills/quarkus-security/SKILL.md) | Quarkus security implementation patterns: JWT and OIDC authentication, @RolesAllowed RBAC and SecurityIdentity checks, Bean Val... |
| [`react-patterns`](skills/react-patterns/SKILL.md) | React 18/19 patterns including hooks discipline, server/client component boundaries, Suspense + error boundaries, form actions,... |
| [`recovering-deleted-files-with-photorec`](skills/recovering-deleted-files-with-photorec/SKILL.md) | Recovers deleted files from disk images and storage media using PhotoRec's |
| [`redis-patterns`](skills/redis-patterns/SKILL.md) | Redis data structure patterns, caching strategies, distributed locks, rate limiting, pub/sub, and connection management for pro... |
| [`relaying-ntlm-for-adcs-esc8`](skills/relaying-ntlm-for-adcs-esc8/SKILL.md) | Uses Impacket's ntlmrelayx.py with a coercion tool (PetitPotam, Coercer, |
| [`remediating-s3-bucket-misconfiguration`](skills/remediating-s3-bucket-misconfiguration/SKILL.md) | Provides step-by-step procedures for remediating Amazon S3 bucket |
| [`repo-scan`](skills/repo-scan/SKILL.md) | Bootstrap pointer that installs the external repo-scan skill from a pinned, reviewable commit. Use when repo-scan must be insta... |
| [`research-ops`](skills/research-ops/SKILL.md) | Evidence-first current-state research workflow for ECC. Use when the user wants fresh facts, comparisons, enrichment, or a reco... |
| [`reverse-engineering-ios-app-with-frida`](skills/reverse-engineering-ios-app-with-frida/SKILL.md) | Reverse engineers iOS applications using Frida dynamic instrumentation |
| [`rules-distill`](skills/rules-distill/SKILL.md) | Scan skills to extract cross-cutting principles and distill them into rules — append, revise, or create new rule files. Use whe... |
| [`scanning-network-with-nmap-advanced`](skills/scanning-network-with-nmap-advanced/SKILL.md) | Performs advanced network recon using Nmap''s Scripting Engine (NSE), |
| [`scientific-thinking-literature-review`](skills/scientific-thinking-literature-review/SKILL.md) | Systematic literature-review workflow for academic, biomedical, technical, and scientific topics, including search planning, so... |
| [`securing-helm-chart-deployments`](skills/securing-helm-chart-deployments/SKILL.md) | >- |
| [`securing-historian-server-in-ot-environment`](skills/securing-historian-server-in-ot-environment/SKILL.md) | Audits and hardens process historian servers (OSIsoft PI, Honeywell PHD, |
| [`securing-remote-access-to-ot-environment`](skills/securing-remote-access-to-ot-environment/SKILL.md) | Designs and configures secure remote access to OT/ICS environments for |
| [`shipping-and-launch`](skills/shipping-and-launch/SKILL.md) | Prepares production launches. Use when preparing to deploy to production, or when asking what needs to be in place before shipp... |
| [`skill-host-compat`](skills/skill-host-compat/SKILL.md) | Lint ECC skills for Codex/Cursor-safe frontmatter and Claude-only substitutions before a skill PR. |
| [`skill-scout`](skills/skill-scout/SKILL.md) | Search existing local, marketplace, GitHub, and web skill sources before creating a new skill. Use when the user wants to creat... |
| [`springboot-security`](skills/springboot-security/SKILL.md) | Spring Security best practices for authn/authz, validation, CSRF, secrets, headers, rate limiting, and dependency security in J... |
| [`strategic-compact`](skills/strategic-compact/SKILL.md) | Suggests manual context compaction at logical intervals to preserve context through task phases rather than arbitrary auto-comp... |
| [`swift-actor-persistence`](skills/swift-actor-persistence/SKILL.md) | Thread-safe data persistence in Swift using actors — in-memory cache with file-backed storage, eliminating data races by design... |
| [`token-budget-advisor`](skills/token-budget-advisor/SKILL.md) | Offer a choice of response depth (25%/50%/75%/100%) with token estimates before answering, then answer at that level. Use when ... |
| [`triaging-security-alerts-in-splunk`](skills/triaging-security-alerts-in-splunk/SKILL.md) | Triages security alerts in Splunk Enterprise Security by classifying |
| [`triaging-security-incident`](skills/triaging-security-incident/SKILL.md) | Performs initial triage of security incidents using the NIST SP |
| [`triaging-security-incident-with-ir-playbook`](skills/triaging-security-incident-with-ir-playbook/SKILL.md) | Classifies and prioritizes security incidents using structured IR |
| [`triaging-windows-with-kape`](skills/triaging-windows-with-kape/SKILL.md) | Runs KAPE (Kroll Artifact Parser and Extractor) to collect targeted |
| [`unified-notifications-ops`](skills/unified-notifications-ops/SKILL.md) | Operate notifications as one ECC-native workflow across GitHub, Linear, desktop alerts, hooks, and connected communication surf... |
| [`unity-match3-farm-builder`](skills/unity-match3-farm-builder/SKILL.md) | Complete Unity game development skill for hybrid Match-3 and Farm simulation games (like Farm Bloom, Gardenscapes, Farm Heroes ... |
| [`unity-mcp`](skills/unity-mcp/SKILL.md) | Unity game development, C# scripting, and editor automation using CoplayDev/unity-mcp. Use when the user asks about Unity, game... |
| [`validating-backup-integrity-for-recovery`](skills/validating-backup-integrity-for-recovery/SKILL.md) | Validates backup integrity through cryptographic hash verification, |
| [`verifying-build-provenance-with-slsa-sigstore`](skills/verifying-build-provenance-with-slsa-sigstore/SKILL.md) | Verifies artifact signatures and SLSA provenance using Sigstore's |
| [`videodb`](skills/videodb/SKILL.md) | Ingest, index, search, edit, and monitor video and audio with the VideoDB Python SDK — upload from files, URLs, or RTSP feeds, ... |
| [`vite-patterns`](skills/vite-patterns/SKILL.md) | Vite build tool patterns including config, plugins, HMR, env variables, proxy setup, SSR, library mode, dependency pre-bundling... |

---

## 🧪 Tests, QA & Validation Logicielle (69 skills)

| Compétence | Description |
| :--- | :--- |
| [`assessing-vector-and-embedding-weaknesses`](skills/assessing-vector-and-embedding-weaknesses/SKILL.md) | Test RAG vector stores (Pinecone, Qdrant, Weaviate, Chroma, pgvector, |
| [`auto-skill-activator`](skills/auto-skill-activator/SKILL.md) | Universal Skill Router and Autonomous Activator. Continuously monitors every incoming user request, maps it to the best matchin... |
| [`benchmark`](skills/benchmark/SKILL.md) | Measure performance baselines and detect regressions across browser Core Web Vitals (LCP, INP, CLS, page weight), API endpoint ... |
| [`benchmark-methodology`](skills/benchmark-methodology/SKILL.md) | Score a scoped competitor set into comparable profile cards: nine weighted dimensions (positioning, voice, visual craft, offer ... |
| [`browser-qa`](skills/browser-qa/SKILL.md) | Run automated post-deploy UI verification with a browser automation MCP (claude-in-chrome, Playwright, or Puppeteer): console-e... |
| [`browser-testing-with-devtools`](skills/browser-testing-with-devtools/SKILL.md) | Tests in real browsers via Chrome DevTools MCP. Use when building or debugging anything that runs in a browser. Use when you ne... |
| [`building-patch-tuesday-response-process`](skills/building-patch-tuesday-response-process/SKILL.md) | Establish a repeatable operational process for triaging, testing, and |
| [`bun-runtime`](skills/bun-runtime/SKILL.md) | Bun as runtime, package manager, bundler, and test runner. When to choose Bun vs Node, migration notes, and Vercel support. |
| [`competitive-platform-analysis`](skills/competitive-platform-analysis/SKILL.md) | Use when scoping a competitive landscape — identifying, categorising, and score-filtering a competitor set before any benchmark... |
| [`competitive-report-structure`](skills/competitive-report-structure/SKILL.md) | Assemble scored competitor profile cards (from benchmark-methodology) into a decision-grade competitive report with landscape m... |
| [`conducting-api-security-testing`](skills/conducting-api-security-testing/SKILL.md) | Conducts security testing of REST, GraphQL, and gRPC APIs to identify |
| [`conducting-mobile-app-penetration-test`](skills/conducting-mobile-app-penetration-test/SKILL.md) | Conducts penetration testing of iOS and Android mobile applications |
| [`conducting-wireless-network-penetration-test`](skills/conducting-wireless-network-penetration-test/SKILL.md) | Conducts authorized wireless network penetration tests to assess the |
| [`csharp-testing`](skills/csharp-testing/SKILL.md) | C# and .NET testing patterns with xUnit, FluentAssertions, mocking, integration tests, and test organization best practices. Us... |
| [`dart-flutter-patterns`](skills/dart-flutter-patterns/SKILL.md) | Production-ready Dart and Flutter patterns covering null safety, immutable state with Freezed, async composition, widget archit... |
| [`django-celery`](skills/django-celery/SKILL.md) | Django + Celery async task patterns — configuration, task design, beat scheduling, retries, canvas workflows, monitoring, and t... |
| [`django-tdd`](skills/django-tdd/SKILL.md) | Django testing strategies with pytest-django, TDD methodology, factory_boy, mocking, coverage, and testing Django REST Framewor... |
| [`fsharp-testing`](skills/fsharp-testing/SKILL.md) | F# testing patterns with xUnit, FsUnit, Unquote, FsCheck property-based testing, integration tests, and test organization best ... |
| [`generating-python-installer`](skills/generating-python-installer/SKILL.md) | Commercial-grade Python installer expert for Windows: Nuitka extreme compilation, dist slimming, DLL footprint analysis, and In... |
| [`golang-testing`](skills/golang-testing/SKILL.md) | Go testing patterns including table-driven tests, subtests, benchmarks, fuzzing, and test coverage. Follows TDD methodology wit... |
| [`hardening-linux-endpoint-with-cis-benchmark`](skills/hardening-linux-endpoint-with-cis-benchmark/SKILL.md) | Hardens Linux endpoints using CIS Benchmark recommendations for Ubuntu, |
| [`hardening-windows-endpoint-with-cis-benchmark`](skills/hardening-windows-endpoint-with-cis-benchmark/SKILL.md) | Hardens Windows endpoints using CIS (Center for Internet Security) Benchmark |
| [`idea-refine`](skills/idea-refine/SKILL.md) | Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. Use when an idea is sti... |
| [`implementing-api-security-testing-with-42crunch`](skills/implementing-api-security-testing-with-42crunch/SKILL.md) | Implements API security testing on the 42Crunch platform, combining |
| [`implementing-patch-management-workflow`](skills/implementing-patch-management-workflow/SKILL.md) | Patch management is the systematic process of identifying, testing, deploying, |
| [`interview-me`](skills/interview-me/SKILL.md) | Extracts what the user actually wants instead of what they think they should want. Achieves this through one-question-at-a-time... |
| [`kotlin-coroutines-flows`](skills/kotlin-coroutines-flows/SKILL.md) | Kotlin Coroutines and Flow patterns for Android and KMP — structured concurrency, Flow operators, StateFlow, error handling, an... |
| [`kotlin-ktor-patterns`](skills/kotlin-ktor-patterns/SKILL.md) | Ktor server patterns including routing DSL, plugins, authentication, Koin DI, kotlinx.serialization, WebSockets, and testApplic... |
| [`kotlin-testing`](skills/kotlin-testing/SKILL.md) | Kotlin testing patterns with Kotest, MockK, coroutine testing, property-based testing, and Kover coverage. Follows TDD methodol... |
| [`laravel-verification`](skills/laravel-verification/SKILL.md) | Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage, security scans, and deployme... |
| [`orch-change-feature`](skills/orch-change-feature/SKILL.md) | Orchestrate altering an existing, working feature to new desired behavior — update its tests to the new spec, change the implem... |
| [`orch-refine-code`](skills/orch-refine-code/SKILL.md) | Orchestrate a behavior-preserving refactor — confirm tests are green, restructure without changing behavior, keep tests green, ... |
| [`osint-investigation`](skills/osint-investigation/SKILL.md) | Sparse-clue OSINT investigation methodology for extracting overlooked leads, connecting fragmented evidence, and testing explan... |
| [`performing-api-security-testing-with-postman`](skills/performing-api-security-testing-with-postman/SKILL.md) | Uses Postman to build structured API security test collections covering |
| [`performing-clickjacking-attack-test`](skills/performing-clickjacking-attack-test/SKILL.md) | Testing web applications for clickjacking vulnerabilities by assessing |
| [`performing-csrf-attack-simulation`](skills/performing-csrf-attack-simulation/SKILL.md) | Testing web applications for Cross-Site Request Forgery vulnerabilities |
| [`performing-directory-traversal-testing`](skills/performing-directory-traversal-testing/SKILL.md) | Test web applications for path traversal and Local/Remote File Inclusion |
| [`performing-external-network-penetration-test`](skills/performing-external-network-penetration-test/SKILL.md) | Conduct a comprehensive external network penetration test to identify |
| [`performing-graphql-depth-limit-attack`](skills/performing-graphql-depth-limit-attack/SKILL.md) | Execute and test GraphQL depth limit attacks using deeply nested recursive |
| [`performing-jwt-none-algorithm-attack`](skills/performing-jwt-none-algorithm-attack/SKILL.md) | Execute and test the JWT none algorithm attack, crafting tokens with |
| [`performing-soap-web-service-security-testing`](skills/performing-soap-web-service-security-testing/SKILL.md) | Performs security testing of SOAP web services by analyzing WSDL definitions |
| [`performing-thick-client-application-penetration-test`](skills/performing-thick-client-application-penetration-test/SKILL.md) | Conduct a thick client application penetration test to identify insecure |
| [`performing-web-application-penetration-test`](skills/performing-web-application-penetration-test/SKILL.md) | Performs systematic security testing of web applications following the |
| [`performing-wireless-network-penetration-test`](skills/performing-wireless-network-penetration-test/SKILL.md) | Execute a wireless network penetration test to assess WiFi security by |
| [`perl-testing`](skills/perl-testing/SKILL.md) | Perl testing patterns using Test2::V0, Test::More, prove runner, mocking, coverage with Devel::Cover, and TDD methodology. Use ... |
| [`product-lens`](skills/product-lens/SKILL.md) | Validate the why before building through four product diagnostics — a YC-style product diagnostic that produces PRODUCT-BRIEF.m... |
| [`python-testing`](skills/python-testing/SKILL.md) | Python testing strategies using pytest, TDD methodology, fixtures, mocking, parametrization, and coverage requirements. Use whe... |
| [`quarkus-tdd`](skills/quarkus-tdd/SKILL.md) | Test-driven development for Quarkus 3.x LTS using JUnit 5, Mockito, REST Assured, Camel testing, and JaCoCo. Use when adding fe... |
| [`react-testing`](skills/react-testing/SKILL.md) | React component testing with React Testing Library, Vitest/Jest, MSW for network mocking, accessibility assertions with axe, an... |
| [`rust-testing`](skills/rust-testing/SKILL.md) | Rust testing patterns including unit tests, integration tests, async testing, property-based testing, mocking, and coverage. Fo... |
| [`spec-driven-development`](skills/spec-driven-development/SKILL.md) | Creates specs before coding. Use when starting a new project, feature, or significant change and no specification exists yet. U... |
| [`swift-protocol-di-testing`](skills/swift-protocol-di-testing/SKILL.md) | Protocol-based dependency injection for testable Swift code — mock file system, network, and external APIs using focused protoc... |
| [`test-collaboration`](skills/test-collaboration/SKILL.md) | Inventory and govern a project's test assets. Connect requirements, business rules, risks, bugs, and cross-boundary contracts t... |
| [`test-driven-development`](skills/test-driven-development/SKILL.md) | Drives development with tests using the red-green-refactor loop. Use when implementing any logic, fixing any bug, or changing a... |
| [`testing-android-intents-for-vulnerabilities`](skills/testing-android-intents-for-vulnerabilities/SKILL.md) | Tests Android inter-process communication (IPC) through intents for |
| [`testing-api-authentication-weaknesses`](skills/testing-api-authentication-weaknesses/SKILL.md) | Tests API authentication mechanisms for weaknesses including broken |
| [`testing-api-for-broken-object-level-authorization`](skills/testing-api-for-broken-object-level-authorization/SKILL.md) | Tests REST and GraphQL APIs for Broken Object Level Authorization (BOLA/IDOR, |
| [`testing-for-broken-access-control`](skills/testing-for-broken-access-control/SKILL.md) | Systematically tests web applications and APIs for broken access control |
| [`testing-for-host-header-injection`](skills/testing-for-host-header-injection/SKILL.md) | Test web applications for HTTP Host header injection vulnerabilities |
| [`testing-for-json-web-token-vulnerabilities`](skills/testing-for-json-web-token-vulnerabilities/SKILL.md) | Tests JWT implementations for algorithm confusion, "none" algorithm bypass, |
| [`testing-for-xss-vulnerabilities`](skills/testing-for-xss-vulnerabilities/SKILL.md) | Tests web applications for reflected, stored, and DOM-based Cross-Site |
| [`testing-for-xss-vulnerabilities-with-burpsuite`](skills/testing-for-xss-vulnerabilities-with-burpsuite/SKILL.md) | Identifying and validating cross-site scripting vulnerabilities using |
| [`testing-jwt-token-security`](skills/testing-jwt-token-security/SKILL.md) | Assessing JSON Web Token implementations for cryptographic weaknesses, |
| [`testing-mobile-api-authentication`](skills/testing-mobile-api-authentication/SKILL.md) | Tests authentication and authorization mechanisms in mobile application |
| [`testing-websocket-api-security`](skills/testing-websocket-api-security/SKILL.md) | Tests WebSocket API implementations for missing upgrade-handshake authentication, |
| [`ui-demo`](skills/ui-demo/SKILL.md) | Record polished UI demo videos using Playwright. Use when the user asks to create a demo, walkthrough, screen recording, or tut... |
| [`validating-tpm-measured-boot-attestation`](skills/validating-tpm-measured-boot-attestation/SKILL.md) | Verifies TPM 2.0 measured-boot integrity and remote attestation with |
| [`webapp-testing`](skills/webapp-testing/SKILL.md) | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, de... |
| [`windows-desktop-e2e`](skills/windows-desktop-e2e/SKILL.md) | E2E testing for Windows native desktop apps (WPF, WinForms, Win32/MFC, Qt) using pywinauto and Windows UI Automation. Use when ... |

---

## 📋 Architecture, API, FinOps & Gouvernance (62 skills)

| Compétence | Description |
| :--- | :--- |
| [`achieving-cmmc-level-2-compliance`](skills/achieving-cmmc-level-2-compliance/SKILL.md) | >- |
| [`android-clean-architecture`](skills/android-clean-architecture/SKILL.md) | Clean Architecture patterns for Android and Kotlin Multiplatform projects — module structure, dependency rules, UseCases, Repos... |
| [`api-and-interface-design`](skills/api-and-interface-design/SKILL.md) | Guides stable API and interface design. Use when designing APIs, module boundaries, or any public interface. Use when creating ... |
| [`api-connector-builder`](skills/api-connector-builder/SKILL.md) | Build a new API connector or provider by matching the target repo's existing integration pattern exactly. Use when adding one m... |
| [`api-design`](skills/api-design/SKILL.md) | REST API design patterns including resource naming, status codes, pagination, filtering, error responses, versioning, and rate ... |
| [`article-writing`](skills/article-writing/SKILL.md) | Write articles, guides, blog posts, tutorials, newsletter issues, and other long-form content in a distinctive voice derived fr... |
| [`bypassing-authentication-with-forced-browsing`](skills/bypassing-authentication-with-forced-browsing/SKILL.md) | Discovering and accessing unprotected pages, APIs, and administrative |
| [`claude-api`](skills/claude-api/SKILL.md) | - |
| [`codebase-onboarding`](skills/codebase-onboarding/SKILL.md) | Analyze an unfamiliar codebase and generate a structured onboarding guide with architecture map, key entry points, conventions,... |
| [`compose-multiplatform-patterns`](skills/compose-multiplatform-patterns/SKILL.md) | Compose Multiplatform and Jetpack Compose patterns for KMP projects — state management, navigation, theming, performance, and p... |
| [`conducting-gdpr-compliance-assessment`](skills/conducting-gdpr-compliance-assessment/SKILL.md) | >- |
| [`connections-optimizer`](skills/connections-optimizer/SKILL.md) | Reorganize the user's X and LinkedIn network with review-first pruning, add/follow recommendations, and channel-specific warm o... |
| [`customer-billing-ops`](skills/customer-billing-ops/SKILL.md) | Operate customer billing workflows such as subscriptions, refunds, churn triage, billing-portal recovery, and plan analysis usi... |
| [`customs-trade-compliance`](skills/customs-trade-compliance/SKILL.md) | Codified customs and trade compliance expertise — HS/HTS tariff classification with GRI rules, commercial invoices and entry do... |
| [`deploying-software-defined-perimeter`](skills/deploying-software-defined-perimeter/SKILL.md) | Deploys a Software-Defined Perimeter per the CSA v2.0 specification, configuring Single Packet Authorization, mutual TLS, and S... |
| [`django-patterns`](skills/django-patterns/SKILL.md) | Django architecture patterns, REST API design with DRF, ORM best practices, caching, signals, middleware, and production-grade ... |
| [`doc-coauthoring`](skills/doc-coauthoring/SKILL.md) | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals... |
| [`docs-governance`](skills/docs-governance/SKILL.md) | Route broad documentation-governance requests to existing ECC skills and run an opt-in, read-only audit of mapped documentation... |
| [`flutter-dart-code-review`](skills/flutter-dart-code-review/SKILL.md) | Library-agnostic Flutter/Dart code review checklist covering widget best practices, state management patterns (BLoC, Riverpod, ... |
| [`frontend-design`](skills/frontend-design/SKILL.md) | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic dir... |
| [`frontend-design-direction`](skills/frontend-design-direction/SKILL.md) | Set an ECC-specific frontend design direction for production UI work. Use when building or improving websites, dashboards, appl... |
| [`hipaa-compliance`](skills/hipaa-compliance/SKILL.md) | HIPAA-specific entrypoint for healthcare privacy and security work. Use when a task is explicitly framed around HIPAA, PHI hand... |
| [`implementing-api-abuse-detection-with-rate-limiting`](skills/implementing-api-abuse-detection-with-rate-limiting/SKILL.md) | Implements API abuse detection using token bucket, sliding window, and |
| [`implementing-api-key-security-controls`](skills/implementing-api-key-security-controls/SKILL.md) | Implements secure API key generation with sufficient entropy, server-side |
| [`implementing-api-rate-limiting-and-throttling`](skills/implementing-api-rate-limiting-and-throttling/SKILL.md) | Implements API rate limiting and throttling with token bucket, sliding |
| [`implementing-api-security-posture-management`](skills/implementing-api-security-posture-management/SKILL.md) | Implements API Security Posture Management (API-SPM) to continuously |
| [`implementing-conduit-security-for-ot-remote-access`](skills/implementing-conduit-security-for-ot-remote-access/SKILL.md) | Implements secure conduit architecture for OT remote access under the |
| [`implementing-deception-based-detection-with-canarytoken`](skills/implementing-deception-based-detection-with-canarytoken/SKILL.md) | Deploys and monitors Canary Tokens via the Thinkst Canary REST API for |
| [`implementing-nerc-cip-compliance-controls`](skills/implementing-nerc-cip-compliance-controls/SKILL.md) | Implements NERC CIP controls for Bulk Electric System (BES) cyber systems: asset |
| [`implementing-network-traffic-analysis-with-arkime`](skills/implementing-network-traffic-analysis-with-arkime/SKILL.md) | Queries Arkime (formerly Moloch) full packet capture via its API to search sessions, |
| [`implementing-ot-incident-response-playbook`](skills/implementing-ot-incident-response-playbook/SKILL.md) | Develops OT-specific incident response playbooks using a SANS PICERL-based Python |
| [`implementing-pci-dss-compliance-controls`](skills/implementing-pci-dss-compliance-controls/SKILL.md) | Implements PCI DSS 4.0.1's 12 requirements across 6 control objectives |
| [`implementing-rapid7-insightvm-for-scanning`](skills/implementing-rapid7-insightvm-for-scanning/SKILL.md) | Deploy and configure Rapid7 InsightVM Security Console and Scan Engines, |
| [`implementing-zero-trust-for-saas-applications`](skills/implementing-zero-trust-for-saas-applications/SKILL.md) | Secures SaaS apps (Microsoft 365, Google Workspace, Salesforce, Slack) via CASB/SSPM deployment, conditional access policies, O... |
| [`implementing-zero-trust-network-access-with-zscaler`](skills/implementing-zero-trust-network-access-with-zscaler/SKILL.md) | Configures Zero Trust Network Access using Zscaler Private Access (ZPA) to broker identity-based, context-aware connections bet... |
| [`ios-icon-gen`](skills/ios-icon-gen/SKILL.md) | Generate iOS app icons as PNG imagesets for Xcode asset catalogs from SF Symbols (5000+ Apple-native) or Iconify API (275k+ ope... |
| [`java-coding-standards`](skills/java-coding-standards/SKILL.md) | Java coding standards for Spring Boot and Quarkus services: naming, immutability, Optional usage, streams, exceptions, generics... |
| [`jira-integration`](skills/jira-integration/SKILL.md) | Use this skill when retrieving Jira tickets, analyzing requirements, updating ticket status, adding comments, or transitioning ... |
| [`laravel-patterns`](skills/laravel-patterns/SKILL.md) | Laravel architecture patterns, routing/controllers, Eloquent ORM, service layers, queues, events, caching, and API resources fo... |
| [`laravel-security`](skills/laravel-security/SKILL.md) | Laravel security best practices — authentication, authorization, Eloquent safety, CSRF, XSS prevention, API security, and secur... |
| [`master-agreement-generator`](skills/master-agreement-generator/SKILL.md) | Generate review drafts of counterparty master agreements from one template plus a JSON spec, with role-selected clauses and a S... |
| [`messages-ops`](skills/messages-ops/SKILL.md) | Evidence-first live messaging workflow for ECC. Use when the user wants to read texts or DMs, recover a recent one-time code, i... |
| [`motion-advanced`](skills/motion-advanced/SKILL.md) | Advanced motion patterns for React / Next.js — drag & drop, gestures, text animations, SVG path drawing, custom hooks, imperati... |
| [`motion-patterns`](skills/motion-patterns/SKILL.md) | Production-ready animation patterns for React / Next.js — button, modal, toast, stagger, page transitions, exit animations, scr... |
| [`nasiko-control-plane`](skills/nasiko-control-plane/SKILL.md) | Manage the experimental Nasiko CLI lifecycle through ECC — read-only status checks, consent-gated install of the pinned qualifi... |
| [`nestjs-patterns`](skills/nestjs-patterns/SKILL.md) | NestJS architecture patterns for modules, controllers, providers, DTO validation, guards, interceptors, config, and production-... |
| [`network-bgp-diagnostics`](skills/network-bgp-diagnostics/SKILL.md) | Diagnostics-only BGP troubleshooting patterns for neighbor state, route exchange, prefix policy, AS path inspection, and safe e... |
| [`performing-api-fuzzing-with-restler`](skills/performing-api-fuzzing-with-restler/SKILL.md) | Uses Microsoft RESTler to perform stateful REST API fuzzing: compiles |
| [`performing-api-inventory-and-discovery`](skills/performing-api-inventory-and-discovery/SKILL.md) | Performs API inventory and discovery to identify all API endpoints in |
| [`performing-graphql-security-assessment`](skills/performing-graphql-security-assessment/SKILL.md) | Assessing GraphQL API endpoints for introspection leaks, injection attacks, |
| [`performing-ip-reputation-analysis-with-shodan`](skills/performing-ip-reputation-analysis-with-shodan/SKILL.md) | Analyze IP address reputation using the Shodan API to identify open ports, |
| [`performing-ssl-tls-inspection-configuration`](skills/performing-ssl-tls-inspection-configuration/SKILL.md) | >- |
| [`planning-and-task-breakdown`](skills/planning-and-task-breakdown/SKILL.md) | Breaks work into ordered tasks. Use when you have a spec or clear requirements and need to break work into implementable tasks.... |
| [`quarkus-patterns`](skills/quarkus-patterns/SKILL.md) | Quarkus 3.x LTS architecture patterns with Camel for messaging, RESTful API design, CDI services, data access with Panache, and... |
| [`react-native-patterns`](skills/react-native-patterns/SKILL.md) | React Native and Expo app patterns — Expo Router navigation, state separation (server/client/route/form), TanStack Query data f... |
| [`security-review`](skills/security-review/SKILL.md) | Use this skill when adding authentication, handling user input, working with secrets, creating API endpoints, or implementing p... |
| [`springboot-patterns`](skills/springboot-patterns/SKILL.md) | Spring Boot architecture patterns, REST API design, layered services, data access, caching, async processing, and logging. Use ... |
| [`swiftui-patterns`](skills/swiftui-patterns/SKILL.md) | SwiftUI architecture patterns, state management with @Observable, view composition, navigation, performance optimization, and m... |
| [`triaging-vulnerabilities-with-ssvc-framework`](skills/triaging-vulnerabilities-with-ssvc-framework/SKILL.md) | Triages and prioritizes vulnerabilities with CISA's Stakeholder-Specific |
| [`ui-to-vue`](skills/ui-to-vue/SKILL.md) | Use when the user has UI screenshots or design exports that need batch conversion into Vue 3 components, especially with Vant, ... |
| [`vue-patterns`](skills/vue-patterns/SKILL.md) | Vue.js 3 Composition API patterns, component architecture, reactivity best practices, Pinia state management, Vue Router naviga... |
| [`x-api`](skills/x-api/SKILL.md) | X/Twitter API integration for posting tweets, threads, reading timelines, search, and analytics. Covers OAuth auth patterns, ra... |

---

## 🚀 Structure & Format d'une Skill

Chaque compétence est un sous-dossier modulaire et autonome respectant la spécification **Agent Skills** :
- **`SKILL.md`** : Métadonnées YAML (nom, description, triggers d'activation, conditions d'exclusion) suivies des instructions opératoires détaillées.
- **`scripts/`** *(si présent)* : Outils et scripts d'exécution automatique.
- **`references/`** *(si présent)* : Documentation technique approfondie et spécifications.
- **`examples/`** *(si présent)* : Modèles et exemples d'implémentation de référence.
