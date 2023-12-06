from thw.helpers.api import TSHOCKClient


class WorldList(object):
    """
    Represents the lists for world
    """

    @staticmethod
    def get_world_details(api):
        """
        Get world

        :param api: tshock client api
        :type api: TSHOCKClient
        :return: dict
        """

        return api.get(path="world/read", old_api=True)

