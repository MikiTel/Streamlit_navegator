import streamlit as st
from google.cloud import bigquery

# Set up BigQuery client
client = bigquery.Client()

# Streamlit app code
def main():
    st.title("Data Filtering and Update with Streamlit and BigQuery")

    # Enter your BigQuery project ID and dataset ID
    project_id = st.text_input("Project ID")
    dataset_id = st.text_input("Dataset ID")
    table_name = st.text_input("Table Name")

    if project_id and dataset_id and table_name:
        # Query BigQuery table
        query = f"SELECT * FROM `{project_id}.{dataset_id}.{table_name}`"
        table = client.query(query).to_dataframe()

        # Pagination
        page_size = st.number_input("Page Size", value=10)
        page_number = st.number_input("Page Number", min_value=1, step=1, value=1)
        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size
        paginated_table = table[start_index:end_index]

        # Display paginated table
        st.write(paginated_table)

        # Select column to filter
        filter_col = st.selectbox("Select column to filter", table.columns)

        # Get unique values from selected column
        filter_values = table[filter_col].unique()
        selected_value = st.selectbox("Select filter value", filter_values)

        # Filter the data based on user input
        filtered_data = table[table[filter_col] == selected_value]

        # Display filtered data
        st.write(filtered_data)

        table_name_output = st.text_input("Table Name for Output",'table_cluster')
        # Update data in BigQuery
        if st.button("Update Data in BigQuery"):
            # Insert filtered data into BigQuery table
            filtered_data.to_gbq(
                f"{project_id}.{dataset_id}.{table_name_output}",
                project_id=project_id,
                if_exists="append"
            )
            st.write("Table loaded!")

# Run the Streamlit app
if __name__ == '__main__':
    main()
