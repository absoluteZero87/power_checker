#!/usr/bin/env python3

import requests
import json

url = "https://api.amberelectric.com.au/prices/listprices"
philips_hue_url ="https://10.0.1.95/api/OAS1SXoKgm2ggc2X6lvAiOUpyKChLkvmaGWqlMHc/lights/12/state"
data = '{ "postcode": "3011" }'
var = "serviceResponseType"

response = requests.post(url, data=data)
res = response.json()



#print(res)
o1 = float(res["data"]["staticPrices"]["E1"]["totalfixedKWHPrice"])
o2 = float(res["data"]["staticPrices"]["E1"]["lossFactor"])
o3 = float(res["data"]["variablePricesAndRenewables"][0]["wholesaleKWHPrice"])
print("part 1 is " + str(o1))
print("part 2 is " + str(o2))
print("part 3 is " + str(o3))
#
o4 = o1 + (o2 * o3)
#
print("and finally " + str(o4))

if o4 > 30:
    colour_data = '{"xy" : [0.6451,0.3059]}'
elif 20 < o4 <= 30:
    colour_data = '{"xy" : [0.4669,0.4738]}'
elif o4 <= 20:
    colour_data = '{"xy" : [0.4084,0.5168]}'
    
requests.put(philips_hue_url, data=colour_data, verify=False)

