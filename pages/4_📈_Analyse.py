import streamlit as st
# ----------------------------------------------------------------------------------------------------------------------------------------

st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:65px'>Analyse</h1>", unsafe_allow_html=True)
st.markdown("<br><hr>", unsafe_allow_html=True)

st.markdown("""<style>.btn {
    background-image: none;
    border-radius: 30px;
    border-style: solid;
    border-width: 1px;
    cursor: pointer;
    display: inline-block;
    font-family: Montserrat, Avenir, "Avenir Next", Trebuchet, Verdana,
        sans-serif;
    font-size: 1rem;
    font-weight: 700;
    line-height: 1.6rem;
    margin-bottom: 0;
    padding: 0.65rem 2.2rem 0.55rem;
    text-align: center;
    text-decoration: none;
    -ms-touch-action: manipulation;
    touch-action: manipulation;
    -webkit-transition: background-color 0.2s ease-out, background 0.2s ease-out,
        color 0.2s ease-out, border 0.2s ease-out;
    transition: background-color 0.2s ease-out, background 0.2s ease-out,
        color 0.2s ease-out, border 0.2s ease-out;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    vertical-align: middle;
    white-space: nowrap;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;    
    background-color: #E8570E;
    border-color: #E8570E;
    color: #262b3a;
}</style>""", unsafe_allow_html=True)

st.markdown("<img src = 'https://www.syncfusion.com/blogs/wp-content/uploads/2018/08/stock_markets_60999aa9-1280x720.png' style='width:70%; height:60%; object-fit: cover; display: block;margin-right: auto; margin-left:auto;'>",unsafe_allow_html=True)
st.markdown("<br><hr><br>",unsafe_allow_html=True)

st.markdown("<h1> All Brands Analysis</h1>", unsafe_allow_html=True)
st.markdown("""<a href="https://app.powerbi.com/reportEmbed?reportId=9a846a60-6279-4b70-8064-27fad04b27db&autoAuth=true&ctid=f0fa9813-b937-4151-a49f-d5944e994861"><button class="btn">Click me !</button></a><div>""", unsafe_allow_html=True)
st.markdown("<br><hr><br>",unsafe_allow_html=True)

st.markdown("<img src = 'https://tradebrains.in/wp-content/uploads/2020/04/How-to-do-Fundamental-Analysis-on-Stocks-cover.jpg' style='width:70%; height:60%; object-fit: cover; display: block;margin-right: auto; margin-left:auto;'>",unsafe_allow_html=True)
st.markdown("<br><hr><br>",unsafe_allow_html=True)

st.markdown("<h1> Brandwise Analysis</h1>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Samsung", "Xiaomi", "Asus", "Google", "Infinix", "Vivo", "Oppo", "Oneplus"])
with tab1:
    st.markdown("""<br><a href="https://app.powerbi.com/reportEmbed?reportId=c0cc2f92-5194-4205-94ba-351e72753718&autoAuth=true&ctid=f0fa9813-b937-4151-a49f-d5944e994861"><button class="btn">Samsung</button></a><div>""", unsafe_allow_html=True)

with tab2:
    st.markdown("""<br><a href="https://app.powerbi.com/reportEmbed?reportId=17d725c6-1bca-4c89-9746-316bfe1a4c15&autoAuth=true&ctid=f0fa9813-b937-4151-a49f-d5944e994861"><button class="btn">Xiaomi</button></a></div>""", unsafe_allow_html=True)

with tab3:
    st.markdown("""<br><a href="https://app.powerbi.com/reportEmbed?reportId=668423a9-9e92-497b-984e-fdec1cf532a8&autoAuth=true&ctid=f0fa9813-b937-4151-a49f-d5944e994861"><button class="btn">Asus</button></a><div>""", unsafe_allow_html=True)

with tab4:
    st.markdown("""<br><a href="https://app.powerbi.com/reportEmbed?reportId=91db327d-397a-49c6-b872-3bf53270b517&autoAuth=true&ctid=f0fa9813-b937-4151-a49f-d5944e994861"><button class="btn">Google</button></a></div>""", unsafe_allow_html=True)

with tab5:
    st.markdown("""<br><a href="https://app.powerbi.com/reportEmbed?reportId=e8fb327d-ef31-447f-bc47-36c6cbd1c9ab&autoAuth=true&ctid=f0fa9813-b937-4151-a49f-d5944e994861"><button class="btn">Infinix</button></a><div>""", unsafe_allow_html=True)

with tab6:
    st.markdown("""<br><a href=""><button class="btn">Vivo</button></a></div>""", unsafe_allow_html=True)

with tab7:
    st.markdown("""<br><a href="https://app.powerbi.com/reportEmbed?reportId=f6df1e20-f7fa-4f66-9230-d039e100f7e5&autoAuth=true&ctid=f0fa9813-b937-4151-a49f-d5944e994861"><button class="btn">Oppo</button></a><div>""", unsafe_allow_html=True)

with tab8:
    st.markdown("""<br><a href="https://app.powerbi.com/reportEmbed?reportId=d6b4cc0b-b99a-4482-973f-8ec04131c5fc&autoAuth=true&ctid=f0fa9813-b937-4151-a49f-d5944e994861"><button class="btn">Oneplus</button></a></div>""", unsafe_allow_html=True)

st.markdown("<br><hr><br>",unsafe_allow_html=True)
st.markdown("<img src = 'https://as2.ftcdn.net/v2/jpg/01/42/68/77/1000_F_142687727_ZjpVAN3Enj6ijy7ijvYGc2l4gf26YkNy.jpg' style='width:70%; height:60%; object-fit: cover; display: block;margin-right: auto; margin-left:auto;'>",unsafe_allow_html=True)
st.markdown("<br><hr><br>",unsafe_allow_html=True)
st.markdown("<h1> Brandwise Inference</h1>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Samsung", "Xiaomi", "Asus", "Google", "Infinix", "Vivo", "Oppo", "Oneplus"])
with tab1:
    with st.expander("Samsung"):
        st.markdown("""<br><ul>
                        <li>Samsung has a wide range of products with different features, prices and release dates. Generally, as the weight, storage, screen size, resolution, RAM, camera and battery capacity of a Samsung phone increases, the price also tends to increase.</li>
                        <li>There seems to be a seasonal trend in Samsung phone releases, with many new models being released in the second half of the year.</li>
                        <li>From 2020 to 2022, Samsung has focused on releasing phones with large batteries and storage capacities.</li>
                        <li>The release of the Samsung Galaxy S23, S23+ and S23 Ultra in February 2023 suggests that Samsung is likely to continue producing premium flagship phones with high-end features and prices, mostly during the month of January and February</li>
                        <li>Based on the data, we can observe that Samsung has products in a wide range of price points. The price of Samsung phones ranges from Rs. 8,499 for the Samsung Galaxy F04 to Rs. 1,89,999 for the Samsung Galaxy Z Fold2 5G.</li>
                        <li>There is a positive correlation between RAM and price. It is expected that Samsung's flagship phones will continue to have high RAM capacity in the future.</li>
                        <li>There is also a positive correlation between screen size and price, which suggests that Samsung is likely to continue producing larger phones in the future.</li>
                        <li>Based on the trends observed in the data, it is likely that Samsung will continue to focus on producing 5G-capable phones with large batteries and storage capacities, as these features are becoming increasingly important to consumers.</li>
                        </ul><br>
                        <p>Based on these observations, we can predict that Samsung will continue to release phones with larger batteries, more RAM, higher storage capacity and larger screens, and that they will continue to focus on producing premium flagship phones with high-end features and prices. It is also likely that they will continue to produce phones at a variety of price points to appeal to a wide range of consumers.</p>""", unsafe_allow_html=True)

with tab2:
    with st.expander("Xiaomi"):
        st.markdown("""<br><ul>
                        <li>The data shows that Xiaomi releases new smartphone models almost every month, with the highest number of releases in the months of May and December.</li>
                        <li>The prices of Xiaomi smartphones in the dataset vary widely, ranging from 5,749 INR for the Poco C50 to 79,999 INR for the Xiaomi 13 Pro. The average price of a Xiaomi smartphone in the dataset is around 25,000 INR.</li>
                        <li>The most common storage capacity for Xiaomi smartphones in the dataset is 128 GB, with only a few models having 64 GB or 32 GB storage.</li>
                        <li>Xiaomi smartphones have a range of screen sizes, with the most common screen size being 6.67 inches. The screen resolution for most models is 1080x2400 pixels.</li>
                        <li>Xiaomi smartphones have a wide range of battery capacities, with the most common capacity being 5000 mAh. The highest battery capacity in the dataset is 6000 mAh, which is found in a few models such as Redmi 10 Prime 2022 and Redmi 10 Power.</li>
                        <li>The camera specs for Xiaomi smartphones also vary widely, with the highest camera resolution being 108 MP found in a few models such as Redmi Note 11T Pro+ and Poco X5 Pro.</li>
                        <li>The data does not show a clear pattern of seasonality, but it does suggest that Xiaomi tends to release new smartphone models more frequently towards the end of the year.</li>
                        </ul><br>""", unsafe_allow_html=True)

with tab3:
    with st.expander("Asus"):
        st.markdown("""<br><ul>
                        <li>The weight of the smartphones ranges from 140 grams to 247 grams, with an average weight of 211 grams.</li>
                        <li>The internal storage of the smartphones ranges from 16 GB to 512 GB, with an average storage of 256 GB.</li>
                        <li>The screen resolution of the smartphones is consistent, with all the smartphones having a resolution of 1080x2448 or 1080x2400 pixels.</li>
                        <li>The selling price of the smartphones ranges from INR 6499 to INR 118400, with an average selling price of INR 59928.92.</li>
                        </ul><br>
                        <p>We can observe that the average selling price of Asus smartphones has been increasing steadily over the years. There is a sudden increase in the average selling price in 2021 and 2022, which could be due to the release of high-end smartphones with advanced features.</p>
                        <br><p> We can observe that there is a positive correlation between the selling price and RAM, storage, and camera resolution. This indicates that smartphones with higher RAM, storage, and camera resolution tend to have a higher selling price. There is also a positive correlation between the selling price and release date, indicating that newer smartphones tend to have a higher selling price.</p>""", unsafe_allow_html=True)

with tab4:
    with st.expander("Google"):
        st.markdown("""<br>
                        <p>From the summary statistics, we can see that the prices of Google smartphones vary widely, ranging from Rs. 6,999 to Rs. 84,999. The mean price is Rs. 27,813.9, and the standard deviation is Rs. 25,219.8, indicating that there is a high level of variation in the prices.</p>
                        <br><p>We can observe that RAM, Storage, and Camera are positively correlated with the price of Google smartphones. On the other hand, Weight, Battery, and Screen Size have a relatively low positive correlation with the price.</p>
                        <br><p>We can observe that the latest releases of Google smartphones are the Google Pixel 7 Pro and Google Pixel 7, both released in October 2022. The Pixel 7 Pro has a higher price than the Pixel 7, which could be due to its larger screen size, higher screen resolution, and larger battery.</p>
                        <br><p>In terms of seasonality, we can observe that the latest releases tend to be in the second half of the year, with the exception of the Google Pixel 3a and Pixel 3a XL, which were released in May 2019. This could be due to the fact that the second half of the year is the period where most people buy new phones, especially during the holiday season.</p>
                        <br><p>We can also see that there is a clear trend of increasing prices for Google smartphones over time, with the most expensive models being the most recent releases. This suggests that the demand for Google smartphones is increasing, or that the company is positioning itself as a premium smartphone brand.</p>""", unsafe_allow_html=True)


with tab5:
    with st.expander("Infinix"):
        st.markdown("""<br><ul>
                        <li>Infinix appears to be releasing new smartphones frequently, with several models launched each month. This suggests a highly competitive market for smartphones in which companies must constantly innovate to remain relevant.</li>
                        <li>There is a wide range of prices among Infinix smartphones, with some models costing less than 10,000 rupees and others costing more than 30,000 rupees. This indicates that Infinix is targeting a diverse range of consumers with varying budgets.</li>
                        <li>The Infinix Note 12 Pro and Note 12 Pro 5G both feature a high-quality camera (108 MP) and a large amount of storage (256 GB), but the 5G version is slightly more expensive. This suggests that Infinix is charging a premium for the added 5G connectivity, which may be a selling point for consumers looking for faster internet speeds.</li>
                        <li>The most popular screen size among Infinix smartphones in the dataset is 6.7 inches, which is featured in several models including the Note 12, Note 12i, and Hot 11. This suggests that Infinix is catering to consumers who prefer larger screen sizes for activities such as gaming or streaming.</li>
                        <li>In terms of battery size, several Infinix models feature a large 6000 mAh battery, including the Smart 7, Hot 20 Play, and Hot 12 Play. This may be a selling point for consumers who use their smartphones frequently and require a long battery life.</li>
                        </ul>
                        <br><p>Overall, the data suggests that Infinix is a company that is trying to cater to a wide range of consumers with varying budgets and preferences. The company is constantly releasing new models with different features and specifications, which indicates a competitive market in which innovation is key to success.</p>""", unsafe_allow_html=True)

with tab6:
    with st.expander("Vivo"):
        st.markdown("""<br><ul>
                        <li></li>
                        <li></li>
                        <li></li>
                        <li></li>
                        <li></li>
                        </ul>
                        <br><p></p>""", unsafe_allow_html=True)

with tab7:
    with st.expander("Oppo"):
        st.markdown("""<br><ul>
                        <li>The price of the phones ranges from 9,499 to 94,890, with a mean of 29,310. The standard deviation is 22,605, indicating that there is a wide variation in the prices of the phones.</li>
                        <li>We can also look at the correlation between the different variables in the dataset. The correlation matrix indicates that there is a strong positive correlation between the RAM and screen size of the phone, which is expected. However, there does not seem to be a strong correlation between the price of the phone and any of the other variables.</li>
                        <li>The newer models, such as the Oppo Reno8 T and Oppo Reno8 T 5G, are priced higher than older models like the Oppo A17k and Oppo A17. This indicates that Oppo's pricing strategy is influenced by the age of the phone.</li>
                        </ul>""", unsafe_allow_html=True)

with tab8:
    with st.expander("Oneplus"):
        st.markdown("""<br><ul>
                        <li>Looking at the release dates of the Oneplus smartphones, it is clear that Oneplus releases new models frequently, with some months seeing multiple new models. This suggests that Oneplus is committed to staying competitive in the smartphone market by keeping up with the latest technology and trends.</li>
                        <li>There is a clear trend of increasing storage and RAM in the Oneplus smartphones over time, with the latest models having much higher specifications than those released just a year or two ago. This suggests that Oneplus is catering to consumers who need more storage and processing power for their smartphones.</li>
                        <li>The majority of Oneplus smartphones in the dataset have a battery capacity of 4500mAh or higher, which suggests that Oneplus is prioritizing battery life and longevity in their devices. This is likely a response to consumer demand for smartphones with long battery life.</li>
                        <li>The camera specifications of Oneplus smartphones in the dataset are relatively consistent, with most models having a 50-megapixel main camera and a 16-megapixel front-facing camera. However, there are some outliers, such as the Oneplus Nord N200 5G, which has a much lower-resolution camera compared to other models.</li>
                        <li>Oneplus smartphones in the dataset range in price from around 15,000 INR to over 60,000 INR. The most expensive models tend to have higher specifications and more advanced features, such as 5G connectivity and higher storage and RAM. The lower-priced models tend to have fewer features but may still offer good value for consumers on a budget.</li>
                        </ul>
                        <br><p>Overall, the data shows that Oneplus is a company that prioritizes high specifications, especially in terms of storage, RAM, battery life, and screen size. As new models are released, these specifications tend to improve, suggesting that Oneplus is committed to staying competitive in the smartphone market.</p>""", unsafe_allow_html=True)

