import streamlit as st
import pandas as pd
import plotly.express as px


# Page configuration
st.set_page_config(
    page_title="HEV BMS Dashboard",
    page_icon="🔋",
    layout="wide"
)


# Title
st.title("🔋 HEV Battery Management System")
st.subheader("Hybrid Electric Vehicle Battery Simulation Dashboard")


# Load simulation data
data = pd.read_csv("simulation_data.csv")


# Get latest battery values
latest = data.iloc[-1]


# Battery parameters
soc = latest["SOC (%)"]
voltage = latest["Voltage (V)"]
current = latest["Current (A)"]
temperature = latest["Temperature (°C)"]
status = latest["BMS Status"]
warnings = latest["Warnings"]

# Calculate battery power
power = (voltage * current) / 1000


# SOC Gauge
st.markdown("### 🔋 Battery SOC Level")

fig_gauge = px.pie(
    values=[soc, 100 - soc],
    names=["SOC", "Remaining Capacity"],
    hole=0.7,
    title=f"Battery SOC: {soc}%"
)

st.plotly_chart(fig_gauge, use_container_width=True)


# Battery status
st.markdown("### Battery Status")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("🔋 SOC", f"{soc}%")

with col2:
    st.metric("⚡ Voltage", f"{voltage} V")

with col3:
    st.metric("🔌 Current", f"{current} A")

with col4:
    st.metric("🌡️ Temperature", f"{temperature} °C")

with col5:
    st.metric("⚡ Power", f"{power:.2f} kW")


# BMS protection status
st.markdown("### 🛡️ BMS Protection Status")

if status == "NORMAL":
    st.success("✅ BMS STATUS: NORMAL")
else:
    st.error("⚠️ BMS STATUS: PROTECTION ACTIVE")
    st.warning(f"⚠️ Warning: {warnings}")


# SOC graph
st.markdown("### 📈 State of Charge")

fig_soc = px.line(
    data,
    x="Time (min)",
    y="SOC (%)",
    markers=True,
    title="Battery SOC During HEV Driving Cycle"
)

st.plotly_chart(fig_soc, use_container_width=True)


# Temperature graph
st.markdown("### 🌡️ Battery Temperature")

fig_temp = px.line(
    data,
    x="Time (min)",
    y="Temperature (°C)",
    markers=True,
    title="Battery Temperature During HEV Driving Cycle"
)

st.plotly_chart(fig_temp, use_container_width=True)


# Current graph
st.markdown("### 🔌 Battery Current")

fig_current = px.bar(
    data,
    x="Time (min)",
    y="Current (A)",
    title="Battery Current During HEV Driving Cycle"
)

st.plotly_chart(fig_current, use_container_width=True)


# Driving cycle
st.markdown("### 🚗 HEV Driving Cycle")

st.dataframe(
    data[
        [
            "Time (min)",
            "Driving Mode",
            "Current (A)",
            "SOC (%)",
            "Temperature (°C)",
            "BMS Status"
        ]
    ],
    use_container_width=True
)


# Fault simulator
st.markdown("### ⚠️ BMS Fault Simulator")

st.write(
    "Select a simulated battery fault to test the BMS protection logic."
)

fault = st.selectbox(
    "Select Test Condition",
    [
        "Normal Condition",
        "Over Voltage",
        "Under Voltage",
        "Over Temperature",
        "Over Current",
        "Low SOC",
        "High SOC"
    ]
)


# Simulated fault values
test_voltage = 360
test_current = 40
test_temperature = 30
test_soc = 80


if fault == "Over Voltage":
    test_voltage = 420

elif fault == "Under Voltage":
    test_voltage = 280

elif fault == "Over Temperature":
    test_temperature = 50

elif fault == "Over Current":
    test_current = 120

elif fault == "Low SOC":
    test_soc = 5

elif fault == "High SOC":
    test_soc = 95


# Display simulated values
st.markdown("#### Simulated Battery Values")

fault_col1, fault_col2, fault_col3, fault_col4 = st.columns(4)

with fault_col1:
    st.metric("Voltage", f"{test_voltage} V")

with fault_col2:
    st.metric("Current", f"{test_current} A")

with fault_col3:
    st.metric("Temperature", f"{test_temperature} °C")

with fault_col4:
    st.metric("SOC", f"{test_soc}%")


# Check simulated fault
if (
    test_voltage > 400
    or test_voltage < 300
    or test_temperature > 45
    or abs(test_current) > 100
    or test_soc < 10
    or test_soc > 90
):

    st.error("🚨 PROTECTION ACTIVE")

else:

    st.success("✅ SYSTEM NORMAL")