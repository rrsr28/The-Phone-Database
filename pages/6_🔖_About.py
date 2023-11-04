import streamlit as st

# ----------------------------------------------------------------------------------------------------------------------------------------
# About the Webpage
# ------------------
st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:65px'>About the Webpage</h1>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""<p style=' font-size:20px'>We are living in a world where the use of mobile phones is increasing rapidly. It has become an integral part of our life. With the ever-increasing number of smartphone companies, it is difficult for a user to choose the best one. To make this task easier, it is necessary to have data about the phones that can be used for comparison purposes. 
GSMArena Phones Dataset is a labeled dataset extracted from GSMArena, one of the most popular online providers of phone information, and holds a large collection of phone specifications. It has been providing information about mobile phones for more than 10 years. This data can be used to analyze the features and prices of mobile phones. 
Scraper:
	Web Scraping has been done with the help of BeautifulSoup of GSMArena.
</p>""", unsafe_allow_html=True)


st.markdown("<br><hr>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------------------------------------------------------------
# About the Project
# ------------------
st.markdown("<h1 style='text-align: center; color : #E8570E; font-size:65px'>About the Project</h1><br>", unsafe_allow_html=True)
st.markdown("<br><p style='color : white; font-size:30px'>Disclaimer :</p><p style='color : white; font-size:20px'> The dataset is not being updated because it puts a lot of load on GSMArena Servers resulting in IP bans. Therefore, if you don't delete the previous contents of the soup variable, you will be left with nothing to store in case of an IP ban. Hence the previous value will be used. Therefore empty that variable.</p>", unsafe_allow_html=True)
st.markdown("<br><p style='color : white; font-size:30px'>Scraper :</p><p style='color : white; font-size:20px'>Web Scraping has been done with the help of BeautifulSoup of GSMArena.</p>", unsafe_allow_html=True)
st.markdown("<br><p style='color : white; font-size:30px'>Inspiration :</p><p style='color : white; font-size:20px'>This dataset provides some very interesting visualizations. One can look at simple things like how prices change over time, graph and compare multiple phones at once, or generate and graph new metrics from the data provided. From these data, we can predict the prices of future prices of phones such as moving averages can be easily calculated.</p><br>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Main Features", "Libraries", "References"])
with tab1:
   
   st.markdown("""<ul>  
                        <li>Dataset is obtained through Web Scraping</li>
                        <li>Data Cleaning</li>
                        <li>Data Wrangling</li>
                        <li>User Interface (Website)</li>                      
                        <li>Data Visualisation</li>
                        <li>Dashboard PowerBI</li>
                        <li>Predicting price of New Launch </li>    
                                                                      </ul> """, unsafe_allow_html=True) 
with tab2:
   st.markdown("""<ul>  
                        <li>Numpy</li>
                        <li>Pandas</li>
                        <li>BeautifulSoup</li>
                        <li>Requests</li>
                        <li>CSV</li>
                        <li>Streamlit</li>
                                          </ul> """, unsafe_allow_html=True) 
with tab3:
   st.markdown("""<ul>  
                        <li>GeekforGeeks</li>
                        <li>Streamlit Documentation</li>
                        <li>Towards Data Science</li>
                        <li>Freecodecamp</li>
                        <li>Bootstrap Icons</li>
                        <li>Towards Data Science</li>
                        <li>Coding is Fun - Youtube</li>
                                          </ul> """, unsafe_allow_html=True) 


st.markdown("<br><hr>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------------------------------------------------------------
