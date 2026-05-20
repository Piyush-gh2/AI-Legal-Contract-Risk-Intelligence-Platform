from src.loader import load_data
from src.contract_analyzer import analyze_contracts
from src.risk_engine import detect_legal_risk
from src.explainable_ai import explain_risk

def run_legal_ai():

    df = load_data()

    summary = analyze_contracts(df)

    latest_clause = df["clause"].iloc[0]

    risk = detect_legal_risk(latest_clause)

    explanation = explain_risk(latest_clause)

    return df, summary, risk, explanation