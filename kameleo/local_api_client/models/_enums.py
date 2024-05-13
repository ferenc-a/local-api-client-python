# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.6, generator: @autorest/python@6.5.1)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AudioSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies how the audio will be spoofed. Possible values:
    'noise': Add some noise to the Audio generation
    'block': Completely block the Audio API
    'off': Turn off the spoofing, use the original settings.
    """

    OFF = "off"
    NOISE = "noise"
    BLOCK = "block"


class CanvasSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies how the canvas will be spoofed. Possible values:
    'intelligent': Use intelligent canvas spoofing. This will result non-unique canvas
    fingerprints.
    'noise': Add some noise to canvas generation.
    'block': Completely block the 2D API.
    'off': Turn off the spoofing, use the original settings.
    """

    INTELLIGENT = "intelligent"
    NOISE = "noise"
    BLOCK = "block"
    OFF = "off"


class DeviceMemorySpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies how the deviceMemory will be spoofed. Possible values:
    'automatic': Automatically set the values based on the Base Profile.
    'manual': Manually set the value in the profile. Valid values: 0.25, 0.5, 1, 2, 4, 8.
    'off': Turn off the spoofing, use the original settings.
    """

    AUTOMATIC = "automatic"
    MANUAL = "manual"
    OFF = "off"


class FontSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies how the fonts will be spoofed. Possible values:
    'enabled': Enable fonts spoofing.
    'disable': Disable fonts spoofing.
    """

    ENABLED = "enabled"
    DISABLED = "disabled"


class GeolocationSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies how the geolocation will be spoofed. Possible values:
    'automatic': Automatically set the values based on the IP address
    'manual': Manually set the longitude and latitude in the profile
    'block': Completely block the Geolocation API
    'off': Turn off the spoofing, use the original settings.
    """

    AUTOMATIC = "automatic"
    MANUAL = "manual"
    BLOCK = "block"
    OFF = "off"


class HardwareConcurrencySpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies how the hardwareConcurrency will be spoofed. Possible values:
    'automatic': Automatically set the values based on the Base Profile.
    'manual': Manually set the value in the profile. Valid values: 1, 2, 4, 8, 12, 16.
    'off': Turn off the spoofing, use the original settings.
    """

    AUTOMATIC = "automatic"
    MANUAL = "manual"
    OFF = "off"


class PasswordManagerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines whether the browser can save login credentials. Possible values are:
    'enabled': Credential saving is allowed.
    'disabled': Credential saving is blocked.
    """

    ENABLED = "enabled"
    DISABLED = "disabled"


class ProfileLifetimeState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Represents the lifetime states of a profile, indicating which actions
    can be performed with the associated browser engine at each state. Possible values are:


    * Unknown: State of the profile is undefined.
    * Created: Profile is created; the associated browser engine is not started.
    * Starting: The associated browser engine is starting.
    * Running: The associated browser engine is currently running.
    * Terminating: The associated browser engine is in the process of terminating.
    * Terminated: The associated browser engine is not running but has been started at least once.
    """

    CREATED = "created"
    STARTING = "starting"
    RUNNING = "running"
    TERMINATING = "terminating"
    TERMINATED = "terminated"
    LOCKED = "locked"
    UNKNOWN = "unknown"


class ProfilePersistenceState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the current save state of a profile, including cloud sync status. Possible values:
    'unsaved': The profile is not saved
    'saved': The profile is saved and current
    'syncing': The profile is currently synchronizing with the cloud.
    """

    UNSAVED = "unsaved"
    SAVED = "saved"
    SYNCING = "syncing"


class ProfileStorageLocation(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ProfileStorageLocation."""

    LOCAL = "local"
    CLOUD = "cloud"


class ProxyConnectionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Proxy connection settings of the profiles. Possible values:
    'none': Direct connection without any proxy.
    'http': Use a HTTP proxy for upstream communication.
    'socks5': Use a SOCKS5 proxy for upstream communication.
    'ssh': Use an SSH connection for upstream communication. Basically a SOCKS5 proxy created at
    the given SSH host.
    """

    NONE = "none"
    HTTP = "http"
    SOCKS5 = "socks5"
    SSH = "ssh"


class ScreenSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies how the screen will be spoofed. Possible values:
    'automatic': Automatically override the screen resolution based on the Base Profile.
    'manual': Manually override the screen resolution.
    'off': Turn off the spoofing, use the original settings.
    """

    AUTOMATIC = "automatic"
    MANUAL = "manual"
    OFF = "off"


class TimezoneSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies how the timezone will be spoofed. Possble values:
    'automatic': Timezone is automatically set by the IP
    'manual': Timezone is manually overridden in the profile
    'off': Turn off the spoofing, use the original settings.
    """

    AUTOMATIC = "automatic"
    MANUAL = "manual"
    OFF = "off"


class WebglMetaSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies how the WebGL vendor and renderer will be spoofed. Possible values:
    'automatic': The vendor and renderer values comes from the base profile.
    'manual': Manually set the vendor and renderer values.
    'off': Turn off the spoofing, use the original settings.
    """

    AUTOMATIC = "automatic"
    MANUAL = "manual"
    OFF = "off"


class WebglSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies how the WebGL will be spoofed. Possible values:
    'noise': Add some noise to the WebGL generation
    'block': Completely block the 3D API
    'off': Turn off the spoofing, use the original settings.
    """

    NOISE = "noise"
    BLOCK = "block"
    OFF = "off"


class WebRtcSpoofingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies how the WebRTC will be spoofed. Possible values:
    'automatic': Automatically set the webRTC public IP by the IP, and generates a random private
    IP like '2d2f78e7-1b1e-4345-a21b-07c904c98394.local'
    'manual': Manually override the webRTC public IP and private IP in the profile
    'block': Block the WebRTC functionality
    'off': Turn off the spoofing, use the original settings.
    """

    AUTOMATIC = "automatic"
    MANUAL = "manual"
    BLOCK = "block"
    OFF = "off"
