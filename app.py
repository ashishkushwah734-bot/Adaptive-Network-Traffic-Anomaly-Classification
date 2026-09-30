import streamlit as st
import joblib
import pandas as pd

# Load the lightweight model and scaler
model = joblib.load('dt_lite.pkl')
scaler = joblib.load('scaler_lite.pkl')

st.set_page_config(page_title="Network Anomaly Detector", layout="centered")
st.title("🛡️ Adaptive Network Traffic Anomaly Classification")
st.markdown("Enter the top 5 network flow metrics below to determine if the traffic is Normal or Anomalous.")

# Create input fields for the 5 features
col1, col2 = st.columns(2)

with col1:
    src_bytes = st.number_input("Source Bytes (src_bytes)", min_value=0, value=250)
    dst_bytes = st.number_input("Destination Bytes (dst_bytes)", min_value=0, value=800)
    
with col2:
    protocol = st.selectbox("Protocol Type", options=["tcp", "udp", "icmp"])
    dst_host_srv_count = st.number_input("Dest Host Srv Count", min_value=0, value=10)
    hot = st.number_input("Hot Indicators", min_value=0, value=0)

# Map protocol strings to the LabelEncoder numeric values
protocol_map = {"icmp": 0, "tcp": 1, "udp": 2}
protocol_encoded = protocol_map[protocol]

if st.button("Analyze Traffic", use_container_width=True):
    # 1. Organize inputs into a DataFrame
    input_data = pd.DataFrame({
        'src_bytes': [src_bytes],
        'protocol_type': [protocol_encoded],
        'dst_host_srv_count': [dst_host_srv_count],
        'hot': [hot],
        'dst_bytes': [dst_bytes]
    })
    
    # 2. Scale ONLY the numerical columns
    numerical_cols = ['src_bytes', 'dst_host_srv_count', 'hot', 'dst_bytes']
    input_data[numerical_cols] = scaler.transform(input_data[numerical_cols])
    
    # 3. Predict
    prediction = model.predict(input_data)
    
    # 4. Display Results
    st.divider()
    if prediction[0] == 1:
        st.error("🚨 **ANOMALY DETECTED:** This network behavior matches known malicious patterns.")
    else:
        st.success("✅ **NORMAL:** This network traffic appears safe.")