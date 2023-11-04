import time
import mysql.connector
import streamlit as st
# ----------------------------------------------------------------------------------------------------------------------------------------

st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:65px'>Compare</h1>", unsafe_allow_html=True)
st.markdown("<br><hr>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------------------------------------------------------

#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "ThisIsMahPass", database = "MahDatabase")  
  
#printing the connection object   
print(myconn)   
  
#creating the cursor object  
cur = myconn.cursor()
# ----------------------------------------------------------------------------------------------------------------------------------------

Nums_of = st.select_slider('Compare:', [2, 3])

if Nums_of == 2:

    col1c, col2c = st.columns(2)

    with col1c:

        brandsa = st.multiselect('Choose Brand:', ['Samsung', 'Xiaomi', 'Asus', 'Google', 'Oneplus', 'Infinix', 'Oppo', 'Vivo'], default="Samsung", key="a1", max_selections=1)       
        brandsa = brandsa[0]
        query = f"SELECT Name FROM dav_package.WholeDataset WHERE Brand = '{brandsa}';"
        cur.execute(query)
        resulta = cur.fetchall()
        st.markdown("<br>", unsafe_allow_html=True)  

        for i in range(0, len(resulta)):
            resulta[i] = resulta[i][0]

        Namesa = st.selectbox('Choose Phone:', resulta, key="a2")

        query = f"SELECT * FROM dav_package.WholeDataset WHERE Name = '{Namesa}';"
        cur.execute(query)
        resulta = cur.fetchall()
        st.markdown("<br>", unsafe_allow_html=True)  

        for i in range(0, len(resulta)):

            Linkq    = resulta[i][0]
            Imageq   = resulta[i][1]
            Nameq    = resulta[i][3]
            RDq      = resulta[i][4]
            Weightq  = resulta[i][5]
            OSq      = resulta[i][6]
            Storageq = resulta[i][7]
            SSq      = resulta[i][8]
            SRq      = resulta[i][9]
            RAMq     = resulta[i][10]
            Batteryq = resulta[i][11]
            Cameraq  = resulta[i][12]
            Priceq   = resulta[i][13]

            Nameq = Nameq.split(" ", 1).pop(1)
            st.markdown(f"<h1 style='text-align:center; color : #E8570E; font-size:45px'>{Nameq}</h1>", unsafe_allow_html=True)
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown(f"""<img src="{Imageq}" style="display: block; margin-left: 100px; margin-right: 100px; width:50%; height:50%; object-fit: cover; display: block;margin-right: 20px;">""", unsafe_allow_html=True)
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown(f"""<ul text-align:center;><li style="font-size:20px">Release Date &nbsp; : &nbsp; {RDq}</li><li style="font-size:20px">Weight &nbsp; : &nbsp; {Weightq} grams</li><li style="font-size:20px">OS &nbsp; : &nbsp; {OSq}</li><li style="font-size:20px">Storage &nbsp; : &nbsp; {Storageq} GB</li><li style="font-size:20px">Screen Size &nbsp; : &nbsp; {SSq}"</li><li style="font-size:20px">Resolution &nbsp; : &nbsp; {SRq} Pixels</li><li style="font-size:20px">RAM &nbsp; : &nbsp; {RAMq} GB</li><li style="font-size:20px">Battery &nbsp; : &nbsp; {Batteryq} mAh</li><li style="font-size:20px">Camera &nbsp; : &nbsp; {Cameraq} MP</li><li style="font-size:20px">Price &nbsp; : &nbsp; Rs. {Priceq}</li></ul>""", unsafe_allow_html=True)

        st.markdown("<br><hr><br>", unsafe_allow_html=True)


    with col2c:

        brandsb = st.multiselect('Choose Brand:', ['Samsung', 'Xiaomi', 'Asus', 'Google', 'Oneplus', 'Infinix', 'Oppo', 'Vivo'], default="Samsung", key="b1", max_selections=1)       
        brandsb = brandsb[0]
        query = f"SELECT Name FROM dav_package.WholeDataset WHERE Brand = '{brandsb}';"
        cur.execute(query)
        resultb = cur.fetchall()
        st.markdown("<br>", unsafe_allow_html=True)  

        for i in range(0, len(resultb)):
            resultb[i] = resultb[i][0] 

        Namesb = st.selectbox('Choose Phone:', resultb, key="b2")

        query = f"SELECT * FROM dav_package.WholeDataset WHERE Name = '{Namesb}';"
        cur.execute(query)
        resultb = cur.fetchall()
        st.markdown("<br>", unsafe_allow_html=True)  

        for i in range(0, len(resultb)):

            Linkq    = resultb[i][0]
            Imageq   = resultb[i][1]
            Nameq    = resultb[i][3]
            RDq      = resultb[i][4]
            Weightq  = resultb[i][5]
            OSq      = resultb[i][6]
            Storageq = resultb[i][7]
            SSq      = resultb[i][8]
            SRq      = resultb[i][9]
            RAMq     = resultb[i][10]
            Batteryq = resultb[i][11]
            Cameraq  = resultb[i][12]
            Priceq   = resultb[i][13]

            Nameq = Nameq.split(" ", 1).pop(1)
            st.markdown(f"<h1 style='text-align:center; color : #E8570E; font-size:45px'>{Nameq}</h1>", unsafe_allow_html=True)
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown(f"""<img src="{Imageq}" style="display: block; margin-left: 100px; margin-right: 100px; width:50%; height:50%; object-fit: cover; display: block;margin-right: 20px;">""", unsafe_allow_html=True)
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown(f"""<ul text-align:center;><li style="font-size:20px">Release Date &nbsp; : &nbsp; {RDq}</li><li style="font-size:20px">Weight &nbsp; : &nbsp; {Weightq} grams</li><li style="font-size:20px">OS &nbsp; : &nbsp; {OSq}</li><li style="font-size:20px">Storage &nbsp; : &nbsp; {Storageq} GB</li><li style="font-size:20px">Screen Size &nbsp; : &nbsp; {SSq}"</li><li style="font-size:20px">Resolution &nbsp; : &nbsp; {SRq} Pixels</li><li style="font-size:20px">RAM &nbsp; : &nbsp; {RAMq} GB</li><li style="font-size:20px">Battery &nbsp; : &nbsp; {Batteryq} mAh</li><li style="font-size:20px">Camera &nbsp; : &nbsp; {Cameraq} MP</li><li style="font-size:20px">Price &nbsp; : &nbsp; Rs. {Priceq}</li></ul>""", unsafe_allow_html=True)

        st.markdown("<br><hr><br>", unsafe_allow_html=True)


if Nums_of == 3:

    col1c, col2c, col3c = st.columns(3)

    with col1c:

        brandsa1 = st.multiselect('Choose Brand:', ['Samsung', 'Xiaomi', 'Asus', 'Google', 'Oneplus', 'Infinix'], default="Samsung", key="a11", max_selections=1)       
        brandsa1 = brandsa1[0]
        query = f"SELECT Name FROM dav_package.WholeDataset WHERE Brand = '{brandsa1}';"
        cur.execute(query)
        resulta1 = cur.fetchall()
        st.markdown("<br>", unsafe_allow_html=True)  

        for i in range(0, len(resulta1)):
            resulta1[i] = resulta1[i][0]

        Namesa1 = st.selectbox('Choose Phone:', resulta1, key="a21")

        query = f"SELECT * FROM dav_package.WholeDataset WHERE Name = '{Namesa1}';"
        cur.execute(query)
        resulta1 = cur.fetchall()
        st.markdown("<br>", unsafe_allow_html=True)  

        for i in range(0, len(resulta1)):

            Linkq    = resulta1[i][0]
            Imageq   = resulta1[i][1]
            Nameq    = resulta1[i][3]
            RDq      = resulta1[i][4]
            Weightq  = resulta1[i][5]
            OSq      = resulta1[i][6]
            Storageq = resulta1[i][7]
            SSq      = resulta1[i][8]
            SRq      = resulta1[i][9]
            RAMq     = resulta1[i][10]
            Batteryq = resulta1[i][11]
            Cameraq  = resulta1[i][12]
            Priceq   = resulta1[i][13]

            Nameq = Nameq.split(" ", 1).pop(1)
            st.markdown(f"<h1 style='text-align:center; color : #E8570E; font-size:45px'>{Nameq}</h1>", unsafe_allow_html=True)
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown(f"""<img src="{Imageq}" style="display: block; margin-left: 100px; margin-right: 100px; width:50%; height:50%; object-fit: cover; display: block;margin-right: 20px;">""", unsafe_allow_html=True)
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown(f"""<ul text-align:center;><li style="font-size:20px">Release Date &nbsp; : &nbsp; {RDq}</li><li style="font-size:20px">Weight &nbsp; : &nbsp; {Weightq} grams</li><li style="font-size:20px">OS &nbsp; : &nbsp; {OSq}</li><li style="font-size:20px">Storage &nbsp; : &nbsp; {Storageq} GB</li><li style="font-size:20px">Screen Size &nbsp; : &nbsp; {SSq}"</li><li style="font-size:20px">Resolution &nbsp; : &nbsp; {SRq} Pixels</li><li style="font-size:20px">RAM &nbsp; : &nbsp; {RAMq} GB</li><li style="font-size:20px">Battery &nbsp; : &nbsp; {Batteryq} mAh</li><li style="font-size:20px">Camera &nbsp; : &nbsp; {Cameraq} MP</li><li style="font-size:20px">Price &nbsp; : &nbsp; Rs. {Priceq}</li></ul>""", unsafe_allow_html=True)

        st.markdown("<br><hr><br>", unsafe_allow_html=True)

    with col2c:

        brandsb1 = st.multiselect('Choose Brand:', ['Samsung', 'Xiaomi', 'Asus', 'Google', 'Oneplus', 'Infinix'], default="Samsung", key="b11", max_selections=1)       
        brandsb1 = brandsb1[0]
        query = f"SELECT Name FROM dav_package.WholeDataset WHERE Brand = '{brandsb1}';"
        cur.execute(query)
        resultb1 = cur.fetchall()
        st.markdown("<br>", unsafe_allow_html=True)  

        for i in range(0, len(resultb1)):
            resultb1[i] = resultb1[i][0] 

        Namesb1 = st.selectbox('Choose Phone:', resultb1, key="b21")

        query = f"SELECT * FROM dav_package.WholeDataset WHERE Name = '{Namesb1}';"
        cur.execute(query)
        resultb1 = cur.fetchall()
        st.markdown("<br>", unsafe_allow_html=True)  

        for i in range(0, len(resultb1)):

            Linkq    = resultb1[i][0]
            Imageq   = resultb1[i][1]
            Nameq    = resultb1[i][3]
            RDq      = resultb1[i][4]
            Weightq  = resultb1[i][5]
            OSq      = resultb1[i][6]
            Storageq = resultb1[i][7]
            SSq      = resultb1[i][8]
            SRq      = resultb1[i][9]
            RAMq     = resultb1[i][10]
            Batteryq = resultb1[i][11]
            Cameraq  = resultb1[i][12]
            Priceq   = resultb1[i][13]

            Nameq = Nameq.split(" ", 1).pop(1)
            st.markdown(f"<h1 style='text-align:center; color : #E8570E; font-size:45px'>{Nameq}</h1>", unsafe_allow_html=True)
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown(f"""<img src="{Imageq}" style="display: block; margin-left: 100px; margin-right: 100px; width:50%; height:50%; object-fit: cover; display: block;margin-right: 20px;">""", unsafe_allow_html=True)
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown(f"""<ul text-align:center;><li style="font-size:20px">Release Date &nbsp; : &nbsp; {RDq}</li><li style="font-size:20px">Weight &nbsp; : &nbsp; {Weightq} grams</li><li style="font-size:20px">OS &nbsp; : &nbsp; {OSq}</li><li style="font-size:20px">Storage &nbsp; : &nbsp; {Storageq} GB</li><li style="font-size:20px">Screen Size &nbsp; : &nbsp; {SSq}"</li><li style="font-size:20px">Resolution &nbsp; : &nbsp; {SRq} Pixels</li><li style="font-size:20px">RAM &nbsp; : &nbsp; {RAMq} GB</li><li style="font-size:20px">Battery &nbsp; : &nbsp; {Batteryq} mAh</li><li style="font-size:20px">Camera &nbsp; : &nbsp; {Cameraq} MP</li><li style="font-size:20px">Price &nbsp; : &nbsp; Rs. {Priceq}</li></ul>""", unsafe_allow_html=True)

        st.markdown("<br><hr><br>", unsafe_allow_html=True)
    
    with col3c:

        brandsc1 = st.multiselect('Choose Brand:', ['Samsung', 'Xiaomi', 'Asus', 'Google', 'Oneplus', 'Infinix'], default="Samsung", key="c11", max_selections=1)       
        brandsc1 = brandsc1[0]
        query = f"SELECT Name FROM dav_package.WholeDataset WHERE Brand = '{brandsc1}';"
        cur.execute(query)
        resultc1 = cur.fetchall()
        st.markdown("<br>", unsafe_allow_html=True)  

        for i in range(0, len(resultc1)):
            resultc1[i] = resultc1[i][0] 

        Namesc1 = st.selectbox('Choose Phone:', resultc1, key="c21")

        query = f"SELECT * FROM dav_package.WholeDataset WHERE Name = '{Namesc1}';"
        cur.execute(query)
        resultc1 = cur.fetchall()
        st.markdown("<br>", unsafe_allow_html=True)  

        for i in range(0, len(resultc1)):

            Linkq    = resultc1[i][0]
            Imageq   = resultc1[i][1]
            Nameq    = resultc1[i][3]
            RDq      = resultc1[i][4]
            Weightq  = resultc1[i][5]
            OSq      = resultc1[i][6]
            Storageq = resultc1[i][7]
            SSq      = resultc1[i][8]
            SRq      = resultc1[i][9]
            RAMq     = resultc1[i][10]
            Batteryq = resultc1[i][11]
            Cameraq  = resultc1[i][12]
            Priceq   = resultc1[i][13]

            Nameq = Nameq.split(" ", 1).pop(1)
            st.markdown(f"<h1 style='text-align:center; color : #E8570E; font-size:45px'>{Nameq}</h1>", unsafe_allow_html=True)
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown(f"""<img src="{Imageq}" style="display: block; margin-left: 100px; margin-right: 100px; width:50%; height:50%; object-fit: cover; display: block;margin-right: 20px;">""", unsafe_allow_html=True)
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown(f"""<ul text-align:center;><li style="font-size:20px">Release Date &nbsp; : &nbsp; {RDq}</li><li style="font-size:20px">Weight &nbsp; : &nbsp; {Weightq} grams</li><li style="font-size:20px">OS &nbsp; : &nbsp; {OSq}</li><li style="font-size:20px">Storage &nbsp; : &nbsp; {Storageq} GB</li><li style="font-size:20px">Screen Size &nbsp; : &nbsp; {SSq}"</li><li style="font-size:20px">Resolution &nbsp; : &nbsp; {SRq} Pixels</li><li style="font-size:20px">RAM &nbsp; : &nbsp; {RAMq} GB</li><li style="font-size:20px">Battery &nbsp; : &nbsp; {Batteryq} mAh</li><li style="font-size:20px">Camera &nbsp; : &nbsp; {Cameraq} MP</li><li style="font-size:20px">Price &nbsp; : &nbsp; Rs. {Priceq}</li></ul>""", unsafe_allow_html=True)

        st.markdown("<br><hr><br>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------------------------------------------------------------------

# disconnecting from server
myconn.close()

# -----------------------------------------------------------------------------------------------------------------------------------------