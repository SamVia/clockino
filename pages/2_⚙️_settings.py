import streamlit as st
from zoneinfo import available_timezones



st.set_page_config(
  page_title="Clock",
  page_icon="🕔"
)
st.title("Settings:")

hide_st_style = """
    <style>
    header {visibility: hidden;}
    </stile>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)


if "timezones" not in st.session_state:
  
    timezones = available_timezones()
    
    filtered_time_zones = [tz for tz in timezones if "/" in tz and "Etc" not in tz]
    
    filtered_time_zones.sort()
    st.session_state.timezones = filtered_time_zones
print(st.session_state.timezones)
if "timezones_tp" not in st.session_state:
  timezones_tp = []
  for elem in st.session_state.timezones:
    elem = elem.replace("/", ": ", 1)
    elem = elem.replace("/", " ")
    elem =elem.replace("_", " ")
    timezones_tp.append(elem)
  st.session_state.timezones_tp = timezones_tp
print(st.session_state.timezones_tp)
def format_funct(val):
  i = st.session_state.timezones.index(val)
  return st.session_state.timezones_tp[i]

st.session_state.timezone = st.selectbox("Select Timezone:", st.session_state.timezones, index=424, format_func=format_funct, placeholder="Europe: Italy")

