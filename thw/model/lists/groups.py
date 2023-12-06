from thw.helpers.api import TSHOCKClient
from thw.helpers.permission import TSHOCKPermission


class GroupList(object):
    """
    Represents the lists for groups
    """

    @staticmethod
    def list_permissions():
        """
        Lists the permissions

        :return:
        """

        return TSHOCKPermission.list_permissions()

    @staticmethod
    def list_permission_groups():
        """
        Lists the groups in permissions of TSHOCK

        :return:
        """

        return TSHOCKPermission.list_permission_groups()

    @staticmethod
    def get_permissions_by_category(category_name):
        """
        Get permissions by a group name

        :param category_name:
        :type category_name:
        :return:
        """

        return TSHOCKPermission.get_permissions_by_category_name(cat_name=category_name)

    @staticmethod
    def get_groups(api):
        """
        Get groups

        :param api: tshock client api
        :type api: TSHOCKClient
        :return: dict
        :rtype: dict
        """

        return api.get(path="groups/list")['groups']

    @staticmethod
    def get_group_by_name(api, group_name):
        """
        Get group details by name

        :param group_name: name of a existing group
        :type group_name: str
        :param api: tshock client api
        :type api: TSHOCKClient
        :return: dict
        :rtype: dict
        """

        return api.get(path="groups/read", params={'group': group_name})
