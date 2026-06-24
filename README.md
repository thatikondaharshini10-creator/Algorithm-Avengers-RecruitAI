# RecruitAI

AI-powered candidate ranking system built for the Redrob Data & AI Challenge 2026.

## Problem Statement

Recruiters often rely on keyword matching systems that fail to understand the complete profile of a candidate. RecruitAI addresses this challenge by combining semantic retrieval with multi-factor candidate scoring to identify candidates who genuinely fit the role.

## Approach

RecruitAI uses a hybrid ranking architecture:

1. Semantic Retrieval

   * Sentence Transformers (all-MiniLM-L6-v2)
   * Candidate embeddings
   * Cosine similarity search

2. Candidate Ranking

   * Semantic relevance score
   * Career alignment score
   * Experience score
   * Behavioral signals score
   * Retrieval expertise score
   * Production ML score
   * Company quality score
   * Honeypot penalty

3. Reasoning Generation

   * Generates recruiter-friendly explanations
   * Uses career history, skills, experience and behavioral signals
   * Provides transparent ranking decisions

## Architecture

Job Description
↓
Embedding Generation
↓
Semantic Retrieval
↓
Top 2000 Candidates
↓
Multi-Factor Scoring
↓
Honeypot Detection
↓
Reasoning Generation
↓
Top 100 Ranked Candidates

## Scoring Formula

Final Score =
0.25 × Semantic Score +
0.15 × Behavior Score +
0.15 × Career Score +
0.10 × Experience Score +
0.15 × Retrieval Score +
0.10 × Production ML Score +
0.10 × Company Score
− Honeypot Penalty

## Project Structure

src/

* Ranking pipeline
* Scoring modules
* Candidate processing

data/

* Job description
* Candidate schema

artifacts/

* Precomputed embeddings
* Candidate ID mapping

output/

* Ranked candidate output

experiments/

* Exploratory analysis
* Evaluation scripts

## Reproduction

Step 1

python src/precompute_embeddings.py

Step 2

python src/fast_ranker.py

Output:

output/ranked_candidates_top100.csv

## Runtime

Embedding Precomputation:
~24 minutes

Ranking Pipeline:
~30 seconds

Hardware:
13th Gen Intel Core i5-13420H
16 GB RAM
Windows 11

## Features

* Semantic candidate retrieval
* Career history understanding
* Behavioral signal analysis
* Retrieval and recommendation expertise detection
* Production ML experience scoring
* Honeypot protection
* Explainable ranking

## Team

Algorithm Avengers

T Harshini

* Lead Developer & AI/ML Engineer

V Lavanya Reddy

* Research, Documentation & Presentation

## Challenge Submission

Redrob Data & AI Challenge 2026
