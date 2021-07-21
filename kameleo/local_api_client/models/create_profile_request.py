# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CreateProfileRequest(Model):
    """CreateProfileRequest.

    All required parameters must be populated in order to send to Azure.

    :param base_profile_id: Required. The unique identifier of the base
     profile. This references the base profile which should be used to build
     the new profile.
    :type base_profile_id: str
    :param canvas: Required. Possible values include: 'intelligent', 'noise',
     'block', 'off'
    :type canvas: str or ~kameleo.local_api_client.models.enum
    :param webgl: Required.
    :type webgl:
     ~kameleo.local_api_client.models.WebglSpoofingTypeWebglSpoofingOptionsMultiLevelChoice
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
    :param start_page: This website will be opened in the browser when the
     profile launches.
    :type start_page: str
    :param password_manager: Possible values include: 'enabled', 'disabled'
    :type password_manager: str or ~kameleo.local_api_client.models.enum
    :param extensions: A list of abolute paths from where the profile should
     load extensions or addons when starting the browser. For chrome and edge
     use CRX3 format extensions. For firefox use signed xpi format addons.
    :type extensions: list[str]
    :param notes: A free text including any notes written by the user.
    :type notes: str
    :param launcher: The mode how the profile should be launched. It
     determines which browser to launch. This cannot be modified after
     creation. Possible values are 'automatic', 'chrome', 'chromium',
     'firefox', 'edge', 'external'
    :type launcher: str
    """

    _validation = {
        'base_profile_id': {'required': True},
        'canvas': {'required': True},
        'webgl': {'required': True},
        'timezone': {'required': True},
        'geolocation': {'required': True},
        'proxy': {'required': True},
        'web_rtc': {'required': True},
        'fonts': {'required': True},
        'plugins': {'required': True},
        'screen': {'required': True},
    }

    _attribute_map = {
        'base_profile_id': {'key': 'baseProfileId', 'type': 'str'},
        'canvas': {'key': 'canvas', 'type': 'str'},
        'webgl': {'key': 'webgl', 'type': 'WebglSpoofingTypeWebglSpoofingOptionsMultiLevelChoice'},
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
        'launcher': {'key': 'launcher', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CreateProfileRequest, self).__init__(**kwargs)
        self.base_profile_id = kwargs.get('base_profile_id', None)
        self.canvas = kwargs.get('canvas', None)
        self.webgl = kwargs.get('webgl', None)
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
        self.launcher = kwargs.get('launcher', None)