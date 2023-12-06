# TSHOCK WEB Panel 
> A Working / Fixed Clone of [radishes/tshockweb](https://github.com/radishes/tshockweb) for terraria server management!
> *Note: This is a clone of a clone actually, [kinvaris/tshockweb](https://github.com/kinvaris/tshockweb), And I only made it work for newer version of the TShock Server.

## Description
~~This is the new, improved & lightweight version of the TSHOCK-WEB~~

This is a new, improved & lightweight version of the TSHOCK-WEB And updated version of kinvaris/tshockweb.

## Requirements
* `Flask`
* `python-pip`
* `Python3.7` (MIGHT* work with `python3.11`)

## Easy deployment
* Edit the following config file: `config/tshockweb.json`
* The `tshock_web` section contains the `api` and `web` settings
* The `tshock_server` section contains the settings to the tshock terraria server
* Execute as: `python tshockweb.py`
* Visit the following pages to validate the workability: `http://127.0.0.1:4891` & `http://127.0.0.1:4891/api`

## GUI

* Easily manage your tshockweb with account(s) that have `superadmin` rights
![](http://i.imgur.com/PiXO1kj.png)

* Easily monitor your tshock terraria server with the dashboard
![](http://i.imgur.com/tFlLHtU.png)
![](http://i.imgur.com/k9sayny.png)

* Easily manage your raw tshock commands with an online command tool
![](http://i.imgur.com/Q1R4Rzx.png)

* Check and manage what online users are doing/carrying on your server
![](http://i.imgur.com/siUIN5u.png)

## Development
* Easy python API:
```
from thw.model.lists.players import PlayerList
from thw.helpers.api import TSHOCKClient

api = TSHOCKClient(ip="tshock-api-url", port=7878, username='superadmin-username', password='superadmin-password')
print PlayerList.get_current_players(api=api)
```

* Easy API: 
```
import requests

requests.get('http://127.0.0.1:4891/api/login', json={"username": "superadmin-username", "password": "superadmin-password"}
{
  "result": {
    "token": "B542D501E90A62615F257BCCC47996B4597BAF0E06C9BB727785FFB880CA6F9E"
  }, 
  "status": 200, 
  "valid": true
}

requests.get('http://127.0.0.1:4891/api/model/lists/players/get_current_players', json={"token": "B542D501E90A62615F257BCCC47996B4597BAF0E06C9BB727785FFB880CA6F9E"})
{
  "result": {
    "api_path": "model/lists/players", 
    "method": "get_current_players", 
    "output": []
  }, 
  "status": 200, 
  "valid": true
}

curl -H "Content-Type: application/json" -X GET -d '{"username":"superadmin-username","password":"superadmin-password"}' http://localhost:4891/api/login
```

* Default JSON output:
```
{
  "result": {},  // result of the api call
  "status": 200, // status code of tshockweb api call
  "valid": true  // is valid call to the tshock terraria server
}
```

## Documentation
We try to make the API as generic and self documenting as possible. Currently we list the whole directory structure with classes,methods and their respective parameters. 
```
http://127.0.0.1:4891/api/documentation

{
  "result": {
    "controllers": {
      "groups": {
        "add_group": [
          "group_name", 
          "permissions"
        ], 
        "delete_group": [
          "group_name"
        ], 
        "update_group": [
          "group_name", 
          "permissions"
        ]
      }, 
      "manager": {
        "execute_cmd": [
          "command"
        ]
      }, 
      "players": {
        "add_player": [
          "username", 
          "password", 
          "group", 
          "ip"
        ], 
        "ban_player_by_ip": [
          "ip", 
          "reason"
        ], 
        "ban_player_by_username": [
          "username", 
          "reason"
        ], 
        "delete_player": [
          "username"
        ], 
        "kick_player_by_username": [
          "username", 
          "reason"
        ], 
        "kill_player_by_username": [
          "username", 
          "reason"
        ], 
        
```

## Fetching new terraria images
You can convert your terraria images to `image/PNG` with `TExtract`: https://forums.terraria.org/index.php?threads/textract-extract-terrarias-images-sound-effects-and-music.937/
Items can be mapped through this website: http://terraria.gamepedia.com/Item_IDs_Part1
Copy everything to a file, delete the tabs and delete everything matching `.+?(png)`

## Known issues
* The meteor can sometimes throw a `Internal server error`, this is being discussed in https://github.com/NyxStudios/TShock/issues/1361
* Armor/Inventory can sometimes show up other items than in reality (although 90% should be spot on). This because of ID overlapping in terraria itself. As seen here: http://terraria.gamepedia.com/Item_IDs#1801_.E2.86.92_2100
* If a item is not available in our image databank, it will display a empty image
* If the tshock server crashes its possible that the internal `Flask` server will crash with a `Broken Pipe` error. A restart of the server is required when this occurs.
* Missing (de)buffs in the `terraria_buffs.json` result in `XXX not found` and broken image in GUI.

## Current unimplemented features
* The `Server Activity` is currently generating fake results
* The `Live server status` is currently generating fake results