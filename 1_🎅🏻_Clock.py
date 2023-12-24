import streamlit as st
import time
from zoneinfo import ZoneInfo
from datetime import datetime
import base64

st.set_page_config(
  page_title="Clock",
  page_icon="🎄"
)
st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </stile>
    """, unsafe_allow_html=True)



#link_gif = "https://www.icegif.com/wp-content/uploads/snow-icegif-29.gif" 
#link_gif = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/a2205e2c-52eb-46b3-89fb-bd0fd5da780e/dbyn08r-83e1c070-bfa6-48da-ae25-b7d7409639fe.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2EyMjA1ZTJjLTUyZWItNDZiMy04OWZiLWJkMGZkNWRhNzgwZVwvZGJ5bjA4ci04M2UxYzA3MC1iZmE2LTQ4ZGEtYWUyNS1iN2Q3NDA5NjM5ZmUuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.pFhMtU06SUSgNo6CA5fLFNJlv9h69s9oE89E2E6iAGk"
#phone
#link_gif = "https://media.wallpaperchill.com/1080x2400-wallpapers/1080x2400-hd-wallpaper-s181.jpg"
#link_gif = "https://f8n-production.s3.us-east-2.amazonaws.com/collections/awzn1l17u-beach%20relax-export.gif"

def get_image_data_url(img_bytes):
    encoded = base64.b64encode(img_bytes).decode()
    return f"data:image/png;base64,{encoded}"

def music_player(id):
    return f"""<iframe style="display:none;" width="560" height="315" src="https://www.youtube.com/embed/{id}?autoplay=1&loop=1&playlist={id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>"""

def set_bg(link):
    return f"""
            <style>
            [data-testid="stAppViewContainer"] > .main {{
            background-image: url({link});
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: local;
            }}
            [data-testid="stHeader"] {{
            background: rgba(0,0,0,0);
            }}
            </style>
            """

def generate_dot(angle, color, number=None, width='8px', height='8px', left='198px', top='198px', color_t="white"):
    return f"""<div class="rectangle" style="
        width:{width};
        height: {height};
        background-color: {color};
        transform-origin: center;
        border: 1px solid rgba(0,0,0,0.1);
        position: absolute;
        left:{left};
        top:{top};
        border-radius:50%;
        transform: rotate({angle-90}deg) translate(200px) rotate(100deg);
    "></div>"""

def play_sound(link):
    html_string = f"""
            <audio autoplay>
              <source src="{link}" type="audio/mp3">
            </audio>
            """
    st.markdown(html_string, unsafe_allow_html=True)

def generate_number(angle, color, number=None, width='8px', height='16px', left='190px', top='190px', color_t="white"):
    css = f"""<div class="rectangle" style="
        width:24px;
        height: 24px;
        background-color: {color};
        transform-origin: center;
        border: 1px solid rgba(0,0,0,0.1);
        position: absolute;
        left:{left};
        top:{top};
        border-radius:3px;
        transform: rotate({angle-90}deg) translate(200px) rotate(90deg);
    ">"""
    if number is not None:
        css += f'<div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-weight:bold; font-size:60px; color: {color_t};">{number}</div>'
    css += '</div>'
    return css



def animated_timer(link_colored="#721D45", num_divisions=24):
    html_code = f'<div class="circle" style="position: fixed;top:50%;left:50%; width: 400px; height: 400px; border-radius: 50%; border: 1px transparent;transform: translate(-50%, -30%);">'
    counter = 0
    for i in range(1, num_divisions+1, 2):
        angle = (i) * (360 / num_divisions)
        html_code += generate_dot(angle, color_t = link_colored, color= "white",number=None)
        angle = (i+1) * (360 / num_divisions)
        html_code += generate_number(angle, color_t = link_colored, color = "transparent", number=i-counter)
        counter+=1
    html_code += '</div>'
    return html_code
def clock_hands(hours, minutes, url_hours, url_mins):
    deg_min = minutes * 6
    deg_h = hours * 30 + minutes/2
    
    html_code = f'<img src="{url_hours}" style="width: 400px; height: 400px;background-color:transparent; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -30%) rotate({deg_h+180}deg);">'
    html_code += f'<img src="{url_mins}" style="width: 400px; height: 400px;background-color:transparent; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -30%) rotate({deg_min}deg);">'
    return html_code
if "timeout_h" not in st.session_state:
    st.session_state.timeout_h = 22
if "timeout_m" not in st.session_state:
    st.session_state.timeout_m = 22
    
if "selected_video" not in st.session_state:
    st.session_state.selected_video = ("None","")

if "image" not in st.session_state:
    st.session_state.image = "https://a-static.besthdwallpaper.com/santa-clause-over-the-house-wallpaper-1920x1280-105223_38.jpg"

if "timezone" not in st.session_state:
    st.session_state.timezone = "Europe/Rome"    

if "color" not in st.session_state:
    st.session_state.color = "#ffffff"

if "screen_dim" not in st.session_state:
    st.session_state.screen_dim = [1920, 1080]

if "links" not in st.session_state:
    st.session_state.links = [
        "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/a2205e2c-52eb-46b3-89fb-bd0fd5da780e/dbyn08r-83e1c070-bfa6-48da-ae25-b7d7409639fe.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2EyMjA1ZTJjLTUyZWItNDZiMy04OWZiLWJkMGZkNWRhNzgwZVwvZGJ5bjA4ci04M2UxYzA3MC1iZmE2LTQ4ZGEtYWUyNS1iN2Q3NDA5NjM5ZmUuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.pFhMtU06SUSgNo6CA5fLFNJlv9h69s9oE89E2E6iAGk",
        "https://www.icegif.com/wp-content/uploads/snow-icegif-29.gif",
        "https://images3.alphacoders.com/129/1295531.jpg",
        "https://wallpaperset.com/w/full/0/0/1/94197.jpg",
        "https://cutewallpaper.org/23/christmas-snow-live-wallpaper/2297917019.jpg",      
        "https://wallpapers.com/images/featured/3d-christmas-bw37ez6p9clxblpj.jpg",
        "https://cutewallpaper.org/37x/7p7o4oi8x/187265578.jpg",
        "https://www.teahub.io/photos/full/26-266600_christmas-snow-lantern-4k-ultra-hd-desktop-wallpaper.jpg",
        "https://a-static.besthdwallpaper.com/santa-clause-over-the-house-wallpaper-1920x1280-105223_38.jpg",
        "https://i.pinimg.com/originals/d4/85/bc/d485bc64977f6683d5798bca083b8b0a.jpg"
    ]
if "minute_hand" not in st.session_state:
    st.session_state.minute_hand = r"https://github.com/SamVia/clockino/blob/christmas-clockino/images/minutes.png?raw=true"
if "hour_hand" not in st.session_state:
    st.session_state.hour_hand = r"https://github.com/SamVia/clockino/blob/christmas-clockino/images/hours.png?raw=true"
if "loaded" not in st.session_state:
    st.session_state.loaded = False
if "canstart" not in st.session_state:
    st.session_state.canstart = False    
    
st.markdown(music_player(st.session_state.selected_video[1]), unsafe_allow_html=True)
if not st.session_state.loaded:
    empty = st.empty()
    if empty.button("load images"):
        for i in range(len(st.session_state.links)):
            empty.markdown(set_bg(st.session_state.links[i]), unsafe_allow_html=True)
            time.sleep(1)
        empty.empty()
        st.session_state.loaded = True
        st.rerun()
else:
    
        
    zoneinfo = ZoneInfo(st.session_state.timezone)
    dt = datetime.now(zoneinfo)
    time_to_print = dt.strftime("%H:%M:%S")
    get_time = time_to_print.split(":")
    seconds = int(get_time[2])
    minutes = int(get_time[1])
    hours = int(get_time[0])
    time_to_print= "{:02d}:{:02d}".format(hours, minutes)
    if not st.session_state.canstart:
        if seconds < 5:
            st.session_state.canstart = True
            st.rerun()
        else:
            time.sleep(1)
            st.rerun()
    else:
        index_bg = minutes//6
        if hours >= st.session_state.timeout_h and minutes >= st.session_state.timeout_m:
            st.balloons()
            st.snow()
            play_sound(link="https://soundboardguy.com/wp-content/uploads/2022/12/santa-clause-ho-ho-ho-sound-effect-professional-and-free-mp3cut-1.mp3")
            time.sleep(10)
        if minutes == 16:
            play_sound("https://www.myinstants.com/media/sounds/clock-tower-bell_L85zGsl.mp3")
        if minutes == 18:
            play_sound("https://www.myinstants.com/media/sounds/bell.mp3")

        
        st.markdown(clock_hands(hours,minutes, st.session_state.minute_hand, st.session_state.hour_hand), unsafe_allow_html=True)
        st.markdown(animated_timer(link_colored=st.session_state.color),unsafe_allow_html=True)
        print_m = f"""<div style="
            position: fixed; 
            top: 20%; 
            left: 50%;
            transform: translate(-50%,-50%); 
            color: {st.session_state.color}; 
            font-size: 75px; 
            font-weight:bold; 
            z-index: 2;">
            {time_to_print}
            </div>"""
        st.markdown(print_m, unsafe_allow_html=True)


        st.markdown(set_bg(st.session_state.links[index_bg]), unsafe_allow_html=True)




        

        time.sleep(20)
        st.rerun()