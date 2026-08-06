# Manufacturing Troubleshooting Assistant

A production-style Retrieval-Augmented Generation application that helps
manufacturing engineers diagnose equipment problems using technical manuals,
troubleshooting procedures and historical incident records.

## Business problem

Manufacturing engineers frequently search across disconnected manuals,
procedures and historical logs to diagnose equipment problems. This increases
search time, duplicates troubleshooting effort and delays manufacturing test
cycles.

## Solution

The assistant retrieves relevant information from approved enterprise
documents and generates a structured troubleshooting response containing:

- A concise problem summary
- Likely causes
- Ordered troubleshooting steps
- Mandatory safety warnings
- Source citations
- Confidence indication
- Escalation when evidence is insufficient

## Target users

- Manufacturing engineers
- Process engineers
- Field-service engineers
- Equipment technicians

## Initial MVP

The first implementation will support:

- One synthetic equipment family
- 10–20 synthetic technical documents
- English-language questions
- Hybrid document retrieval
- Structured answers
- Source citations
- Safety warnings
- Low-confidence fallback

## Out of scope for the MVP

- Real-time sensor ingestion
- Equipment control
- Predictive maintenance
- ERP integration
- Production multilingual support
- A production user interface

## Architecture

Add the architecture image here later:

![High-level architecture](docs/architecture/high-level-architecture.png)

## Planned technology stack

- Python
- Azure OpenAI
- Azure AI Search
- LangGraph
- FastAPI
- Docker
- Pytest
- Azure Monitor/Application Insights

An equivalent AWS architecture will use Amazon Bedrock, Amazon OpenSearch
Service, Amazon S3, AWS Lambda or Amazon ECS, Amazon Cognito and Amazon
CloudWatch.

## Success metrics

### Technical metrics

- Retrieval Precision@5 greater than 90%
- Response latency below five seconds
- Correct citations for material claims
- Safe fallback when evidence is insufficient

### Business targets

- Reduce document-search time by 70%
- Improve manufacturing test-cycle time by 10%
- Reduce duplicate troubleshooting effort

Business targets are project objectives and are not claimed as measured
portfolio-project results.

## Project status

Current phase: Project setup and documentation.

## Repository structure

Explain the purpose of the major project folders here.

## Running locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.main
pytest