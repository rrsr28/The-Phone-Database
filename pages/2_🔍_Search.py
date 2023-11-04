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

st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:65px'>Search</h1>", unsafe_allow_html=True)
st.markdown("<br><hr><br>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------------------------------------------------------------

query = 'SELECT Name FROM dav_package.WholeDataset'
cur.execute(query)
result = cur.fetchall()

for i in range(0, len(result)):
    result[i] = result[i][0]

Name = st.selectbox("Choose your Phone : ", result)

query = f"SELECT * FROM dav_package.WholeDataset WHERE Name LIKE '%{Name}%' "
cur.execute(query)
result = cur.fetchall()

st.markdown("<br><hr><br>", unsafe_allow_html=True)

for i in range(0, len(result)):

    Link    = result[i][0]
    Image   = result[i][1]
    Name    = result[i][3]
    RD      = result[i][4]
    Weight  = result[i][5]
    OS      = result[i][6]
    Storage = result[i][7]
    SS      = result[i][8]
    SR      = result[i][9]
    RAM     = result[i][10]
    Battery = result[i][11]
    Camera  = result[i][12]
    Price   = result[i][13]

    st.markdown(f"<h1 style='text-align: center; color : #E8570E; font-size:45px'>{Name}</h1>", unsafe_allow_html=True)
    st.markdown(f"""<br><br><img src="{Image}" style="width:25%; height:25%; object-fit: cover; display: block;margin-right: auto;margin-left:auto"><br><br>""", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:40px'>Release Date</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color : white; font-size:30px'>{RD}</p><br><hr><br>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:40px'>Weight</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color : white; font-size:30px'>{Weight} grams</p><br><hr><br>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:40px'>OS</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color : white; font-size:30px'>{OS}</p><br><hr><br>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:40px'>Storage</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color : white; font-size:30px'>{Storage} GB</p><br><hr><br>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:40px'>Screen Size</h1>", unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center; color : white; font-size:30px">{SS}"</p><br><hr><br>', unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:40px'>Screen Resolution</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color : white; font-size:30px'>{SR} pixels</p><br><hr><br>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:40px'>RAM</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color : white; font-size:30px'>{RAM} GB</p><br><hr><br>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:40px'>Battery</h1>", unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center; color : white; font-size:30px">{Battery} mAh</p><br><hr><br>', unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:40px'>Camera</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color : white; font-size:30px'>{Camera} MP</p><br><hr><br>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:40px'>Price</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color : white; font-size:30px'>₹ {Price}</p><br><hr><br>", unsafe_allow_html=True)


