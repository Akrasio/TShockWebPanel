from thw.helpers.api import TSHOCKClient


class PlayerController(object):
    """
    Represents the controller for players
    """

    @staticmethod
    def add_player(api, username, password, group, ip=None):
        """
        Add a new player

        :param username: name of a new player
        :type username: str
        :param password: A "secret" password
        :type password: str
        :param group: a name of a existing group
        :type group: str
        :param ip: a ip address
        :type ip: str
        :param api: tshock client api
        :type api: TSHOCKClient
        :return: dict
        :rtype: dict
        """
        params = {'user': username, 'password': password, 'group': group}
        if ip is not None:
            params['ip'] = ip

        return api.post(path="users/create", params=params)

    @staticmethod
    def delete_player(api, username):
        """
        Delete a existing player

        :param api: tshock client api
        :type api: TSHOCKClient
        :param username: name of a existing user
        :type username: str
        :return: dict
        :rtype: dict
        """

        return api.delete(path="users/destroy", params={'user': username})

    @staticmethod
    def update_player(api, username, password, group=None):
        """
        Update a existing group

        :param api: tshock client api
        :type api: TSHOCKClient
        :param username: name of a existing user
        :type username: str
        :param password: a "secret" password
        :type password: str
        :param group: a name of existing group
        :type group: str
        :return: dict
        :rtype: dict
        """

        return api.post(path="users/update", params={'user': username, 'password': password, 'group': group})

    @staticmethod
    def ban_player_by_ip(api, ip, reason=None):
        """
        Ban a player

        :param api:
        :param ip:
        :param reason:
        :return:
        """

        params={'name': ip}
        if reason is not None:
            params['reason'] = reason

        return api.post(path="bans/create", old_api=True, params=params)

    @staticmethod
    def unban_player(api, username=None, ip=None):
        """
        Unban a player

        :param api:
        :param ip:
        :param username:
        :return:
        """

        if username is not None:
            params = {'ban': username, 'type': username}
        elif ip is not None:
            params = {'ban': ip, 'type': ip}
        else:
            raise RuntimeError("Missing username or ip")

        return api.post(path="bans/destroy", params=params)

    @staticmethod
    def ban_player_by_username(api, username, reason=None):
        """
        Ban a player by username

        :param api:
        :param username:
        :param reason:
        :return:
        """
        params = {'player': username}
        if reason is not None:
            params['reason'] = reason

        return api.post(path="players/ban", params=params)

    @staticmethod
    def kill_player_by_username(api, username, reason=None):
        """
        Kill a player by username

        :param api:
        :param username:
        :param reason:
        :return:
        """
        params = {'player': username}
        if reason is not None:
            params['reason'] = reason

        return api.post(path="players/kill", params=params)

    @staticmethod
    def mute_player_by_username(api, username, reason=None):
        """
        Mute a player by username

        :param api:
        :param username:
        :param reason:
        :return:
        """
        params = {'player': username}
        if reason is not None:
            params['reason'] = reason

        return api.post(path="players/mute", params=params)

    @staticmethod
    def unmute_player_by_username(api, username, reason=None):
        """
        Unmute a player by username

        :param api:
        :param username:
        :param reason:
        :return:
        """
        params = {'player': username}
        if reason is not None:
            params['reason'] = reason

        return api.post(path="players/unmute", params=params)

    @staticmethod
    def kick_player_by_username(api, username, reason=None):
        """
        Kick a player by username

        :param api:
        :param username:
        :param reason:
        :return:
        """
        params = {'player': username}
        if reason is not None:
            params['reason'] = reason

        return api.post(path="players/kick", params=params)