import streamlit as st


def add_to_cart(artwork: dict):
    st.session_state.cart.append(artwork)
    st.toast(f"{artwork['title']} added to cart.", icon="✅")


def toggle_favorite(artwork_id: int):
    favorites = st.session_state.favorites

    if artwork_id in favorites:
        favorites.remove(artwork_id)
        st.toast("Removed from favorites.", icon="💔")
    else:
        favorites.append(artwork_id)
        st.toast("Saved to favorites.", icon="❤️")


def render_artwork_card(artwork: dict):
    is_favorite = artwork["id"] in st.session_state.favorites

    with st.container(border=True):
        st.image(artwork["image"], use_container_width=True)
        st.subheader(artwork["title"])
        st.markdown(f"<div class='art-meta'>By {artwork['artist']}</div>", unsafe_allow_html=True)
        st.markdown(
            f"<div class='art-meta'>{artwork['category']} • {artwork['medium']}</div>",
            unsafe_allow_html=True,
        )
        st.write(f"**ZAR {artwork['price']:,}**")
        st.caption(artwork["dimensions"])
        st.write(artwork["description"])

        col1, col2 = st.columns(2)

        with col1:
            if st.button(
                "Add to Collection",
                key=f"add_{artwork['id']}",
                use_container_width=True,
            ):
                add_to_cart(artwork)

        with col2:
            fav_label = "Unfavorite" if is_favorite else "Favorite"
            if st.button(
                fav_label,
                key=f"fav_{artwork['id']}",
                use_container_width=True,
            ):
                toggle_favorite(artwork["id"])
