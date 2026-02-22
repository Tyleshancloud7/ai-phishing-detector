# AI-Powered Phishing Detection Tool

## Project Overview
This project is an AI-powered phishing detection tool developed in Python. It leverages behavioral pattern recognition and risk scoring to identify suspicious email activity, addressing the growing sophistication of AI-generated phishing emails. Traditional signature-based approaches are increasingly ineffective, so this tool integrates human oversight to ensure high detection accuracy while reducing false positives.

---

## Business Problem
Phishing attacks have evolved with AI, making them increasingly difficult to detect using traditional methods. According to KnowBe4’s latest report, over 82% of phishing emails now contain AI-generated content. Organizations need solutions that combine **automation, behavioral analysis, and human verification** to stay ahead of these threats.

---

## Solution
This project provides a **hands-on solution** for detecting potentially malicious emails:

1. **Behavioral Pattern Recognition**: The tool analyzes email metadata, sender behavior, and content patterns to identify anomalies.  
2. **Risk Scoring**: Each email is assigned a risk score based on suspicious indicators (e.g., unusual sender, unexpected attachments, or AI-generated phrasing).  
3. **Decision Tree / AI Logic**: Events are categorized as LOW, MEDIUM, or HIGH risk.  
4. **Human-in-the-Loop Verification**: High-risk emails are flagged for analyst review before action is taken.  
5. **Feedback Loop**: Analyst verification updates the model over time to improve accuracy.

---

## Key Features
- Detects AI-generated phishing emails
- Assigns dynamic risk scores
- Integrates human oversight
- Easy-to-extend Python codebase
- Logs flagged events for reporting and analysis

---

## Sample Data
A CSV of simulated email login activity is included to demonstrate the tool’s functionality:

| Email_ID | Sender | Subject | Received_Time | Location | Risk_Score |
|----------|--------|--------|---------------|---------|------------|
| 001      | spoof@bank.com | Urgent: Verify Account | 2026-02-15 09:15 | NY, USA | HIGH |
| 002      | hr@company.com | Policy Update | 2026-02-15 11:00 | NY, USA | LOW |

---

## Technologies Used
- Python 3.x  
- pandas (for data handling)  
- numpy (for calculations)  
- decision tree logic (rule-based AI model)  
- matplotlib / seaborn (optional visualization)

---

## How to Run
1. Clone the repository:  
```bash
git clone https://github.com/tyleshancloud7/ai-phishing-detection.git
