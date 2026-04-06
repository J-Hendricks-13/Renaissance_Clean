import streamlit as st


def render_invoice_preview(invoice: dict | None):
    st.subheader("Invoice Preview")

    if not invoice:
        st.info("Select a transaction to preview.")
        return

    st.markdown(
        f"""
        <div style="font-family: sans-serif; padding: 10px; border: 1px solid #ececec; border-radius: 14px; background: white;">
            <h2 style="color: #FF4B00; margin-bottom: 0.5rem;">RENAISSANCE</h2>
            <p style="font-size: 12px; color: #555;">
                Tax Invoice: <b>{invoice['ref']}</b><br>
                Date: {invoice['date']}
            </p>
            <hr>
            <table style="width: 100%; font-size: 14px;">
                <tr>
                    <td>Subtotal (Excl. VAT)</td>
                    <td style="text-align: right;">ZAR {invoice['subtotal']:,.2f}</td>
                </tr>
                <tr>
                    <td>VAT (15.0%)</td>
                    <td style="text-align: right;">ZAR {invoice['vat']:,.2f}</td>
                </tr>
                <tr style="font-weight: bold;">
                    <td style="padding-top: 10px;">Total (Incl. VAT)</td>
                    <td style="text-align: right; padding-top: 10px;">ZAR {invoice['total']:,.2f}</td>
                </tr>
            </table>
            <hr>
            <p style="font-size: 12px; color: #666; margin-bottom: 0;">
                Status: {invoice['status']}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
