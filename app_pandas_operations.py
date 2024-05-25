import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title
st.set_page_config(page_title='Pandas Operations App', layout='wide')

# Create a file uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display dataset overview
    st.header('Dataset Overview')
    st.dataframe(df.head())
    st.write(f'Number of rows: {len(df)}')
    st.write(f'Number of columns: {len(df.columns)}')

    # Sidebar for operation selection
    st.sidebar.header('Select Operation')
    operation = st.sidebar.selectbox('Choose an operation', [
        'Filter Data', 'Sort Data', 'Group By', 'Merge Data', 'Pivot Table', 'Apply Function', 'Aggregate'
    ])

    if operation == 'Filter Data':
        st.subheader('Filter Data')
        column = st.selectbox('Select a column', df.columns)
        condition = st.text_input('Enter a condition (e.g., > 5)')
        if condition:
            filtered_df = df.query(f'{column} {condition}')
            st.dataframe(filtered_df)

    elif operation == 'Sort Data':
        st.subheader('Sort Data')
        column = st.selectbox('Select a column', df.columns)
        ascending = st.checkbox('Ascending', value=True)
        sorted_df = df.sort_values(by=column, ascending=ascending)
        st.dataframe(sorted_df)

    elif operation == 'Group By':
        st.subheader('Group By')
        column = st.selectbox('Select a column', df.columns)
        aggregation = st.selectbox('Select an aggregation', ['count', 'mean', 'sum', 'min', 'max'])
        grouped_df = df.groupby(column).agg(aggregation)
        st.dataframe(grouped_df)

    elif operation == 'Merge Data':
        st.subheader('Merge Data')
        uploaded_file2 = st.file_uploader("Choose another CSV file", type="csv")
        if uploaded_file2 is not None:
            df2 = pd.read_csv(uploaded_file2)
            merge_column = st.selectbox('Select a column to merge on', df.columns)
            merged_df = pd.merge(df, df2, on=merge_column)
            st.dataframe(merged_df)

    elif operation == 'Pivot Table':
        st.subheader('Pivot Table')
        index_column = st.selectbox('Select an index column', df.columns)
        values_column = st.selectbox('Select a values column', df.columns)
        agg_func = st.selectbox('Select an aggregation function', ['mean', 'sum', 'count'])
        pivot_table = pd.pivot_table(df, index=index_column, values=values_column, aggfunc=agg_func)
        st.dataframe(pivot_table)

    elif operation == 'Apply Function':
        st.subheader('Apply Function')
        column = st.selectbox('Select a column', df.columns)
        function = st.text_input('Enter a function (e.g., lambda x: x * 2)')
        if function:
            transformed_df = df[column].apply(eval(function))
            st.dataframe(transformed_df)

    elif operation == 'Aggregate':
        st.subheader('Aggregate')
        agg_funcs = st.multiselect('Select aggregation functions', ['count', 'mean', 'sum', 'min', 'max'])
        if agg_funcs:
            agg_df = df.agg(agg_funcs)
            st.dataframe(agg_df)