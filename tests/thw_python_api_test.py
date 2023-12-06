from thw.model.lists.server import ServerList
from thw.model.lists.world import WorldList
from thw.model.lists.players import PlayerList
from thw.model.lists.groups import GroupList
from thw.controllers.servercontroller import ServerController
from thw.controllers.groupcontroller import GroupController
from thw.controllers.playercontroller import PlayerController
from thw.controllers.worldcontroller import WorldController
from thw.helpers.api import TSHOCKClient, HttpException

# setup api
api = TSHOCKClient(ip="epic-ip-address", port=7878, username='epic-username', password='epic-password')

# delete the things if already exists
try:
    GroupController.delete_group(api=api, group_name="foobar")
except HttpException:
    pass
try:
    PlayerController.delete_player(api=api, username="foo")
except HttpException:
    pass

# testing the lists
ServerList.get_motd(api=api)
ServerList.get_server_details(api=api)
ServerList.get_server_rules(api=api)
WorldList.get_world_details(api=api)
PlayerList.get_banned_players(api=api)
PlayerList.get_current_players(api=api)
PlayerList.get_user_in_database(api=api, username="Kinvaris")
# PlayerList.get_user_in_world(api=api, username="Kinvaris")
GroupList.get_group_by_name(api=api, group_name="superadmin")  # run 1
GroupList.get_groups(api=api)
GroupList.get_permissions_by_category(category_name="PLAYER")  # run 2
GroupList.list_permissions()
GroupList.list_permission_groups()

# testing the controllers
ServerController.broadcast_message(api=api, message="foo bar")
ServerController.reload_server_configs(api=api)
GroupController.add_group(api=api, group_name="foobar")
GroupController.update_group(api=api, group_name="foobar",
                             permissions="tshock.rest.users.view,tshock.rest.users.info,tshock.rest.users.manage")
PlayerController.add_player(api=api, username="foo", password="bar", group="foobar")
# PlayerController.kill_player_by_username(api=api, username="foo", reason="foo bar")
# PlayerController.mute_player_by_username(api=api, username="foo", reason="foo bar")
# PlayerController.unmute_player_by_username(api=api, username="foo", reason="foo bar")
PlayerController.ban_player_by_ip(api=api, ip="192.168.1.1", reason="foo bar")
# PlayerController.ban_player_by_username(api=api, username="foo", reason="foo bar")
# PlayerController.unban_player(api=api, username="foo")
PlayerController.unban_player(api=api, ip="192.168.1.1")  # run 3 --> blocked
PlayerController.update_player(api=api, username="foo", password="bar2", group="foobar")
#PlayerController.kick_player_by_username(api=api, username="foo", reason="foo bar")
PlayerController.delete_player(api=api, username="foo")
GroupController.delete_group(api=api, group_name="foobar")
WorldController.butcher_npcs(api=api, status=True)
WorldController.butcher_npcs(api=api, status=False)
WorldController.drop_meteor(api=api)
WorldController.save_world(api=api)
WorldController.set_autosave_world(api=api, status=True)
WorldController.set_autosave_world(api=api, status=False)
WorldController.set_blood_moon(api=api, status=True)
WorldController.set_blood_moon(api=api, status=False)
