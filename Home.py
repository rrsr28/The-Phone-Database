import base64
import time
import streamlit as st
from streamlit_option_menu import option_menu

# ---------------------------------------------------------------------------------------------------------------------------------------

st.set_page_config( page_title='Home', page_icon="🏠")

# ---------------------------------------------------------------------------------------------------------------------------------------

st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:65px'>The Phone Database</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:17px'>Mining the data for your phone needs</p>", unsafe_allow_html=True)
st.markdown("<br><hr><br>", unsafe_allow_html=True)   

video_file = open('ThePhoneDatabase.mp4', 'rb')
video_da = video_file.read()

st.video(video_da)

st.markdown("<br><hr><br><p style='text-align: center; color : #E8570E; font-size:20px'>Samsung &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Xiaomi &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Google &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Asus &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Oppo &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Oneplus &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Infinix &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Vivo</p>", unsafe_allow_html=True)
st.markdown("<br><hr>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------------------------------------------------------
# New Release
# -------------
st.markdown("<p style='text-align: center; font-size:35px'>New Releases</p>", unsafe_allow_html=True)

images = ["https://www.smartprix.com/bytes/wp-content/uploads/2023/01/ultra.png", "https://fdn.gsmarena.com/imgroot/news/22/12/xiaomi-13-pro-green-combo-ip-rating/-1220x526/gsmarena_001.jpg", "https://www.91-cdn.com/hub/wp-content/uploads/2022/09/Google-Pixel-7-and-7-Pro.jpg", "https://i.gadgets360cdn.com/large/asus_rog_phone_6d_ultimate_1663596377339.jpg", "https://www.01net.com/app/uploads/2022/10/Oppo-Reno-8-Pro_dos.jpg", "https://www.91-cdn.com/hub/wp-content/uploads/2023/02/Vivo-V27-India-launch-date.png"]

image_html = ''
for url in images:
    image_html += f'<img src="{url}" style="width:2000px; height:500px; object-fit: cover; display: block;margin-right: 20px;">'

st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )
st.markdown("<br><hr>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------------------------------------------------------
# Spotlight
# ----------
st.markdown("<p style='text-align: center; font-size:35px'>Spotlight</p>", unsafe_allow_html=True)

images = ["https://www.smartprix.com/bytes/wp-content/uploads/2022/06/FUv8xvpWUAQIKJj-photoutils.com_.jpeg", "https://i.ytimg.com/vi/6bLXGf6Jhy4/maxresdefault.jpg", "https://m-cdn.phonearena.com/images/article/145268-wide-two_1200/Samsung-Galaxy-S23-Ultra-goes-official-The-best-Samsung-phone-bar-none.jpg", "https://i.ytimg.com/vi/gUkIHqna-Fw/maxresdefault.jpg", "https://images.samsung.com/in/smartphones/galaxy-s23-ultra/images/galaxy-s23-ultra-highlights-spen.jpg", "https://i.ytimg.com/vi/iY-1Bl3OVDI/maxresdefault.jpg", "https://www.ngmisr.com/wp-content/uploads/2022/06/galaxy-s23-ultra.jpg"]

image_html = ''
for url in images:
    image_html += f'<img src="{url}" style="width:2000px; height:500px; object-fit: cover; display: block;margin-right: 20px;">'

st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )
st.markdown("<br><br><br><hr>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------------------------------------------------------
# Specials
# ----------
st.markdown("<p style='text-align: center; font-size:35px'>Specials</p>", unsafe_allow_html=True)

images = ["https://www.mobigyaan.com/wp-content/uploads/2023/02/realme-10-Pro-5G-Coca-Cola-Edition-India-3.jpg", "https://imgeng.jagran.com/images/2023/feb/Realme%2010%20Pro%205G%20Cocacola%20edition1676013686417.jpg", "https://www.mobigyaan.com/wp-content/uploads/2023/02/realme-10-Pro-5G-Coca-Cola-Edition-India-2.jpg", "https://static.c.realme.com/IN/wm-thread/1623901930780667904.png"]

image_html = ''
for url in images:
    image_html += f'<img src="{url}" style="width:2000px; height:500px; object-fit: cover; display: block;margin-right: 20px;">'

st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )
st.markdown("<br><br><br><hr>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------------------------------------------------------
# Android
# --------
st.markdown("<br>", unsafe_allow_html=True)

images = ["https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/HeroHomepage_2880x1200.jpg"]

image_html = ''
for url in images:
    image_html += f'<img src="{url}" style="width:20%; height:20%; object-fit: cover; display: block;margin-right: auto; margin-left: auto;">'

st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )
st.markdown("<br><hr>", unsafe_allow_html=True)


st.markdown("""<style>.icon-container {bottom: 20px;right: 20px;} .icon-containera {display:block;margin-left: auto; margin-right:auto;}</style>""",unsafe_allow_html=True)
st.markdown(
    """
    <div class="icon-containera">
      <a href="https://www.instagram.com/" onclick="showAccount('instagram')"><img src="https://cdn4.iconfinder.com/data/icons/social-media-icons-the-circle-set/48/instagram_circle-512.png" width="30" height="30"></a>
      <a href="https://www.whatsapp.com/" onclick="showAccount('whatsapp')"><img src="https://cdn4.iconfinder.com/data/icons/social-messaging-ui-color-shapes-2-free/128/social-whatsapp-circle-512.png" width="30" height="30"></a>
      <a href="https://www.twitter.com/" onclick="showAccount('twitter')"><img src="https://cdn3.iconfinder.com/data/icons/social-icons-5/607/Twitterbird.png" width="30" height="30"></a>
      <a href="https://www.gmail.com/" onclick="showAccount('mail')"><img src="https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/gmail-512.png" width="30" height="30"></a>
    </div> """,unsafe_allow_html=True)

# ----------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------
hide_st_style = """ <style>footer{visibility:hidden;}</style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)
# -----------------------------------------------------------------------------------------------------------------------------------------
