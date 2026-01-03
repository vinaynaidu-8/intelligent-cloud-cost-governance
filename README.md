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

## 🏗️ System Architecture (Conceptual)

<img width="1536" height="1024" alt="artchitecture flow" src="https://github.com/user-attachments/assets/a499151f-39db-4170-88a1-475885b5eebb" />

---

## 🚀 Project Workflow (Start to End)

This section explains **how the project was built and executed from start to end**, covering the complete lifecycle from cloud setup to dashboard visualization.

---

### Step 1: Cloud Environment Setup

- An **AWS EC2 instance** was launched to act as the execution environment.
- Secure access was established using **SSH and key-based authentication**.
- A **Linux (Ubuntu)** environment was used to simulate a real-world cloud setup.

<img width="1919" height="1009" alt="EC2 instance" src="https://github.com/user-attachments/assets/001c45ce-425f-4a53-a7cc-0c238db3117f" />


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

<img width="1919" height="1016" alt="cloudwatch metrics" src="https://github.com/user-attachments/assets/0b63b6ad-014a-4d2c-aad6-75b2d4c8b142" />


---

### Step 4: Cost Data Collection (AWS Cost Explorer)

Another Python module retrieves:

- Actual billing data using the **AWS Cost Explorer API**
- Daily cost grouped by service

This ensures:
- Real billing data (not estimates)
- Direct linkage to actual cloud spend

<img width="1919" height="1019" alt="cost explorer" src="https://github.com/user-attachments/assets/3cba20fc-d614-474c-8bef-10aca9bedb12" />

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

<img width="1915" height="1018" alt="dashboard" src="https://github.com/user-attachments/assets/4a2a86db-ed85-4127-b907-30ac6dfdc068" />


## ⚙️ Technology Stack

- **Cloud Platform**: AWS (EC2, CloudWatch, Cost Explorer)
- **Backend**: Python, Boto3
- **Data Processing**: Pandas, NumPy
- **Web Framework**: Flask
- **Operating System**: Linux (Ubuntu)
- **Version Control**: Git & GitHub

## 📌 Phase-1 Scope Summary

- Focused on **Amazon EC2**
- Single AWS account
- Rule-based governance logic
- Manual recommendation execution
- Historical-data-based forecasting


## 🔮 Future Enhancements (Phase-2)

- Support for additional AWS services (S3, RDS, VPC)
- Multi-resource dashboard filters
- Advanced ML-based cost forecasting
- Automated governance actions
- Organization-level (multi-account) support








