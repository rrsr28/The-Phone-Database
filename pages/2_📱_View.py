import time
import streamlit as st
import mysql.connector
from streamlit_option_menu import option_menu

# ----------------------------------------------------------------------------------------------------------------------------------------

#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "ThisIsMahPass", database = "MahDatabase")  
  
#printing the connection object   
print(myconn)   
  
#creating the cursor object  
cur = myconn.cursor()
# ----------------------------------------------------------------------------------------------------------------------------------------

st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:65px'>Brands</h1>", unsafe_allow_html=True)
st.markdown("<br><hr><br>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------------------------------------------------------------
images = ["https://www.smartprix.com/bytes/wp-content/uploads/2023/01/ultra.png", "https://fdn.gsmarena.com/imgroot/news/22/12/xiaomi-13-pro-green-combo-ip-rating/-1220x526/gsmarena_001.jpg", "https://i0.wp.com/www.smartprix.com/bytes/wp-content/uploads/2022/06/Google-Pixel-7-and-Google-Pixel-7-Pro.jpg?fit=1212%2C808&ssl=1", "https://i.gadgets360cdn.com/large/asus_rog_phone_6d_ultimate_1663596377339.jpg", "https://www.01net.com/app/uploads/2022/10/Oppo-Reno-8-Pro_dos.jpg", "https://www.91-cdn.com/hub/wp-content/uploads/2023/02/Vivo-V27-India-launch-date.png"]

image_html = ''
for url in images:
    image_html += f'<img src="{url}" style="width:185px; height:500px; object-fit: cover; display: block;margin-right: 20px;">'

st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )
st.markdown("<br><hr><br>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------------------------------------------------------------

Brands = ["Samsung"]

col1a, col2a, col3a = st.columns(3)

with col1a:
    
    brands = st.multiselect('Choose Brand:', ['Samsung', 'Xiaomi', 'Asus', 'Google', 'Oneplus', 'Infinix', 'Oppo', 'Vivo'], default="Samsung")
    st.markdown("<br>", unsafe_allow_html=True)
    weights = st.slider('Maximum Weight:', 175, 300)
    st.markdown("<br>", unsafe_allow_html=True)

with col2a:
    Batteries = st.selectbox('Choose Minimum Battery mAh:', [1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500])
    st.markdown("<br>", unsafe_allow_html=True)    
    Storages = st.select_slider('Pick a Storage Size', [8, 16, 32, 64, 128, 256, 512])
    st.markdown("<br>", unsafe_allow_html=True)

with col3a:
    Prices    = st.selectbox('Choose Price:', [1000, 3000, 5000, 7000, 10000, 15000, 20000, 25000, 40000, 50000, 75000, 80000, 90000, 100000])
    st.markdown("<br>", unsafe_allow_html=True)    
    Rams = st.select_slider('Pick a RAM', [1, 1.5, 2, 3, 4, 6, 8, 12, 16, 32])
    st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------------------------------------------------------------------

string_for_q = "("
for i in range(0, len(brands)):

    string_for_q = string_for_q + ",'" + brands[i] + "'"

string_for_q = string_for_q + ")"
string_for_q = string_for_q.replace(",", "", 1)

query = f'SELECT * FROM dav_package.WholeDataset WHERE Brand IN {string_for_q} AND Weight <= {weights} AND Battery >= "{Batteries}" AND Price <= {Prices} AND RAM = {Rams} AND Storage >= {Storages};'
cur.execute(query)
result = cur.fetchall()

# -----------------------------------------------------------------------------------------------------------------------------------------

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.05)
    my_bar.progress(percent_complete + 1, text=progress_text)

time.sleep(0.1)
my_bar.empty()
st.markdown("<br><br>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------------------------------------------------------------------

for i in range(0, len(result)):

    Linkq    = result[i][0]
    Imageq   = result[i][1]
    Nameq    = result[i][3]
    RDq      = result[i][4]
    Weightq  = result[i][5]
    OSq      = result[i][6]
    Storageq = result[i][7]
    SSq      = result[i][8]
    SRq     = result[i][9]
    RAMq     = result[i][10]
    Batteryq = result[i][11]
    Cameraq  = result[i][12]
    Priceq   = result[i][13]

    col1b, col2b= st.columns(2)

    with col1b:
        st.markdown(f"""<img src="{Imageq}" style="width:50%; height:50%; object-fit: cover; display: block;margin-right: 20px;">""", unsafe_allow_html=True)

    with col2b:
        st.markdown(f"<h1 style='color : #E8570E; font-size:45px'>{Nameq}</h1>", unsafe_allow_html=True)
        st.markdown(f"""<ul><li style="font-size:17px">Realease Date &nbsp; : &nbsp; {RDq}</li><li style="font-size:17px">Weight &nbsp; : &nbsp; {Weightq} grams</li><li style="font-size:17px">OS &nbsp; : &nbsp; {OSq}</li><li style="font-size:17px">Storage &nbsp; : &nbsp; {Storageq} GB</li><li style="font-size:17px">Screen Size &nbsp; : &nbsp; {SSq}"</li><li style="font-size:17px">Resolution &nbsp; : &nbsp; {SRq} Pixels</li><li style="font-size:17px">RAM &nbsp; : &nbsp; {RAMq} GB</li><li style="font-size:17px">Battery &nbsp; : &nbsp; {Batteryq} mAh</li><li style="font-size:17px">Camera &nbsp; : &nbsp; {Cameraq} MP</li><li style="font-size:17px">Price &nbsp; : &nbsp; Rs. {Priceq}</li></ul>""", unsafe_allow_html=True)

    st.markdown("<br><hr><br>", unsafe_allow_html=True)

    
# -----------------------------------------------------------------------------------------------------------------------------------------

# disconnecting from server
myconn.close()

# -----------------------------------------------------------------------------------------------------------------------------------------