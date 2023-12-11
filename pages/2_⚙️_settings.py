import streamlit as st
from zoneinfo import available_timezones
import base64


st.set_page_config(
  page_title="Clock",
  page_icon="🕔"
)
st.title("Settings:")

hide_st_style = """<style> header {visibility: hidden;} footer {visibility: hidden;} </stile>"""
st.markdown(hide_st_style, unsafe_allow_html=True)

if "timezone" not in st.session_state:
    st.session_state.timezone = "Europe/Rome"  

if "color" not in st.session_state:
    st.session_state.color = "#ffffff"
    
if "screen_dim" not in st.session_state:
    st.session_state.screen_dim = [1920, 1080]

if "timezones" not in st.session_state:
    #timezones to execute in the following format Area/Main_City
    timezones = available_timezones()
    filtered_time_zones = [tz for tz in timezones if "/" in tz and "Etc" not in tz] #removal of undesired timez
    filtered_time_zones.sort()
    st.session_state.timezones = filtered_time_zones

if "timezones_tp" not in st.session_state:
  #timezones to print in the following format Area: Main City
  timezones_tp = []
  for elem in st.session_state.timezones:
    elem = elem.replace("/", ": ", 1)
    elem = elem.replace("/", " ")
    elem =elem.replace("_", " ")
    timezones_tp.append(elem)
  st.session_state.timezones_tp = timezones_tp


if "image" not in st.session_state:
    st.session_state.image = "https://f8n-production.s3.us-east-2.amazonaws.com/collections/awzn1l17u-beach%20relax-export.gif"

#function to change format from printable to executable
def format_funct(val):
  i = st.session_state.timezones.index(val)
  return st.session_state.timezones_tp[i]

#function to extract the index of the current timezone:
def get_index(val):
  return st.session_state.timezones.index(val)
def get_image_data_url(img_bytes):
    encoded = base64.b64encode(img_bytes).decode()
    return f"data:image/png;base64,{encoded}"
#save timezone value:
st.session_state.timezone = st.selectbox("Select Timezone:", st.session_state.timezones, index=get_index(st.session_state.timezone), format_func=format_funct, placeholder="Europe: Italy")

st.session_state.color = st.color_picker("select a color", st.session_state.color)

st.session_state.screen_dim[0] = st.number_input("select width pixels", min_value=1, value = st.session_state.screen_dim[0])
st.session_state.screen_dim[1] = st.number_input("select height pixels", min_value=1, value = st.session_state.screen_dim[1])

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg", "gif"])
if uploaded_file is not None:
  st.session_state.image = get_image_data_url(uploaded_file.read())