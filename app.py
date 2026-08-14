
import os, json, time, warnings
import numpy as np
import pandas as pd
from groq import Groq
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from datetime import datetime
import gradio as gr
warnings.filterwarnings("ignore")

# ── API Key (from HuggingFace Secrets) ────────────────────────────────
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
if not GROQ_API_KEY:
    raise ValueError("Set GROQ_API_KEY in HuggingFace Space Secrets")
groq_client = Groq(api_key=GROQ_API_KEY)

# ── Load data ─────────────────────────────────────────────────────────
EXCEL_PATH = "Dataset_Agentic_AI.xlsx"
df_sgpa    = pd.read_excel(EXCEL_PATH, sheet_name="SGPA Trends")
df_results = pd.read_excel(EXCEL_PATH, sheet_name="Semester Results")
df_payment = pd.read_excel(EXCEL_PATH, sheet_name="Payment Status")

# [PASTE: build_risk_features, classify_student, kb_*, llm_reason,
#  all agent functions, coordinator_agent, gradio_classify, gradio_full_agent,
#  and the Blocks demo from Phase 11 above]

# Last line:
# demo.launch()
