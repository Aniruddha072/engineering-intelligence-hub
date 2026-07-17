# Engineering Intelligence Hub

![CI](https://github.com/Aniruddha072/engineering-intelligence-hub/actions/workflows/ci.yml/badge.svg)

> A production-grade Hybrid RAG platform for engineering knowledge.

Engineering Intelligence Hub (EIH) is an end-to-end Retrieval-Augmented Generation (RAG) platform designed to explore how modern AI-powered knowledge systems are engineered beyond simple prototypes.

The project focuses on building a scalable and maintainable architecture for ingesting, indexing, retrieving, and generating insights from technical documentation using production-oriented engineering practices.

---

## Why This Project?

Most RAG tutorials stop at:

- Loading a PDF
- Generating embeddings
- Storing vectors
- Asking questions

Real-world AI systems require much more than that.

Engineering Intelligence Hub is being built to explore:

- Document ingestion pipelines
- Hybrid search (Vector + Keyword)
- Reranking strategies
- Authentication & Authorization
- Evaluation workflows
- Observability & Monitoring
- Scalable software architecture
- Production engineering practices

The goal is not just to build another chatbot, but to understand how enterprise-grade AI systems are designed and implemented.

---

## Current Status

### Phase 0 — Foundation & Infrastructure ✅

Phase 0 established the engineering foundation of the platform and introduced the tooling, infrastructure, and development workflow required for future modules.

#### Completed

##### Project Foundation

- [x] Repository structure
- [x] Modular project layout
- [x] Configuration management
- [x] Development environment setup

##### Application Layer

- [x] FastAPI application bootstrap
- [x] Health check endpoint
- [x] API documentation via Swagger/OpenAPI

##### Database Infrastructure

- [x] PostgreSQL setup using Docker
- [x] pgvector extension enabled
- [x] Local database environment verified

##### Engineering Tooling

- [x] Ruff linting
- [x] MyPy static type checking
- [x] Pytest testing framework
- [x] GitHub Actions CI pipeline
- [x] uv package management

#### Upcoming

##### Phase 1 — Authentication & Users

- [ ] SQLAlchemy Async database layer
- [ ] Alembic migration setup
- [ ] User domain model
- [ ] User repository
- [ ] JWT authentication
- [ ] Authorization framework

##### Future Phases

- [ ] Document Ingestion Module
- [ ] Retrieval Module
- [ ] Generation Module
- [ ] Observability Module
- [ ] Evaluation Framework
- [ ] Production Deployment

---

## Roadmap Progress

| Phase | Status |
|---------|---------|
| Phase 0 — Foundation & Infrastructure | ✅ Complete |
| Phase 1 — Authentication & Users | ⏳ Next |
| Phase 2 — Document Ingestion | ⬜ Planned |
| Phase 3 — Embeddings & Vector Storage | ⬜ Planned |
| Phase 4 — Retrieval Pipeline | ⬜ Planned |
| Phase 5 — Generation Pipeline | ⬜ Planned |
| Phase 6 — Observability & Production Readiness | ⬜ Planned |
---

## High-Level Architecture

```text
                    ┌─────────────────┐
                    │     Client      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     FastAPI     │
                    └────────┬────────┘
                             │
            ┌────────────────┼────────────────┐
            ▼                ▼                ▼

     ┌──────────┐    ┌──────────────┐   ┌──────────┐
     │  Auth    │    │  Retrieval   │   │Generation│
     │  Module  │    │   Module     │   │  Module  │
     └────┬─────┘    └──────┬───────┘   └────┬─────┘
          │                 │                │
          └─────────────────┼────────────────┘
                            ▼

                 ┌───────────────────┐
                 │ Shared Kernel     │
                 └─────────┬─────────┘
                           │
                           ▼

                 ┌───────────────────┐
                 │ PostgreSQL        │
                 │ + pgvector        │
                 └───────────────────┘
```

---

## Project Structure

```text
engineering-intelligence-hub/
│
├── docs/
│   └── adr/
│
├── infra/
│   └── docker/
│
├── migrations/
│
├── observability/
│
├── scripts/
│
├── src/
│   └── eih/
│       ├── auth/
│       ├── ingestion/
│       ├── retrieval/
│       ├── generation/
│       ├── shared_kernel/
│       └── observability/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
├── pyproject.toml
├── .env.example
└── README.md
```

---

## Architecture Principles

This project follows several software engineering principles:

### Modular Monolith

The system is developed as a modular monolith before introducing any distributed complexity.

### Hexagonal Architecture

Business logic remains independent from frameworks, databases, and external services.

### Domain-Driven Design

Modules are organized around business capabilities rather than technical layers.

### API First

All capabilities are exposed through well-defined APIs.

### Observability by Default

Logging, tracing, and monitoring are treated as first-class concerns.

---

## Planned Features

### Authentication

- User registration
- Login & JWT authentication
- Role-based access control

### Document Ingestion

- PDF ingestion
- DOCX ingestion
- Metadata extraction
- Chunking pipeline
- Embedding generation

### Retrieval

- Vector search
- BM25 keyword search
- Hybrid retrieval
- Cross-encoder reranking

### Generation

- Retrieval-Augmented Generation
- Prompt orchestration
- Source attribution

### Observability

- Structured logging
- Distributed tracing
- Metrics collection
- Health monitoring

---

## Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.11+ |
| Backend | FastAPI |
| Validation | Pydantic |
| ORM | SQLAlchemy |
| Database | PostgreSQL |
| Vector Search | pgvector |
| Migrations | Alembic |
| Testing | Pytest |
| Containerization | Docker |
| Observability | OpenTelemetry |
| LLM Integration | OpenAI / Local Models |

---

## Learning Goals

This project serves as a practical exploration of:

- Production-grade RAG systems
- Backend architecture
- AI infrastructure
- System design
- Software engineering best practices
- MLOps foundations
- Observability and monitoring
- Scalable Python applications

---

## Roadmap

The complete implementation roadmap is maintained separately and tracks the evolution of the platform from initial setup to production deployment.

Future milestones include:

- Foundation & Infrastructure
- Authentication & Security
- Knowledge Ingestion
- Hybrid Retrieval
- RAG Generation Pipeline
- Observability & Evaluation
- Deployment & Operations

---

## Disclaimer

This project is primarily a learning-focused engineering initiative intended to explore the architecture, implementation, and operational challenges involved in building modern AI-powered knowledge systems.

While production practices are intentionally followed, the primary objective is understanding *how* such systems are built rather than creating a commercial product.

---

## Author

**Aniruddha More**

GitHub: https://github.com/Aniruddha072

---
