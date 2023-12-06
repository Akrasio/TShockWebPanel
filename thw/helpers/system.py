import os
import imp
import inspect


class SystemHelper(object):
    """
    Represents the system of the server
    """

    @staticmethod
    def get_system_statistics():
        """
        Gets the local system statistics
            * CPU % usage
            * RAM % usage
            * DISK % usage

        :return:
        """

        return

    @staticmethod
    def list_directories(path):
        """
        Gets the directories from a path

        :param path:
        :return:
        """

        return [directory for directory in os.listdir(path) if os.path.isdir(path+'/'+directory)]

    @staticmethod
    def list_files(path, remove_suffix=False):
        """
        Gets the files from a path

        :param path:
        :return:
        """
        if not remove_suffix:
            return [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)
                    and 'pyc' not in directory and '__init__.py' not in directory]
        else:
            return [directory.split('.')[0] for directory in os.listdir(path)
                    if not os.path.isdir(path + '/' + directory)
                    and 'pyc' not in directory and '__init__.py' not in directory]

    @staticmethod
    def list_methods_of_module(path, module_name):
        """
        Lists the methods by path and module names

        :param path: relative path of module (e.g. thw/model/lists/playercontroller.py)
        :type path: str
        :param module_name: name of a module (e.g. players)
        :type module_name: str
        :return: list of methods for given class
        :rtype: list
        """

        module = imp.load_source(module_name, path)
        for member in inspect.getmembers(module):
            try:
                if member[1].__module__ == module_name:
                    return [method for method in member[1].__dict__.keys() if '__' not in method
                            and not method.isupper()]
            except AttributeError:
                continue

    @staticmethod
    def get_class_by_path(path, module_name):
        """
        Fetch a class by path and module name

        :param path: relative path of module (e.g. thw/model/lists/playercontroller.py)
        :type path: str
        :param module_name: name of a module (e.g. players)
        :type module_name: str
        :return: Class
        :rtype: Class
        """

        module = imp.load_source(module_name, path)
        for member in inspect.getmembers(module):
            try:
                if member[1].__module__ == module_name:
                    return member[1]
            except AttributeError:
                continue
