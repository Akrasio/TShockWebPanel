from thw.helpers.api import TSHOCKClient


class ServerController(object):
    """
    Represents the lists for server
    """

    @staticmethod
    def broadcast_message(api, message):
        """
        Get server

        :param api: tshock client api
        :type api: TSHOCKClient
        :param message: the message to be broadcasted
        :type message: str
        :return: dict
        """

        return api.get(path="server/broadcast", params={'msg': message})['response']

    @staticmethod
    def restart_server(api, message, save=True):
        """
        Restart the server

        :param api: tshock client api
        :type api: TSHOCKClient
        :param message: the message to be broadcasted before shutdown
        :type message: str
        :param save: server save before shutdown?
        :type save: bool
        :return: dict
        """

        return api.get(path="server/restart", params={'msg': message, 'confirm': True, 'nosave': not save},
                       version='v3')

    @staticmethod
    def stop_server(api, message, save=True):
        """
        Stop the server

        :param api: tshock client api
        :type api: TSHOCKClient
        :param message: the message to be broadcasted before shutdown
        :type message: str
        :param save: server save before shutdown?
        :type save: bool
        :return: dict
        """

        return api.get(path="server/off", params={'msg': message, 'confirm': True, 'nosave': not save})

    @staticmethod
    def reload_server_configs(api):
        """
        Reload config files for the server

        :param api: tshock client api
        :type api: TSHOCKClient
        :return: dict
        """

        return api.get(path="server/reload", version='v3')

    @staticmethod
    def destroy_token(api, token):
        """
        Destroy a token on the tshock server (e.g. for user logout)

        :param api: tshock client api
        :type api: TSHOCKClient
        :param token: a valid tshock api token
        :type token: str
        :return: dict
        """

        return api.get(path="token/destroy/{0}".format(token), old_api=True)['response']

    @staticmethod
    def execute_cmd(api, command):
        """
        Execute a command on the server

        :param api: tshock client api
        :type api: TSHOCKClient
        :param command: the command and arguments to execute
        :type command: str
        :return: dict
        """

        return api.get(path="server/rawcmd", params={'cmd': command}, version='v3')['response']