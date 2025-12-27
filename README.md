# Bug Copilot

**Bug Copilot** is a live bug report analyzer built using **Pathway’s streaming engine**.

It enables **real-time monitoring** of bug tickets and dynamically updates bug severity, priorities, and reports as new information arrives — without batch processing or stale analysis.

## What it does
- Continuously monitors live bug tickets using Pathway  
- Triggers an AI agent on every new or updated bug  
- Dynamically adjusts severity and priorities  
- Maintains long-horizon context and generates evolving reports  

## Why it matters
Most bug tracking systems work in batches and assign static priorities.  
Bug Copilot stays **always live**, helping teams focus on the **most critical bugs at the right time**.

## Tech Stack
- Pathway (real-time streaming engine)  
- Python  
- SentenceTransformers (MiniLM)  

> **Track-1 Alignment:** Bug report analyzer with live ticket feeds and report generation for longer horizons
