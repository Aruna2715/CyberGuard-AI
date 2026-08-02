# ============================================================
# CYBERGUARD AI
# NETWORK INTRUSION DETECTION SYSTEM
# UNSW-NB15 DATASET
# ============================================================

import os
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from xgboost import XGBClassifier


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CyberGuard AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# DARK THEME
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1628;
        color: #e5e7eb;
    }

    [data-testid="stSidebar"] {
        background-color: #111827;
    }

    [data-testid="stSidebar"] * {
        color: #e5e7eb;
    }

    h1, h2, h3 {
        color: #f8fafc !important;
    }

    p {
        color: #cbd5e1;
    }

    [data-testid="stMetric"] {
        background-color: #172033;
        border: 1px solid #334155;
        padding: 18px;
        border-radius: 12px;
    }

    [data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
    }

    [data-testid="stMetricValue"] {
        color: #f8fafc !important;
    }

    .stButton > button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        border: none;
    }

    .stButton > button:hover {
        background-color: #1d4ed8;
    }

    [data-testid="stDataFrame"] {
        border: 1px solid #334155;
        border-radius: 10px;
    }

    [data-testid="stFileUploader"] {
        background-color: #172033;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# FILE PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "xgboost_intrusion_model.json"
PREPROCESSOR_PATH = BASE_DIR / "models" / "preprocessor.pkl"


# ============================================================
# LOAD MODEL AND PREPROCESSOR
# ============================================================

@st.cache_resource(show_spinner=False)
def load_artifacts():
    loaded_model = None
    loaded_preprocessor = None
    model_load_error = None
    preprocessor_load_error = None

    try:
        if MODEL_PATH.exists():
            loaded_model = XGBClassifier()
            loaded_model.load_model(str(MODEL_PATH))
            loaded_model.set_params(n_jobs=1)
        else:
            model_load_error = (
                f"Model file was not found at: {MODEL_PATH}"
            )
    except Exception as exc:
        model_load_error = str(exc)

    try:
        if PREPROCESSOR_PATH.exists():
            loaded_preprocessor = joblib.load(PREPROCESSOR_PATH)
        else:
            preprocessor_load_error = (
                f"Preprocessor file was not found at: {PREPROCESSOR_PATH}"
            )
    except Exception as exc:
        preprocessor_load_error = str(exc)

    return (
        loaded_model,
        loaded_preprocessor,
        model_load_error,
        preprocessor_load_error,
    )


model, preprocessor, model_error, preprocessor_error = load_artifacts()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.title("🛡️ CyberGuard AI")
    st.caption("Network Intrusion Detection System")

    st.divider()
    st.subheader("NAVIGATION")

    page = st.radio(
        "Select a page",
        [
            "🛡️ Security Overview",
            "🔍 Intrusion Detection",
            "📊 Model Analytics",
            "ℹ️ About Project",
        ],
    )

    st.divider()
    st.subheader("SYSTEM STATUS")
    st.success("🟢 SYSTEM ONLINE")
    st.caption("All systems operational")

    st.subheader("MODEL STATUS")

    if model is not None:
        st.success("🧠 XGBoost Model ACTIVE")
    else:
        st.error(f"⚠️ Model not loaded: {model_error}")

    if preprocessor is not None:
        st.success("⚙️ Preprocessor ACTIVE")
    else:
        st.error(f"⚠️ Preprocessor not loaded: {preprocessor_error}")


# ============================================================
# SECURITY OVERVIEW
# ============================================================

if page == "🛡️ Security Overview":
    st.title("🛡️ CyberGuard AI")
    st.subheader("AI-Powered Network Intrusion Detection Platform")

    st.write(
        "An intelligent machine learning system designed to identify "
        "malicious network traffic and protect digital infrastructure "
        "using the UNSW-NB15 dataset."
    )

    st.divider()
    st.header("📊 Model Performance")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🎯 Model Accuracy", "87.37%")

    with col2:
        st.metric("🛡️ Attack Recall", "98.60%")

    with col3:
        st.metric("📈 ROC-AUC Score", "98.43%")

    with col4:
        st.metric("⚡ ML Algorithm", "XGBoost")

    st.divider()
    st.header("🔄 AI Detection Pipeline")

    step1, step2, step3, step4, step5 = st.columns(5)

    with step1:
        st.info("🌐\n\n**Network Traffic**\n\nRaw network connection data")

    with step2:
        st.info("🧹\n\n**Data Cleaning**\n\nPrepare network data")

    with step3:
        st.info("⚙️\n\n**Feature Transformation**\n\nEncode and scale features")

    with step4:
        st.info("🧠\n\n**XGBoost Model**\n\nClassify network behavior")

    with step5:
        st.error("🚨\n\n**Threat Detection**\n\nNormal or Attack")

    st.divider()
    st.header("📊 Model Performance Comparison")

    comparison_df = pd.DataFrame(
        {
            "Model": ["Logistic Regression", "Random Forest", "XGBoost"],
            "Accuracy": ["80.97%", "87.14%", "87.37%"],
            "Precision": ["75.35%", "81.74%", "82.08%"],
            "Recall": ["97.25%", "98.70%", "98.60%"],
            "F1-Score": ["84.91%", "89.42%", "89.58%"],
            "ROC-AUC": ["95.58%", "97.91%", "98.43%"],
        }
    )

    st.dataframe(comparison_df, width="stretch", hide_index=True)

    st.divider()
    st.header("🏆 Why XGBoost?")

    left, right = st.columns(2)

    with left:
        st.success(
            """
            **✅ Key Strengths**

            ✔ Highest ROC-AUC score: **98.43%**

            ✔ Excellent attack detection recall: **98.60%**

            ✔ Strong balance between precision and recall

            ✔ Handles complex nonlinear relationships

            ✔ Effective for high-dimensional network traffic data
            """
        )

    with right:
        st.info(
            """
            **🔬 Dataset Information**

            **Dataset:** UNSW-NB15

            **Training Records:** 175,341

            **Testing Records:** 82,332

            **Input Features:** 42

            **Classes:** Normal Traffic / Attack Traffic
            """
        )


# ============================================================
# INTRUSION DETECTION
# ============================================================

elif page == "🔍 Intrusion Detection":
    st.title("🔍 Network Intrusion Detection")

    st.write(
        "Upload network traffic data to classify each connection "
        "as Normal Traffic or Attack Traffic."
    )

    st.info(
        "The uploaded CSV file must contain network traffic features "
        "matching the UNSW-NB15 dataset structure."
    )

    uploaded_file = st.file_uploader(
        "Upload Network Traffic CSV",
        type=["csv"],
    )

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as exc:
            st.error(f"Could not read the CSV file: {exc}")
            st.stop()

        if df.empty:
            st.error("The uploaded CSV file contains no records.")
            st.stop()

        st.success("Dataset uploaded successfully!")
        st.subheader("📄 Dataset Preview")
        st.dataframe(df.head(10), width="stretch")
        st.write(f"**Dataset Shape:** {df.shape}")

        st.divider()

        if st.button("🚨 Detect Intrusions", type="primary"):
            if model is None:
                st.error(f"XGBoost model could not be loaded: {model_error}")
                st.stop()

            if preprocessor is None:
                st.error(
                    f"Preprocessor could not be loaded: {preprocessor_error}"
                )
                st.stop()

            try:
                X_input = df.copy()

                for column in ["label", "attack_cat"]:
                    if column in X_input.columns:
                        X_input = X_input.drop(columns=[column])

                if "id" in X_input.columns:
                    X_input = X_input.drop(columns=["id"])

                expected_columns = list(
                    getattr(preprocessor, "feature_names_in_", [])
                )

                if expected_columns:
                    missing_columns = [
                        column
                        for column in expected_columns
                        if column not in X_input.columns
                    ]
                    extra_columns = [
                        column
                        for column in X_input.columns
                        if column not in expected_columns
                    ]

                    if missing_columns:
                        st.error(
                            "The uploaded file is missing required columns: "
                            + ", ".join(missing_columns)
                        )
                        st.stop()

                    if extra_columns:
                        X_input = X_input.drop(columns=extra_columns)

                    X_input = X_input[expected_columns]

                # Batch processing reduces memory use on free hosting platforms.
                batch_size = 1_000
                prediction_batches = []
                probability_batches = []

                total_rows = len(X_input)
                progress_bar = st.progress(0)
                status_text = st.empty()

                for start_index in range(0, total_rows, batch_size):
                    end_index = min(start_index + batch_size, total_rows)

                    status_text.write(
                        f"Processing records {start_index + 1:,}–"
                        f"{end_index:,} of {total_rows:,}..."
                    )

                    batch = X_input.iloc[start_index:end_index]
                    batch_processed = preprocessor.transform(batch)

                    batch_predictions = model.predict(batch_processed)
                    batch_probabilities = model.predict_proba(
                        batch_processed
                    )[:, 1]

                    prediction_batches.append(batch_predictions)
                    probability_batches.append(batch_probabilities)

                    progress_bar.progress(end_index / total_rows)

                predictions = np.concatenate(prediction_batches)
                probabilities = np.concatenate(probability_batches)

                progress_bar.empty()
                status_text.empty()

                results = df.copy()
                results["Prediction"] = np.where(
                    predictions == 1,
                    "Attack",
                    "Normal",
                )
                results["Attack Probability (%)"] = (
                    probabilities * 100
                ).round(2)

                st.success("Intrusion detection completed successfully!")

                total_records = len(results)
                attack_count = int(
                    (results["Prediction"] == "Attack").sum()
                )
                normal_count = int(
                    (results["Prediction"] == "Normal").sum()
                )
                attack_percentage = (
                    attack_count / total_records * 100
                    if total_records
                    else 0.0
                )

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric("Total Records", f"{total_records:,}")

                with col2:
                    st.metric("Normal Traffic", f"{normal_count:,}")

                with col3:
                    st.metric("Detected Attacks", f"{attack_count:,}")

                with col4:
                    st.metric(
                        "Attack Percentage",
                        f"{attack_percentage:.2f}%",
                    )

                st.divider()

                chart_df = pd.DataFrame(
                    {
                        "Traffic Type": ["Normal", "Attack"],
                        "Count": [normal_count, attack_count],
                    }
                )

                fig = px.bar(
                    chart_df,
                    x="Traffic Type",
                    y="Count",
                    text="Count",
                    title="Traffic Classification Distribution",
                )

                fig.update_layout(
                    template="plotly_dark",
                    paper_bgcolor="#0e1628",
                    plot_bgcolor="#0e1628",
                    font_color="#e5e7eb",
                )

                st.plotly_chart(fig, width="stretch")

                st.divider()
                st.subheader("🔎 Detailed Prediction Results")

                selected_columns = [
                    "id",
                    "proto",
                    "service",
                    "state",
                    "Prediction",
                    "Attack Probability (%)",
                ]

                display_columns = [
                    column
                    for column in selected_columns
                    if column in results.columns
                ]

                preview_limit = 1_000
                st.dataframe(
                    results[display_columns].head(preview_limit),
                    width="stretch",
                )

                if len(results) > preview_limit:
                    st.info(
                        f"Showing the first {preview_limit:,} records. "
                        "Download the CSV to view all prediction results."
                    )

                csv_data = results.to_csv(index=False).encode("utf-8")

                st.download_button(
                    label="⬇️ Download Prediction Results",
                    data=csv_data,
                    file_name="intrusion_detection_results.csv",
                    mime="text/csv",
                )

            except Exception as exc:
                st.error(f"Prediction failed: {exc}")


# ============================================================
# MODEL ANALYTICS
# ============================================================

elif page == "📊 Model Analytics":
    st.title("📊 Model Analytics")

    st.write(
        "Performance analysis of the machine learning models "
        "trained for network intrusion detection."
    )

    st.divider()
    st.header("📈 Final XGBoost Performance")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Accuracy", "87.37%")

    with col2:
        st.metric("Precision", "82.08%")

    with col3:
        st.metric("Recall", "98.60%")

    with col4:
        st.metric("F1-Score", "89.58%")

    with col5:
        st.metric("ROC-AUC", "98.43%")

    st.divider()

    metric_df = pd.DataFrame(
        {
            "Metric": [
                "Accuracy",
                "Precision",
                "Recall",
                "F1-Score",
                "ROC-AUC",
            ],
            "Score": [87.37, 82.08, 98.60, 89.58, 98.43],
        }
    )

    fig = px.bar(
        metric_df,
        x="Metric",
        y="Score",
        text="Score",
        title="XGBoost Performance Metrics",
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0e1628",
        plot_bgcolor="#0e1628",
        font_color="#e5e7eb",
        yaxis_range=[0, 100],
    )

    st.plotly_chart(fig, width="stretch")

    st.divider()
    st.header("📊 Model Comparison")

    model_comparison = pd.DataFrame(
        {
            "Model": ["Logistic Regression", "Random Forest", "XGBoost"],
            "Accuracy": [80.97, 87.14, 87.37],
            "Precision": [75.35, 81.74, 82.08],
            "Recall": [97.25, 98.70, 98.60],
            "F1-Score": [84.91, 89.42, 89.58],
            "ROC-AUC": [95.58, 97.91, 98.43],
        }
    )

    st.dataframe(model_comparison, width="stretch", hide_index=True)


# ============================================================
# ABOUT PROJECT
# ============================================================

elif page == "ℹ️ About Project":
    st.title("ℹ️ About CyberGuard AI")

    st.write(
        "CyberGuard AI is a machine learning-based Network Intrusion "
        "Detection System developed using the UNSW-NB15 dataset."
    )

    st.divider()
    st.header("📌 Project Overview")

    st.write(
        "The system analyzes network traffic features and predicts "
        "whether a connection represents normal activity or a "
        "potential cyber attack."
    )

    st.divider()
    st.header("🧪 Technologies Used")

    technology_df = pd.DataFrame(
        {
            "Technology": [
                "Python",
                "XGBoost",
                "Scikit-learn",
                "Pandas",
                "NumPy",
                "Streamlit",
                "Plotly",
            ],
            "Purpose": [
                "Programming Language",
                "Machine Learning Model",
                "Preprocessing and Evaluation",
                "Data Processing",
                "Numerical Computation",
                "Dashboard Development",
                "Data Visualization",
            ],
        }
    )

    st.dataframe(technology_df, width="stretch", hide_index=True)

    st.divider()
    st.header("📊 Dataset Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Training Records", "175,341")

    with col2:
        st.metric("Testing Records", "82,332")

    with col3:
        st.metric("Input Features", "42")

    with col4:
        st.metric("Target Classes", "2")


# ============================================================
# FOOTER
# ============================================================

st.divider()
st.caption(
    "🛡️ CyberGuard AI | AI-Powered Network Intrusion Detection System"
)
st.caption("Built using Machine Learning and the UNSW-NB15 Dataset")
