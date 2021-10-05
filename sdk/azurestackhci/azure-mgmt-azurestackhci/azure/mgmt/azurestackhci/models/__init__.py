# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ArcSetting
    from ._models_py3 import ArcSettingList
    from ._models_py3 import Cluster
    from ._models_py3 import ClusterList
    from ._models_py3 import ClusterNode
    from ._models_py3 import ClusterPatch
    from ._models_py3 import ClusterReportedProperties
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import Extension
    from ._models_py3 import ExtensionList
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import PerNodeExtensionState
    from ._models_py3 import PerNodeState
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import TrackedResource
except (SyntaxError, ImportError):
    from ._models import ArcSetting  # type: ignore
    from ._models import ArcSettingList  # type: ignore
    from ._models import Cluster  # type: ignore
    from ._models import ClusterList  # type: ignore
    from ._models import ClusterNode  # type: ignore
    from ._models import ClusterPatch  # type: ignore
    from ._models import ClusterReportedProperties  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import Extension  # type: ignore
    from ._models import ExtensionList  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import PerNodeExtensionState  # type: ignore
    from ._models import PerNodeState  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import TrackedResource  # type: ignore

from ._azure_stack_hci_client_enums import (
    ActionType,
    ArcSettingAggregateState,
    CreatedByType,
    ExtensionAggregateState,
    NodeArcState,
    NodeExtensionState,
    Origin,
    ProvisioningState,
    Status,
)

__all__ = [
    'ArcSetting',
    'ArcSettingList',
    'Cluster',
    'ClusterList',
    'ClusterNode',
    'ClusterPatch',
    'ClusterReportedProperties',
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorResponse',
    'Extension',
    'ExtensionList',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'PerNodeExtensionState',
    'PerNodeState',
    'ProxyResource',
    'Resource',
    'TrackedResource',
    'ActionType',
    'ArcSettingAggregateState',
    'CreatedByType',
    'ExtensionAggregateState',
    'NodeArcState',
    'NodeExtensionState',
    'Origin',
    'ProvisioningState',
    'Status',
]