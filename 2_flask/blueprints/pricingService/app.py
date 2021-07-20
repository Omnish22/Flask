from models.items import Item



url="https://www.flipkart.com/apple-ipad-pro-2021-3rd-generation-8-gb-ram-256-rom-11-inches-wi-fi-only-space-grey/p/itm6dd0764296f1e?pid=TABG2DM4AJNPEJUZ&lid=LSTTABG2DM4AJNPEJUZKIVYR7&marketplace=FLIPKART&q=ipad+pro&store=tyy%2Fhry&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_4_na_na_na&fm=SEARCH&iid=9aca1736-73e0-4952-aad9-06475381a4dc.TABG2DM4AJNPEJUZ.SEARCH&ppt=hp&ppn=homepage&ssid=vm0qn17b000000001626721049641&qH=03e7257babd850e9"

tag_name="div"
query = {"class":"_30jeq3 _16Jk6d"}

ipad = Item(url,tag_name,query,"iPad")
ipad.add()

items = Item.getAll()
print(items)
print(items[0].load_price())