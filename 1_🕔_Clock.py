import streamlit as st
import time
from zoneinfo import ZoneInfo, available_timezones
from datetime import datetime


st.set_page_config(
  page_title="Clock",
  page_icon="🕔"
)




#link_gif = "https://www.icegif.com/wp-content/uploads/snow-icegif-29.gif" 
link_gif = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/a2205e2c-52eb-46b3-89fb-bd0fd5da780e/dbyn08r-83e1c070-bfa6-48da-ae25-b7d7409639fe.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2EyMjA1ZTJjLTUyZWItNDZiMy04OWZiLWJkMGZkNWRhNzgwZVwvZGJ5bjA4ci04M2UxYzA3MC1iZmE2LTQ4ZGEtYWUyNS1iN2Q3NDA5NjM5ZmUuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.pFhMtU06SUSgNo6CA5fLFNJlv9h69s9oE89E2E6iAGk"
color = "white"

#link_gif = "https://f8n-production.s3.us-east-2.amazonaws.com/collections/awzn1l17u-beach%20relax-export.gif"
#color = "black"


if "timezones" not in st.session_state:
    timezones = available_timezones()
    filtered_time_zones = [tz for tz in timezones if "/" in tz and "Etc" not in tz]
    st.session_state.timezones = filtered_time_zones.sort()

if "timezone" not in st.session_state:
    st.session_state.timezone = "Europe/Rome"    

zoneinfo = ZoneInfo(st.session_state.timezone)
dt = datetime.now(zoneinfo)
  

time_to_print = dt.strftime("%H:%M:%S")
date_to_print = dt.strftime("%a %d/%m/%Y")
    
st.title("")

hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </stile>
"""
st_title = f"""
<div style="position: absolute; top: 150px; left: -200px; height: 100vh; font-size: 35px; font-weight: bold; color: {color}">
    {date_to_print}
</div>
"""
st.markdown(st_title, unsafe_allow_html=True)
st.markdown(hide_st_style, unsafe_allow_html=True)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url({link_gif});
background-size: 100% auto;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
margin-top:-140px;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""



print_m = f"""<div style="display: flex; justify-content: center; align-items: center; height: 100vh; font-size: 100px; font-weight: bold; margin-top: -100px; color: {color}">
    {time_to_print}
</div>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown(print_m, unsafe_allow_html=True)
time.sleep(1)
st.rerun()