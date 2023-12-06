from thw.helpers.api import TSHOCKClient


class WorldController(object):
    """
    Represents the lists for world
    """

    @staticmethod
    def drop_meteor(api):
        """
        Drop a meteor in the world

        :param api: tshock client api
        :type api: TSHOCKClient
        :return: dict
        """

        return api.get(path="world/meteor", old_api=True)

    @staticmethod
    def set_blood_moon(api, status):
        """
        Set the status of the bloodmoon

        :param api: tshock client api
        :type api: TSHOCKClient
        :param status: status of the bloodmoon
        :type status: bool
        :return:
        """

        return api.get(path="world/bloodmoon/{0}".format(status), old_api=True)

    @staticmethod
    def butcher_npcs(api, status=True):
        """
        Butcher the NPCs

        :param api: tshock client api
        :type api: TSHOCKClient
        :param status: status if the NPCs can be butchered
        :type status: bool
        :return:
        """

        return api.get(path="world/butcher", params={'killfriendly': status})['response']

    @staticmethod
    def save_world(api):
        """
        Save the world

        :param api: tshock client api
        :type api: TSHOCKClient
        :return:
        """

        return api.get(path="world/save")

    @staticmethod
    def set_autosave_world(api, status):
        """
        Set the status of autosave

        :param api: tshock client api
        :type api: TSHOCKClient
        :param status: status of the autosave
        :type status: bool
        :return:
        """

        return api.get(path="world/autosave/state/{0}".format(status))
