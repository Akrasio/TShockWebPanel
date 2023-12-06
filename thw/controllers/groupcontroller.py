from thw.helpers.api import TSHOCKClient


class GroupController(object):
    """
    Represents the controller for groups
    """

    @staticmethod
    def add_group(api, group_name, permissions=None):
        """
        Add a new group

        :param group_name: name of a new group
        :type group_name: str
        :param permissions: A comma seperated list of permissions for the new group (DEFAULT=None)
        :type permissions: str
        :param api: tshock client api
        :type api: TSHOCKClient
        :return: dict
        :rtype: dict
        """
        params = {'group': group_name}
        if permissions is not None:
            params['permissions'] = permissions

        return api.post(path="groups/create", params=params)

    @staticmethod
    def delete_group(api, group_name):
        """
        Delete a existing group

        :param api: tshock client api
        :type api: TSHOCKClient
        :param group_name: name of a existing group
        :type group_name: str
        :return: dict
        :rtype: dict
        """

        return api.delete(path="groups/destroy", params={'group': group_name})

    @staticmethod
    def update_group(api, group_name, permissions=None):
        """
        Update a existing group

        :param api: tshock client api
        :type api: TSHOCKClient
        :param group_name: name of a existing group
        :type group_name: str
        :param permissions: A comma seperated list of permissions for the new group (DEFAULT=None)
        :type permissions: str
        :return: dict
        :rtype: dict
        """

        params = {'group': group_name}
        if permissions is not None:
            params['permissions'] = permissions

        return api.post(path="groups/update", params=params)


