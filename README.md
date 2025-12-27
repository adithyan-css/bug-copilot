# Bug Copilot

> **Track-1 Alignment:** Bug report analyzer with live ticket feeds and report generation for longer horizons

**Bug Copilot** is a real-time bug report analyzer built using **Pathway’s streaming engine**.  
It continuously monitors bug tickets and dynamically updates severity, priority, and reports as new information arrives.

---

## Problem
Software teams receive bug reports continuously, but most traditional bug tracking tools are **not truly real-time**.  
They require **manual or repeated re-runs** to reprocess data when new bug information arrives and typically assign priority only once. This leads to delayed responses, stale analysis, and critical issues going unnoticed.

---

## Solution
Bug Copilot brings **real-time intelligence** to bug triaging.

- Live monitoring of bug tickets using Pathway  
- Event-driven AI agent triggered on every update  
- Dynamic severity and priority updates  
- Reports evolve automatically over long horizons  

The system always reflects the **current system state**, without batch reprocessing.

---
## Why it matters
- No manual reruns or re-triaging  
- Real-time focus on critical bugs  
- Clear visibility into recurring risks  

---

## How it works
1. Bug tickets are added or updated in `data/tickets/`  
2. Pathway detects changes in real time  
3. An AI agent reasons over cumulative bug history  
4. Updated insights and reports are generated instantly  

---

## Demo

**Live monitoring with Pathway**  
![Pathway live monitoring](screenshots/pathway_live_dashboard.png)

**Automatically generated bug report**  
![Generated bug report](screenshots/generated_bug_report.png)

---

## Tech Stack
- Pathway (real-time streaming engine)  
- Python  
- SentenceTransformers (MiniLM)  

---

## Setup & Usage
```bash
pip install -r requirements.txt
python main.py
