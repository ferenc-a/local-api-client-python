# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UpdateProfileRequest(Model):
    """UpdateProfileRequest.

    All required parameters must be populated in order to send to Azure.

    :param canvas: Required. Possible values include: 'intelligent', 'noise',
     'block', 'off'
    :type canvas: str or ~kameleo.local_api_client.models.enum
    :param webgl: Required. Possible values include: 'noise', 'block', 'off'
    :type webgl: str or ~kameleo.local_api_client.models.enum
    :param webgl_meta: Required.
    :type webgl_meta:
     ~kameleo.local_api_client.models.WebglMetaSpoofingTypeWebglMetaSpoofingOptionsMultiLevelChoice
    :param audio: Required. Possible values include: 'off', 'noise', 'block'
    :type audio: str or ~kameleo.local_api_client.models.enum
    :param timezone: Required.
    :type timezone:
     ~kameleo.local_api_client.models.TimezoneSpoofingTypeTimezoneMultiLevelChoice
    :param geolocation: Required.
    :type geolocation:
     ~kameleo.local_api_client.models.GeolocationSpoofingTypeGeolocationSpoofingOptionsMultiLevelChoice
    :param proxy: Required.
    :type proxy:
     ~kameleo.local_api_client.models.ProxyConnectionTypeServerMultiLevelChoice
    :param web_rtc: Required.
    :type web_rtc:
     ~kameleo.local_api_client.models.WebRtcSpoofingTypeWebRtcSpoofingOptionsMultiLevelChoice
    :param fonts: Required.
    :type fonts:
     ~kameleo.local_api_client.models.FontSpoofingTypeFontIListMultiLevelChoice
    :param plugins: Required.
    :type plugins:
     ~kameleo.local_api_client.models.PluginSpoofingTypePluginIListMultiLevelChoice
    :param screen: Required.
    :type screen:
     ~kameleo.local_api_client.models.ScreenSpoofingTypeScreenSizeMultiLevelChoice
    :param start_page: Required. This website will be opened in the browser
     when the profile launches.
    :type start_page: str
    :param password_manager: Required. Possible values include: 'enabled',
     'disabled'
    :type password_manager: str or ~kameleo.local_api_client.models.enum
    :param extensions: A list of extensions or addons should be loaded to the
     browser when starting the profile. For extensions that are added now, it
     should be an absolute path.
     For extensions already added to the profile in a previous update, the name
     is only enough.
     For chrome and edge use CRX3 format extensions. For firefox use signed xpi
     format addons.
    :type extensions: list[str]
    :param notes: A free text including any notes written by the user.
    :type notes: str
    :param name: Required. Profile name property. The value obtained by file
     name for existing profiles. For new profiles the value is generated by a
     random name generator.
    :type name: str
    :param tags: Profile tags
    :type tags: list[str]
    :param launcher: The mode how the profile should be launched. It
     determines which browser to launch. This cannot be modified after
     creation. Possible values are 'automatic', 'chrome', 'chromium',
     'firefox', 'edge', 'external'
    :type launcher: str
    """

    _validation = {
        'canvas': {'required': True},
        'webgl': {'required': True},
        'webgl_meta': {'required': True},
        'audio': {'required': True},
        'timezone': {'required': True},
        'geolocation': {'required': True},
        'proxy': {'required': True},
        'web_rtc': {'required': True},
        'fonts': {'required': True},
        'plugins': {'required': True},
        'screen': {'required': True},
        'start_page': {'required': True},
        'password_manager': {'required': True},
        'name': {'required': True, 'min_length': 1},
    }

    _attribute_map = {
        'canvas': {'key': 'canvas', 'type': 'str'},
        'webgl': {'key': 'webgl', 'type': 'str'},
        'webgl_meta': {'key': 'webglMeta', 'type': 'WebglMetaSpoofingTypeWebglMetaSpoofingOptionsMultiLevelChoice'},
        'audio': {'key': 'audio', 'type': 'str'},
        'timezone': {'key': 'timezone', 'type': 'TimezoneSpoofingTypeTimezoneMultiLevelChoice'},
        'geolocation': {'key': 'geolocation', 'type': 'GeolocationSpoofingTypeGeolocationSpoofingOptionsMultiLevelChoice'},
        'proxy': {'key': 'proxy', 'type': 'ProxyConnectionTypeServerMultiLevelChoice'},
        'web_rtc': {'key': 'webRtc', 'type': 'WebRtcSpoofingTypeWebRtcSpoofingOptionsMultiLevelChoice'},
        'fonts': {'key': 'fonts', 'type': 'FontSpoofingTypeFontIListMultiLevelChoice'},
        'plugins': {'key': 'plugins', 'type': 'PluginSpoofingTypePluginIListMultiLevelChoice'},
        'screen': {'key': 'screen', 'type': 'ScreenSpoofingTypeScreenSizeMultiLevelChoice'},
        'start_page': {'key': 'startPage', 'type': 'str'},
        'password_manager': {'key': 'passwordManager', 'type': 'str'},
        'extensions': {'key': 'extensions', 'type': '[str]'},
        'notes': {'key': 'notes', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'launcher': {'key': 'launcher', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(UpdateProfileRequest, self).__init__(**kwargs)
        self.canvas = kwargs.get('canvas', None)
        self.webgl = kwargs.get('webgl', None)
        self.webgl_meta = kwargs.get('webgl_meta', None)
        self.audio = kwargs.get('audio', None)
        self.timezone = kwargs.get('timezone', None)
        self.geolocation = kwargs.get('geolocation', None)
        self.proxy = kwargs.get('proxy', None)
        self.web_rtc = kwargs.get('web_rtc', None)
        self.fonts = kwargs.get('fonts', None)
        self.plugins = kwargs.get('plugins', None)
        self.screen = kwargs.get('screen', None)
        self.start_page = kwargs.get('start_page', None)
        self.password_manager = kwargs.get('password_manager', None)
        self.extensions = kwargs.get('extensions', None)
        self.notes = kwargs.get('notes', None)
        self.name = kwargs.get('name', None)
        self.tags = kwargs.get('tags', None)
        self.launcher = kwargs.get('launcher', None)
