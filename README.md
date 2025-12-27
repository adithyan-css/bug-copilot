# Bug Copilot

> **Track-1 Alignment:** Bug report analyzer with live ticket feeds and report generation for longer horizons

**Bug Copilot** is a live bug report analyzer built using **Pathway’s streaming engine**.

It enables **real-time monitoring** of bug tickets and dynamically updates bug severity, priorities, and reports as new information arrives — ensuring decisions are always based on the latest system state.

## What it does
- Continuously monitors live bug tickets using Pathway  
- Triggers an AI agent on every new or updated bug  
- Dynamically adjusts severity and priorities  
- Maintains long-horizon context and generates evolving reports  

## Why it matters
Most bug tracking systems assign priorities once and rarely adapt as new details emerge.  
Bug Copilot stays **always live**, helping teams focus on the **most critical issues as they evolve**, not as they were initially reported.

For developers, this means:
- Less time triaging bugs  
- Faster response to production-critical issues  
- Clear visibility into recurring and high-risk problem areas  

## Tech Stack
- Pathway (real-time streaming engine)  
- Python  
- SentenceTransformers (MiniLM)  

