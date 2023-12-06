import json
from functools import wraps
from requests import ConnectionError
from thw.helpers.decorators import pack
from thw.helpers.system import SystemHelper
from thw.controllers.servercontroller import ServerController
from thw.helpers.api import TSHOCKClient, HttpException
from flask import Flask, send_from_directory, request, redirect, jsonify


with open('config/tshockweb.json') as settings_file:
    settings = json.load(settings_file)
with open('config/terraria_items_by_name.json') as terraria_file:
    terraria_items_by_name = json.load(terraria_file)
with open('config/terraria_items_by_numbers.json') as terraria_file:
    terraria_items_by_id = json.load(terraria_file)
with open('config/terraria_buffs.json') as terraria_file:
    terraria_buff_by_id = json.load(terraria_file)

app = Flask(__name__, static_folder=settings['tshock_web']['web']['base_location'])
API_BASE_PATH = "/api"


def authenicate(func):
    """
    Authenticate the provided token

    :return: function if token is valid, Response if token is invalid
    """

    @wraps(func)
    def validate(*args, **kwargs):
        try:
            content = request.json
            if content is not None and 'token' in content:
                TSHOCKClient(ip=settings['tshock_server']['host'],
                             port=settings['tshock_server']['port'], token=content['token'])
            else:
                raise RuntimeError(403, 'No token provided')
            return func(*args, **kwargs)
        except HttpException as ex:
            return jsonify({'status': 403, 'result': ex, 'valid': False})
        except (RuntimeError, AttributeError, IOError) as ex:
            return jsonify({'status': 403, 'result': ex.ex, 'valid': True})
        except ConnectionError:
            return jsonify({'status': 500, 'result': 'Connection errors to TSHOCK server, '
                                                     'probably a wrong IP/PORT provided in `config/tshockweb.json`',
                            'valid': False})

    return validate


@app.route(API_BASE_PATH)
@pack
def base():
    """
    Ping the client back that the API is working :)

    :return: pong
    """
    return 'The TSHOCK WEB API is working!', 200


@app.route(API_BASE_PATH + "/config")
@pack
def config():
    """
    Fetch the config of tshockweb

    :return: config settings
    """

    return settings, 200


@app.route(API_BASE_PATH + "/config/terraria/item/by_name", methods=['POST'])
@pack
def get_item_by_name():
    """
    Fetch the item by name

    :return: item id
    """

    content = request.json
    if content is not None and 'name' in content:
        return terraria_items_by_name[content['name']], 200
    else:
        raise RuntimeError('No name provided')


@app.route(API_BASE_PATH + "/config/terraria/item/by_id", methods=['POST'])
@pack
def get_item_by_id():
    """
    Fetch the item by id

    :return: item name
    """

    content = request.json
    if content is not None and 'id' in content:
        return terraria_items_by_id[str(content['id'])], 200
    else:
        raise RuntimeError('No id provided')


@app.route(API_BASE_PATH + "/config/terraria/buff/by_id", methods=['POST'])
@pack
def get_buff_by_id():
    """
    Fetch the buff by id

    :return: buff name
    """

    content = request.json
    if content is not None and 'id' in content:
        return terraria_buff_by_id[str(content['id'])], 200
    else:
        raise RuntimeError('No id provided')


@app.route(API_BASE_PATH + "/login", methods=['POST'])
@pack
def login():
    """
    Login into the TSHOCK server

    :return: dict if token is valid, string if token is invalid
    """
    content = request.json
    try:
        if content is not None:
            if 'username' in content and 'password' in content:
                api = TSHOCKClient(ip=settings['tshock_server']['host'], port=settings['tshock_server']['port'],
                                   username=content['username'], password=content['password'])
                return {'token': api.token()}, 200
            else:
                raise HttpException(403, 'No username/password provided')
        else:
            raise HttpException(403, 'No username/password provided')
    except HttpException as ex:
        return str(ex), 403
    except (RuntimeError, AttributeError, IOError) as ex:
        return str(ex), 403
    except ConnectionError:
        return 'Connection errors to TSHOCK server, probably a wrong IP/PORT provided in `config/tshockweb.json`', 500


@app.route(API_BASE_PATH + "/logout", methods=['POST'])
@authenicate
@pack
def logout():
    """
    Logout from the TSHOCK server

    :return: message if logout was successful
    """
    content = request.json
    if content is not None and 'token' in content:
        api = TSHOCKClient(ip=settings['tshock_server']['host'],
                           port=settings['tshock_server']['port'], token=content['token'])
        return ServerController.destroy_token(api=api, token=content['token']), 200


@app.route(API_BASE_PATH + "/validation", methods=['POST'])
@authenicate
@pack
def validation():
    """
    Validate token on TSHOCK server

    :return: string if the token is valid
    """
    return 'The given token is valid!', 200


@app.route(API_BASE_PATH + "/documentation")
@pack
def documentation():
    """
    Documentation generator that generates the API documentation

    :return: dict
    """
    docs = {}

    for directory in SystemHelper.list_directories(settings['tshock_web']['api']['base']):
        subdirs = SystemHelper.list_directories('{0}/{1}'.format(settings['tshock_web']['api']['base'], directory))
        if len(subdirs) != 0:
            for subdir in subdirs:
                temp_subdir = {}
                files = SystemHelper.list_files(path='{0}/{1}/{2}'.format(settings['tshock_web']['api']['base'],
                                                                          directory, subdir), remove_suffix=True)
                for filename in files:
                    temp_subdir[filename] = {}
                    methods = SystemHelper.list_methods_of_module(path='{0}/{1}/{2}/{3}.py'.format(
                        settings['tshock_web']['api']['base'], directory, subdir, filename), module_name=filename)
                    for method in methods:
                        # fetch method parameters
                        current_class = SystemHelper.get_class_by_path(path='{0}/{1}/{2}/{3}.py'.format(
                            settings['tshock_web']['api']['base'], directory, subdir, filename), module_name=filename)
                        current_method = getattr(current_class, method)
                        temp_subdir[filename][method] = [argument for argument in
                                                         list(current_method.func_code.co_varnames)
                                                         if 'api' not in argument and 'params' not in argument]

                docs[directory] = temp_subdir
        else:
            temp_subdir = {}
            files = SystemHelper.list_files(path='{0}/{1}'.format(settings['tshock_web']['api']['base'],
                                                                  directory), remove_suffix=True)
            for filename in files:
                temp_subdir[filename] = {}
                methods = SystemHelper.list_methods_of_module(path='{0}/{1}/{2}.py'.format(
                    settings['tshock_web']['api']['base'], directory, filename), module_name=filename)
                for method in methods:
                    # fetch method parameters
                    current_class = SystemHelper.get_class_by_path(path='{0}/{1}/{2}.py'.format(
                    settings['tshock_web']['api']['base'], directory, filename), module_name=filename)
                    current_method = getattr(current_class, method)
                    temp_subdir[filename][method] = [argument for argument in list(current_method.func_code.co_varnames)
                                                     if 'api' not in argument and 'params' not in argument]
            docs[directory] = temp_subdir

    return docs, 200


@app.route(API_BASE_PATH + "/<path:path>", methods=['POST'])
@authenicate
@pack
def serve_api(path):
    """
    Serve the PYTHON api through flask as REST API

    :param path: api path + method (e.g. model/lists/players/get_current_players)
    :type path: str
    :return: results from path + method
    """

    seperated_path = path.split('/')

    content = request.json
    api = TSHOCKClient(ip=settings['tshock_server']['host'], port=settings['tshock_server']['port'],
                       token=content['token'])

    # parse api path
    api_path = path.replace('/' + seperated_path[-1], '')

    # fetch class
    current_class = SystemHelper.get_class_by_path(path="{0}/{1}.py".format(settings['tshock_web']['api']['base'],
                                                                            api_path),
                                                   module_name=seperated_path[-2])
    # remove token and add api
    del content['token']
    content['api'] = api

    # fetch method
    method = getattr(current_class, seperated_path[-1])

    try:
        result = method(**content)
        return {'api_path': api_path,
                'method': seperated_path[-1],
                'output': result}, 200
    except TypeError as ex:
        # remove api argument because its not needed as we pass a token
        arguments = [argument for argument in list(method.func_code.co_varnames) if 'api' not in argument]
        return {'api_path': api_path,
                'method': seperated_path[-1],
                'output': str(ex + ',' + ' required arguments: ' + str(arguments))}, 404


@app.route('/<path:filename>')
def serve_files(filename):
    """
    Serves the HTML files for tshockweb

    :param filename: a filename under `webapps` (e.g. html/pages/login.html)
    :type filename: str
    :return: file
    """

    return send_from_directory(app.static_folder, filename)


@app.route('/')
def serve_homepage():
    """
    Serves the homepage for tshockweb

    :return: file
    """
    return redirect(settings['tshock_web']['web']['base_location'] + '/' + settings['tshock_web']['web']['homepage'])


if __name__ == "__main__":
    app.run(host=settings['tshock_web']['api']['host'], port=settings['tshock_web']['api']['port'],
            debug=settings['tshock_web']['api']['debug'])
