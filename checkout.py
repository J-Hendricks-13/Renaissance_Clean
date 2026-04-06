import streamlit as st
import time


VAT_RATE = 0.15


def remove_cart_item(index: int):
    removed = st.session_state.cart.pop(index)
    st.toast(f"{removed['title']} removed from cart.", icon="🗑️")


def generate_transaction(total_val: float):
    subtotal = total_val / (1 + VAT_RATE)
    vat_amt = total_val - subtotal

    transaction = {
        "ref": f"PAY-BANK-{int(time.time())}",
        "date": time.strftime("%Y-%m-%d %H:%M"),
        "total": total_val,
        "subtotal": subtotal,
        "vat": vat_amt,
        "status": "Settled",
    }

    st.session_state.ledger.append(transaction)
    st.session_state.active_invoice = transaction
    st.session_state.cart = []


def render_checkout_page():
    st.title("💳 Cart & Checkout")

    if not st.session_state.cart:
        st.info("Your cart is empty. Start your collection in the portal.")
        return

    total_val = sum(item["price"] for item in st.session_state.cart)

    left_col, right_col = st.columns([1, 2], gap="large")

    with left_col:
        st.subheader("Your Selection")

        for idx, item in enumerate(st.session_state.cart):
            with st.expander(f"{item['title']} — ZAR {item['price']:,}"):
                st.image(item["image"], use_container_width=True)
                st.caption(f"{item['artist']} • {item['category']} • {item['medium']}")
                if st.button("Remove Item", key=f"remove_{idx}", use_container_width=True):
                    remove_cart_item(idx)
                    st.rerun()

        st.divider()
        st.metric("Total Payable", f"ZAR {total_val:,.2f}")

    with right_col:
        st.markdown(
            "<div style='text-align: left; margin-bottom: 20px;'><span style='color: #666;'>← Add money</span><br><span style='font-size: 14px; color: #888;'>Amount (ZAR)</span></div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<h1 style='margin-top: -20px;'>{total_val:,.2f}</h1>",
            unsafe_allow_html=True,
        )

        tab_bank, tab_card, tab_other = st.tabs(
            ["⚡ Pay by Bank", "💳 Card Payment", "🏛️ Alternative Methods"]
        )

        with tab_bank:
            st.markdown(
                """
                <div class="payment-option-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-weight: bold; font-size: 18px;">Pay by bank</span>
                        <span class="bank-badge">Recommended</span>
                    </div>
                    <p style="color: #444; margin-top: 10px;">
                        Make a <b>fast, secure</b> payment from your bank account.
                    </p>
                    <div style="margin: 15px 0;">
                        <span class="bank-dot" style="background-color: #E21E26;"></span>
                        <span class="bank-dot" style="background-color: #0069B3;"></span>
                        <span class="bank-dot" style="background-color: #009639;"></span>
                        <span class="bank-dot" style="background-color: #FFCD00;"></span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button("Confirm & Pay via Bank", type="primary", use_container_width=True):
                with st.status("Linking to Secure Banking Gateway...", expanded=True) as status:
                    time.sleep(1)
                    generate_transaction(total_val)
                    status.update(label="Payment Verified!", state="complete")

                st.balloons()
                st.rerun()

        with tab_card:
            st.info("Card payment is available in the full production version.")

        with tab_other:
            st.info("Alternative methods can be added later based on client requirements.")
