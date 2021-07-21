# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Server(Model):
    """Represents a server connection. It can be used as a proxy server connection
    as well.

    All required parameters must be populated in order to send to Azure.

    :param host: Required. Gets or sets the hostname where the service is
     provided from.
    :type host: str
    :param port: Required. Gets or sets the port where the service is provided
     from.
    :type port: int
    :param id: Gets or sets the identity information provided for the service.
     This could be a custom id or username or anything which identifies a
     resource on the remote service. Use it as a proxy username. This field is
     optional.
    :type id: str
    :param secret: Gets or sets the shared secret between the client and the
     service provider. Use it as a proxy password. This field is optional.
    :type secret: str
    """

    _validation = {
        'host': {'required': True},
        'port': {'required': True},
    }

    _attribute_map = {
        'host': {'key': 'host', 'type': 'str'},
        'port': {'key': 'port', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'secret': {'key': 'secret', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Server, self).__init__(**kwargs)
        self.host = kwargs.get('host', None)
        self.port = kwargs.get('port', None)
        self.id = kwargs.get('id', None)
        self.secret = kwargs.get('secret', None)