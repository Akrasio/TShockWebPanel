class TSHOCKPermission(object):
    """
    Represents the TSHOCK permissions
    """

    GROUPS = {'tshock.rest.groups.manage': ['Create a new group', 'Delete a group'],
              'tshock.rest.groups.view': ['Display information of a group', 'View all groups in the TShock database']}
    PLAYER = {'tshock.rest.bans.manage': ['Create a new ban entry', 'Delete an existing ban entry'],
              'tshock.rest.bans.view': ['View the details of a specific ban', 'View all bans in the TShock database'],
              'tshock.rest.kick': ['Kick a player off the server'],
              'tshock.rest.kill': ['Kill a player'],
              'tshock.rest.mute': ['Mute a player', 'Unmute a player'],
              'tshock.rest.users.info': ['Get information for a user'],
              'tshock.rest.users.view': ['Returns the list of user accounts that are currently in use on the server',
                                         'List detailed information for a user account',
                                         'Lists all user accounts in the TShock database'],
              'tshock.rest.users.manage': ['Create a new TShock user account', 'Destroy a TShock user account',
                                           'Update a users information.']}
    SERVER = {'tshock.rest.command': ['Executes a remote command on the server, and returns the output of the command'],
              'tshock.rest.maintenance': ['Turn the server off', 'Attempt to restart the server'],
              'tshock.rest.cfg': ['Reload config files for the server', 'Save the world']}
    WORLD = {'tshock.rest.causeevents': ['Toggle the status of blood moon', 'Drops a meteor on the world'],
             'tshock.rest.butcher': ['Butcher NPCs']}

    @staticmethod
    def list_permissions():
        """
        Lists the permissions of TSHOCK

        :return:
        """

        return {perm_category: getattr(TSHOCKPermission, perm_category)
                for perm_category in TSHOCKPermission.list_permission_groups()}

    @staticmethod
    def list_permission_groups():
        """
        Lists the groups in permissions of TSHOCK

        :return:
        """

        return [perm_category for perm_category in dir(TSHOCKPermission) if '__' not in perm_category
                and perm_category.isupper()]

    @staticmethod
    def get_permissions_by_category_name(cat_name):
        """
        Get permissions by a group name

        :param cat_name:
        :type cat_name:
        :return:
        """

        if hasattr(TSHOCKPermission, cat_name):
            return getattr(TSHOCKPermission, cat_name)
        else:
            raise RuntimeError('Permission `{0}` does not exists'.format(cat_name))
