# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AccessUri
    from ._models_py3 import AdditionalUnattendContent
    from ._models_py3 import ApiEntityReference
    from ._models_py3 import ApiError
    from ._models_py3 import ApiErrorBase
    from ._models_py3 import AutoOSUpgradePolicy
    from ._models_py3 import AvailabilitySet
    from ._models_py3 import AvailabilitySetListResult
    from ._models_py3 import AvailabilitySetUpdate
    from ._models_py3 import BootDiagnostics
    from ._models_py3 import BootDiagnosticsInstanceView
    from ._models_py3 import ComputeOperationListResult
    from ._models_py3 import ComputeOperationValue
    from ._models_py3 import CreationData
    from ._models_py3 import DataDisk
    from ._models_py3 import DataDiskImage
    from ._models_py3 import DiagnosticsProfile
    from ._models_py3 import Disk
    from ._models_py3 import DiskEncryptionSettings
    from ._models_py3 import DiskInstanceView
    from ._models_py3 import DiskList
    from ._models_py3 import DiskSku
    from ._models_py3 import DiskUpdate
    from ._models_py3 import EncryptionSettings
    from ._models_py3 import GrantAccessData
    from ._models_py3 import HardwareProfile
    from ._models_py3 import Image
    from ._models_py3 import ImageDataDisk
    from ._models_py3 import ImageDiskReference
    from ._models_py3 import ImageListResult
    from ._models_py3 import ImageOSDisk
    from ._models_py3 import ImageReference
    from ._models_py3 import ImageStorageProfile
    from ._models_py3 import ImageUpdate
    from ._models_py3 import InnerError
    from ._models_py3 import InstanceViewStatus
    from ._models_py3 import KeyVaultAndKeyReference
    from ._models_py3 import KeyVaultAndSecretReference
    from ._models_py3 import KeyVaultKeyReference
    from ._models_py3 import KeyVaultSecretReference
    from ._models_py3 import LinuxConfiguration
    from ._models_py3 import ListUsagesResult
    from ._models_py3 import LogAnalyticsInputBase
    from ._models_py3 import LogAnalyticsOperationResult
    from ._models_py3 import LogAnalyticsOutput
    from ._models_py3 import MaintenanceRedeployStatus
    from ._models_py3 import ManagedDiskParameters
    from ._models_py3 import NetworkInterfaceReference
    from ._models_py3 import NetworkProfile
    from ._models_py3 import OSDisk
    from ._models_py3 import OSDiskImage
    from ._models_py3 import OSProfile
    from ._models_py3 import Plan
    from ._models_py3 import ProximityPlacementGroup
    from ._models_py3 import ProximityPlacementGroupListResult
    from ._models_py3 import ProximityPlacementGroupUpdate
    from ._models_py3 import PurchasePlan
    from ._models_py3 import RecoveryWalkResponse
    from ._models_py3 import RequestRateByIntervalInput
    from ._models_py3 import Resource
    from ._models_py3 import RollbackStatusInfo
    from ._models_py3 import RollingUpgradePolicy
    from ._models_py3 import RollingUpgradeProgressInfo
    from ._models_py3 import RollingUpgradeRunningStatus
    from ._models_py3 import RollingUpgradeStatusInfo
    from ._models_py3 import RunCommandDocument
    from ._models_py3 import RunCommandDocumentBase
    from ._models_py3 import RunCommandInput
    from ._models_py3 import RunCommandInputParameter
    from ._models_py3 import RunCommandListResult
    from ._models_py3 import RunCommandParameterDefinition
    from ._models_py3 import RunCommandResult
    from ._models_py3 import Sku
    from ._models_py3 import Snapshot
    from ._models_py3 import SnapshotList
    from ._models_py3 import SnapshotSku
    from ._models_py3 import SnapshotUpdate
    from ._models_py3 import SourceVault
    from ._models_py3 import SshConfiguration
    from ._models_py3 import SshPublicKey
    from ._models_py3 import StorageProfile
    from ._models_py3 import SubResource
    from ._models_py3 import SubResourceReadOnly
    from ._models_py3 import ThrottledRequestsInput
    from ._models_py3 import UpdateResource
    from ._models_py3 import UpgradeOperationHistoricalStatusInfo
    from ._models_py3 import UpgradeOperationHistoricalStatusInfoProperties
    from ._models_py3 import UpgradeOperationHistoryStatus
    from ._models_py3 import UpgradePolicy
    from ._models_py3 import Usage
    from ._models_py3 import UsageName
    from ._models_py3 import VaultCertificate
    from ._models_py3 import VaultSecretGroup
    from ._models_py3 import VirtualHardDisk
    from ._models_py3 import VirtualMachine
    from ._models_py3 import VirtualMachineAgentInstanceView
    from ._models_py3 import VirtualMachineCaptureParameters
    from ._models_py3 import VirtualMachineCaptureResult
    from ._models_py3 import VirtualMachineExtension
    from ._models_py3 import VirtualMachineExtensionHandlerInstanceView
    from ._models_py3 import VirtualMachineExtensionImage
    from ._models_py3 import VirtualMachineExtensionInstanceView
    from ._models_py3 import VirtualMachineExtensionUpdate
    from ._models_py3 import VirtualMachineExtensionsListResult
    from ._models_py3 import VirtualMachineHealthStatus
    from ._models_py3 import VirtualMachineIdentity
    from ._models_py3 import VirtualMachineImage
    from ._models_py3 import VirtualMachineImageResource
    from ._models_py3 import VirtualMachineInstanceView
    from ._models_py3 import VirtualMachineListResult
    from ._models_py3 import VirtualMachineScaleSet
    from ._models_py3 import VirtualMachineScaleSetDataDisk
    from ._models_py3 import VirtualMachineScaleSetExtension
    from ._models_py3 import VirtualMachineScaleSetExtensionListResult
    from ._models_py3 import VirtualMachineScaleSetExtensionProfile
    from ._models_py3 import VirtualMachineScaleSetIPConfiguration
    from ._models_py3 import VirtualMachineScaleSetIdentity
    from ._models_py3 import VirtualMachineScaleSetInstanceView
    from ._models_py3 import VirtualMachineScaleSetInstanceViewStatusesSummary
    from ._models_py3 import VirtualMachineScaleSetIpTag
    from ._models_py3 import VirtualMachineScaleSetListOSUpgradeHistory
    from ._models_py3 import VirtualMachineScaleSetListResult
    from ._models_py3 import VirtualMachineScaleSetListSkusResult
    from ._models_py3 import VirtualMachineScaleSetListWithLinkResult
    from ._models_py3 import VirtualMachineScaleSetManagedDiskParameters
    from ._models_py3 import VirtualMachineScaleSetNetworkConfiguration
    from ._models_py3 import VirtualMachineScaleSetNetworkConfigurationDnsSettings
    from ._models_py3 import VirtualMachineScaleSetNetworkProfile
    from ._models_py3 import VirtualMachineScaleSetOSDisk
    from ._models_py3 import VirtualMachineScaleSetOSProfile
    from ._models_py3 import VirtualMachineScaleSetPublicIPAddressConfiguration
    from ._models_py3 import VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings
    from ._models_py3 import VirtualMachineScaleSetSku
    from ._models_py3 import VirtualMachineScaleSetSkuCapacity
    from ._models_py3 import VirtualMachineScaleSetStorageProfile
    from ._models_py3 import VirtualMachineScaleSetUpdate
    from ._models_py3 import VirtualMachineScaleSetUpdateIPConfiguration
    from ._models_py3 import VirtualMachineScaleSetUpdateNetworkConfiguration
    from ._models_py3 import VirtualMachineScaleSetUpdateNetworkProfile
    from ._models_py3 import VirtualMachineScaleSetUpdateOSDisk
    from ._models_py3 import VirtualMachineScaleSetUpdateOSProfile
    from ._models_py3 import VirtualMachineScaleSetUpdatePublicIPAddressConfiguration
    from ._models_py3 import VirtualMachineScaleSetUpdateStorageProfile
    from ._models_py3 import VirtualMachineScaleSetUpdateVMProfile
    from ._models_py3 import VirtualMachineScaleSetVM
    from ._models_py3 import VirtualMachineScaleSetVMExtensionsSummary
    from ._models_py3 import VirtualMachineScaleSetVMInstanceIDs
    from ._models_py3 import VirtualMachineScaleSetVMInstanceRequiredIDs
    from ._models_py3 import VirtualMachineScaleSetVMInstanceView
    from ._models_py3 import VirtualMachineScaleSetVMListResult
    from ._models_py3 import VirtualMachineScaleSetVMProfile
    from ._models_py3 import VirtualMachineSize
    from ._models_py3 import VirtualMachineSizeListResult
    from ._models_py3 import VirtualMachineStatusCodeCount
    from ._models_py3 import VirtualMachineUpdate
    from ._models_py3 import WinRMConfiguration
    from ._models_py3 import WinRMListener
    from ._models_py3 import WindowsConfiguration
except (SyntaxError, ImportError):
    from ._models import AccessUri  # type: ignore
    from ._models import AdditionalUnattendContent  # type: ignore
    from ._models import ApiEntityReference  # type: ignore
    from ._models import ApiError  # type: ignore
    from ._models import ApiErrorBase  # type: ignore
    from ._models import AutoOSUpgradePolicy  # type: ignore
    from ._models import AvailabilitySet  # type: ignore
    from ._models import AvailabilitySetListResult  # type: ignore
    from ._models import AvailabilitySetUpdate  # type: ignore
    from ._models import BootDiagnostics  # type: ignore
    from ._models import BootDiagnosticsInstanceView  # type: ignore
    from ._models import ComputeOperationListResult  # type: ignore
    from ._models import ComputeOperationValue  # type: ignore
    from ._models import CreationData  # type: ignore
    from ._models import DataDisk  # type: ignore
    from ._models import DataDiskImage  # type: ignore
    from ._models import DiagnosticsProfile  # type: ignore
    from ._models import Disk  # type: ignore
    from ._models import DiskEncryptionSettings  # type: ignore
    from ._models import DiskInstanceView  # type: ignore
    from ._models import DiskList  # type: ignore
    from ._models import DiskSku  # type: ignore
    from ._models import DiskUpdate  # type: ignore
    from ._models import EncryptionSettings  # type: ignore
    from ._models import GrantAccessData  # type: ignore
    from ._models import HardwareProfile  # type: ignore
    from ._models import Image  # type: ignore
    from ._models import ImageDataDisk  # type: ignore
    from ._models import ImageDiskReference  # type: ignore
    from ._models import ImageListResult  # type: ignore
    from ._models import ImageOSDisk  # type: ignore
    from ._models import ImageReference  # type: ignore
    from ._models import ImageStorageProfile  # type: ignore
    from ._models import ImageUpdate  # type: ignore
    from ._models import InnerError  # type: ignore
    from ._models import InstanceViewStatus  # type: ignore
    from ._models import KeyVaultAndKeyReference  # type: ignore
    from ._models import KeyVaultAndSecretReference  # type: ignore
    from ._models import KeyVaultKeyReference  # type: ignore
    from ._models import KeyVaultSecretReference  # type: ignore
    from ._models import LinuxConfiguration  # type: ignore
    from ._models import ListUsagesResult  # type: ignore
    from ._models import LogAnalyticsInputBase  # type: ignore
    from ._models import LogAnalyticsOperationResult  # type: ignore
    from ._models import LogAnalyticsOutput  # type: ignore
    from ._models import MaintenanceRedeployStatus  # type: ignore
    from ._models import ManagedDiskParameters  # type: ignore
    from ._models import NetworkInterfaceReference  # type: ignore
    from ._models import NetworkProfile  # type: ignore
    from ._models import OSDisk  # type: ignore
    from ._models import OSDiskImage  # type: ignore
    from ._models import OSProfile  # type: ignore
    from ._models import Plan  # type: ignore
    from ._models import ProximityPlacementGroup  # type: ignore
    from ._models import ProximityPlacementGroupListResult  # type: ignore
    from ._models import ProximityPlacementGroupUpdate  # type: ignore
    from ._models import PurchasePlan  # type: ignore
    from ._models import RecoveryWalkResponse  # type: ignore
    from ._models import RequestRateByIntervalInput  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import RollbackStatusInfo  # type: ignore
    from ._models import RollingUpgradePolicy  # type: ignore
    from ._models import RollingUpgradeProgressInfo  # type: ignore
    from ._models import RollingUpgradeRunningStatus  # type: ignore
    from ._models import RollingUpgradeStatusInfo  # type: ignore
    from ._models import RunCommandDocument  # type: ignore
    from ._models import RunCommandDocumentBase  # type: ignore
    from ._models import RunCommandInput  # type: ignore
    from ._models import RunCommandInputParameter  # type: ignore
    from ._models import RunCommandListResult  # type: ignore
    from ._models import RunCommandParameterDefinition  # type: ignore
    from ._models import RunCommandResult  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import Snapshot  # type: ignore
    from ._models import SnapshotList  # type: ignore
    from ._models import SnapshotSku  # type: ignore
    from ._models import SnapshotUpdate  # type: ignore
    from ._models import SourceVault  # type: ignore
    from ._models import SshConfiguration  # type: ignore
    from ._models import SshPublicKey  # type: ignore
    from ._models import StorageProfile  # type: ignore
    from ._models import SubResource  # type: ignore
    from ._models import SubResourceReadOnly  # type: ignore
    from ._models import ThrottledRequestsInput  # type: ignore
    from ._models import UpdateResource  # type: ignore
    from ._models import UpgradeOperationHistoricalStatusInfo  # type: ignore
    from ._models import UpgradeOperationHistoricalStatusInfoProperties  # type: ignore
    from ._models import UpgradeOperationHistoryStatus  # type: ignore
    from ._models import UpgradePolicy  # type: ignore
    from ._models import Usage  # type: ignore
    from ._models import UsageName  # type: ignore
    from ._models import VaultCertificate  # type: ignore
    from ._models import VaultSecretGroup  # type: ignore
    from ._models import VirtualHardDisk  # type: ignore
    from ._models import VirtualMachine  # type: ignore
    from ._models import VirtualMachineAgentInstanceView  # type: ignore
    from ._models import VirtualMachineCaptureParameters  # type: ignore
    from ._models import VirtualMachineCaptureResult  # type: ignore
    from ._models import VirtualMachineExtension  # type: ignore
    from ._models import VirtualMachineExtensionHandlerInstanceView  # type: ignore
    from ._models import VirtualMachineExtensionImage  # type: ignore
    from ._models import VirtualMachineExtensionInstanceView  # type: ignore
    from ._models import VirtualMachineExtensionUpdate  # type: ignore
    from ._models import VirtualMachineExtensionsListResult  # type: ignore
    from ._models import VirtualMachineHealthStatus  # type: ignore
    from ._models import VirtualMachineIdentity  # type: ignore
    from ._models import VirtualMachineImage  # type: ignore
    from ._models import VirtualMachineImageResource  # type: ignore
    from ._models import VirtualMachineInstanceView  # type: ignore
    from ._models import VirtualMachineListResult  # type: ignore
    from ._models import VirtualMachineScaleSet  # type: ignore
    from ._models import VirtualMachineScaleSetDataDisk  # type: ignore
    from ._models import VirtualMachineScaleSetExtension  # type: ignore
    from ._models import VirtualMachineScaleSetExtensionListResult  # type: ignore
    from ._models import VirtualMachineScaleSetExtensionProfile  # type: ignore
    from ._models import VirtualMachineScaleSetIPConfiguration  # type: ignore
    from ._models import VirtualMachineScaleSetIdentity  # type: ignore
    from ._models import VirtualMachineScaleSetInstanceView  # type: ignore
    from ._models import VirtualMachineScaleSetInstanceViewStatusesSummary  # type: ignore
    from ._models import VirtualMachineScaleSetIpTag  # type: ignore
    from ._models import VirtualMachineScaleSetListOSUpgradeHistory  # type: ignore
    from ._models import VirtualMachineScaleSetListResult  # type: ignore
    from ._models import VirtualMachineScaleSetListSkusResult  # type: ignore
    from ._models import VirtualMachineScaleSetListWithLinkResult  # type: ignore
    from ._models import VirtualMachineScaleSetManagedDiskParameters  # type: ignore
    from ._models import VirtualMachineScaleSetNetworkConfiguration  # type: ignore
    from ._models import VirtualMachineScaleSetNetworkConfigurationDnsSettings  # type: ignore
    from ._models import VirtualMachineScaleSetNetworkProfile  # type: ignore
    from ._models import VirtualMachineScaleSetOSDisk  # type: ignore
    from ._models import VirtualMachineScaleSetOSProfile  # type: ignore
    from ._models import VirtualMachineScaleSetPublicIPAddressConfiguration  # type: ignore
    from ._models import VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings  # type: ignore
    from ._models import VirtualMachineScaleSetSku  # type: ignore
    from ._models import VirtualMachineScaleSetSkuCapacity  # type: ignore
    from ._models import VirtualMachineScaleSetStorageProfile  # type: ignore
    from ._models import VirtualMachineScaleSetUpdate  # type: ignore
    from ._models import VirtualMachineScaleSetUpdateIPConfiguration  # type: ignore
    from ._models import VirtualMachineScaleSetUpdateNetworkConfiguration  # type: ignore
    from ._models import VirtualMachineScaleSetUpdateNetworkProfile  # type: ignore
    from ._models import VirtualMachineScaleSetUpdateOSDisk  # type: ignore
    from ._models import VirtualMachineScaleSetUpdateOSProfile  # type: ignore
    from ._models import VirtualMachineScaleSetUpdatePublicIPAddressConfiguration  # type: ignore
    from ._models import VirtualMachineScaleSetUpdateStorageProfile  # type: ignore
    from ._models import VirtualMachineScaleSetUpdateVMProfile  # type: ignore
    from ._models import VirtualMachineScaleSetVM  # type: ignore
    from ._models import VirtualMachineScaleSetVMExtensionsSummary  # type: ignore
    from ._models import VirtualMachineScaleSetVMInstanceIDs  # type: ignore
    from ._models import VirtualMachineScaleSetVMInstanceRequiredIDs  # type: ignore
    from ._models import VirtualMachineScaleSetVMInstanceView  # type: ignore
    from ._models import VirtualMachineScaleSetVMListResult  # type: ignore
    from ._models import VirtualMachineScaleSetVMProfile  # type: ignore
    from ._models import VirtualMachineSize  # type: ignore
    from ._models import VirtualMachineSizeListResult  # type: ignore
    from ._models import VirtualMachineStatusCodeCount  # type: ignore
    from ._models import VirtualMachineUpdate  # type: ignore
    from ._models import WinRMConfiguration  # type: ignore
    from ._models import WinRMListener  # type: ignore
    from ._models import WindowsConfiguration  # type: ignore

from ._compute_management_client_enums import (
    AccessLevel,
    CachingTypes,
    DiskCreateOption,
    DiskCreateOptionTypes,
    IPVersion,
    IntervalInMins,
    MaintenanceOperationResultCodeTypes,
    OperatingSystemStateTypes,
    OperatingSystemTypes,
    ProtocolTypes,
    ProximityPlacementGroupType,
    ResourceIdentityType,
    RollingUpgradeActionType,
    RollingUpgradeStatusCode,
    SettingNames,
    SnapshotStorageAccountTypes,
    StatusLevelTypes,
    StorageAccountTypes,
    UpgradeMode,
    UpgradeOperationInvoker,
    UpgradeState,
    VirtualMachineEvictionPolicyTypes,
    VirtualMachinePriorityTypes,
    VirtualMachineScaleSetSkuScaleType,
    VirtualMachineSizeTypes,
)

__all__ = [
    'AccessUri',
    'AdditionalUnattendContent',
    'ApiEntityReference',
    'ApiError',
    'ApiErrorBase',
    'AutoOSUpgradePolicy',
    'AvailabilitySet',
    'AvailabilitySetListResult',
    'AvailabilitySetUpdate',
    'BootDiagnostics',
    'BootDiagnosticsInstanceView',
    'ComputeOperationListResult',
    'ComputeOperationValue',
    'CreationData',
    'DataDisk',
    'DataDiskImage',
    'DiagnosticsProfile',
    'Disk',
    'DiskEncryptionSettings',
    'DiskInstanceView',
    'DiskList',
    'DiskSku',
    'DiskUpdate',
    'EncryptionSettings',
    'GrantAccessData',
    'HardwareProfile',
    'Image',
    'ImageDataDisk',
    'ImageDiskReference',
    'ImageListResult',
    'ImageOSDisk',
    'ImageReference',
    'ImageStorageProfile',
    'ImageUpdate',
    'InnerError',
    'InstanceViewStatus',
    'KeyVaultAndKeyReference',
    'KeyVaultAndSecretReference',
    'KeyVaultKeyReference',
    'KeyVaultSecretReference',
    'LinuxConfiguration',
    'ListUsagesResult',
    'LogAnalyticsInputBase',
    'LogAnalyticsOperationResult',
    'LogAnalyticsOutput',
    'MaintenanceRedeployStatus',
    'ManagedDiskParameters',
    'NetworkInterfaceReference',
    'NetworkProfile',
    'OSDisk',
    'OSDiskImage',
    'OSProfile',
    'Plan',
    'ProximityPlacementGroup',
    'ProximityPlacementGroupListResult',
    'ProximityPlacementGroupUpdate',
    'PurchasePlan',
    'RecoveryWalkResponse',
    'RequestRateByIntervalInput',
    'Resource',
    'RollbackStatusInfo',
    'RollingUpgradePolicy',
    'RollingUpgradeProgressInfo',
    'RollingUpgradeRunningStatus',
    'RollingUpgradeStatusInfo',
    'RunCommandDocument',
    'RunCommandDocumentBase',
    'RunCommandInput',
    'RunCommandInputParameter',
    'RunCommandListResult',
    'RunCommandParameterDefinition',
    'RunCommandResult',
    'Sku',
    'Snapshot',
    'SnapshotList',
    'SnapshotSku',
    'SnapshotUpdate',
    'SourceVault',
    'SshConfiguration',
    'SshPublicKey',
    'StorageProfile',
    'SubResource',
    'SubResourceReadOnly',
    'ThrottledRequestsInput',
    'UpdateResource',
    'UpgradeOperationHistoricalStatusInfo',
    'UpgradeOperationHistoricalStatusInfoProperties',
    'UpgradeOperationHistoryStatus',
    'UpgradePolicy',
    'Usage',
    'UsageName',
    'VaultCertificate',
    'VaultSecretGroup',
    'VirtualHardDisk',
    'VirtualMachine',
    'VirtualMachineAgentInstanceView',
    'VirtualMachineCaptureParameters',
    'VirtualMachineCaptureResult',
    'VirtualMachineExtension',
    'VirtualMachineExtensionHandlerInstanceView',
    'VirtualMachineExtensionImage',
    'VirtualMachineExtensionInstanceView',
    'VirtualMachineExtensionUpdate',
    'VirtualMachineExtensionsListResult',
    'VirtualMachineHealthStatus',
    'VirtualMachineIdentity',
    'VirtualMachineImage',
    'VirtualMachineImageResource',
    'VirtualMachineInstanceView',
    'VirtualMachineListResult',
    'VirtualMachineScaleSet',
    'VirtualMachineScaleSetDataDisk',
    'VirtualMachineScaleSetExtension',
    'VirtualMachineScaleSetExtensionListResult',
    'VirtualMachineScaleSetExtensionProfile',
    'VirtualMachineScaleSetIPConfiguration',
    'VirtualMachineScaleSetIdentity',
    'VirtualMachineScaleSetInstanceView',
    'VirtualMachineScaleSetInstanceViewStatusesSummary',
    'VirtualMachineScaleSetIpTag',
    'VirtualMachineScaleSetListOSUpgradeHistory',
    'VirtualMachineScaleSetListResult',
    'VirtualMachineScaleSetListSkusResult',
    'VirtualMachineScaleSetListWithLinkResult',
    'VirtualMachineScaleSetManagedDiskParameters',
    'VirtualMachineScaleSetNetworkConfiguration',
    'VirtualMachineScaleSetNetworkConfigurationDnsSettings',
    'VirtualMachineScaleSetNetworkProfile',
    'VirtualMachineScaleSetOSDisk',
    'VirtualMachineScaleSetOSProfile',
    'VirtualMachineScaleSetPublicIPAddressConfiguration',
    'VirtualMachineScaleSetPublicIPAddressConfigurationDnsSettings',
    'VirtualMachineScaleSetSku',
    'VirtualMachineScaleSetSkuCapacity',
    'VirtualMachineScaleSetStorageProfile',
    'VirtualMachineScaleSetUpdate',
    'VirtualMachineScaleSetUpdateIPConfiguration',
    'VirtualMachineScaleSetUpdateNetworkConfiguration',
    'VirtualMachineScaleSetUpdateNetworkProfile',
    'VirtualMachineScaleSetUpdateOSDisk',
    'VirtualMachineScaleSetUpdateOSProfile',
    'VirtualMachineScaleSetUpdatePublicIPAddressConfiguration',
    'VirtualMachineScaleSetUpdateStorageProfile',
    'VirtualMachineScaleSetUpdateVMProfile',
    'VirtualMachineScaleSetVM',
    'VirtualMachineScaleSetVMExtensionsSummary',
    'VirtualMachineScaleSetVMInstanceIDs',
    'VirtualMachineScaleSetVMInstanceRequiredIDs',
    'VirtualMachineScaleSetVMInstanceView',
    'VirtualMachineScaleSetVMListResult',
    'VirtualMachineScaleSetVMProfile',
    'VirtualMachineSize',
    'VirtualMachineSizeListResult',
    'VirtualMachineStatusCodeCount',
    'VirtualMachineUpdate',
    'WinRMConfiguration',
    'WinRMListener',
    'WindowsConfiguration',
    'AccessLevel',
    'CachingTypes',
    'DiskCreateOption',
    'DiskCreateOptionTypes',
    'IPVersion',
    'IntervalInMins',
    'MaintenanceOperationResultCodeTypes',
    'OperatingSystemStateTypes',
    'OperatingSystemTypes',
    'ProtocolTypes',
    'ProximityPlacementGroupType',
    'ResourceIdentityType',
    'RollingUpgradeActionType',
    'RollingUpgradeStatusCode',
    'SettingNames',
    'SnapshotStorageAccountTypes',
    'StatusLevelTypes',
    'StorageAccountTypes',
    'UpgradeMode',
    'UpgradeOperationInvoker',
    'UpgradeState',
    'VirtualMachineEvictionPolicyTypes',
    'VirtualMachinePriorityTypes',
    'VirtualMachineScaleSetSkuScaleType',
    'VirtualMachineSizeTypes',
]