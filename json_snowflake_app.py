import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("Order Delivery status")



#snowflake related functions
def get_running_order_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select order_details:order_id  ,order_details:user_id,order_details:user_name ,order_details:order_datetime,order_details:delivery_datetime ,order_details:status,order_details:email,order_details:origin_location ,order_details:destination_location from order_db.public.orders where order_details:status !='delivered'")
    return my_cur.fetchall()

def get_completed_order_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select order_details:order_id  ,order_details:user_id,order_details:user_name ,order_details:order_datetime,order_details:delivery_datetime ,order_details:status,order_details:email,order_details:origin_location ,order_details:destination_location from order_db.public.orders where order_details:status ='delivered'")
    return my_cur.fetchall()  
  
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows_running_order=get_running_order_list()
my_cnx.close();

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows_completed_order=get_completed_order_list()
my_cnx.close();

errorMsg="In Delivery:"+str(len(my_data_rows_running_order));
streamlit.error(errorMsg);
successMsg="Total delivered:"+str(len(my_data_rows_completed_order));
streamlit.success(successMsg);

streamlit.dataframe(my_data_rows_running_order);
streamlit.dataframe(my_data_rows_completed_order);
