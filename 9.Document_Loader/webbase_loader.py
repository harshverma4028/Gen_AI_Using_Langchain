from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup
url = "https://www.flipkart.com/acer-predator-helios-neo-16-intel-core-i7-14th-gen-14700hx-16-gb-1-tb-ssd-windows-11-home-6-gb-graphics-nvidia-geforce-rtx-4050-phn16-72-77gz-gaming-laptop/p/itm34f68c296ce65?pid=COMGZKFB3ZTQGRT4&lid=LSTCOMGZKFB3ZTQGRT44OF4LD&marketplace=FLIPKART&q=acer+predator+helios+neo+16&store=6bo%2Fb5g&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_27_sc_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_27_sc_na_ps&fm=search-autosuggest&iid=b966d49b-9ede-4699-b06d-a1ab2ea05d87.COMGZKFB3ZTQGRT4.SEARCH&ppt=sp&ppn=sp&ssid=ra04xfcckw0000001743600940410&qH=e90df6a61ba4ce38"

loader = WebBaseLoader()

docs = loader.load()

print(docs[0].page_content)