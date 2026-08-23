# Imaging Retrieval Operations

## A Workflow and Data Analysis of Diagnostic Imaging Retrieval Operations

> Based on real healthcare operations experience managing diagnostic imaging retrieval across SaaS imaging platforms and physical-media workflows.

---

# README Update — Project Evolution & Roadmap

## Project Evolution

The project began as a small PostgreSQL prototype exploring the operational differences between SaaS imaging retrieval and physical CD-based retrieval.

The original model focused primarily on retrieval method, turnaround time, platform coverage, and delays across a small synthetic dataset.

As the project developed, the original schema revealed an important limitation: imaging retrieval is not simply a comparison between SaaS and physical media. A single case may require imaging from multiple healthcare facilities, each facility may support multiple imaging platforms, and each imaging request may progress through a different retrieval pathway.

The project has therefore been redesigned as a broader **Imaging Retrieval Operations** case study.

The revised project uses MySQL and is being expanded into a 12-month synthetic operational dataset representing approximately **50,000 cases, 75,000–85,000 imaging requests, 400 healthcare facilities, and six synthetic SaaS imaging platforms**.

The redesigned model focuses on request-level workflow, facility-platform relationships, retrieval-event history, physical shipment activity, operational workload, and process variation.

---

## Data Source

This project was built from direct healthcare operations experience managing diagnostic imaging retrieval across external healthcare facilities.

The dataset is fully synthetic, but the workflow structure, terminology, operational rules, and data-model requirements were informed by patterns observed firsthand while working in health information operations.

No patient records, proprietary organizational data, historical case data, or real facility performance metrics are used in the project.

The synthetic dataset is designed to reproduce the **structure and complexity of the workflow**, not the historical performance of any specific organization.

---

## Database Design

The redesigned relational model centers on the individual imaging request.

A patient may be associated with multiple cases, and each case may contain multiple imaging requests when imaging is required from more than one healthcare facility.

Facilities may support zero, one, or multiple SaaS imaging platforms. Because platforms may also be associated with multiple facilities, facility-to-platform coverage is modeled as a many-to-many relationship.

The database includes:

- `patients` — synthetic patient identifiers used to preserve patient-to-case relationships
- `cases` — individual cases associated with synthetic patients
- `facilities` — healthcare facilities holding requested imaging
- `imaging_platforms` — synthetic SaaS imaging platforms
- `facility_platforms` — documented facility-to-platform relationships
- `imaging_requests` — individual facility-level imaging retrieval requests
- `imaging_retrieval_events` — operational event history for each request
- `physical_shipments` — shipment activity associated with physical-media retrieval

Patient demographics and other identifying information are intentionally excluded because they are not required for the operational analysis.

---

## Tools

- MySQL
- MySQL Workbench
- Python
- VS Code
- Git
- GitHub
- Tableau *(planned)*

---

## Project Plan

The redesigned project extends beyond a simple retrieval-method comparison into a broader operational workflow and data analysis case study.

Planned development includes:

- synthetic generation of 12 months of imaging retrieval operations
- relational and data-quality validation
- analysis of facility-level retrieval workload
- SaaS platform coverage and utilization analysis
- physical-media retrieval and shipment analysis
- retrieval-event and follow-up workload analysis
- identification of operational outliers and workflow friction
- dashboard development for retrieval operations and KPI monitoring
- scenario analysis of potential workflow and platform-coverage changes

---

## Phase 2 — Synthetic Operations Modeling & Analysis

The original SQL analysis raised broader questions about how imaging retrieval behaves across facilities, platforms, cases, and retrieval pathways.

Phase 2 rebuilds the project around a more realistic relational model and a substantially larger synthetic operational environment.

Python is being used to generate reproducible synthetic data representing patients, cases, healthcare facilities, facility-platform relationships, imaging requests, retrieval events, and physical shipments.

The resulting dataset will then be loaded into MySQL for validation and exploratory operational analysis.

Because the dataset is synthetic, the project distinguishes between **modeled assumptions and analytical findings**. Relationships explicitly created by the data-generation logic are treated as validation targets rather than empirical discoveries. Exploratory analysis focuses on patterns that emerge from interactions among multiple modeled operational variables.

Results describe the behavior of the synthetic system and should not be interpreted as real-world healthcare performance benchmarks.

---

### Phase 2 Deliverables

- Imaging retrieval workflow SOP
- Business rules
- Synthetic data specification
- Revised relational data model
- MySQL database schema
- Python synthetic-data generator
- 12-month synthetic operational dataset
- Data-quality and relational validation
- SQL operational analysis
- Retrieval operations dashboard
- Scenario and sensitivity analysis

---

## Project Documentation

Supporting project documentation is maintained in the `docs/` directory:

- `imaging-retrieval-operations_sop.md` — modeled imaging retrieval workflow and scope
- `business-rules.md` — operational rules governing the modeled workflow
- `data-model.md` — relational entities and relationships
- `synthetic-data-specification.md` — assumptions governing synthetic data generation

---

## Current Status

The relational schema has been redesigned and implemented in MySQL.

Synthetic data generation is currently in progress using Python. Initial generation includes:

- 6 synthetic SaaS imaging platforms
- 400 synthetic healthcare facilities
- 44,754 synthetic patients
- 50,000 synthetic cases
- facility-to-platform relationships

The next stage will generate imaging requests, retrieval events, and physical shipment activity before the dataset is validated and loaded for SQL analysis.

---

## Live Database

A public database environment and completed analytical queries will be added after synthetic data generation and validation are complete.