# ADR-002: PostgreSQL + pgvector as Primary Vector Store

## Status

Accepted

## Date

2026-07-17

---

## Context

Engineering Intelligence Hub (EIH) requires a vector storage solution to support semantic search and Retrieval-Augmented Generation (RAG) workflows.

The platform needs to:

- Store document metadata
- Store document chunks
- Store vector embeddings
- Support similarity search
- Support hybrid retrieval strategies
- Maintain operational simplicity
- Remain cost-effective for local development

Several vector storage options were considered:

- PostgreSQL + pgvector
- ChromaDB
- FAISS
- Pinecone
- Weaviate
- Qdrant

---

## Decision

Engineering Intelligence Hub will use PostgreSQL with the pgvector extension as the primary vector storage solution.

All application data, including:

- Users
- Documents
- Chunks
- Metadata
- Embeddings

will be stored within PostgreSQL whenever practical.

Vector similarity search will be implemented using pgvector indexes and PostgreSQL query capabilities.

---

## Rationale

### Unified Storage

Using PostgreSQL allows both relational data and vector data to coexist within a single database.

This avoids maintaining separate systems for:

- Application data
- Metadata
- Embeddings

and simplifies development and operations.

### Operational Simplicity

The platform already requires PostgreSQL for core application functionality.

Adding pgvector introduces vector search capabilities without introducing additional infrastructure.

### Local Development Experience

PostgreSQL and pgvector can be run locally using Docker with minimal setup.

This supports rapid experimentation and reproducible development environments.

### Industry Adoption

PostgreSQL is widely adopted, well-documented, and trusted in production environments.

pgvector has become a common choice for production RAG systems that do not require dedicated vector database infrastructure.

### Future Hybrid Retrieval

PostgreSQL supports combining:

- Structured filtering
- Metadata filtering
- Keyword search
- Vector similarity search

which aligns with the long-term retrieval strategy of EIH.

---

## Consequences

### Positive

- Single database system
- Simplified deployment
- Reduced operational complexity
- Lower infrastructure costs
- Easier backups and maintenance
- Strong support for hybrid retrieval approaches

### Negative

- Not specialized exclusively for vector workloads
- May require optimization at larger scales
- Dedicated vector databases may outperform pgvector for extremely large datasets

---

## Alternatives Considered

### ChromaDB

Rejected because:

- Additional infrastructure
- Less mature operational ecosystem
- Separate storage system from application database

### FAISS

Rejected because:

- Primarily a vector indexing library rather than a complete database
- Requires additional persistence and metadata management layers

### Pinecone

Rejected because:

- External managed service
- Additional cost
- Vendor dependency
- Less suitable for learning underlying infrastructure concepts

### Weaviate

Rejected because:

- Additional operational complexity
- Separate infrastructure requirement

### Qdrant

Rejected because:

- Additional service to manage
- Unnecessary complexity for the current project scope

---

## Notes

The vector storage layer should be abstracted behind retrieval interfaces wherever practical.

This preserves the ability to migrate to a dedicated vector database in the future if scaling requirements justify the change.