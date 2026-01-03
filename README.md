# Intelligent Cloud Cost Governance

An end-to-end **cloud cost governance system** that correlates **real-time AWS usage metrics** with **billing data** to generate **cost optimization recommendations and future cost forecasts**.

This project demonstrates how cloud resource usage (starting with Amazon EC2) can be analyzed intelligently to identify waste, improve efficiency, and reduce unnecessary cloud spend.

> **Phase-1 Scope:**  
> This implementation is validated using **Amazon EC2**.  
> The architecture is **service-agnostic** and designed to support additional cloud resources (S3, RDS, etc.) in future phases.

---

## 📌 Why This Project Exists (Problem Statement)

In real-world cloud environments, organizations often waste **20–30% of their cloud budget** due to:
- Underutilized compute resources
- Lack of visibility between usage and cost
- Reactive (post-spend) cost analysis
- Limited actionable recommendations

Existing tools mostly show **what was spent**, not **why it was spent** or **what should be done next**.

This project addresses that gap by:
- Collecting **actual usage metrics**
- Mapping them to **actual billing data**
- Generating **governance recommendations**
- Predicting **future costs**
- Presenting everything in a **single dashboard**

---

## 🧠 What This Project Does (High-Level)

1. Monitors real cloud resource usage (CPU, runtime, state)
2. Retrieves real AWS billing data
3. Correlates usage with cost
4. Identifies inefficiencies
5. Generates recommendations
6. Forecasts future cost
7. Displays insights via a web dashboard

---

## 🏗️ System Architecture (Conceptual)

**Placeholder – Add architecture diagram**


## 🚀 Project Workflow (Start to End)

This section explains **how the project was built and executed from start to end**, covering the complete lifecycle from cloud setup to dashboard visualization.

---

### Step 1: Cloud Environment Setup

- An **AWS EC2 instance** was launched to act as the execution environment.
- Secure access was established using **SSH and key-based authentication**.
- A **Linux (Ubuntu)** environment was used to simulate a real-world cloud setup.

---

### Step 2: Environment Preparation

Inside the EC2 instance:

- A **Python virtual environment** was created.
- Required dependencies were installed:
  - `boto3`
  - `pandas`
  - `numpy`
  - `flask`
- **AWS CLI** and **IAM access** were configured securely.

This ensured:
- Dependency isolation
- Secure interaction with AWS APIs
- Reproducibility of the setup

---

### Step 3: Usage Metrics Collection (AWS CloudWatch)

A Python script was developed to:

- Query **AWS CloudWatch**
- Collect EC2 usage metrics such as:
  - CPU utilization
  - Instance state
  - Instance type

**Purpose of this step:**
- Capture real usage data
- Normalize it
- Store it in structured **JSON format**

---

### Step 4: Cost Data Collection (AWS Cost Explorer)

Another Python module retrieves:

- Actual billing data using the **AWS Cost Explorer API**
- Daily cost grouped by service

This ensures:
- Real billing data (not estimates)
- Direct linkage to actual cloud spend

---

### Step 5: Usage–Cost Correlation

The collected usage and cost datasets are:

- Cleaned
- Normalized
- Correlated using timestamps

This creates a **single unified dataset** that answers:

> **“How much did this resource cost based on how it was used?”**

---

### Step 6: Governance Recommendations

Based on predefined logic:

- Underutilized resources are detected
- Recommendations are generated, such as:
  - Stopping unused instances
  - Downsizing instance types

This step transforms **raw data into actionable insights**.

---

### Step 7: Cost Forecasting

Historical cost data is used to:

- Compute average daily cost
- Predict future spend:
  - **30-day forecast**
  - **90-day forecast**

This helps users:
- Anticipate future bills
- Make proactive cost decisions

---

### Step 8: Dashboard Visualization

A **Flask-based web dashboard** was built to:

- Display usage metrics
- Show correlated cost data
- Present governance recommendations
- Visualize cost forecasts

This removes the need to inspect raw data files and provides a **user-friendly interface**.

---

## 🖥️ Dashboard Preview

**Placeholder – Add dashboard screenshot**




