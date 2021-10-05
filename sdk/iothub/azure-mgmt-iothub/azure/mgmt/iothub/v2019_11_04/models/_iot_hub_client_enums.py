# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AccessRights(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The permissions assigned to the shared access policy.
    """

    REGISTRY_READ = "RegistryRead"
    REGISTRY_WRITE = "RegistryWrite"
    SERVICE_CONNECT = "ServiceConnect"
    DEVICE_CONNECT = "DeviceConnect"
    REGISTRY_READ_REGISTRY_WRITE = "RegistryRead, RegistryWrite"
    REGISTRY_READ_SERVICE_CONNECT = "RegistryRead, ServiceConnect"
    REGISTRY_READ_DEVICE_CONNECT = "RegistryRead, DeviceConnect"
    REGISTRY_WRITE_SERVICE_CONNECT = "RegistryWrite, ServiceConnect"
    REGISTRY_WRITE_DEVICE_CONNECT = "RegistryWrite, DeviceConnect"
    SERVICE_CONNECT_DEVICE_CONNECT = "ServiceConnect, DeviceConnect"
    REGISTRY_READ_REGISTRY_WRITE_SERVICE_CONNECT = "RegistryRead, RegistryWrite, ServiceConnect"
    REGISTRY_READ_REGISTRY_WRITE_DEVICE_CONNECT = "RegistryRead, RegistryWrite, DeviceConnect"
    REGISTRY_READ_SERVICE_CONNECT_DEVICE_CONNECT = "RegistryRead, ServiceConnect, DeviceConnect"
    REGISTRY_WRITE_SERVICE_CONNECT_DEVICE_CONNECT = "RegistryWrite, ServiceConnect, DeviceConnect"
    REGISTRY_READ_REGISTRY_WRITE_SERVICE_CONNECT_DEVICE_CONNECT = "RegistryRead, RegistryWrite, ServiceConnect, DeviceConnect"

class Capabilities(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The capabilities and features enabled for the IoT hub.
    """

    NONE = "None"
    DEVICE_MANAGEMENT = "DeviceManagement"

class EndpointHealthStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Health statuses have following meanings. The 'healthy' status shows that the endpoint is
    accepting messages as expected. The 'unhealthy' status shows that the endpoint is not accepting
    messages as expected and IoT Hub is retrying to send data to this endpoint. The status of an
    unhealthy endpoint will be updated to healthy when IoT Hub has established an eventually
    consistent state of health. The 'dead' status shows that the endpoint is not accepting
    messages, after IoT Hub retried sending messages for the retrial period. See IoT Hub metrics to
    identify errors and monitor issues with endpoints. The 'unknown' status shows that the IoT Hub
    has not established a connection with the endpoint. No messages have been delivered to or
    rejected from this endpoint
    """

    UNKNOWN = "unknown"
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    DEAD = "dead"

class IotHubNameUnavailabilityReason(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The reason for unavailability.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"

class IotHubReplicaRoleType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The role of the region, can be either primary or secondary. The primary region is where the IoT
    hub is currently provisioned. The secondary region is the Azure disaster recovery (DR) paired
    region and also the region where the IoT hub can failover to.
    """

    PRIMARY = "primary"
    SECONDARY = "secondary"

class IotHubScaleType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the scaling enabled.
    """

    AUTOMATIC = "Automatic"
    MANUAL = "Manual"
    NONE = "None"

class IotHubSku(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The name of the SKU.
    """

    F1 = "F1"
    S1 = "S1"
    S2 = "S2"
    S3 = "S3"
    B1 = "B1"
    B2 = "B2"
    B3 = "B3"

class IotHubSkuTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The billing tier for the IoT hub.
    """

    FREE = "Free"
    STANDARD = "Standard"
    BASIC = "Basic"

class IpFilterActionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The desired action for requests captured by this rule.
    """

    ACCEPT = "Accept"
    REJECT = "Reject"

class JobStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the job.
    """

    UNKNOWN = "unknown"
    ENQUEUED = "enqueued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class JobType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the job.
    """

    UNKNOWN = "unknown"
    EXPORT = "export"
    IMPORT_ENUM = "import"
    BACKUP = "backup"
    READ_DEVICE_PROPERTIES = "readDeviceProperties"
    WRITE_DEVICE_PROPERTIES = "writeDeviceProperties"
    UPDATE_DEVICE_CONFIGURATION = "updateDeviceConfiguration"
    REBOOT_DEVICE = "rebootDevice"
    FACTORY_RESET_DEVICE = "factoryResetDevice"
    FIRMWARE_UPDATE = "firmwareUpdate"

class RouteErrorSeverity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Severity of the route error
    """

    ERROR = "error"
    WARNING = "warning"

class RoutingSource(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The source that the routing rule is to be applied to, such as DeviceMessages.
    """

    INVALID = "Invalid"
    DEVICE_MESSAGES = "DeviceMessages"
    TWIN_CHANGE_EVENTS = "TwinChangeEvents"
    DEVICE_LIFECYCLE_EVENTS = "DeviceLifecycleEvents"
    DEVICE_JOB_LIFECYCLE_EVENTS = "DeviceJobLifecycleEvents"

class RoutingStorageContainerPropertiesEncoding(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Encoding that is used to serialize messages to blobs. Supported values are 'avro',
    'avrodeflate', and 'JSON'. Default value is 'avro'.
    """

    AVRO = "Avro"
    AVRO_DEFLATE = "AvroDeflate"
    JSON = "JSON"

class TestResultStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Result of testing route
    """

    UNDEFINED = "undefined"
    FALSE = "false"
    TRUE = "true"