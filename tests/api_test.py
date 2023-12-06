from thw.helpers.api import TSHOCKClient

# based on: https://tshock.readme.io/reference#rest-api-endpoints &
# https://tshock.atlassian.net/wiki/display/TSHOCKPLUGINS/REST+API+Endpoints &
# https://tshock.atlassian.net/wiki/display/TSHOCKPLUGINS/Commands+List

api = TSHOCKClient(ip="epic-ip-address", port=7878, username='epic-username', password='epic-password')
print api.get(path="server/broadcast", params={'msg': 'bla bla'})
print api.get(path="server/status")
print api.validate()
print api.get(path="players/list")
print api.get(path="users/activelist")
print api.get(path="users/read", params={'user': 'Kinvaris'})
print api.get(path="world/read", old_api=True)
# print api.get(path="world/meteor", old_api=True)
print api.get(path="bans/list")
print api.get(path="groups/list")

