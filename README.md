🦅 LogHawk

Cloud-hosted application security monitoring with SOC-style log analysis and brute-force detection

📌 Overview

LogHawk is a cloud security monitoring project designed to simulate how a Security Operations Center (SOC) detects and analyzes brute-force authentication attacks against an internet-exposed application.

The project deploys a web application on an AWS EC2 instance and monitors authentication activity through log analysis. Using threshold-based detection logic, LogHawk identifies abnormal login behavior and generates alerts, mimicking SIEM-style security workflows in a cloud environment.

The primary focus of this project is cloud workload security, log-based detection, and SOC analyst workflows, rather than application development.

☁️ Cloud Environment

Cloud Provider: Amazon Web Services (AWS)

Compute Service: EC2

Operating System: Ubuntu Linux

The application is hosted on an AWS EC2 instance with a public IP address, making it accessible over the internet. This exposure reflects real-world cloud environments and introduces common security risks such as unauthorized access and brute-force attacks.

Network access is controlled using AWS Security Groups, allowing only required ports for administration and application access.

🔐 Secure Server Access (SSH)

Secure Shell (SSH) is used for encrypted remote administration of the EC2 instance.

Security considerations include:

Key-based authentication for secure access

Restricted network access via security group rules

Monitoring of authentication activity to detect suspicious behavior

SSH security is critical in cloud environments because compromised administrative access can lead to full server takeover.

🌐 Web Application

Framework: Python Flask

A lightweight Flask-based web application provides a login interface exposed to the internet. The application is intentionally simple and serves as a controlled workload for generating authentication events rather than as a production system.

The application runs on the EC2 instance and is accessible through the instance’s public IP and designated application port.

📝 Authentication Logging

Authentication logging is implemented within the application to record login attempts.

Each log entry includes:

Username

Source IP address

Timestamp

Authentication result

These logs are stored in an application authentication log file (auth.log) on the EC2 instance and act as the primary data source for security monitoring.

🔍 Log Monitoring

Authentication logs are monitored in real time to observe login activity as it occurs. This simulates the monitoring process performed by SOC analysts, where raw logs are continuously reviewed for signs of malicious behavior.

Real-time monitoring provides visibility into:

Normal user behavior

Repeated failed login attempts

Abnormal authentication patterns

🚨 Brute-Force Detection Logic

LogHawk implements a threshold-based detection mechanism using a Bash script.

Detection logic includes:

Parsing recent authentication log entries

Counting login attempts within a defined scope

Comparing activity against a predefined threshold

When login activity exceeds expected behavior, the system classifies it as a potential brute-force attack and generates an alert.

This approach simulates how SIEM platforms apply correlation rules to raw log data without relying on enterprise-scale tooling.

⚠️ Alert Generation

When the detection threshold is exceeded, an alert is generated and written to an alert log file (alerts.log).

These alerts represent security events that require analyst attention and simulate SIEM-style alerting in a simplified, transparent manner.

🧠 SOC Analysis & Incident Workflow

After an alert is generated, the SOC analyst performs the following steps:

Review authentication logs associated with the alert

Validate repeated login attempts and source IP behavior

Assess the severity of the activity

Classify the incident as a brute-force attack attempt

This workflow reflects real-world SOC analysis practices, where alerts are validated through log correlation and investigation.

🛡️ Response & Mitigation Strategy

Recommended response actions include:

Blocking or rate-limiting the attacker IP address

Strengthening authentication controls

Reviewing SSH access policies

Continued monitoring for repeated attack patterns

These actions represent standard incident response measures used in cloud security environments.

🔧 Technology Stack

Cloud: AWS EC2

OS: Ubuntu Linux

Web Framework: Flask

Scripting: Bash

Logging: Application authentication logs

Monitoring Style: SIEM-inspired log analysis

📚 Key Learnings

Understanding cloud workload exposure and security risks

Monitoring authentication activity through log analysis

Designing threshold-based detection logic

Simulating SOC-style alerting and investigation workflows

Applying cloud-native security controls

🚀 Future Enhancements

Potential future improvements include:

Per-IP and time-window–based detection rules

Automated attacker IP blocking

Centralized log aggregation

Integration with full-scale SIEM platforms

SOC dashboards for alert visualization

👥 Collaboration

This project is developed collaboratively, with responsibilities divided between:

Cloud infrastructure and application setup

Security monitoring, detection logic, and SOC analysis
