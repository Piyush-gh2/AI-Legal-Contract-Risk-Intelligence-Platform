def detect_legal_risk(clause):

    if "Missing GDPR" in clause:
        return "High Compliance Risk"

    elif "Ambiguous" in clause:
        return "Contract Interpretation Risk"

    elif "Incomplete confidentiality" in clause:
        return "Data Protection Risk"

    else:
        return "Low Legal Risk"