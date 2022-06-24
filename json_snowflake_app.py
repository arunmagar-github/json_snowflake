import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("Order Delivery status")
streamlit.header("Order not delivered yet")

#snowflake related functions
def get_order_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * FROM ORDER_DB.PUBLIC.ORDERS")
    return my_cur.fetchall()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows=get_order_list()
my_cnx.close();
streamlit.dataframe(my_data_rows)
