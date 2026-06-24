# RecruitAI

AI-powered candidate ranking system built for the Redrob Data & AI Challenge 2026.

---

## Live Demo

**Streamlit Sandbox**

https://algorithm-avengers-recruitai-nyrc7mbfwlqxcqjly3lqkh.streamlit.app

**GitHub Repository**

https://github.com/thatikondaharshini10-creator/Algorithm-Avengers-RecruitAI

---

## Problem Statement

Traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching, often failing to identify candidates whose experience and expertise are expressed differently from the exact job description.

RecruitAI addresses this challenge by combining semantic retrieval with a hybrid scoring framework that evaluates candidate relevance, career history, experience, behavioral signals, production ML expertise, retrieval knowledge, and profile quality.

---

## Why RecruitAI?

Traditional keyword-based systems:

* Miss relevant candidates
* Reward keyword stuffing
* Provide limited explainability

RecruitAI improves candidate discovery through:

* Semantic understanding of profiles
* Multi-factor candidate evaluation
* Explainable recruiter-friendly reasoning
* Honeypot detection and penalty mechanisms
* Fast ranking on large-scale datasets

---

## Approach

RecruitAI uses a hybrid ranking architecture consisting of three major stages:

### 1. Semantic Retrieval

* Sentence Transformers (all-MiniLM-L6-v2)
* Candidate profile embeddings
* Job description embedding
* Cosine similarity retrieval
* Top 2000 candidate selection

### 2. Multi-Factor Candidate Ranking

The retrieved candidates are evaluated using:

* Semantic Relevance Score
* Career Alignment Score
* Experience Score
* Behavioral Signal Score
* Retrieval Expertise Score
* Production ML Experience Score
* Company Quality Score
* Honeypot Penalty

### 3. Explainable Reasoning Generation

For every ranked candidate, RecruitAI generates recruiter-friendly reasoning based on:

* Career history
* Experience
* Skills
* Behavioral signals
* Retrieval expertise
* Production ML background

This improves transparency and trust in the ranking process.

---

## System Architecture

Job Description

↓

Sentence Transformer (all-MiniLM-L6-v2)

↓

Semantic Embedding Generation

↓

Cosine Similarity Search

↓

Top 2000 Relevant Candidates

↓

Hybrid Scoring Engine

├── Semantic Score

├── Career Score

├── Experience Score

├── Behavioral Signals

├── Retrieval Expertise

├── Production ML Score

├── Company Quality Score

└── Honeypot Penalty

↓

Reasoning Generation

↓

Top 100 Ranked Candidates

↓

CSV Output + Sandbox Demo

---

## Scoring Formula

Final Score =

0.25 × Semantic Score

* 0.15 × Behavioral Score

* 0.15 × Career Score

* 0.10 × Experience Score

* 0.15 × Retrieval Score

* 0.10 × Production ML Score

* 0.10 × Company Score

− Honeypot Penalty

---

## Results

Dataset Size:

~100,000 Candidate Profiles

Relevant Candidates Identified:

24,872 Candidates

Final Output:

Top 100 Ranked Candidates

Embedding Precomputation Time:

~24 Minutes

Ranking Runtime:

~30 Seconds

Hardware:

* 13th Gen Intel Core i5-13420H
* 16 GB RAM
* Windows 11
* Python 3.13.7

---

## Sandbox Demo

A Streamlit-based sandbox is provided for reproducibility and verification.

Features:

* Run candidate ranking on sample candidates
* View ranked candidate results
* Download ranked CSV outputs
* Demonstrate end-to-end ranking workflow

Demo Link:

https://algorithm-avengers-recruitai-nyrc7mbfwlqxcqjly3lqkh.streamlit.app

---

## Project Structure

RecruitAI/

├── app/

│ └── Streamlit sandbox application

├── artifacts/

│ ├── candidate_embeddings.npy

│ └── candidate_ids.json

├── data/

│ ├── candidates.jsonl

│ ├── job_description.txt

│ └── candidate_schema.json

├── output/

│ └── ranked_candidates_top100.csv

├── src/

│ ├── ranking pipeline

│ ├── scoring modules

│ ├── reasoning generation

│ └── candidate processing

├── experiments/

│ └── exploratory analysis and evaluation scripts

└── README.md

---

## Reproduction

### Step 1 – Generate Candidate Embeddings

python src/precompute_embeddings.py

### Step 2 – Run Ranking Pipeline

python src/fast_ranker.py

### Output

output/ranked_candidates_top100.csv

---

## Features

* Semantic candidate retrieval
* Explainable candidate ranking
* Career history understanding
* Behavioral signal analysis
* Retrieval and recommendation expertise detection
* Production ML experience scoring
* Company quality evaluation
* Honeypot protection
* Top-100 candidate generation
* Streamlit sandbox deployment

---

## Team

### T Harshini

Lead ML Engineer & System Developer

### V Lavanya Reddy

Research, Documentation & Presentation

---

## AI Tools Used

ChatGPT was used for:

* Architecture discussions
* Debugging assistance
* Code review support
* GitHub workflow guidance
* Documentation assistance

All implementation, experimentation, scoring design, testing, optimization, candidate analysis, deployment, and submission preparation were performed by the team.

---

## Challenge Submission

Redrob Data & AI Challenge 2026

Team Name: Algorithm Avengers
