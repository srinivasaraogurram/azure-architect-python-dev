Sure! Here's the **updated and complete mapping table** including the **databases**: **DynamoDB**, **MongoDB**, and **PostgreSQL**, along with their **Azure equivalents**.

---

### ✅ AWS vs Azure Services Mapping (By Classification) – With Database Support

| **Classification**             | **AWS Service(s)**                              | **Azure Equivalent(s)**                                 |
|-------------------------------|--------------------------------------------------|----------------------------------------------------------|
| **API**                       | API Gateway                                      | Azure API Management                                     |
| **Function**                  | Lambda                                           | Azure Functions                                            |
| **Messaging**                 | SNS, SQS, SES, EventBridge, Kafka (MSK)          | Event Grid, Queue Storage / Service Bus, SendGrid, Event Hubs, Confluent for Azure |
| **Function Orchestration**    | Step Functions                                   | Azure Durable Functions                                  |
| **Infrastructure as Code (IaC)** | CloudFormation, AWS CDK                          | ARM Templates, Bicep, Azure SDKs                         |
| **Keys / Secrets / Parameters** | Parameter Store, Secrets Manager                | Azure Key Vault, Azure App Configuration                 |
| **Containerization**          | EKS, Fargate, EC2, ECR                           | AKS, ACI, Virtual Machines, Azure Container Registry     |
| **Routing**                   | Route 53                                         | Azure DNS                                                |
| **Authentication & Authorization** | IAM, Cognito                                | Azure Active Directory (AAD), Azure AD B2C               |
| **App Deployment**            | Elastic Beanstalk                                | Azure App Services                                       |
| **CI/CD**                     | CodeCommit, CodeBuild, CodeDeploy                | Azure Repos, Azure Pipelines                             |
| **Storage**                   | S3                                               | Azure Blob Storage                                       |
| **Storage Reporting**         | Athena                                           | Azure Synapse Analytics                                  |
| **ELT / ETL**                 | Glue                                             | Azure Data Factory                                       |
| **Monitoring**                | CloudWatch, CloudTrail, X-Ray                    | Azure Monitor, Application Insights, Activity Logs       |
| **NoSQL Database**            | DynamoDB                                         | **Azure Cosmos DB** (supports NoSQL, MongoDB API)        |
| **Document / NoSQL Database** | MongoDB                                          | **Azure Cosmos DB** (with MongoDB API compatibility)     |
| **Relational Database**       | PostgreSQL                                       | **Azure Database for PostgreSQL**                        |

---

## 🔍 Detailed Breakdown of Databases

### 1. **Amazon DynamoDB → Azure Cosmos DB**
- **DynamoDB**: Fully managed NoSQL database (key-value & document).
- **Azure Equivalent**: **Cosmos DB** (supports NoSQL/document model and offers low-latency global distribution, auto-scaling, etc.)

> Cosmos DB also supports APIs like MongoDB, Cassandra, Gremlin (Graph), and Table (similar to DynamoDB).

---

### 2. **MongoDB → Azure Cosmos DB (MongoDB API)**
- **MongoDB**: Popular open-source NoSQL document database.
- **Azure Equivalent**: **Azure Cosmos DB using MongoDB API**
- You can migrate MongoDB apps directly to Azure Cosmos DB without code changes thanks to API compatibility.

---

### 3. **PostgreSQL → Azure Database for PostgreSQL**
- **PostgreSQL**: Open-source relational database with advanced features.
- **Azure Equivalent**: **Azure Database for PostgreSQL**
  - Available in two deployment options:
    - **Single Server** (simpler, cost-effective)
    - **Flexible Server** (more control, better performance)

> Also consider **Azure SQL Database** if you're using a fully managed Microsoft SQL variant.

---

## 📄 Summary Table: Database Services

| **Database Type**      | **AWS Service**      | **Azure Equivalent**                          |
|------------------------|----------------------|-----------------------------------------------|
| NoSQL (Key-Value)      | DynamoDB             | **Azure Cosmos DB (Core API)**                |
| Document / NoSQL       | MongoDB              | **Azure Cosmos DB (MongoDB API)**             |
| Relational (PostgreSQL)| Amazon RDS for PostgreSQL | **Azure Database for PostgreSQL**       |

---

If you'd like a downloadable version (Excel or CSV format), or want to include GCP equivalents too, just let me know!