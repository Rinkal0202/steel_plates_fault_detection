# Steel Plates Fault Detection 🚧🔍

This project aims to automate the quality control process in the steel manufacturing industry by using machine learning to **detect
and classify faults in steel plates before dispatch**. Built using **XGBoost**, synthetic data, and deployed via **Streamlit**, this 
model helps prevent the shipment of defective products with high accuracy and speed.

## 🔗 Project Link
➡️ [GitHub Repository](https://github.com/Rinkal0202/steel_plates_fault_detection)

---

## 📌 Table of Contents
- Overview
- Objectives
- Methodology
- Technology Stack
- Installation
- Usage
- Future Work
- Contributors

---

## 🧠 Overview

The project uses **sensor-based synthetic data** to simulate real-world fault scenarios and classifies steel plates as **"Pass"** or **"Fail"** using machine learning. 
An interactive interface built with Streamlit allows real-time prediction and visualization of results.

---

## 🎯 Objectives

**Primary Objective:**
- Build a fault classification model to ensure steel quality control.

**Secondary Objectives:**
- Generate and balance synthetic data.
- Develop an interactive web app using Streamlit.

**Measurable Goals:**
- ✅ Accuracy > 90%
- ✅ Recall (for faults) > 85%
- ✅ Balanced F1-score

---

## ⚙️ Methodology

### 📁 Phase 1: Data Generation & Preprocessing
- Synthetic sensor data using NumPy
- Scaling and balancing to address class imbalance

### 📊 Phase 2: Model Training & Deployment
- XGBoost 
- Evaluation using precision, recall, accuracy, F1-score
- Streamlit app for interactive predictions

---

## 🧰 Technology Stack

| Category         | Tools Used                           |
|------------------|--------------------------------------|
| Languages        | Python                               |
| ML Frameworks    | Scikit-learn, XGBoost                |
| Data Handling    | Pandas, NumPy, CSV                   |
| Deployment       | Streamlit, GitHub                    |

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/Rinkal0202/steel_plates_fault_detection.git
cd steel_plates_fault_detection
```
```bash
# Install dependencies
pip install pandas scikit-learn xgboost joblib streamlit
```
```bash
# Run the Streamlit app
streamlit run app1.py
```
---

## 🚀 Usage
Launch the Streamlit app

Input steel plate sensor values

Get instant prediction: Pass ✅ or Fail ❌

---

## 🔮 Future Work
Incorporate real-world fault data

Integrate computer vision for image-based fault detection

Optimize app for real-time factory use

Improve synthetic data generation techniques

---

## 👥 Contributors
Rinkal Narsinghani 

Bhadoriya Khushi

