import streamlit as st

from src.agents import run_legal_ai
from src.rag import load_knowledge, build_index, retrieve

st.title("⚖️ AI Legal Contract Risk Intelligence Platform")

query = st.text_input("Ask Legal Insight")

if st.button("Analyze Contracts"):

    df, summary, risk, explanation = run_legal_ai()

    st.subheader("📊 Contract Dataset")
    st.dataframe(df)

    st.subheader("📈 Contract Risk Summary")
    st.write(summary)

    st.subheader("⚠️ Legal Risk Detection")
    st.write(risk)

    st.subheader("🧠 Explainable AI Insight")
    st.write(explanation)

    st.bar_chart(df["risk_level"].value_counts())

    # RAG
    docs = load_knowledge()
    index = build_index(docs)

    if query:

        insights = retrieve(query, docs, index)

        st.subheader("🔎 Legal Governance Insights")

        for i in insights:
            st.write(i) 