def explain_risk(clause):

    if "GDPR" in clause:
        return "Risk detected due to missing GDPR compliance clause."

    elif "payment" in clause:
        return "Risk detected due to unclear financial obligations."

    elif "confidentiality" in clause:
        return "Risk detected due to incomplete confidentiality protections."

    else:
        return "Contract compliance appears stable."