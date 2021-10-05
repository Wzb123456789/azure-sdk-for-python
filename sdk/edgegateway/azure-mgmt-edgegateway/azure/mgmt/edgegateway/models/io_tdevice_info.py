# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IoTDeviceInfo(Model):
    """Metadata of IoT device/IoT Edge device to be configured.

    All required parameters must be populated in order to send to Azure.

    :param device_id: Required. ID of the IoT device/edge device.
    :type device_id: str
    :param io_thost_hub: Required. Host name for the IoT hub associated to the
     device.
    :type io_thost_hub: str
    :param authentication: IoT device authentication info.
    :type authentication: ~azure.mgmt.edgegateway.models.Authentication
    """

    _validation = {
        'device_id': {'required': True},
        'io_thost_hub': {'required': True},
    }

    _attribute_map = {
        'device_id': {'key': 'deviceId', 'type': 'str'},
        'io_thost_hub': {'key': 'ioTHostHub', 'type': 'str'},
        'authentication': {'key': 'authentication', 'type': 'Authentication'},
    }

    def __init__(self, **kwargs):
        super(IoTDeviceInfo, self).__init__(**kwargs)
        self.device_id = kwargs.get('device_id', None)
        self.io_thost_hub = kwargs.get('io_thost_hub', None)
        self.authentication = kwargs.get('authentication', None)