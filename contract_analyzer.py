def analyze_contracts(df):

    high_risk = df[df["risk_level"] == "High"]

    medium_risk = df[df["risk_level"] == "Medium"]

    low_risk = df[df["risk_level"] == "Low"]

    return {
        "high": len(high_risk),
        "medium": len(medium_risk),
        "low": len(low_risk)
    }