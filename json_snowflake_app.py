import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("Order Delivery status")


#snowflake related functions
def get_order_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute('select order_details:"order_id" as "orderId" ,
order_details:"user_id" as "userId",
order_details:"user_name" as "UserName",
order_details:"order_datetime" as "OrderDateTime",
order_details:"delivery_datetime" as "DeliveryDatetime",
order_details:"status" as "CurrentStatus",
order_details:"email" as "UserEmail",
order_details:"origin_location" as "Origin",
order_details:"destination_location" as "Destination"
from order_db.public.orders')
    return my_cur.fetchall()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows=get_order_list()
my_cnx.close();
streamlit.dataframe(my_data_rows)
