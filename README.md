# 🔋 Smart Battery Management System for Hybrid Electric Vehicles

## 📌 Project Overview

This project presents a software-based simulation of a Smart Battery Management System (BMS) designed for Hybrid Electric Vehicle (HEV) applications.

The system simulates battery parameters such as State of Charge (SOC), voltage, current, and temperature while monitoring the battery through different HEV driving conditions.

A Streamlit dashboard provides an interactive interface for monitoring battery performance and testing BMS protection conditions.

> **Note:** This is a software simulation project and does not use physical battery or BMS hardware.

## 🎯 Objectives

* Simulate battery behavior during different HEV driving conditions.
* Monitor battery SOC, voltage, current, and temperature.
* Implement BMS protection logic.
* Simulate regenerative braking and battery charging.
* Detect abnormal battery conditions.
* Store simulation data in CSV format.
* Visualize battery performance through an interactive dashboard.

## 🚗 HEV Driving Conditions

The simulation includes:

* Acceleration
* Cruising
* Regenerative Braking

These conditions are represented using different battery current values to simulate energy discharge and regeneration.

## 🛡️ BMS Protection Features

The BMS monitors the battery for:

* Over Voltage
* Under Voltage
* Over Temperature
* Over Current
* Low SOC
* High SOC

When a simulated abnormal condition is detected, the dashboard displays **Protection Active**.

## 📊 Dashboard Features

The Streamlit dashboard provides:

* Battery SOC indicator
* Battery voltage monitoring
* Battery current monitoring
* Battery temperature monitoring
* Battery power calculation
* SOC trend graph
* Temperature trend graph
* Current trend graph
* HEV driving-cycle data
* BMS status monitoring
* Interactive BMS fault simulator

## 🧰 Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Plotly
* CSV Data Processing

## 📁 Project Structure

```text
HEV_BMS_Simulation/
│
├── app.py
├── battery_model.py
├── bms_logic.py
├── simulation.py
├── test_bms.py
├── simulation_data.csv
├── requirements.txt
└── README.md
```

## ⚙️ How to Run

### 1. Install the required libraries

```bash
pip install -r requirements.txt
```

### 2. Run the HEV battery simulation

```bash
python simulation.py
```

This generates the simulation data file:

```text
simulation_data.csv
```

### 3. Launch the dashboard

```bash
streamlit run app.py
```

The Streamlit dashboard will open in your web browser.

## 🧪 BMS Testing

The project includes test cases for:

1. Normal battery operation
2. Over-temperature
3. Over-voltage
4. Under-voltage
5. Over-current
6. Low SOC

These tests demonstrate the BMS protection logic.

## 📈 Expected Outcome

The simulation demonstrates how a software-based BMS can monitor battery parameters and identify abnormal operating conditions in an HEV environment.

The dashboard provides a visual representation of battery behavior throughout the simulated driving cycle.

## 👨‍💻 Project Type

**Academic / Internship Project**

**Domain:** Hybrid Electric Vehicles (HEV) / Battery Management Systems (BMS)

**Developed as part of:** Skillentrix Technologies Internship
