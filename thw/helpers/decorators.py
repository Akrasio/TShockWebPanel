from flask import jsonify
from functools import wraps
from requests import ConnectionError
from thw.helpers.api import HttpException


def pack(func):
    """
    Translate and pack the output of a function in a default JSON output format

    :param func: function
    :type func: Function
    """

    @wraps(func)
    def validate(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return jsonify({'status': result[1], 'result': result[0], 'valid': True})
        except HttpException as ex:
            return jsonify({'status': 403, 'result': ex, 'valid': False})
        except (RuntimeError, AttributeError, IOError, TypeError) as ex:
            return jsonify({'status': 500, 'result': str(ex), 'valid': True})
        except KeyError as ex:
            return jsonify({'status': 404, 'result': str(ex) + " not found", 'valid': True})
        except ConnectionError:
            return jsonify({'status': 500, 'result': 'Connection errors to TSHOCK server, '
                                                     'probably a wrong IP/PORT provided in `config/tshockweb.json`',
                            'valid': False})

    return validate

