# 🦅 LogHawk

**SOC-style security monitoring for a cloud-hosted application**

---

## 🔍 Overview

LogHawk is a cloud security project that simulates how a Security Operations Center (SOC) detects and analyzes brute-force authentication attacks against an internet-exposed application.

A lightweight web application is deployed on an AWS EC2 instance and monitored using log-based, threshold-driven detection logic. When abnormal authentication behavior is identified, alerts are generated to mimic SIEM-style security workflows in a cloud environment.

---

## ☁️ Architecture (High-Level)

- Cloud-hosted application running on **AWS EC2 (Ubuntu Linux)**
- Public-facing login endpoint exposed to the internet
- Authentication events logged on the server
- Bash-based detection logic for brute-force activity
- Alert generation for SOC analyst review

---

## 🛠️ Technology Stack

- **Cloud Provider:** Amazon Web Services (AWS)
- **Compute:** EC2
- **Operating System:** Ubuntu Linux
- **Web Application:** Python Flask
- **Scripting:** Bash
- **Logs:** Application authentication logs
- **Monitoring Style:** SIEM-inspired, rule-based detection

---

## 🔐 Security Focus

LogHawk focuses on **cloud workload security** and **SOC analyst workflows**, including:

- Awareness of public cloud exposure and attack surface
- Secure administrative access using SSH
- Authentication log monitoring
- Threshold-based brute-force detection
- Alert validation and incident analysis

---

## 🚨 Detection & Alerting

- Authentication activity is logged to `auth.log`
- A Bash script analyzes recent login attempts
- Abnormal behavior exceeding a defined threshold triggers an alert
- Alerts are written to `alerts.log` for analyst investigation

This approach demonstrates **SIEM-style detection logic** without relying on enterprise SIEM tooling.

---

## 🧠 SOC Workflow

1. Monitor authentication logs  
2. Detect abnormal login behavior  
3. Generate alerts  
4. Validate activity through log analysis  
5. Classify the incident and recommend mitigation  

This workflow mirrors real-world SOC operations at a simplified scale.

---

## 🛡️ Cloud Security Controls

- **AWS Security Groups** for network-level access control
- Restricted ports for application and administrative access
- Secure SSH-based server administration
- Continuous monitoring of authentication activity on a public cloud server

---

## 📂 Repository Structure

