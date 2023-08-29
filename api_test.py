import requests

url = "https://skuld-auth.questmarine.app/auth/realms/marine/protocol/openid-connect/token"
payload = [{'client_id':'broker', 'username':'api-skuld@skuld.com', 'password':'7>T65`yH.uvXH]WS', 'grant_type':'password', 'client_secret':'e483c28e-9237-464a-b769-1554a1bb1f28'}]

grant_type=password&username={username}&password={password}&scope=customer-api



response = requests.get(url)

response_json = response.json()

print(response_json)



"""
client_id=broker&username=@pipeline().parameters.username&password=@pipeline().parameters.password&grant_type=password&client_secret@pipeline().parameters.client_secret"""