import streamlit as st

from components.invoice_preview import render_invoice_preview


def render_financial_ops_page():
    st.title("📑 Financial Operations")

    if not st.session_state.ledger:
        st.info("No transactions found. Complete a purchase to generate financial records.")
        return

    total_turnover = sum(txn["total"] for txn in st.session_state.ledger)
    total_vat = sum(txn["vat"] for txn in st.session_state.ledger)
    success_rate = "100%" if st.session_state.ledger else "0%"

    m1, m2, m3 = st.columns(3)
    m1.metric("Total Settlement", f"ZAR {total_turnover:,.2f}")
    m2.metric("VAT Liabilities (15%)", f"ZAR {total_vat:,.2f}")
    m3.metric("Settlement Success", success_rate)

    st.divider()

    left_col, right_col = st.columns([1.5, 1], gap="large")

    with left_col:
        st.subheader("Transaction Ledger")

        for idx, txn in enumerate(st.session_state.ledger):
            with st.container(border=True):
                c1, c2, c3 = st.columns([2, 1, 1])
                c1.write(f"**{txn['ref']}**\n\n{txn['date']}")
                c2.markdown(f":green[{txn['status']}]")
                c3.markdown(f"**ZAR {txn['total']:,.2f}**")

                if st.button("View Invoice", key=f"invoice_{idx}", use_container_width=True):
                    st.session_state.active_invoice = txn

    with right_col:
        render_invoice_preview(st.session_state.active_invoice)
