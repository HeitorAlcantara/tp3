from services.services import dashboard_goals, upload_csv_file 
import pandas as pd
import streamlit as st


def show_dashboard() -> None:
    dashboard_goals()
    st.divider()
    upload_csv_file()
    st.divider()


if __name__ == "__main__":
    show_dashboard()
    pass