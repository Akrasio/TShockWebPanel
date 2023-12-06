from thw.helpers.api import TSHOCKClient


class ServerList(object):
    """
    Represents the lists for server
    """

    @staticmethod
    def get_server_information(api):
        """
        Get server

        :param api: tshock client api
        :type api: TSHOCKClient
        :return: dict
        """

        return api.get(path="server/status")

    @staticmethod
    def get_motd(api):
        """
        Get server motd

        :param api: tshock client api
        :type api: TSHOCKClient
        :return: dict
        """

        return api.get(path="server/motd", version='v3')

    @staticmethod
    def get_server_rules(api):
        """
        Get server rules

        :param api: tshock client api
        :type api: TSHOCKClient
        :return: dict
        """

        return api.get(path="server/rules", version='v3')