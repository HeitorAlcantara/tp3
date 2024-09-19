from services.services import dashboard_goals, upload_csv_file, csv_file_to_dataframe, selection_box, expander_show_dataframe, filter_by_continent
import streamlit as st


def main() -> None:
    dashboard_goals()
    csv_file = upload_csv_file()
    pd_dataframe = csv_file_to_dataframe(csv_file)
    st.divider()
    selection_box(pd_dataframe)
    st.divider()
    filter_by_continent(pd_dataframe)
    st.divider()
    expander_show_dataframe(pd_dataframe)


if __name__ == "__main__":
    main()
    pass