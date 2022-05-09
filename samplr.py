import requests
url = "{{request.get_path}}api/covid-data/"
payload = 'country_region=Nigeria'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
