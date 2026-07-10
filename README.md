# Secure Semantic Soundness for Digital Threads (S³DT)

This repository accompanies the paper:

**Semantic Integrity: A Lifecycle Security Property for Software Digital Threads**

It contains the reference implementation and empirical evaluation of the **S³DT (Secure Semantic Soundness for Digital Threads)** framework for detecting semantic drift across software lifecycle artifacts using Security Integrity Constraints (SICs) and hybrid neuro-symbolic reasoning.

---

## Repository Overview

The repository is organised into two main components:

```
case_studies/
evaluation/
```

The case study notebooks implement the complete S³DT workflow, including semantic projection, semantic digital thread construction, Security Integrity Constraint evaluation, and hybrid semantic assessment.

The evaluation notebook reproduces the empirical evaluation reported in the paper using the transition-level datasets generated from both case studies.

---

## Repository Structure

```
S3DT/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── case_studies/
│   ├── AI_Orchestrated_Cyber_Espionage.ipynb
│   └── Capital_One_Cloud_Configuration_Drift.ipynb
│
├── evaluation/
│   ├── Empirical_Evaluation.ipynb
│   ├── evaluation_anthropic.csv
│   ├── capitalone_transition_dataset.csv
│   └── combined_transition_evaluation_labelled.csv
```

---

## Case Studies

### AI-Orchestrated Cyber-Espionage

This notebook demonstrates the complete application of S³DT to an AI-orchestrated cyber-espionage campaign reconstructed from publicly available reports.

The notebook implements:

- semantic claim extraction;
- semantic digital thread construction;
- semantic delta generation;
- Security Integrity Constraint (SIC) evaluation;
- hybrid semantic drift assessment; and
- explainable security decision generation.

---

### Capital One Cloud Configuration Drift

This notebook applies S³DT to the Capital One cloud breach, illustrating how semantic inconsistencies propagate from security intent through cloud configuration and deployment into runtime behaviour.

The notebook follows the same three-stage workflow as the AI case study, enabling direct comparison between the two scenarios.

---

## Empirical Evaluation

The evaluation notebook reproduces all empirical results presented in the paper.

Using the transition-level datasets generated from both case studies, it computes:

- classification accuracy;
- precision, recall, and F1-score;
- confusion matrices;
- early semantic drift detection results; and
- framework characteristic metrics.

All reported tables and quantitative results can be reproduced directly by executing the notebook.

---

## Transition-Level Evaluation Datasets

The repository contains the transition datasets used for empirical evaluation.

| Dataset | Description |
|---------|-------------|
| `evaluation_anthropic.csv` | Transition-level dataset generated from the AI-Orchestrated Cyber-Espionage case study |
| `capitalone_transition_dataset.csv` | Transition-level dataset generated from the Capital One case study |
| `combined_transition_evaluation_labelled.csv` | Combined dataset containing all 47 semantic lifecycle transitions used throughout the empirical evaluation |

---

## Software Requirements

The implementation is written in Python and was developed using Jupyter Notebooks.

Required packages include:

- networkx
- pandas
- numpy
- matplotlib
- sentence-transformers
- pydantic
- scikit-learn

Dependencies can be installed using

```bash
pip install -r requirements.txt
```

---

## Reproducing the Results

1. Install the required dependencies.
2. Execute both case study notebooks to reproduce the semantic digital threads and candidate drift events.
3. Run `Empirical_Evaluation.ipynb`.
4. Load the transition datasets when prompted.
5. The notebook reproduces all evaluation results reported in the paper.

---

## Repository–Paper Mapping

| Paper | Repository |
|------|------------|
| Case Study I | `case_studies/AI_Orchestrated_Cyber_Espionage.ipynb` |
| Case Study II | `case_studies/Capital_One_Cloud_Configuration_Drift.ipynb` |
| Section VI: Empirical Evaluation | `evaluation/Empirical_Evaluation.ipynb` |
| Transition-level datasets | `evaluation/*.csv` |

---

## Citation

If you use this repository, please cite:

> K. Rekanar and D. O'Shea,
> *Semantic Security for Software Digital Threads*,

---

## License

This project is released under the **MIT License**.

See the `LICENSE` file for details.
