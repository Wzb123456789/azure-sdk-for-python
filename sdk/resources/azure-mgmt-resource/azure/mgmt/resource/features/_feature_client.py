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

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from msrest import Deserializer, Serializer

from ._configuration import FeatureClientConfiguration
from ._operations_mixin import FeatureClientOperationsMixin

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline.transport import HttpRequest, HttpResponse

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class FeatureClient(FeatureClientOperationsMixin, MultiApiClientMixin, _SDKClient):
    """Azure Feature Exposure Control (AFEC) provides a mechanism for the resource providers to control feature exposure to users. Resource providers typically use this mechanism to provide public/private preview for new features prior to making them generally available. Users need to explicitly register for AFEC features to get access to such functionality.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2021-07-01'
    _PROFILE_TAG = "azure.mgmt.resource.features.FeatureClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        api_version=None, # type: Optional[str]
        base_url=None,  # type: Optional[str]
        profile=KnownProfiles.default, # type: KnownProfiles
        **kwargs  # type: Any
    ):
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = FeatureClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(FeatureClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2015-12-01: :mod:`v2015_12_01.models<azure.mgmt.resource.features.v2015_12_01.models>`
           * 2021-07-01: :mod:`v2021_07_01.models<azure.mgmt.resource.features.v2021_07_01.models>`
        """
        if api_version == '2015-12-01':
            from .v2015_12_01 import models
            return models
        elif api_version == '2021-07-01':
            from .v2021_07_01 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def features(self):
        """Instance depends on the API version:

           * 2015-12-01: :class:`FeaturesOperations<azure.mgmt.resource.features.v2015_12_01.operations.FeaturesOperations>`
           * 2021-07-01: :class:`FeaturesOperations<azure.mgmt.resource.features.v2021_07_01.operations.FeaturesOperations>`
        """
        api_version = self._get_api_version('features')
        if api_version == '2015-12-01':
            from .v2015_12_01.operations import FeaturesOperations as OperationClass
        elif api_version == '2021-07-01':
            from .v2021_07_01.operations import FeaturesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'features'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def subscription_feature_registrations(self):
        """Instance depends on the API version:

           * 2021-07-01: :class:`SubscriptionFeatureRegistrationsOperations<azure.mgmt.resource.features.v2021_07_01.operations.SubscriptionFeatureRegistrationsOperations>`
        """
        api_version = self._get_api_version('subscription_feature_registrations')
        if api_version == '2021-07-01':
            from .v2021_07_01.operations import SubscriptionFeatureRegistrationsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'subscription_feature_registrations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)