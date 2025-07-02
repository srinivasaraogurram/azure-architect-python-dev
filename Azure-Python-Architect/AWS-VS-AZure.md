Here is a table mapping the AWS services you use to their corresponding Azure services:  

| **AWS Service**       | **Azure Service**                          | **Description**                                                                 |
|-----------------------|-------------------------------------------|---------------------------------------------------------------------------------|
| **API Gateway**       | **Azure API Management**                  | Managed API gateway for publishing, securing, and analyzing APIs.              |
| **IAM**               | **Azure Active Directory (Azure AD) + RBAC** | Identity and access management with role-based access control.                 |
| **SNS**               | **Azure Event Grid** / **Azure Service Bus** | Pub/sub messaging (Event Grid) or advanced messaging (Service Bus).            |
| **SES**               | **Azure Communication Services Email** / **SendGrid** | Email sending services (SendGrid is now part of Azure).                       |
| **SQS**               | **Azure Queue Storage** / **Azure Service Bus** | Simple queuing (Queue Storage) or advanced messaging (Service Bus).            |
| **Event Bridge**      | **Azure Event Grid**                      | Event-driven automation and integration.                                        |
| **Kafka** (Managed)   | **Azure Event Hubs (Kafka-enabled)**      | Managed Kafka service for real-time data streaming.                            |
| **Lambda**            | **Azure Functions**                       | Serverless compute for event-driven applications.                              |
| **Step Functions**    | **Azure Logic Apps** / **Azure Durable Functions** | Workflow orchestration (Logic Apps) or stateful serverless workflows (Durable Functions). |
| **AWS Glue**          | **Azure Data Factory**                    | ETL (Extract, Transform, Load) and data integration service.                   |
| **Athena**            | **Azure Synapse Analytics (Serverless SQL Pool)** | Serverless querying over data in storage (Blob, ADLS).                         |
| **DynamoDB**          | **Azure Cosmos DB (Table API or NoSQL API)** | NoSQL database with low latency and global distribution.                       |
| **MongoDB**           | **Azure Cosmos DB (MongoDB API)**         | Fully managed MongoDB-compatible database.                                      |
| **PostgreSQL**        | **Azure Database for PostgreSQL**         | Managed PostgreSQL relational database.                                        |
| **Parameter Store**   | **Azure App Configuration** / **Azure Key Vault** | App settings (App Config) or secrets management (Key Vault).                   |
| **Secrets Manager**   | **Azure Key Vault**                       | Centralized secrets and certificate management.                                 |
| **Route 53**          | **Azure DNS**                             | Managed DNS service for domain name resolution.                                 |
| **EKS**               | **Azure Kubernetes Service (AKS)**        | Managed Kubernetes container orchestration service.                             |
| **S3**                | **Azure Blob Storage**                    | Object storage for unstructured data.                                           |

### Notes:
- **For Event-Driven Services**:  
  - **AWS SNS → Azure Event Grid** (for lightweight pub/sub) or **Azure Service Bus** (for advanced messaging).  
  - **AWS SQS → Azure Queue Storage** (basic queues) or **Service Bus** (premium features).  

- **For Serverless Compute**:  
  - **AWS Lambda → Azure Functions** (similar event-driven compute).  

- **For Managed Databases**:  
  - **AWS DynamoDB → Azure Cosmos DB** (supports multiple APIs including NoSQL and Table API).  
  - **AWS RDS (PostgreSQL) → Azure Database for PostgreSQL**.  

- **For ETL & Data Processing**:  
  - **AWS Glue → Azure Data Factory** (with mapping data flows).  
  - **AWS Athena → Azure Synapse Serverless SQL Pool** (query data in storage).  

Would you like a deeper comparison on any specific service?