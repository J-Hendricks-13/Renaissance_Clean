import streamlit as st

from pages.gallery import render_gallery_page
from pages.checkout import render_checkout_page
from pages.financial_ops import render_financial_ops_page
from pages.immersive_demo import render_immersive_demo_page
from pages.artist_onboarding import render_artist_onboarding_page


def initialize_session_state():
    if "cart" not in st.session_state:
        st.session_state.cart = []

    if "ledger" not in st.session_state:
        st.session_state.ledger = []

    if "favorites" not in st.session_state:
        st.session_state.favorites = []

    if "active_invoice" not in st.session_state:
        st.session_state.active_invoice = None


def inject_global_styles():
    st.markdown(
        """
        <style>
            .main-payment-box {
                background-color: #ffffff;
                padding: 30px;
                border-radius: 15px;
                border: 1px solid #f0f0f0;
                box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            }

            .payment-option-card {
                padding: 20px;
                border-radius: 12px;
                border: 1px solid #eee;
                transition: all 0.3s ease;
                cursor: pointer;
                margin-bottom: 15px;
            }

            .payment-option-card:hover {
                border-color: #FF4B00;
                background-color: #fff9f6;
                transform: translateY(-2px);
            }

            .bank-badge {
                background-color: #FF4B00;
                color: white;
                padding: 4px 12px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: 600;
            }

            .bank-dot {
                height: 15px;
                width: 15px;
                border-radius: 50%;
                display: inline-block;
                margin-right: 8px;
            }

            .art-meta {
                color: #666;
                font-size: 0.95rem;
                margin-bottom: 0.25rem;
            }

            .hero-box {
                padding: 1.25rem 1.5rem;
                border: 1px solid #ececec;
                border-radius: 18px;
                background: linear-gradient(135deg, #ffffff 0%, #faf7f4 100%);
                margin-bottom: 1rem;
            }

            .small-muted {
                color: #777;
                font-size: 0.9rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main():
    st.set_page_config(
        page_title="Renaissance Pro Demo",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    initialize_session_state()
    inject_global_styles()

    st.sidebar.title("⚜️ Renaissance")
    page = st.sidebar.radio(
        "Navigation",
        [
            "Art Discovery Portal",
            "Cart & Checkout",
            "Financial Operations",
            "Immersive Experience",
            "For Artists",
        ],
    )

    st.sidebar.divider()
    st.sidebar.metric("Cart Count", len(st.session_state.cart))
    st.sidebar.metric("Favorites", len(st.session_state.favorites))

    if page == "Art Discovery Portal":
        render_gallery_page()
    elif page == "Immersive Experience":
        render_immersive_demo_page()
    elif page == "Cart & Checkout":
        render_checkout_page()
    elif page == "Financial Operations":
        render_financial_ops_page()
    elif page == "For Artists":
        render_artist_onboarding_page()


if __name__ == "__main__":
    main()
