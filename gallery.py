import streamlit as st

from data.artworks import ARTWORKS
from components.artwork_card import render_artwork_card


def render_gallery_page():
    st.title("🎨 Art Discovery Portal")

    st.markdown(
        """
        <div class="hero-box">
            <h3 style="margin-bottom: 0.4rem;">Discover premium art in a more immersive way</h3>
            <p class="small-muted" style="margin-bottom: 0;">
                Browse curated works, build your collection, and test a stronger digital art-buying experience.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, mid, right = st.columns([2, 1, 1])

    with left:
        search = st.text_input(
            "🔍 Search artworks, artists, or medium",
            placeholder="Try: Elena, sculpture, abstract...",
        )

    with mid:
        categories = sorted({art["category"] for art in ARTWORKS})
        selected_category = st.selectbox("Category", ["All"] + categories)

    with right:
        sort_by = st.selectbox(
            "Sort by",
            ["Featured", "Price: Low to High", "Price: High to Low", "Artist A-Z"],
        )

    st.divider()

    filtered_artworks = []
    search_lower = search.strip().lower()

    for art in ARTWORKS:
        matches_search = (
            search_lower in art["title"].lower()
            or search_lower in art["artist"].lower()
            or search_lower in art["medium"].lower()
            or search_lower in art["category"].lower()
            or search_lower == ""
        )

        matches_category = selected_category == "All" or art["category"] == selected_category

        if matches_search and matches_category:
            filtered_artworks.append(art)

    if sort_by == "Featured":
        filtered_artworks.sort(key=lambda x: (not x["featured"], x["title"]))
    elif sort_by == "Price: Low to High":
        filtered_artworks.sort(key=lambda x: x["price"])
    elif sort_by == "Price: High to Low":
        filtered_artworks.sort(key=lambda x: x["price"], reverse=True)
    elif sort_by == "Artist A-Z":
        filtered_artworks.sort(key=lambda x: x["artist"])

    if not filtered_artworks:
        st.warning("No artworks match your current filters.")
        return

    cols = st.columns(3)
    for idx, artwork in enumerate(filtered_artworks):
        with cols[idx % 3]:
            render_artwork_card(artwork)
