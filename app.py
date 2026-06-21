# app.py

import streamlit as st

st.set_page_config(page_title="My Streamlit Page", layout="centered")

# --- Hero / Home Section ---
st.title("Welcome")
st.markdown(
    "#### Experience simplicity and clarity  \n"
    "A modern, minimalist web app showcasing smooth navigation, professional insights, and easy reach-out options."
)
st.button("Explore My Page")  # visual prompt to scroll down (no anchor possible in Streamlit)

st.divider()

# --- About Section ---
st.subheader("This Is My Page")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Professional Summary**")
    st.write(
        "Passionate software engineer with extensive experience in creating\n"
        "clean and user-friendly web applications. Dedicated to best practices in\n"
        "frontend and backend design."
    )

with col2:
    st.markdown("**Skills Grid**")
    st.write(
        "- Python\n"
        "- Streamlit\n"
        "- Frontend UI/UX\n"
        "- Responsive Design"
    )

with col3:
    st.markdown("**Mission Statement**")
    st.write(
        "Deliver high-quality, performant applications that\n"
        "offer intuitive user experiences and robust results."
    )

st.divider()

# --- Highlights Section ---
st.markdown("### Highlights")

col_a, col_b, col_c = st.columns(3)
with col_a:
    with st.expander("Project 1"):
        st.write("Clean placeholder for exciting Project One showcase.")
with col_b:
    with st.expander("Service 2"):
        st.write("Interactive description or insights about Service Two.")
with col_c:
    with st.expander("Featured Content 3"):
        st.write("Highlighting third key content with engagement details.")

st.divider()

# --- Contact & Footer Section ---
st.caption("Get in touch:")
st.link_button(
    label="💬 Chat on WhatsApp",
    url="https://wa.me/03713122237",  # Replace with your actual WhatsApp number (country code + number)
    use_container_width=True,
    type="primary",
)
st.write("📧 Email: youremail@example.com  |  🔗 LinkedIn: linkedin.com/in/yourprofile  |  🐙 GitHub: github.com/yourhandle")

st.divider()

st.markdown(
    """
    <center style="color: gray; font-size: small;">
    © 2024 Your Name — Created with Streamlit
    </center>
    """,
    unsafe_allow_html=True
  )
      
