import json
import requests


class HttpException(RuntimeError):
    """
    Custom Http Exception class
    """

    def __init__(self, status_code, *args, **kwargs):
        super(HttpException, self).__init__(*args, **kwargs)
        self.status_code = status_code


class TSHOCKClient(object):
    """
    Represents the TSHOCK client
    """

    def __init__(self, ip,  port, username=None, password=None, verify=False, main_version='v2', raw_response=False,
                 token=None):
        """
        Initializes the object with credentials and connection information
        """
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.version = main_version
        self.base_url = 'http://{0}:{1}/{2}'.format(self.ip, self.port, self.version)
        self.old_base_url = 'http://{0}:{1}'.format(self.ip, self.port)
        self._token = token
        self._verify = verify
        self._raw_response = raw_response

        # connect to the api if a token has not been provided
        if token is None:
            self._connect()
        else:
            self.validate()

    def _connect(self):
        """
        Authenticates to the api
        """
        raw_response = requests.get('{0}/token/create?username={1}&password={2}'.format(self.base_url, self.username,
                                                                                        self.password)).text
        try:
            response = self._process(raw_response=raw_response)
        except HttpException:
            if self._raw_response is True:
                return raw_response
            raise

        self._token = response['token']

    def validate(self):
        """
        Validates if the authentication token works

        :return: Assosiated user
        :rtype: str
        :raises: HttpException
        """
        raw_response = requests.get('{0}/tokentest?token={1}'.format(self.old_base_url, self._token)).text
        try:
            response = self._process(raw_response=raw_response)
            return response['associateduser']
        except HttpException:
            if self._raw_response is True:
                return raw_response
            raise

    def token(self):
        """
        Fetch the authentication token

        :return: auth token
        :rtype: str
        """

        return str(self._token)

    def _process(self, raw_response):
        """
        Processes a raw call and throws any required exceptions

        :param raw_response: a raw requests.text output
        :type raw_response: str
        :return: parsed response or exception
        :rtype: dict
        :raises: HttpException
        """

        parsed_response = self._to_json(raw_response)

        status = int(parsed_response['status'])
        if status != 200:
            raise HttpException(status, parsed_response['error'])
        else:
            return parsed_response

    def _call(self, path, function, params, old_api=False, version=None):
        """
        Performs a call based on the given parameters

        :param path: api path (e.g. /v2/players/unmute -> players/unmute)
        :type path: str
        :param function: request function
        :type function: requests.function
        :param params: optional parameters
        :type params: dict
        :param version: override the main version
        :type version: str
        :return: result of given call
        :rtype: dict
        """
        if version is not None:
            request = '{0}/{1}/{2}?token={3}'.format(self.old_base_url, version, path, self._token)
        elif not old_api:
            request = '{0}/{1}?token={2}'.format(self.base_url, path, self._token)
        else:
            request = '{0}/{1}?token={2}'.format(self.old_base_url, path, self._token)

        if not bool(params):
            raw_response = function(request).text
        else:
            formated_params = ""
            for k, v in params.items():
                formated_params += k+"="+str(v)+"&"
            raw_response = function("{0}&{1}".format(request, formated_params[:-1])).text
        try:
            response = self._process(raw_response=raw_response)
            return response
        except HttpException:
            if self._raw_response is True:
                return raw_response
            raise

    def delete(self, path, params={}, old_api=False, version=None):
        """
        Executes a DELETE call

        :param path: Specification for to fill out in the URL, eg: /players/unmute
        :type path: str
        :param old_api: use the old api base path
        :type old_api: bool
        :param version: override the main version
        :type version: str
        :param params: Additional query parameters, eg: username, password
        :type params: dict
        :return: result
        :rtype: dict
        """
        return self._call(path=path, params=params, function=requests.delete, old_api=old_api, version=version)

    def get(self, path, params={}, old_api=False, version=None):
        """
        Executes a GET call
        :param path: Specification for to fill out in the URL, eg: /players/unmute
        :type path: str
        :param params: Additional query parameters, eg: username, password
        :type params: dict
        :param old_api: use the old api base path
        :type old_api: bool
        :param version: override the main version
        :type version: str
        :return: result
        :rtype: dict
        """
        return self._call(path=path, params=params, function=requests.get, old_api=old_api, version=version)

    def post(self, path, params={}, old_api=False, version=None):
        """
        Executes a POST call
        :param path: Specification for to fill out in the URL, eg: /players/unmute
        :type path: str
        :param old_api: use the old api base path
        :type old_api: bool
        :param params: Additional query parameters, eg: username, password
        :type params: dict
        :param version: override the main version
        :type version: str
        :return: result
        :rtype: dict
        """
        return self._call(path=path, params=params, function=requests.post, old_api=old_api, version=version)

    def put(self, path, params={}, old_api=False, version=None):
        """
        Executes a PUT call
        :param path: Specification for to fill out in the URL, eg: /players/unmute
        :type path: str
        :param old_api: use the old api base path
        :type old_api: bool
        :param params: Additional query parameters, eg: username, password
        :type params: dict
        :param version: override the main version
        :type version: str
        :return: result
        :rtype: dict
        """
        return self._call(path=path, params=params, function=requests.put, old_api=old_api, version=version)

    @staticmethod
    def _to_json(dict_or_json):
        """
        Converts a dict/json to a json

        :param dict_or_json: dict or json with data
        :type dict_or_json: dict/string
        :return: json data
        :rtype: dict
        """
        try:
            json_object = json.loads(str(dict_or_json))
        except ValueError:
            return json.dumps(dict_or_json)
        return json_object
