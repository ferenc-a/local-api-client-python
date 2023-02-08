# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BaseProfile(Model):
    """Representation of a base profile which is used to build profiles from.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. The version of the base profile. As time passes
     new base profile versions will be introduced. It is recommended to use the
     latest one.
    :type version: str
    :param id: Required. The unique identifier of the base profile. You can
     use this as a reference to create a new profile from this base profile.
    :type id: str
    :param device: Required.
    :type device: ~kameleo.local_api_client.models.Device
    :param os: Required.
    :type os: ~kameleo.local_api_client.models.Os
    :param browser: Required.
    :type browser: ~kameleo.local_api_client.models.Browser
    :param language: Required. Language of the base profile. Using ISO 639-1
     language codes.
    :type language: str
    :param resolution: Required. The screen size of the device in pixels
    :type resolution: str
    :param fonts: Required. A list of font types included in the profile
    :type fonts: list[str]
    :param plugins: Required. A list of plugins included in the profile
    :type plugins: list[str]
    :param webgl_meta: Required.
    :type webgl_meta: ~kameleo.local_api_client.models.WebglMeta
    """

    _validation = {
        'version': {'required': True},
        'id': {'required': True},
        'device': {'required': True},
        'os': {'required': True},
        'browser': {'required': True},
        'language': {'required': True},
        'resolution': {'required': True},
        'fonts': {'required': True},
        'plugins': {'required': True},
        'webgl_meta': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'device': {'key': 'device', 'type': 'Device'},
        'os': {'key': 'os', 'type': 'Os'},
        'browser': {'key': 'browser', 'type': 'Browser'},
        'language': {'key': 'language', 'type': 'str'},
        'resolution': {'key': 'resolution', 'type': 'str'},
        'fonts': {'key': 'fonts', 'type': '[str]'},
        'plugins': {'key': 'plugins', 'type': '[str]'},
        'webgl_meta': {'key': 'webglMeta', 'type': 'WebglMeta'},
    }

    def __init__(self, *, version: str, id: str, device, os, browser, language: str, resolution: str, fonts, plugins, webgl_meta, **kwargs) -> None:
        super(BaseProfile, self).__init__(**kwargs)
        self.version = version
        self.id = id
        self.device = device
        self.os = os
        self.browser = browser
        self.language = language
        self.resolution = resolution
        self.fonts = fonts
        self.plugins = plugins
        self.webgl_meta = webgl_meta
