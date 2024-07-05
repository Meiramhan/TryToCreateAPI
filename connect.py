import requests


import requests

url = "https://7103.api.greenapi.com/waInstance7103954757/getSettings/3eb176d047084b1999b22dbe791210b579e115ef6ab24a648d"
url_2 = "https://7103.api.greenapi.com/waInstance7103954757/getStateInstance/3eb176d047084b1999b22dbe791210b579e115ef6ab24a648d"
url_3 = "https://7103.api.greenapi.com/waInstance7103954757/sendMessage/3eb176d047084b1999b22dbe791210b579e115ef6ab24a648d"
url_4 = "https://7103.api.greenapi.com/waInstance7103954757/sendFileByUrl/3eb176d047084b1999b22dbe791210b579e115ef6ab24a648d"

payload = {}
headers= {}

response = requests.request("GET", url)
response_2 = requests.request("GET", url_2)
response_3 = requests.request("POST", url_3)
response_4 = requests.request("POST", url_4)



print(response.text.encode('utf8'))