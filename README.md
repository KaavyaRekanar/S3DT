# Secure Semantic Soundness for Digital Threads (S³DT)

This repository accompanies the manuscript:

**Semantic Integrity: A Lifecycle Security Property for Software Digital Threads**

**Authors:** Kaavya Rekanar and Donna O'Shea  
**Journal:** *IEEE Transactions on Dependable and Secure Computing* (revised manuscript)

It provides the reference implementation, case-study materials, evaluation datasets, and experimental notebooks for **S³DT (Secure Semantic Soundness for Digital Threads)**, a framework for assessing semantic integrity across software lifecycle artifacts using **Security Integrity Constraints (SICs)** and structured, embedding-based, and hybrid reasoning.

The repository includes three case studies and additional validation experiments introduced during manuscript revision. These examine both reconstructed security incidents and authentic historical software development activity.

---

## Repository Overview

The materials are organised primarily into:

- **`case_studies/`** — implementations and associated materials for the two reconstructed incidents and the historical Django study.
- **`Evaluation/`** — transition-level evaluation datasets, evaluation notebooks, and additional validation experiments.

The experiments address six complementary questions:

1. Can SICs identify security-relevant semantic inconsistencies across software lifecycle transitions?
2. Can the framework repeatedly assess security constraints across historical source-code revisions?
3. How accurately are source artifacts projected into semantic claims?
4. How do projection errors affect downstream SIC decisions?
5. What trade-offs arise between structured-only, embedding-only, and hybrid reasoning?
6. What preliminary execution-time overhead is observed for the evaluated workload?

The original **47-transition evaluation** comprises the two reconstructed incident studies. The Django study uses a separate **15-checkpoint × 4-SIC** evaluation design, producing 60 assessments.

---

## Repository Structure

```text
S3DT/
├── README.md
├── LICENSE
├── requirements.txt
├── case_studies/
│   ├── AI_Orchestrated_Cyber_Espionage.ipynb
│   ├── Capital_One_Cloud_Configuration_Drift.ipynb
│   └── [Django historical-revision case-study materials]
└── Evaluation/
    ├── Empirical_Evaluation.ipynb
    ├── evaluation_anthropic.csv
    ├── capitalone_transition_dataset.csv
    ├── combined_transition_evaluation_labelled.csv
    └── [Additional validation and ablation materials]
```

*Square-bracketed entries are descriptive placeholders rather than literal filenames. The exact paths of newly uploaded notebooks and datasets should be inserted after verification.*

---

## Case Studies

### Case Study I — AI-Orchestrated Cyber-Espionage

**Notebook:** `case_studies/AI_Orchestrated_Cyber_Espionage.ipynb`

This study reconstructs an AI-orchestrated cyber-espionage incident from publicly reported evidence and applies S³DT to its security-relevant lifecycle transitions.

The notebook demonstrates:

- Semantic claim extraction and projection from available artifacts.
- Construction of a semantic digital thread.
- Semantic delta generation and transition-level comparisons.
- SIC evaluation and explainable integrity decisions.
- Structured, embedding-based, and hybrid semantic assessment.

The case contributes **28 transitions** to the combined transition-level evaluation dataset.

### Case Study II — Capital One Cloud Configuration Drift

**Notebook:** `case_studies/Capital_One_Cloud_Configuration_Drift.ipynb`

This reconstructed incident study examines how security-relevant semantic inconsistencies propagate across security intent, cloud configuration, deployment, and runtime behaviour.

The notebook applies the same three-stage S³DT workflow as Case Study I, enabling comparison between the two scenarios.

The case contributes **19 transitions** to the combined transition-level evaluation dataset.

### Case Study III — Django Historical Software Evolution

**Location:** Django case-study materials under `case_studies/`

The third case study extends the empirical evaluation beyond reconstructed incident artifacts by examining authentic historical Django source-code revisions associated with documented security vulnerabilities, their remediation, and subsequent development activity.

The study considers four documented security issues:

- Django ticket **#30289**
- **CVE-2019-12308**
- **CVE-2021-31542**
- **CVE-2021-33203**

Across **15 historical checkpoints**, the same four system-level SICs are assessed at each checkpoint, producing **60 SIC–checkpoint assessments**.

The evaluation uses relevance-based artifact selection and SIC-scoped claim reasoning to focus on security-relevant evidence and examine how integrity assessments evolve across development history.

This is a retrospective evaluation. It does not establish automated continuous monitoring, repository-wide scalability, or robustness against increasing volumes of unrelated artifacts.

---

## Experimental Evaluation

### 1. Transition-Level Classification and Reasoning Comparison

**Notebook:** `Evaluation/Empirical_Evaluation.ipynb`

The two reconstructed case studies contribute **47 labelled transitions** in
