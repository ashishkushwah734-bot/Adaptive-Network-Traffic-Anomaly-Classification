🛡️ Adaptive Network Traffic Anomaly Classification

A lightweight, high-speed machine learning prototype designed to classify network traffic as Normal or Anomalous. Built as a localized digital defense protocol, this system analyzes core network heuristics to filter out malicious payloads and unauthorized intrusion attempts before they breach the perimeter.

🎯 Project Objective
Traditional signature-based detection systems often fail to catch zero-day exploits. This project implements an Anomaly-Based Intrusion Detection System (IDS) using foundational ML classification. By reducing the feature space to only the most critical network indicators, the model achieves rapid inference speeds suitable for real-time traffic analysis without relying on heavy deep-learning frameworks.

⚙️ Core Features
⚡ Ultra-Lightweight Inference: Analyzes only the top 5 most critical network features (src_bytes, protocol_type, dst_host_srv_count, hot, dst_bytes), ignoring 36 redundant data points.
🧠 High Accuracy: Powered by a customized Decision Tree classifier achieving 98% accuracy and F1-scores.
🖥️ Interactive UI: Includes a streamlined, zero-cost Streamlit web application for instant manual traffic diagnostics.
📊 Dataset & ModelingDataset: Extracted from the NSL-KDD benchmark dataset.Preprocessing: LabelEncoder for protocol attributes and StandardScaler for byte-count normalization.Model: DecisionTreeClassifier (Max Depth = 5) to prevent overfitting and ensure the decision logic remains highly interpretable.

🏆 Performance Metrics
Metric
Normal Traffic

(0)Anomalous Traffic

(1)Precision

0.990.97
Recall

0.980.99
F1-Score

0.980.98

Overall Accuracy

98%
98%

🚀 Installation & UsageFollow these steps to run the anomaly detection interface on your local machine.

1. Clone the RepositoryBashgit clone https://github.com/ashishkushwah734-bot/Adaptive-Network-Traffic-Anomaly-Classification.git
cd Adaptive-Network-Traffic-Anomaly-Classification
2. Install Dependencies
Ensure you have Python installed, then run:Bashpip install -r requirements.txt
3. Launch the ApplicationStart the Streamlit web server to open the interactive dashboard:Bashstreamlit run app.py
   
📁 Repository StructurePlaintext

📦 Adaptive-Network-Traffic-Anomaly-Classification
 ┣ 📜 app.py               # The main Streamlit web application code
 ┣ 📜 notebook.ipynb       # Google Colab notebook containing EDA & Model Training
 ┣ 📜 dt_lite.pkl          # Serialized Decision Tree model (trained on 5 features)
 ┣ 📜 scaler_lite.pkl      # Serialized StandardScaler for input normalization
 ┣ 📜 requirements.txt     # Python package dependencies
 ┗ 📜 README.md            # Project documentation
