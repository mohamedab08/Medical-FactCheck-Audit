# Medical & Biological Fact-Checking Benchmark

An evaluation framework built to audit Large Language Model (LLM) responses against medical fundamentals, physiology, and pharmacological literature.

## Overview
- **Clinical Hallucination Auditing:** Identifies flawed medical logic, incorrect drug mechanisms, and diagnostic inconsistencies in AI outputs.
- **Pairwise Quality Assurance:** Benchmarks model responses to evaluate safety, precision, and adherence to medical evidence.
- **Automated Dataset Validation:** Features a Python script (`med_validator.py`) that checks dataset formatting and verification integrity.

## File Structure
- `medical_evals.json`: Pairwise comparison dataset of medical/biological prompts, AI answers, and expert clinical justifications.
- `med_validator.py`: Automated Python tool for validating dataset syntax and schema completeness.
