# 🚆 Smart Railway Resource Planning Dashboard

## 📌 Overview
Railway systems manage thousands of trains, platforms, and tracks daily. Manual scheduling and resource planning often lead to inefficient platform usage, train delays, and operational conflicts.

This project presents a Smart Railway Resource Planning System that uses Machine Learning and Data Analytics to analyze train schedules, predict delays, and visualize railway resource usage through an interactive Streamlit dashboard.

The system helps simulate how railway authorities can optimize resource allocation and improve operational efficiency.

This project was developed as part of the Tekworks Innovation Arena Hackathon.

---

## 🎯 Problem Statement
Railways transport millions of passengers every day. However, planning train arrivals, departures, platform allocation, and track usage is complex.

Manual planning can lead to:
- Platform conflicts
- Inefficient track utilization
- Increased train delays
- Poor passenger experience

The goal of this project is to build a data-driven solution to improve railway resource planning.

---

## 💡 Solution
The Smart Railway Resource Planning system provides:

- 📊 Data visualization of railway operations
- ⏱ Train delay prediction using Machine Learning
- 🚉 Platform and track usage analysis
- 📈 Passenger traffic insights
- 🖥 Interactive analytics dashboard using Streamlit

The system uses synthetic railway data to simulate real-world railway operations.

---

## ⚙️ Tech Stack

### Programming
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

### Tools
- GitHub
- VS Code

---

## 📊 Features

### Dataset Visualization
Displays a preview of the railway dataset including:
- Train arrival time
- Departure time
- Passenger count
- Platform number
- Track number
- Delay minutes

### Passenger Traffic Analysis
Visualizes passenger distribution to understand travel demand.

### Train Traffic Analysis
Shows how train arrivals vary across different hours of the day.

### Platform Usage Analysis
Displays how platforms are utilized across the dataset.

### Train Delay Prediction
A Random Forest Machine Learning model predicts expected train delays based on:
- Arrival time
- Departure time
- Passenger count
- Platform number
- Track number

Users can input these values through the dashboard to get a predicted delay.

---

## 📁 Project Structure


smart-railway-planner
│
├── data
│ └── railway_data.csv
│
├── models
│ └── delay_model.pkl
│
├── src
│ └── train_model.py
│
├── app
│ ├── app.py
│ └── style.css
│
├── dataset_generator.py
├── requirements.txt
└── README.md



---

## 📂 Dataset

Since real railway operational data is confidential, this project uses a synthetic dataset generated using Python.

Dataset columns:

| Column | Description |
|------|------|
| train_id | Unique train identifier |
| arrival_hour | Train arrival hour |
| departure_hour | Train departure hour |
| passenger_count | Number of passengers |
| platform_number | Assigned platform |
| track_number | Assigned track |
| delay_minutes | Train delay in minutes |

---

## 🤖 Machine Learning Model

Model Used:  
Random Forest Regressor

Purpose:  
Predict train delay based on operational factors.

Workflow:
1. Load dataset
2. Split into training and testing data
3. Train the machine learning model
4. Save trained model using Joblib
5. Use model in Streamlit dashboard for predictions

---

## 🚀 Installation

### Clone Repository

git clone https://github.com/varsha-reddy18/Smart_railway_planning_hackathon.git

### Navigate to Project

cd smart-railway-planner


### Install Requirements

pip install -r requirements.txt

### Run the Application

cd app
streamlit run app.py



---

## 📸 Dashboard Features

The dashboard provides:

- Railway dataset preview
- Passenger distribution charts
- Train traffic by hour
- Platform usage visualization
- Train delay prediction interface

---

## 🔮 Future Improvements
- Real-time railway data integration
- AI-based platform conflict detection
- Train schedule optimization algorithms
- Passenger demand forecasting
- Multi-station railway network simulation

---

## 🏆 Hackathon Submission

This project was developed for the Tekworks Innovation Arena Hackathon.

Evaluation criteria include:
- Innovation
- Functionality
- Code quality
- Scalability
- Presentation

---

## 👩‍💻 Author

Varsha Reddy  
B.Tech – Artificial Intelligence & Data Science  
CVR College of Engineering

---

## 📜 License

This project is created for educational and hackathon purposes.