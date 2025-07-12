# 🚗 DRIVER-DROWSINESS

_Keeping Drivers Alert to Save Lives with Smarter Driving!_
---

### 🛠️ Built with the tools and technologies:

<p align="center">
  <img src="https://img.shields.io/badge/-Markdown-000000?logo=markdown&logoColor=white" />
  <img src="https://img.shields.io/badge/-Keras-D00000?logo=keras&logoColor=white" />
  <img src="https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/-TOML-9c4221?logo=toml&logoColor=white" />
  <img src="https://img.shields.io/badge/-TensorFlow-FF6F00?logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/-Rich-yellow?style=flat&logo=python" />
  <img src="https://img.shields.io/badge/-NumPy-013243?logo=numpy" />
  <img src="https://img.shields.io/badge/-XML-blue?logo=xml" />
  <img src="https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/-pandas-150458?logo=pandas" />
</p>

---

## 📑 Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Testing](#testing)
- [Features](#features)
- [Dashboard](#dashboard)
- [Tech Stack](#tech-stack)
- [License](#license)
---

## Overview  
### Driver Drowsiness Detection System  
🛠️ <em>Built with Computer Vision, Deep Learning, and Real-Time Data Visualization</em>

<br>

Fatigue-induced drowsiness is a major contributor to road accidents. This project addresses the issue by building a real-time drowsiness detection and alert system using a custom-built convolutional neural network (CNN) and OpenCV.  

The CNN was designed from scratch with **3 convolutional layers**, **ReLU activations**, **max pooling**, and **2 fully connected layers**, optimized for binary eye-state classification (open vs. closed).  

Trained entirely on webcam-collected grayscale images, the model achieved **99.6% training accuracy** and **98.9% validation accuracy**, despite the constrained dataset — showcasing effective preprocessing and generalization.  

The system monitors eye state in real time via webcam, triggers audible alerts on prolonged closure, and logs drowsiness intervals for behavioral insights. A post-session **Streamlit dashboard** visualizes trends such as event frequency, duration, and timestamps.

This project demonstrates well-rounded proficiency across deep learning, real-time computer vision, offline deployment, and interactive analytics.

---
## Getting Started

Follow these steps to run the drowsiness detection system locally.

### Prerequisites

📦 Make sure you have the following installed:

- Python 3.9+
- [pip](https://pip.pypa.io/en/stable/)
- A working webcam
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (recommended)

> ✅ This project is tested on macOS. Works offline, CPU-only.

---

### Installation

 ⚙️  Clone the repository and set up the virtual environment:

<pre>  git clone https://github.com/RajnandiniSen/driver-drowsiness.git 
  cd driver-drowsiness 
  python3 -m venv .venv 
  source .venv/bin/activate # On Windows use: .venv\Scripts\activate</pre>

Install required packages:

<pre> pip install -r requirements.txt</pre>

### Usage

1. Run Detection System 🔎
   
Launch the real-time drowsiness detector:

<pre> python driver_drowsiness.py </pre>

This opens the webcam and begins scanning your eyes for signs of fatigue. When both eyes are detected as closed for a sustained period, a sound alert is triggered, and a log entry is saved.

2. Run Dashboard 📈
   
After a session, launch the analytics dashboard:

<pre> streamlit run dashboard.py </pre>

This provides metrics like:

- Number of drowsy episodes
- Average duration
- Timeline of events

### Testing

📋 To simulate drowsiness, keep your eyes closed for a few seconds while the camera runs. 

Check:
 
- Whether the alert sounds
- Whether the log file (session_log.csv) records the start and end time
- Whether the Streamlit dashboard updates accurately

> _Tested in varying light conditions with webcam. Current limitation: accuracy drops in low-light or occluded frames — potential future enhancement with IR support or multimodal inputs (e.g., head tilt, blink duration)._
---

## Features

### 🧠 Real-Time Eye State Classification (Computer Vision + Deep Learning)
- Captures live webcam frames and detects eye regions using **Haar Cascade classifiers**.
- Uses Haar Cascade for **initial eye region detection**, followed by **CNN-based classification** for improved accuracy and robustness.
- **CNN trained from scratch** on webcam-captured images, achieving **~99.6% training accuracy** and **~98.9% validation accuracy**.

### ⏱️ Intelligent Drowsiness Scoring System
- Implements a **score-based alert logic** that **increments when both eyes are closed** and **decrements when open**.
- **Score halts when eyes are closed continuously**, and only **starts decreasing once eyes reopen**, reducing false positives.
- Designed to trigger alerts **only after persistent drowsiness**, mimicking real-world reaction thresholds.

### 🔊 Audio Alert Mechanism
- Plays a **warning alarm (alarm.wav)** when score threshold is crossed.
- **Intelligent audio logic** avoids constant buzzing and **delays shutoff** for a few seconds after recovery, simulating a real-world alert.

### 📊 Session Logging (Behavioral Analytics)
- Every drowsy episode is **logged with a timestamp** in a structured format:
  - Drowsiness Starts
  - Drowsiness Ends
- **Logs are saved in CSV format** (session_log.csv) for reuse in analytics or reports.

### 📉 Streamlit-Powered Real-Time Dashboard
- **Clean, interactive dashboard built using Streamlit**.
- Displays real-time metrics:
  - **Total number of drowsy events**
  - **Average time between drowsy onsets**
  - **Average duration of each drowsiness event**
- **Line chart visualizes temporal patterns** of fatigue over session time.

### 🔍 Explainable Workflow & Modular Code Design
- **Modular file structure**:
  - capture_dataset.py – Image collection
  - train_model.py – CNN training
  - driver_drowsiness.py – Real-time detection + event logging
  - dashboard.py – Visualization
- **Easy retraining, tuning, and feature extension** (e.g., yawn detection, head pose analysis).

### 💡 Developer-Friendly & Edge-Ready
- **Runs on CPU**, no GPU/cloud needed — tested on local hardware.
- **Fully local and offline capable**, making it suitable for **edge deployment or embedded systems**.
- Uses **Python virtual environment (.venv)** and a clean .gitignore for **reproducibility and GitHub hygiene**.
---

## Dashboard

The system includes a **real-time Streamlit dashboard** designed for interpretability, analytics, and user feedback. Rather than just triggering alerts, it helps understand **behavioral patterns** of driver drowsiness over time.

### ✅ What It Shows
- **🧠 Drowsy Event Counter**: Real-time tally of how many times drowsiness was detected (Drowsiness Starts events).
- **⏱ Average Time Between Drowsy Events**: Measures how frequently fatigue episodes occur, helping estimate driver recovery and alertness windows.
- **📈 Average Duration of Drowsy Events**: Tracks how long each drowsy episode lasts on average, which is crucial for risk analysis.
- **📊 Line Chart**: A dynamic line chart plotting **drowsy event occurrences per minute**, revealing fatigue density and potential clustering patterns.
- **📄 Tabular Log**: Chronological event log (Start, End) with timestamps for transparency and traceability.

### 🧠 Why It Matters
- Adds a **data analysis layer** to a real-time CV system, aligning with expectations for ML Engineers and Data Analysts.
- Simulates **production-grade system monitoring**, enabling insights beyond binary classification (open vs. closed eyes).
- Enables **post-session review**, making the tool useful not only for live alerting but also for driver wellness tracking, fleet analytics, and future research.

### ⚙️ Tech Stack
- Built using **Streamlit** for rapid, interactive prototyping.
- Reads from **CSV logs** (session_log.csv) that are dynamically updated during each session.
- Automatically processes time-series logs to extract trends, durations, and frequencies.

> 💡 _Modular design allows future upgrade to cloud dashboards (e.g., via Grafana, Dash, or Power BI) if needed._
---

## Tech Stack

This project showcases a full-stack integration of **AI, Computer Vision, and Data Visualization** — demonstrating how raw model predictions can evolve into real-time, interpretable systems deployable in practical environments.

---

### 🧠 Machine Learning & Deep Learning

- **TensorFlow + Keras**  
  Used to design and train a custom Convolutional Neural Network (CNN) for binary eye-state classification (open vs. closed).  
  Model saved and deployed using .h5 format for real-time inference in local environments.  
  Achieved **~99.6% training accuracy** and **~98.9% validation accuracy** on webcam-captured grayscale images.

- **CNN Architecture**  
  Built from scratch with:
  - 3 **Convolutional Layers** using **ReLU** activations  
  - **Max Pooling** layers after each convolution block  
  - **Flatten Layer** → 2 **Fully Connected Dense Layers**  
  - Final **Softmax Output Layer** for binary classification  
  Optimized for **low-latency webcam inference (~28 FPS on CPU)**.

---

### 👁️ Computer Vision

- **OpenCV**  
  Handles live webcam streaming, grayscale conversion, and real-time pre-processing.  
  Also used for bounding box overlays and live status rendering (e.g., “Open”, “Closed”, “DROWSY!”).

- **Haar Cascade Classifiers**  
  Lightweight method for detecting face and eyes.  
  **Hybrid system**: Haar used for region-of-interest localization → CNN handles classification, reducing false positives.

---

### 🔊 Audio Alert System

- **Pygame Mixer**  
  Enables real-time **sound-based warnings** using alarm.wav.  
  Smart alarm logic prevents constant buzzing and includes brief post-recovery delay to mimic real-world safety behavior.

---

### 📈 Data Engineering & Logging

- **CSV Logging (datetime + csv)**  
  Logs each **Drowsiness Start** and **Drowsiness End** with timestamps to session_log.csv.  
  Creates a persistent, structured behavioral trace for analysis.

- **Pandas**  
  Used for reading logs, **time-delta calculations**, and **KPI aggregation** (e.g., average event duration, frequency).  
  Enables structured analytics for dashboard rendering.

---

### 📊 Dashboarding & Visualization

- **Streamlit**  
  Built a clean, interactive real-time **dashboard** to visualize fatigue metrics.  
  Displays dynamic KPIs:
  - Total number of drowsy episodes  
  - Average duration of each drowsiness interval  
  - Average time between drowsy events  

- **Matplotlib**  
  Renders **time-indexed line plots** directly in Streamlit — shows **drowsy event occurrences per minute**, revealing fatigue density and clustering patterns across the session.

---

### 💻 Deployment & Dev Tools

- **Python 3.11**  
  Core runtime powering the ML model, computer vision processing, audio interface, and dashboard logic.

- **Virtual Environment (venv)**  
  Containerizes all dependencies for reproducible, environment-specific development.

- **.gitignore + GitHub Hygiene**  
  Excludes .venv, model files, logs, and temporary data for a clean, production-ready repository.

- **Modular Script Design**  
  Codebase is structured into reusable modules:
  - capture_dataset.py – For image collection  
  - train_model.py – CNN model definition and training  
  - driver_drowsiness.py – Real-time detection and logging  
  - dashboard.py – Streamlit visualization interface  

---

> ⚙️ Entire pipeline is optimized for **offline, CPU-only execution** making the system ideal for safety-critical edge deployments, in-vehicle systems, or portable driver monitoring units.
---

## License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute this code for personal, academic, or commercial purposes, with proper attribution.

> See the [LICENSE](LICENSE) file for full license details.

MIT License

Copyright (c) 2025 Rajnandini Sen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
