import requests
import json

url = "https://gateway-staging.ncrcloud.com/order/3/orders/1/find"

payload = json.dumps({
  "enterpriseUnitId": "6df343ac26004ee29e027275a7173ed7"
})
headers = {
  'Content-Type': 'application/json',
  'nep-organization': 'test-drive-27b00b4089b94035b0db4',
  'nep-enterprise-unit': '6df343ac26004ee29e027275a7173ed7',
  'Date': 'Sun, 24 Oct 2021 00:15:36 GMT',
  'Authorization': 'Basic MTg2NGZmZDAtYmZjOC00OTg0LTk0NDEtM2Y1NDllNjFlM2M5Ok5pbW1pb21hcjFA'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
