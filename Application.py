# ============================================================
# CYBERGUARD AI
# NETWORK INTRUSION DETECTION SYSTEM
# UNSW-NB15 DATASET
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import plotly.express as px
from xgboost import XGBClassifier

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CyberGuard AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
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
    unsafe_allow_html=True
)


# ============================================================
# FIND CURRENT APPLICATION FOLDER
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


# ============================================================
# MODEL FILE PATHS
# ============================================================

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "xgboost_intrusion_model.json"
)

PREPROCESSOR_PATH = os.path.join(
    BASE_DIR,
    "models",
    "preprocessor.pkl"
)


# ============================================================
# LOAD MODEL
# ============================================================

model = None
preprocessor = None

model_error = None
preprocessor_error = None


# ---------------- LOAD XGBOOST MODEL ----------------

try:
    if os.path.exists(MODEL_PATH):
        model = XGBClassifier()
        model.load_model(MODEL_PATH)
    else:
        model_error = "XGBoost JSON model file was not found."

except Exception as e:
    model_error = str(e)


# ---------------- LOAD PREPROCESSOR ----------------

try:

    if os.path.exists(PREPROCESSOR_PATH):

        preprocessor = joblib.load(
            PREPROCESSOR_PATH
        )

    else:

        preprocessor_error = (
            "Preprocessor file was not found."
        )

except Exception as e:

    preprocessor_error = str(e)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title(
        "🛡️ CyberGuard AI"
    )

    st.caption(
        "Network Intrusion Detection System"
    )

    st.divider()

    st.subheader(
        "NAVIGATION"
    )

    page = st.radio(

        "Select a page",

        [

            "🛡️ Security Overview",

            "🔍 Intrusion Detection",

            "📊 Model Analytics",

            "ℹ️ About Project"

        ]

    )

    st.divider()

    st.subheader(
        "SYSTEM STATUS"
    )

    st.success(
        "🟢 SYSTEM ONLINE"
    )

    st.caption(
        "All systems operational"
    )

    st.subheader(
        "MODEL STATUS"
    )

    if model is not None:

        st.success(
            "🧠 XGBoost Model ACTIVE"
        )

    else:

        st.error(
            "⚠️ Model not loaded"
        )

    if preprocessor is not None:

        st.success(
            "⚙️ Preprocessor ACTIVE"
        )

    else:

        st.error(
            "⚠️ Preprocessor not loaded"
        )


# ============================================================
# SECURITY OVERVIEW
# ============================================================

if page == "🛡️ Security Overview":

    st.title(
        "🛡️ CyberGuard AI"
    )

    st.subheader(
        "AI-Powered Network Intrusion Detection Platform"
    )

    st.write(

        "An intelligent machine learning system designed "
        "to identify malicious network traffic and protect "
        "digital infrastructure using the UNSW-NB15 dataset."

    )

    st.divider()


    # --------------------------------------------------------
    # MODEL METRICS
    # --------------------------------------------------------

    st.header(
        "📊 Model Performance"
    )

    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(

            label="🎯 Model Accuracy",

            value="87.37%"

        )


    with col2:

        st.metric(

            label="🛡️ Attack Recall",

            value="98.60%"

        )


    with col3:

        st.metric(

            label="📈 ROC-AUC Score",

            value="98.43%"

        )


    with col4:

        st.metric(

            label="⚡ ML Algorithm",

            value="XGBoost"

        )


    st.divider()


    # --------------------------------------------------------
    # SYSTEM PIPELINE
    # --------------------------------------------------------

    st.header(
        "🔄 AI Detection Pipeline"
    )

    step1, step2, step3, step4, step5 = st.columns(5)


    with step1:

        st.info(

            """
            🌐

            **Network Traffic**

            Raw network connection data
            """

        )


    with step2:

        st.info(

            """
            🧹

            **Data Cleaning**

            Prepare network data
            """

        )


    with step3:

        st.info(

            """
            ⚙️

            **Feature Transformation**

            Encode and scale features
            """

        )


    with step4:

        st.info(

            """
            🧠

            **XGBoost Model**

            Classify network behavior
            """

        )


    with step5:

        st.error(

            """
            🚨

            **Threat Detection**

            Normal or Attack
            """

        )


    st.divider()


    # --------------------------------------------------------
    # MODEL COMPARISON
    # --------------------------------------------------------

    st.header(
        "📊 Model Performance Comparison"
    )


    comparison_df = pd.DataFrame(

        {

            "Model": [

                "Logistic Regression",

                "Random Forest",

                "XGBoost"

            ],

            "Accuracy": [

                "80.97%",

                "87.14%",

                "87.37%"

            ],

            "Precision": [

                "75.35%",

                "81.74%",

                "82.08%"

            ],

            "Recall": [

                "97.25%",

                "98.70%",

                "98.60%"

            ],

            "F1-Score": [

                "84.91%",

                "89.42%",

                "89.58%"

            ],

            "ROC-AUC": [

                "95.58%",

                "97.91%",

                "98.43%"

            ]

        }

    )


    st.dataframe(

        comparison_df,

        use_container_width=True,

        hide_index=True

    )


    st.divider()


    # --------------------------------------------------------
    # WHY XGBOOST
    # --------------------------------------------------------

    st.header(
        "🏆 Why XGBoost?"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.success(

            """
            **✅ Key Strengths**

            ✔ Highest ROC-AUC score: **98.43%**

            ✔ Excellent attack detection recall:
            **98.60%**

            ✔ Strong balance between precision and recall

            ✔ Handles complex nonlinear relationships

            ✔ Effective for high-dimensional network traffic data
            """

        )


    with col2:

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

    st.title(
        "🔍 Network Intrusion Detection"
    )

    st.write(

        "Upload network traffic data to classify each "
        "connection as Normal Traffic or Attack Traffic."

    )


    st.info(

        """
        The uploaded CSV file should contain network traffic
        features similar to the UNSW-NB15 dataset.
        """

    )


    uploaded_file = st.file_uploader(

        "Upload Network Traffic CSV",

        type=["csv"]

    )


    if uploaded_file is not None:


        # ----------------------------------------------------
        # READ DATASET
        # ----------------------------------------------------

        df = pd.read_csv(

            uploaded_file

        )


        st.success(

            "Dataset uploaded successfully!"

        )


        st.subheader(

            "📄 Dataset Preview"

        )


        st.dataframe(

            df.head(10),

            use_container_width=True

        )


        st.write(

            f"**Dataset Shape:** {df.shape}"

        )


        st.divider()


        # ----------------------------------------------------
        # PREDICTION
        # ----------------------------------------------------

        if st.button(

            "🚨 Detect Intrusions"

        ):


            if model is None:

                st.error(

                    "XGBoost model could not be loaded."

                )

                st.info(

                    f"Expected model file: {MODEL_PATH}"

                )


            elif preprocessor is None:

                st.error(

                    "Preprocessor could not be loaded."

                )

                st.info(

                    f"Expected preprocessor file: "
                    f"{PREPROCESSOR_PATH}"

                )


            else:


                try:


                    # ----------------------------------------
                    # COPY DATA
                    # ----------------------------------------

                    X_input = df.copy()


                    # ----------------------------------------
                    # REMOVE TARGET COLUMNS
                    # ----------------------------------------

                    columns_to_remove = [

                        "label",

                        "attack_cat"

                    ]


                    for column in columns_to_remove:


                        if column in X_input.columns:


                            X_input = X_input.drop(

                                columns=[column]

                            )


                    # ----------------------------------------
                    # REMOVE ID
                    # ----------------------------------------

                    if "id" in X_input.columns:


                        X_input = X_input.drop(

                            columns=["id"]

                        )


                    # ----------------------------------------
                    # PREPROCESS
                    # ----------------------------------------

                    X_processed = preprocessor.transform(

                        X_input

                    )


                    # ----------------------------------------
                    # PREDICT
                    # ----------------------------------------

                    predictions = model.predict(

                        X_processed

                    )


                    probabilities = model.predict_proba(

                        X_processed

                    )[:, 1]


                    # ----------------------------------------
                    # RESULTS
                    # ----------------------------------------

                    results = df.copy()


                    results["Prediction"] = np.where(

                        predictions == 1,

                        "Attack",

                        "Normal"

                    )


                    results[

                        "Attack Probability (%)"

                    ] = (

                        probabilities * 100

                    ).round(2)


                    st.success(

                        "Intrusion detection completed successfully!"

                    )


                    # ----------------------------------------
                    # SUMMARY
                    # ----------------------------------------

                    total_records = len(

                        results

                    )


                    attack_count = (

                        results["Prediction"]

                        == "Attack"

                    ).sum()


                    normal_count = (

                        results["Prediction"]

                        == "Normal"

                    ).sum()


                    attack_percentage = (

                        attack_count

                        / total_records

                        * 100

                    )


                    col1, col2, col3, col4 = st.columns(4)


                    with col1:

                        st.metric(

                            "Total Records",

                            f"{total_records:,}"

                        )


                    with col2:

                        st.metric(

                            "Normal Traffic",

                            f"{normal_count:,}"

                        )


                    with col3:

                        st.metric(

                            "Detected Attacks",

                            f"{attack_count:,}"

                        )


                    with col4:

                        st.metric(

                            "Attack Percentage",

                            f"{attack_percentage:.2f}%"

                        )


                    st.divider()


                    # ----------------------------------------
                    # CHART
                    # ----------------------------------------

                    chart_df = pd.DataFrame(

                        {

                            "Traffic Type": [

                                "Normal",

                                "Attack"

                            ],

                            "Count": [

                                normal_count,

                                attack_count

                            ]

                        }

                    )


                    fig = px.bar(

                        chart_df,

                        x="Traffic Type",

                        y="Count",

                        text="Count",

                        title=(

                            "Traffic Classification Distribution"

                        )

                    )


                    fig.update_layout(

                        template="plotly_dark",

                        paper_bgcolor="#0e1628",

                        plot_bgcolor="#0e1628",

                        font_color="#e5e7eb"

                    )


                    st.plotly_chart(

                        fig,

                        use_container_width=True

                    )


                    st.divider()


                    # ----------------------------------------
                    # RESULTS TABLE
                    # ----------------------------------------

                    st.subheader(

                        "🔎 Detailed Prediction Results"

                    )


                    display_columns = []


                    selected_columns = [

                        "id",

                        "proto",

                        "service",

                        "state",

                        "Prediction",

                        "Attack Probability (%)"

                    ]


                    for column in selected_columns:


                        if column in results.columns:


                            display_columns.append(

                                column

                            )


                    st.dataframe(

                        results[display_columns],

                        use_container_width=True

                    )


                    # ----------------------------------------
                    # DOWNLOAD
                    # ----------------------------------------

                    csv = results.to_csv(

                        index=False

                    ).encode(

                        "utf-8"

                    )


                    st.download_button(

                        label=(

                            "⬇️ Download Prediction Results"

                        ),

                        data=csv,

                        file_name=(

                            "intrusion_detection_results.csv"

                        ),

                        mime="text/csv"

                    )


                except Exception as e:


                    st.error(

                        f"Prediction failed: {e}"

                    )


# ============================================================
# MODEL ANALYTICS
# ============================================================

elif page == "📊 Model Analytics":

    st.title(

        "📊 Model Analytics"

    )


    st.write(

        "Performance analysis of the machine learning models "
        "trained for network intrusion detection."

    )


    st.divider()


    st.header(

        "📈 Final XGBoost Performance"

    )


    col1, col2, col3, col4, col5 = st.columns(5)


    with col1:

        st.metric(

            "Accuracy",

            "87.37%"

        )


    with col2:

        st.metric(

            "Precision",

            "82.08%"

        )


    with col3:

        st.metric(

            "Recall",

            "98.60%"

        )


    with col4:

        st.metric(

            "F1-Score",

            "89.58%"

        )


    with col5:

        st.metric(

            "ROC-AUC",

            "98.43%"

        )


    st.divider()


    metric_df = pd.DataFrame(

        {

            "Metric": [

                "Accuracy",

                "Precision",

                "Recall",

                "F1-Score",

                "ROC-AUC"

            ],

            "Score": [

                87.37,

                82.08,

                98.60,

                89.58,

                98.43

            ]

        }

    )


    fig = px.bar(

        metric_df,

        x="Metric",

        y="Score",

        text="Score",

        title="XGBoost Performance Metrics"

    )


    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="#0e1628",

        plot_bgcolor="#0e1628",

        font_color="#e5e7eb",

        yaxis_range=[0, 100]

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )


    st.divider()


    st.header(

        "📊 Model Comparison"

    )


    model_comparison = pd.DataFrame(

        {

            "Model": [

                "Logistic Regression",

                "Random Forest",

                "XGBoost"

            ],

            "Accuracy": [

                80.97,

                87.14,

                87.37

            ],

            "Precision": [

                75.35,

                81.74,

                82.08

            ],

            "Recall": [

                97.25,

                98.70,

                98.60

            ],

            "F1-Score": [

                84.91,

                89.42,

                89.58

            ],

            "ROC-AUC": [

                95.58,

                97.91,

                98.43

            ]

        }

    )


    st.dataframe(

        model_comparison,

        use_container_width=True,

        hide_index=True

    )


# ============================================================
# ABOUT PROJECT
# ============================================================

elif page == "ℹ️ About Project":

    st.title(

        "ℹ️ About CyberGuard AI"

    )


    st.write(

        "CyberGuard AI is a machine learning-based "
        "Network Intrusion Detection System developed "
        "using the UNSW-NB15 dataset."

    )


    st.divider()


    st.header(

        "📌 Project Overview"

    )


    st.write(

        """

        The system analyzes network traffic features and

        predicts whether a connection represents normal

        activity or a potential cyber attack.

        """

    )


    st.divider()


    st.header(

        "🧪 Technologies Used"

    )


    technology_df = pd.DataFrame(

        {

            "Technology": [

                "Python",

                "XGBoost",

                "Scikit-learn",

                "Pandas",

                "NumPy",

                "Streamlit",

                "Plotly"

            ],

            "Purpose": [

                "Programming Language",

                "Machine Learning Model",

                "Preprocessing and Evaluation",

                "Data Processing",

                "Numerical Computation",

                "Dashboard Development",

                "Data Visualization"

            ]

        }

    )


    st.dataframe(

        technology_df,

        use_container_width=True,

        hide_index=True

    )


    st.divider()


    st.header(

        "📊 Dataset Summary"

    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(

            "Training Records",

            "175,341"

        )


    with col2:

        st.metric(

            "Testing Records",

            "82,332"

        )


    with col3:

        st.metric(

            "Input Features",

            "42"

        )


    with col4:

        st.metric(

            "Target Classes",

            "2"

        )


# ============================================================
# FOOTER
# ============================================================

st.divider()


st.caption(

    "🛡️ CyberGuard AI | AI-Powered Network Intrusion Detection System"

)


st.caption(

    "Built using Machine Learning and the UNSW-NB15 Dataset"

)