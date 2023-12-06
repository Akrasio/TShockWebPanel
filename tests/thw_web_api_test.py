import json
import requests

#print requests.post('http://127.0.0.1:14789/api/login').text
#print requests.post('http://127.0.0.1:14789/api/login', json={"username": None, "password": None}).text
#print requests.post('http://127.0.0.1:14789/api/login', json={"username": "superadmin-username", "password": "superadmin-password"}).text

response = json.loads(requests.post('http://127.0.0.1:14789/api/login',
                                    json={"username": "", "password": ""}).text)
print response
print requests.post('http://127.0.0.1:14789/api/model/lists/server/get_server_information', json={"token": response['result']['token']}).text
#print requests.post('http://127.0.0.1:14789/api/validate', json={"token": response['result']['token']}).text
#print requests.post('http://127.0.0.1:14789/api/model/lists/get_current_players').text
print requests.post('http://127.0.0.1:14789/api/model/lists/players/get_current_players',
                    json={"token": response['result']['token']}).text
#print requests.post('http://127.0.0.1:14789/api/model/lists/groups/get_groups',
#                   json={"token": response['result']['token']}).text
#print requests.post('http://127.0.0.1:14789/api/model/lists/groups/get_group_by_name',
#                   json={"token": response['result']['token'], "group_name": "guest"}).text
print requests.post('http://127.0.0.1:14789/api/model/lists/groups/get_group_by_name',
                    json={"token": response['result']['token']}).text
#print requests.post('http://127.0.0.1:14789/api/config').text
#print requests.post('http://127.0.0.1:14789/api').text
#print requests.post('http://127.0.0.1:14789/api/documentation').text
print requests.post('http://127.0.0.1:14789/api/model/lists/players/get_user_in_database',
                    json={"token": response['result']['token'], "username": "bla"}).text
print requests.post('http://127.0.0.1:14789/api/model/lists/players/get_users_in_database',
                    json={"token": response['result']['token']}).text
print requests.post('http://127.0.0.1:14789/api/model/lists/players/get_user_in_world',
                    json={"token": response['result']['token'], "username": "Kinvaris"}).text
print requests.post('http://127.0.0.1:14789/api/model/lists/players/get_user_ip_in_world',
                    json={"token": response['result']['token'], "username": "Kinvaris"}).text
print requests.post('http://127.0.0.1:14789/api/controllers/server/broadcast_message',
                    json={"token": response['result']['token'], "message": "hello"}).text
print requests.post('http://127.0.0.1:14789/api/controllers/manager/execute_cmd',
                    json={"token": response['result']['token'], "command": "/broadcast foobar"}).text
print requests.post('http://127.0.0.1:14789/api/model/lists/world/get_world_details',
                    json={"token": response['result']['token']}).text
print requests.post('http://127.0.0.1:14789/api/model/lists/players/get_banned_players',
                    json={"token": response['result']['token']}).text
print requests.post('http://127.0.0.1:14789/api/config/terraria/item/by_id',
                    json={"token": response['result']['token'], "id": 3000}).text
print requests.post('http://127.0.0.1:14789/api/config/terraria/item/by_name',
                    json={"token": response['result']['token'], "name": "Lake of Fire"}).text
print requests.post('http://127.0.0.1:14789/api/logout', json={"token": response['result']['token']}).text
print requests.post('http://127.0.0.1:14789/api/validate', json={"token": response['result']['token']}).text