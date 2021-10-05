# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ADLSGen1FileDataSet
    from ._models_py3 import ADLSGen1FolderDataSet
    from ._models_py3 import ADLSGen2FileDataSet
    from ._models_py3 import ADLSGen2FileDataSetMapping
    from ._models_py3 import ADLSGen2FileSystemDataSet
    from ._models_py3 import ADLSGen2FileSystemDataSetMapping
    from ._models_py3 import ADLSGen2FolderDataSet
    from ._models_py3 import ADLSGen2FolderDataSetMapping
    from ._models_py3 import Account
    from ._models_py3 import AccountList
    from ._models_py3 import AccountUpdateParameters
    from ._models_py3 import BlobContainerDataSet
    from ._models_py3 import BlobContainerDataSetMapping
    from ._models_py3 import BlobDataSet
    from ._models_py3 import BlobDataSetMapping
    from ._models_py3 import BlobFolderDataSet
    from ._models_py3 import BlobFolderDataSetMapping
    from ._models_py3 import ConsumerInvitation
    from ._models_py3 import ConsumerInvitationList
    from ._models_py3 import ConsumerSourceDataSet
    from ._models_py3 import ConsumerSourceDataSetList
    from ._models_py3 import DataSet
    from ._models_py3 import DataSetList
    from ._models_py3 import DataSetMapping
    from ._models_py3 import DataSetMappingList
    from ._models_py3 import DataShareError
    from ._models_py3 import DataShareErrorInfo
    from ._models_py3 import DefaultDto
    from ._models_py3 import DimensionProperties
    from ._models_py3 import Identity
    from ._models_py3 import Invitation
    from ._models_py3 import InvitationList
    from ._models_py3 import KustoClusterDataSet
    from ._models_py3 import KustoClusterDataSetMapping
    from ._models_py3 import KustoDatabaseDataSet
    from ._models_py3 import KustoDatabaseDataSetMapping
    from ._models_py3 import OperationList
    from ._models_py3 import OperationMetaLogSpecification
    from ._models_py3 import OperationMetaMetricSpecification
    from ._models_py3 import OperationMetaServiceSpecification
    from ._models_py3 import OperationModel
    from ._models_py3 import OperationModelProperties
    from ._models_py3 import OperationResponse
    from ._models_py3 import ProviderShareSubscription
    from ._models_py3 import ProviderShareSubscriptionList
    from ._models_py3 import ProxyDto
    from ._models_py3 import ScheduledSourceSynchronizationSetting
    from ._models_py3 import ScheduledSynchronizationSetting
    from ._models_py3 import ScheduledTrigger
    from ._models_py3 import Share
    from ._models_py3 import ShareList
    from ._models_py3 import ShareSubscription
    from ._models_py3 import ShareSubscriptionList
    from ._models_py3 import ShareSubscriptionSynchronization
    from ._models_py3 import ShareSubscriptionSynchronizationList
    from ._models_py3 import ShareSynchronization
    from ._models_py3 import ShareSynchronizationList
    from ._models_py3 import SourceShareSynchronizationSetting
    from ._models_py3 import SourceShareSynchronizationSettingList
    from ._models_py3 import SqlDBTableDataSet
    from ._models_py3 import SqlDBTableDataSetMapping
    from ._models_py3 import SqlDWTableDataSet
    from ._models_py3 import SqlDWTableDataSetMapping
    from ._models_py3 import SynapseWorkspaceSqlPoolTableDataSet
    from ._models_py3 import SynapseWorkspaceSqlPoolTableDataSetMapping
    from ._models_py3 import SynchronizationDetails
    from ._models_py3 import SynchronizationDetailsList
    from ._models_py3 import SynchronizationSetting
    from ._models_py3 import SynchronizationSettingList
    from ._models_py3 import Synchronize
    from ._models_py3 import SystemData
    from ._models_py3 import Trigger
    from ._models_py3 import TriggerList
except (SyntaxError, ImportError):
    from ._models import ADLSGen1FileDataSet  # type: ignore
    from ._models import ADLSGen1FolderDataSet  # type: ignore
    from ._models import ADLSGen2FileDataSet  # type: ignore
    from ._models import ADLSGen2FileDataSetMapping  # type: ignore
    from ._models import ADLSGen2FileSystemDataSet  # type: ignore
    from ._models import ADLSGen2FileSystemDataSetMapping  # type: ignore
    from ._models import ADLSGen2FolderDataSet  # type: ignore
    from ._models import ADLSGen2FolderDataSetMapping  # type: ignore
    from ._models import Account  # type: ignore
    from ._models import AccountList  # type: ignore
    from ._models import AccountUpdateParameters  # type: ignore
    from ._models import BlobContainerDataSet  # type: ignore
    from ._models import BlobContainerDataSetMapping  # type: ignore
    from ._models import BlobDataSet  # type: ignore
    from ._models import BlobDataSetMapping  # type: ignore
    from ._models import BlobFolderDataSet  # type: ignore
    from ._models import BlobFolderDataSetMapping  # type: ignore
    from ._models import ConsumerInvitation  # type: ignore
    from ._models import ConsumerInvitationList  # type: ignore
    from ._models import ConsumerSourceDataSet  # type: ignore
    from ._models import ConsumerSourceDataSetList  # type: ignore
    from ._models import DataSet  # type: ignore
    from ._models import DataSetList  # type: ignore
    from ._models import DataSetMapping  # type: ignore
    from ._models import DataSetMappingList  # type: ignore
    from ._models import DataShareError  # type: ignore
    from ._models import DataShareErrorInfo  # type: ignore
    from ._models import DefaultDto  # type: ignore
    from ._models import DimensionProperties  # type: ignore
    from ._models import Identity  # type: ignore
    from ._models import Invitation  # type: ignore
    from ._models import InvitationList  # type: ignore
    from ._models import KustoClusterDataSet  # type: ignore
    from ._models import KustoClusterDataSetMapping  # type: ignore
    from ._models import KustoDatabaseDataSet  # type: ignore
    from ._models import KustoDatabaseDataSetMapping  # type: ignore
    from ._models import OperationList  # type: ignore
    from ._models import OperationMetaLogSpecification  # type: ignore
    from ._models import OperationMetaMetricSpecification  # type: ignore
    from ._models import OperationMetaServiceSpecification  # type: ignore
    from ._models import OperationModel  # type: ignore
    from ._models import OperationModelProperties  # type: ignore
    from ._models import OperationResponse  # type: ignore
    from ._models import ProviderShareSubscription  # type: ignore
    from ._models import ProviderShareSubscriptionList  # type: ignore
    from ._models import ProxyDto  # type: ignore
    from ._models import ScheduledSourceSynchronizationSetting  # type: ignore
    from ._models import ScheduledSynchronizationSetting  # type: ignore
    from ._models import ScheduledTrigger  # type: ignore
    from ._models import Share  # type: ignore
    from ._models import ShareList  # type: ignore
    from ._models import ShareSubscription  # type: ignore
    from ._models import ShareSubscriptionList  # type: ignore
    from ._models import ShareSubscriptionSynchronization  # type: ignore
    from ._models import ShareSubscriptionSynchronizationList  # type: ignore
    from ._models import ShareSynchronization  # type: ignore
    from ._models import ShareSynchronizationList  # type: ignore
    from ._models import SourceShareSynchronizationSetting  # type: ignore
    from ._models import SourceShareSynchronizationSettingList  # type: ignore
    from ._models import SqlDBTableDataSet  # type: ignore
    from ._models import SqlDBTableDataSetMapping  # type: ignore
    from ._models import SqlDWTableDataSet  # type: ignore
    from ._models import SqlDWTableDataSetMapping  # type: ignore
    from ._models import SynapseWorkspaceSqlPoolTableDataSet  # type: ignore
    from ._models import SynapseWorkspaceSqlPoolTableDataSetMapping  # type: ignore
    from ._models import SynchronizationDetails  # type: ignore
    from ._models import SynchronizationDetailsList  # type: ignore
    from ._models import SynchronizationSetting  # type: ignore
    from ._models import SynchronizationSettingList  # type: ignore
    from ._models import Synchronize  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import Trigger  # type: ignore
    from ._models import TriggerList  # type: ignore

from ._data_share_management_client_enums import (
    CreatedByType,
    DataSetKind,
    DataSetMappingKind,
    DataSetMappingStatus,
    DataSetType,
    InvitationStatus,
    LastModifiedByType,
    OutputType,
    ProvisioningState,
    RecurrenceInterval,
    ShareKind,
    ShareSubscriptionStatus,
    SourceShareSynchronizationSettingKind,
    Status,
    SynchronizationMode,
    SynchronizationSettingKind,
    TriggerKind,
    TriggerStatus,
    Type,
)

__all__ = [
    'ADLSGen1FileDataSet',
    'ADLSGen1FolderDataSet',
    'ADLSGen2FileDataSet',
    'ADLSGen2FileDataSetMapping',
    'ADLSGen2FileSystemDataSet',
    'ADLSGen2FileSystemDataSetMapping',
    'ADLSGen2FolderDataSet',
    'ADLSGen2FolderDataSetMapping',
    'Account',
    'AccountList',
    'AccountUpdateParameters',
    'BlobContainerDataSet',
    'BlobContainerDataSetMapping',
    'BlobDataSet',
    'BlobDataSetMapping',
    'BlobFolderDataSet',
    'BlobFolderDataSetMapping',
    'ConsumerInvitation',
    'ConsumerInvitationList',
    'ConsumerSourceDataSet',
    'ConsumerSourceDataSetList',
    'DataSet',
    'DataSetList',
    'DataSetMapping',
    'DataSetMappingList',
    'DataShareError',
    'DataShareErrorInfo',
    'DefaultDto',
    'DimensionProperties',
    'Identity',
    'Invitation',
    'InvitationList',
    'KustoClusterDataSet',
    'KustoClusterDataSetMapping',
    'KustoDatabaseDataSet',
    'KustoDatabaseDataSetMapping',
    'OperationList',
    'OperationMetaLogSpecification',
    'OperationMetaMetricSpecification',
    'OperationMetaServiceSpecification',
    'OperationModel',
    'OperationModelProperties',
    'OperationResponse',
    'ProviderShareSubscription',
    'ProviderShareSubscriptionList',
    'ProxyDto',
    'ScheduledSourceSynchronizationSetting',
    'ScheduledSynchronizationSetting',
    'ScheduledTrigger',
    'Share',
    'ShareList',
    'ShareSubscription',
    'ShareSubscriptionList',
    'ShareSubscriptionSynchronization',
    'ShareSubscriptionSynchronizationList',
    'ShareSynchronization',
    'ShareSynchronizationList',
    'SourceShareSynchronizationSetting',
    'SourceShareSynchronizationSettingList',
    'SqlDBTableDataSet',
    'SqlDBTableDataSetMapping',
    'SqlDWTableDataSet',
    'SqlDWTableDataSetMapping',
    'SynapseWorkspaceSqlPoolTableDataSet',
    'SynapseWorkspaceSqlPoolTableDataSetMapping',
    'SynchronizationDetails',
    'SynchronizationDetailsList',
    'SynchronizationSetting',
    'SynchronizationSettingList',
    'Synchronize',
    'SystemData',
    'Trigger',
    'TriggerList',
    'CreatedByType',
    'DataSetKind',
    'DataSetMappingKind',
    'DataSetMappingStatus',
    'DataSetType',
    'InvitationStatus',
    'LastModifiedByType',
    'OutputType',
    'ProvisioningState',
    'RecurrenceInterval',
    'ShareKind',
    'ShareSubscriptionStatus',
    'SourceShareSynchronizationSettingKind',
    'Status',
    'SynchronizationMode',
    'SynchronizationSettingKind',
    'TriggerKind',
    'TriggerStatus',
    'Type',
]