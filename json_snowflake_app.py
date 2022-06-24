import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("Order Delivery status")
streamlit.header("Order not delivered yet")
