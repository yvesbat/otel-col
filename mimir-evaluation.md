# Grafana Mimir Feature Evaluation Template

---

## 1. Scalability & Performance

**Sharding and Replication Behavior**  
- Describe how you deployed Mimir with multiple shards and replicas.
- Summarize your experience with data distribution across shards.
- Note any observations about system behavior under load and during failover scenarios (e.g., what happens when a node is taken offline).

**Notes:**  
[Document any relevant findings, challenges, or positive aspects.]

---

## 2. Multi-Tenancy

**Tenant Isolation (Data, Queries, Resource Limits)**  
- Explain how you created multiple tenants.
- Describe how data, queries, and resource usage were isolated between tenants.
- Mention any issues or successes with tenant separation.

**Tenant Management (Creation, Deletion, Quotas)**  
- Outline the process for creating and deleting tenants.
- Discuss how quotas were set and enforced.
- Note any difficulties or smooth experiences with tenant management.

**Authentication and Authorization per Tenant**  
- Describe the authentication methods you configured (e.g., basic auth, OAuth).
- Summarize your experience with access controls and permissions for different tenants.

**Notes:**  
[Include any additional insights or noteworthy points.]

---

## 3. Data Storage & Retention

**Compaction and Data Lifecycle Management**  
- Describe how you observed the compaction process.
- Explain how you tested data retention policies and what the outcomes were.
- Note whether data was deleted or archived as expected.

**Notes:**  
[Add any further observations or comments.]

---

## 4. Security

**Authentication (Basic Auth, OAuth, etc.)**  
- Explain which authentication methods you enabled and tested.
- Summarize your experience with setup and usage.

**TLS Encryption (In-Transit, At-Rest)**  
- Describe the process of enabling TLS for data in transit and at rest.
- Note any challenges or successes in establishing secure connections.

**Notes:**  
[Include any security-related findings or remarks.]

---

## 5. Optional/Advanced Features

**Downsampling and Data Compaction**  
- Describe how you enabled and tested downsampling.
- Summarize the impact on data storage and query performance.

**Global Query Federation (Across Clusters)**  
- Explain how you set up multiple clusters and tested cross-cluster queries.
- Note any observations about data accessibility and query results.

**Support for Exemplars and Tracing Data**  
- Describe the process of ingesting exemplars and tracing data.
- Summarize your experience querying and visualizing this data in Grafana.

**Notes:**  
[Add any additional comments or findings.]

---

## Summary & Recommendations

**Summary:**  
- Provide an overall summary of your evaluation experience.
- Highlight the most significant strengths and any limitations you encountered.

**Recommendations/Next Steps:**  
- Suggest improvements, further areas to investigate, or actions to take based on your findings. 
