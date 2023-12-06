from thw.helpers.api import TSHOCKClient


class PlayerList(object):
    """
    Represents the lists for players
    """

    @staticmethod
    def get_current_players(api):
        """
        Get players

        :param api: tshock client api
        :type api: TSHOCKClient
        :return: dict
        """

        return api.get(path="server/status", params={'players':True})['players']

    @staticmethod
    def get_banned_players(api):
        """
        Get banned players

        :param api: tshock client api
        :type api: TSHOCKClient
        :return: dict
        """

        return api.get(path="bans/list")['bans']

    @staticmethod
    def get_user_in_database(api, username):
        """
        Get user details by username

        :param api: tshock client api
        :type api: TSHOCKClient
        :param username: username of a existing user
        :type username:
        :return:
        """

        return api.get(path="users/read", params={'user': username})

    @staticmethod
    def get_user_in_world(api, username):
        """
        Get information for a user who's playing ingame

        :param api: tshock client api
        :type api: TSHOCKClient
        :param username: username of a existing user
        :type username:
        :return:
        """
        return api.get(path="players/read",old_api=True, params={'player': username})

    @staticmethod
    def get_user_ip_in_world(api, username):
        """
        Get the IP address for a user who's playing ingame

        :param api: tshock client api
        :type api: TSHOCKClient
        :param username: username of a existing user
        :type username:
        :return:
        """
        return PlayerList.get_user_in_world(api="players/read/",old_api=True, params={"player":username})["ip"]

    @staticmethod
    def get_users_in_database(api):
        """
        Get users in database

        :param api: tshock client api
        :type api: TSHOCKClient
        :return:
        """

        return api.get(path="users/list")['users']
