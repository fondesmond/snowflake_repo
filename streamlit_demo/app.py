import streamlit as st
import datetime
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

st.title("Customer Analytics Dashboard")
st.write("Live data from `DE_TUTORIAL.RAW.CUSTOMERS`")

session = get_active_session()

# 1. Add the interactive date picker widget
# Defaulting to Sept 1, 2026 to match your mock data
selected_date = st.date_input("Show customers who joined on or after:", datetime.date(2026, 9, 1))

# 2. Filter the Snowpark DataFrame natively in Snowflake
filtered_df = session.table("CUSTOMERS").filter(col("JOIN_DATE") >= selected_date)

# 3. Pull only the filtered data into Pandas
pdf = filtered_df.to_pandas()

st.subheader("Raw Data")
st.dataframe(pdf, use_container_width=True)

st.subheader("Signups Over Time")
if not pdf.empty:
    chart_data = pdf.groupby('JOIN_DATE').size().reset_index(name='COUNT')
    st.bar_chart(data=chart_data, x='JOIN_DATE', y='COUNT')
else:
    st.warning("No customers found for the selected date range.")
