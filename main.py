import streamlit as st
from pages import home, batting, pitching

st.set_option('deprecation.showPyplotGlobalUse', False)

PAGES = {
    "Home": home,
    "Batting Visualizations": batting,
    "Pitching Visualizations": pitching
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()