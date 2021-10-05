# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import APIServerProfile
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import ClusterProfile
    from ._models_py3 import ConsoleProfile
    from ._models_py3 import Display
    from ._models_py3 import IngressProfile
    from ._models_py3 import MasterProfile
    from ._models_py3 import NetworkProfile
    from ._models_py3 import OpenShiftCluster
    from ._models_py3 import OpenShiftClusterCredentials
    from ._models_py3 import OpenShiftClusterList
    from ._models_py3 import OpenShiftClusterUpdate
    from ._models_py3 import Operation
    from ._models_py3 import OperationList
    from ._models_py3 import Resource
    from ._models_py3 import ServicePrincipalProfile
    from ._models_py3 import TrackedResource
    from ._models_py3 import WorkerProfile
except (SyntaxError, ImportError):
    from ._models import APIServerProfile  # type: ignore
    from ._models import CloudErrorBody  # type: ignore
    from ._models import ClusterProfile  # type: ignore
    from ._models import ConsoleProfile  # type: ignore
    from ._models import Display  # type: ignore
    from ._models import IngressProfile  # type: ignore
    from ._models import MasterProfile  # type: ignore
    from ._models import NetworkProfile  # type: ignore
    from ._models import OpenShiftCluster  # type: ignore
    from ._models import OpenShiftClusterCredentials  # type: ignore
    from ._models import OpenShiftClusterList  # type: ignore
    from ._models import OpenShiftClusterUpdate  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationList  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ServicePrincipalProfile  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import WorkerProfile  # type: ignore

from ._azure_red_hat_open_shift4_client_enums import (
    ProvisioningState,
    VMSize,
    Visibility,
)

__all__ = [
    'APIServerProfile',
    'CloudErrorBody',
    'ClusterProfile',
    'ConsoleProfile',
    'Display',
    'IngressProfile',
    'MasterProfile',
    'NetworkProfile',
    'OpenShiftCluster',
    'OpenShiftClusterCredentials',
    'OpenShiftClusterList',
    'OpenShiftClusterUpdate',
    'Operation',
    'OperationList',
    'Resource',
    'ServicePrincipalProfile',
    'TrackedResource',
    'WorkerProfile',
    'ProvisioningState',
    'VMSize',
    'Visibility',
]