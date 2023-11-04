import streamlit as st

# ----------------------------------------------------------------------------------------------------------------------------------------
# Flagships
# ------------------
st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:65px'>Flagships</h1>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Samsung", "Xiaomi", "Asus", "Vivo", "Oneplus"])
with tab1:

    st.title('Galaxy S23 Ultra')
    images = ["https://images.samsung.com/in/smartphones/galaxy-s23-ultra/buy/DM3-web-6.jpg", "https://images.samsung.com/in/smartphones/galaxy-s23-ultra/buy/DM3-web-1.jpg", "https://images.samsung.com/in/smartphones/galaxy-s23-ultra/buy/DM3-web-3.jpg", "https://images.samsung.com/in/smartphones/galaxy-s23-ultra/buy/DM3-web-5.jpg"]

    image_html = ''
    for url in images:
        image_html += f'<img src="{url}" style="width:2000px; height:500px; object-fit: cover; display: block;margin-right: 20px;">'

    st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )

    # ------------------------------------------------------------------------------------------
    
    st.markdown("<br><br>", unsafe_allow_html=True )
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Storage")
        st.markdown("<ul><li>256 | 12</li><li>512 | 12</li><li>1 TB | 12</li></ul>", unsafe_allow_html=True )

    with col2:
        st.header("Colour")
        st.markdown("<ul><li>Green</li><li>Cream</li><li>Phantom Black</li></ul>", unsafe_allow_html=True )

    with col3:
        st.header("Price")
        st.write("Rs. 1,24,999")
        st.markdown("""<a href="https://www.samsung.com/in/"><button style="background: linear-gradient(to bottom right, #EF4765, #FF9A5A); border: 0; border-radius: 12px; color: #FFFFFF; cursor: pointer;" >Buy</button></a>""", unsafe_allow_html=True )

    # ------------------------------------------------------------------------------------------

with tab2:

    st.title('Mi 12T Pro')
    images = ["https://assets.hardwarezone.com/img/2022/10/Xiaomi-12T-Pro_2.jpg", "https://images.fonearena.com/blog/wp-content/uploads/2022/09/Xiaomi-12-and-12T-Pro.jpg", "https://i02.appmifile.com/781_operator_sg/30/08/2022/6e74a9738a2e116d1a4f3c4f73880ed3.png?f=webp", "https://www.techadvisor.com/wp-content/uploads/2022/06/xiaomi_12_pro_review_3.jpg?quality=50&strip=all", "https://fdn.gsmarena.com/imgroot/reviews/22/xiaomi-12-pro/lifestyle/-1200w5/gsmarena_017.jpg"]

    image_html = ''
    for url in images:
        image_html += f'<img src="{url}" style="width:2000px; height:500px; object-fit: cover; display: block;margin-right: 20px;">'

    st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )

    # ------------------------------------------------------------------------------------------

    st.markdown("<br><br>", unsafe_allow_html=True )
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Storage")
        st.markdown("<ul><li>128 | 8</li><li>256 | 8</li><li>256 | 12</li></ul>", unsafe_allow_html=True )

    with col2:
        st.header("Colour")
        st.markdown("<ul><li>Blue</li><li>Silver</li><li>Black</li></ul>", unsafe_allow_html=True )

    with col3:
        st.header("Price")
        st.write("Rs. 60,490")
        st.markdown("""<a href="https://www.mi.com/in/product/xiaomi-12-pro-5g/"><button style="background: linear-gradient(to bottom right, #EF4765, #FF9A5A); border: 0; border-radius: 12px; color: #FFFFFF; cursor: pointer;" >Buy</button></a>""", unsafe_allow_html=True )


    # ------------------------------------------------------------------------------------------

with tab3:

    st.title('Asus ROG Phone 6D Ultimate')
    images = ["https://www.flashfly.net/wp/wp-content/uploads/2022/11/review-ASUS-ROG-Phone-6D-Ultimate-flashfly-1.jpg", "https://cdn.mos.cms.futurecdn.net/yosLGreSXkcBEP8QKD5WHh.jpg", "https://lh3.googleusercontent.com/eIW9QNeG_dvcsKGDRa-iBUR9Mhke-io-uWoQEVXmzbFVPp0HMHStyZxelZ1uQBhcCw_Ct5odO5FQ1gN4mLd-9JOE4ddNnGy5-nerzGmdZKnZ0x9FXAE0_O6rNxUt1Bb6gV-o9i9_c1OSuG73x8VlReq_ORQvnkhwjVilBXqF1AVbLIrAqNfioHAfCz4g_Gj0Mi5ZYw", "https://www.lowyat.net/wp-content/uploads/2022/09/asus-rog-phone-6d-ultimate-launch-europe-2.jpg", "https://www.91-cdn.com/hub/wp-content/uploads/2022/09/ASUS-ROG-Phone-6D.png"]

    image_html = ''
    for url in images:
        image_html += f'<img src="{url}" style="width:2000px; height:500px; object-fit: cover; display: block;margin-right: 20px;">'

    st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )

    # ------------------------------------------------------------------------------------------

    st.markdown("<br><br>", unsafe_allow_html=True )
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Storage")
        st.markdown("<ul><li>512 | 16</li></ul>", unsafe_allow_html=True )

    with col2:
        st.header("Colour")
        st.markdown("<ul><li>Space Gray</li></ul>", unsafe_allow_html=True )

    with col3:
        st.header("Price")
        st.write("Rs. 1,08,780")
        st.markdown("""<a href="https://rog.asus.com/phones/rog-phone-6d-ultimate-model/"><button style="background: linear-gradient(to bottom right, #EF4765, #FF9A5A); border: 0; border-radius: 12px; color: #FFFFFF; cursor: pointer;" >Buy</button></a>""", unsafe_allow_html=True )

    # ------------------------------------------------------------------------------------------

with tab4:

    st.title('Vivo X80 Pro')
    images = ["https://carlosvassan.com/wp-content/uploads/2022/06/X80_Pro_Teaser59-1024x818.jpg", "https://www.91-cdn.com/hub/wp-content/uploads/2022/05/x80-series-launched.png", "https://www.gizmochina.com/wp-content/uploads/2022/05/vivo-X80-Pro-review-09.jpg", "https://soyacincau.com/wp-content/uploads/2022/05/220508-vivo-x80-pro-5g-malaysia-price-1024x1024.jpg", "https://riggear-web-images.s3.ap-south-1.amazonaws.com/UploadImages/Vivo-Vivo%20X80%20Pro-Skins-b28e43cc-87fa-4cda-a1cb-1e5f28ca9254_big.jpg"]

    image_html = ''
    for url in images:
        image_html += f'<img src="{url}" style="width:2000px; height:500px; object-fit: cover; display: block;margin-right: 20px;">'

    st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )

    # ------------------------------------------------------------------------------------------

    st.markdown("<br><br>", unsafe_allow_html=True )
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Storage")
        st.markdown("<ul><li>256 | 8</li><li>256 | 12</li><li>512 | 12</li></ul>", unsafe_allow_html=True )

    with col2:
        st.header("Colour")
        st.markdown("<ul><li>Blue</li><li>Orange</li><li>Cosmic Black</li></ul>", unsafe_allow_html=True )

    with col3:
        st.header("Price")
        st.write("Rs. 79,999")
        st.markdown("""<a href="https://www.vivo.com/en/products/x80pro"><button style="background: linear-gradient(to bottom right, #EF4765, #FF9A5A); border: 0; border-radius: 12px; color: #FFFFFF; cursor: pointer;" >Buy</button></a>""", unsafe_allow_html=True )

    # ------------------------------------------------------------------------------------------

with tab5:

    st.title('Oneplus 11 5G')
    images = ["https://images-eu.ssl-images-amazon.com/images/G/31/img21/Wireless/ssserene/OP11/LP/Flagship.png", "https://www.lowyat.net/wp-content/uploads/2023/02/oneplus-11-5g-buds-pro-2-a01.jpg", "https://images-eu.ssl-images-amazon.com/images/G/31/img21/Wireless/ssserene/OP11/Pc.jpg", "https://www.cnet.com/a/img/resize/b4e1f110884d25812db4ec7b1095e7fcfd6763de/hub/2023/01/06/bfc63367-5e30-465d-bfee-22a019731556/oneplus-11-promo-2-by-1.jpg?auto=webp", "https://www.91-cdn.com/hub/wp-content/uploads/2023/01/op11-1200.png"]

    image_html = ''
    for url in images:
        image_html += f'<img src="{url}" style="width:2000px; height:500px; object-fit: cover; display: block;margin-right: 20px;">'

    st.markdown(f"""<div style="display: flex; overflow-x: scroll; padding: 10px 0;">{image_html}</div>""", unsafe_allow_html=True )

    # ------------------------------------------------------------------------------------------

    st.markdown("<br><br>", unsafe_allow_html=True )
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Storage")
        st.markdown("<ul><li>128 | 8</li><li>256 | 12</li><li>256 | 16</li><li>512 | 16</li></ul>", unsafe_allow_html=True )

    with col2:
        st.header("Colour")
        st.markdown("<ul><li>Titan Black</li><li>Eternal Green</li></ul>", unsafe_allow_html=True )

    with col3:
        st.header("Price")
        st.write("Rs. 56,999")
        st.markdown("""<a href="https://www.oneplus.in/search?keyword=OnePlus%2011&page=1"><button style="background: linear-gradient(to bottom right, #EF4765, #FF9A5A); border: 0; border-radius: 12px; color: #FFFFFF; cursor: pointer;" >Buy</button></a>""", unsafe_allow_html=True )

    # ------------------------------------------------------------------------------------------

st.markdown("<br><hr>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------------------------------------------------------