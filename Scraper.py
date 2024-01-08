# Web Scraping GSM Arena for phone specifications
# From 15th Feb - 18th Feb

""" 
Notes :
    
    USE PROXY !
    USE DECOMPOSE !
    
    if you dont delete the prev contents of the soup variable, in case you get
    banned there will be nothing to store in the soup variable. Hence the prev
    value will be used. Therefore empty tht variable.
    
"""    

from bs4 import BeautifulSoup
from csv import writer
import requests
import sys

# -----------------------------------------------------------------------------
# To change the IP address after getting banned
# -----------------------------------------------------------------------------

"""
def get_free_proxies():
    
    #--------------------------------------------------------------------------
    # Website with free proxies
    #--------------------------------------------------------------------------
    url = "https://free-proxy-list.net/"
    #--------------------------------------------------------------------------


    # Use dummy proxy HERE !
    # -----------------------
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    proxies = []
    
    for row in soup.find("table", attrs={"class": "table-striped"}).find_all("tr")[1:]:
        
        tds = row.find_all("td")
        
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxies.append(str(ip) + ":" + str(port))
        
        except IndexError:
            continue
    
    return proxies

"""

# -----------------------------------------------------------------------------
# Function to extract the Phones Info
# -----------------------------------------------------------------------------

def smartphone_infos(smartphone):
    
    smartphone_dict = dict()
    smartphone = smartphone.find("a")
    url_smartphone = f"https://www.gsmarena.com/{str(smartphone['href'])}"
    smartphone_dict["Link"] = url_smartphone
    smartphone_dict["Image"] = str(smartphone.find("img")["src"])
    
    # Getting Page Request. Storing Page content into soup+index variable.
    # ---------------------------------------------------------------------
    soup_smartphone = BeautifulSoup( requests.get(url_smartphone).content, 'html.parser')

    
    # Recursive = false means the children will be ignored
    # ----------------------------------------------------
    smartphone_dict["Name"] = str( soup_smartphone.find("h1").find_all(text=True, recursive=False)[0]     )
    
    if smartphone_dict["Name"] == "Too Many Requests" :
        return 99

    # If we get data without being banned
    # ------------------------------------    
    if soup_smartphone.select("td", {"class": "nfo"}):
        
        smartphone_dict["Release date"] = soup_smartphone.find("span", {"data-spec": "released-hl"}).text.strip()
        smartphone_dict["Weight"] = soup_smartphone.find("span", {"data-spec": "body-hl"} ).text.strip()
        smartphone_dict["OS"] = soup_smartphone.find("span", {"data-spec": "os-hl"} ).text.strip()
        smartphone_dict["Storage"] = soup_smartphone.find("span", {"data-spec": "storage-hl"} ).text.strip()
        
        ecran = soup_smartphone.find("li", {"class": "help-display"}).find_all(text = True)
        if ecran:
            smartphone_dict["Screen_size"] = str(ecran[2]).strip()
            smartphone_dict["Screen_resolution"] = str(ecran[3]).strip()
        
        RAM = soup_smartphone.find("li", {"class": "help-expansion"}).find_all(text = True)
        if RAM:
            smartphone_dict["RAM"] = " ".join( [RAM[i].strip() for i in [2, 3]] )
        
        batterie = soup_smartphone.find("li", {"class": "help-battery"}).find_all(text = True)
        if batterie:
                smartphone_dict["Battery"] = " ".join( [batterie[i].strip() for i in [2, 3, 4]] )
        
        
        # Remaining unwanted specifications ( but still storing them )
        # ------------------------------------------------------------
        for spec in soup_smartphone.find_all("td", {"class": "nfo"}):
            
            try:
                type = str(spec["data-spec"].strip())
                value = "".join( 
                    [
                        x.strip()
                        for x in spec.find_all(text=True, recursive=False)
                    ]
                )
                
                smartphone_dict[type] = value.replace("\n", " ").replace("\r", " ")
            
            except Exception:
                pass
     
    # Destroys the tags and contents - to not repeat the prev value when we get banned.
    # ---------------------------------------------------------------------------------
    soup_smartphone.decompose()
    return smartphone_dict

# -----------------------------------------------------------------------------
# Main Function
# -----------------------------------------------------------------------------

# Not using it for now
# --------------------
#proxies = get_free_proxies()


# Main Website we are scrapping from
# -----------------------------------
url_index = "https://www.gsmarena.com/makers.php3"
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
#proxy = '31.186.239.244:8080'

# Getting Page Request. Storing Page content into soup_index variable.
# ---------------------------------------------------------------------
r = requests.get(url_index)
a = r.content
soup_index = BeautifulSoup(a, 'html.parser')


# Find all lines of code with the HTML tag 'a'
# ----------------------------------------------
brands = soup_index.find("div", {"class": "st-text"}).find_all("a")
soup_index.decompose()

brand_name = []
brand_id   = []
url_brand_base = []

p = 0


# For loop for storing all the brand names and their id's before hand
# --------------------------------------------------------------------
for brand in brands:

    index_page = 1
    brand = brand["href"].rsplit("-", 1)
    brand_name.append(str(brand[0]))
    brand_id.append(str(brand[1].split(".")[0]))

    
    # Storing the url for each brand
    # -------------------------------
    url_brand_base.append(f"https://www.gsmarena.com/{brand_name[p]}-f-{brand_id[p]}-0")
    p = p + 1
    
smartphone_list = []
    
Company = input("Enter the mobile phone company : ")
Company = Company + "-phones"
x = brand_name.index(Company)

#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
#proxy = '49.0.2.242:8090'

# Now finding link for that company and scraping all data of its phones
# ----------------------------------------------------------------------
with open('MyScraped.csv', 'a', encoding='utf8', newline = '') as f :

    thewriter = writer(f)

    while True:
    
        # The url for the specific brand
        # ------------------------------    
        url_brand_page = f"{url_brand_base[x]}-p{index_page}.php"
        index_page = index_page + 1

    
        # Getting Page Request. Storing Page content into soup_page variable.
        # ---------------------------------------------------------------------
        soup_page = BeautifulSoup( requests.get(url_brand_page).content, 'html.parser')
       
        if soup_page.find("div", {"class": "section-body"}).select("li"):

        
            # Finding all HTML code with class = section-body, i.e getting the smartphones in that page
            # -----------------------------------------------------------------------------------------
            smartphones = soup_page.find("div", {"class": "section-body"}).find_all("li")
            soup_page.decompose()
            
            z = 0

    
            # Getting all the specs of a particular phone
            # -------------------------------------------
            for smartphone in smartphones:
            
                smartphone_dict = smartphone_infos(smartphone)
                
                if smartphone_dict == 99 :
                    print("ERROR ! Too many requests !")
                    sys.exit()
                
                smartphone_list.append(smartphone_dict)
                
                if(z == 0) :
                    thewriter.writerow(smartphone_dict.keys())
                    z = z + 1
                
                thewriter.writerow(smartphone_dict.values())
            
                print(smartphone_list, "\n\n")
    
    
        # else - case where we get banned
        # -------------------------------            
        else:
            soup_page.decompose()
            break

    
# -----------------------------------------------------------------------------