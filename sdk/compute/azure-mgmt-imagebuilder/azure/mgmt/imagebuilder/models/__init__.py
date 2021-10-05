# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ApiError
    from ._models_py3 import ApiErrorBase
    from ._models_py3 import ComponentsVrq145SchemasImagetemplateidentityPropertiesUserassignedidentitiesAdditionalproperties
    from ._models_py3 import ImageTemplate
    from ._models_py3 import ImageTemplateCustomizer
    from ._models_py3 import ImageTemplateDistributor
    from ._models_py3 import ImageTemplateFileCustomizer
    from ._models_py3 import ImageTemplateIdentity
    from ._models_py3 import ImageTemplateLastRunStatus
    from ._models_py3 import ImageTemplateListResult
    from ._models_py3 import ImageTemplateManagedImageDistributor
    from ._models_py3 import ImageTemplateManagedImageSource
    from ._models_py3 import ImageTemplatePlatformImageSource
    from ._models_py3 import ImageTemplatePowerShellCustomizer
    from ._models_py3 import ImageTemplateRestartCustomizer
    from ._models_py3 import ImageTemplateSharedImageDistributor
    from ._models_py3 import ImageTemplateSharedImageVersionSource
    from ._models_py3 import ImageTemplateShellCustomizer
    from ._models_py3 import ImageTemplateSource
    from ._models_py3 import ImageTemplateUpdateParameters
    from ._models_py3 import ImageTemplateVhdDistributor
    from ._models_py3 import ImageTemplateVmProfile
    from ._models_py3 import ImageTemplateWindowsUpdateCustomizer
    from ._models_py3 import InnerError
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import PlatformImagePurchasePlan
    from ._models_py3 import ProvisioningError
    from ._models_py3 import Resource
    from ._models_py3 import RunOutput
    from ._models_py3 import RunOutputCollection
    from ._models_py3 import SubResource
    from ._models_py3 import VirtualNetworkConfig
except (SyntaxError, ImportError):
    from ._models import ApiError  # type: ignore
    from ._models import ApiErrorBase  # type: ignore
    from ._models import ComponentsVrq145SchemasImagetemplateidentityPropertiesUserassignedidentitiesAdditionalproperties  # type: ignore
    from ._models import ImageTemplate  # type: ignore
    from ._models import ImageTemplateCustomizer  # type: ignore
    from ._models import ImageTemplateDistributor  # type: ignore
    from ._models import ImageTemplateFileCustomizer  # type: ignore
    from ._models import ImageTemplateIdentity  # type: ignore
    from ._models import ImageTemplateLastRunStatus  # type: ignore
    from ._models import ImageTemplateListResult  # type: ignore
    from ._models import ImageTemplateManagedImageDistributor  # type: ignore
    from ._models import ImageTemplateManagedImageSource  # type: ignore
    from ._models import ImageTemplatePlatformImageSource  # type: ignore
    from ._models import ImageTemplatePowerShellCustomizer  # type: ignore
    from ._models import ImageTemplateRestartCustomizer  # type: ignore
    from ._models import ImageTemplateSharedImageDistributor  # type: ignore
    from ._models import ImageTemplateSharedImageVersionSource  # type: ignore
    from ._models import ImageTemplateShellCustomizer  # type: ignore
    from ._models import ImageTemplateSource  # type: ignore
    from ._models import ImageTemplateUpdateParameters  # type: ignore
    from ._models import ImageTemplateVhdDistributor  # type: ignore
    from ._models import ImageTemplateVmProfile  # type: ignore
    from ._models import ImageTemplateWindowsUpdateCustomizer  # type: ignore
    from ._models import InnerError  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import PlatformImagePurchasePlan  # type: ignore
    from ._models import ProvisioningError  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import RunOutput  # type: ignore
    from ._models import RunOutputCollection  # type: ignore
    from ._models import SubResource  # type: ignore
    from ._models import VirtualNetworkConfig  # type: ignore

from ._image_builder_client_enums import (
    ProvisioningErrorCode,
    ProvisioningState,
    ResourceIdentityType,
    RunState,
    RunSubState,
    SharedImageStorageAccountType,
)

__all__ = [
    'ApiError',
    'ApiErrorBase',
    'ComponentsVrq145SchemasImagetemplateidentityPropertiesUserassignedidentitiesAdditionalproperties',
    'ImageTemplate',
    'ImageTemplateCustomizer',
    'ImageTemplateDistributor',
    'ImageTemplateFileCustomizer',
    'ImageTemplateIdentity',
    'ImageTemplateLastRunStatus',
    'ImageTemplateListResult',
    'ImageTemplateManagedImageDistributor',
    'ImageTemplateManagedImageSource',
    'ImageTemplatePlatformImageSource',
    'ImageTemplatePowerShellCustomizer',
    'ImageTemplateRestartCustomizer',
    'ImageTemplateSharedImageDistributor',
    'ImageTemplateSharedImageVersionSource',
    'ImageTemplateShellCustomizer',
    'ImageTemplateSource',
    'ImageTemplateUpdateParameters',
    'ImageTemplateVhdDistributor',
    'ImageTemplateVmProfile',
    'ImageTemplateWindowsUpdateCustomizer',
    'InnerError',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'PlatformImagePurchasePlan',
    'ProvisioningError',
    'Resource',
    'RunOutput',
    'RunOutputCollection',
    'SubResource',
    'VirtualNetworkConfig',
    'ProvisioningErrorCode',
    'ProvisioningState',
    'ResourceIdentityType',
    'RunState',
    'RunSubState',
    'SharedImageStorageAccountType',
]