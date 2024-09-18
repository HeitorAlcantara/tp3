from services.services import dashboard_goals, upload_csv_file, selection_box, button_show_dataframe, filter_by_continent
import streamlit as st


def main() -> None:
    dashboard_goals()
    csv_file = upload_csv_file()
    st.divider()
    selection_box(csv_file)
    st.divider()
    filter_by_continent(csv_file)
    st.divider()
    button_show_dataframe(csv_file)


if __name__ == "__main__":
    main()
    pass