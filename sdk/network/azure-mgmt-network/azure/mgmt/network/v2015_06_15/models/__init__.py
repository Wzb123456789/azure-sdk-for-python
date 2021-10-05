# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AddressSpace
    from ._models_py3 import ApplicationGateway
    from ._models_py3 import ApplicationGatewayBackendAddress
    from ._models_py3 import ApplicationGatewayBackendAddressPool
    from ._models_py3 import ApplicationGatewayBackendHttpSettings
    from ._models_py3 import ApplicationGatewayFrontendIPConfiguration
    from ._models_py3 import ApplicationGatewayFrontendPort
    from ._models_py3 import ApplicationGatewayHttpListener
    from ._models_py3 import ApplicationGatewayIPConfiguration
    from ._models_py3 import ApplicationGatewayListResult
    from ._models_py3 import ApplicationGatewayPathRule
    from ._models_py3 import ApplicationGatewayProbe
    from ._models_py3 import ApplicationGatewayRequestRoutingRule
    from ._models_py3 import ApplicationGatewaySku
    from ._models_py3 import ApplicationGatewaySslCertificate
    from ._models_py3 import ApplicationGatewayUrlPathMap
    from ._models_py3 import AuthorizationListResult
    from ._models_py3 import AzureAsyncOperationResult
    from ._models_py3 import BackendAddressPool
    from ._models_py3 import BgpSettings
    from ._models_py3 import ConnectionResetSharedKey
    from ._models_py3 import ConnectionSharedKey
    from ._models_py3 import ConnectionSharedKeyResult
    from ._models_py3 import DhcpOptions
    from ._models_py3 import DnsNameAvailabilityResult
    from ._models_py3 import Error
    from ._models_py3 import ErrorDetails
    from ._models_py3 import ExpressRouteCircuit
    from ._models_py3 import ExpressRouteCircuitArpTable
    from ._models_py3 import ExpressRouteCircuitAuthorization
    from ._models_py3 import ExpressRouteCircuitListResult
    from ._models_py3 import ExpressRouteCircuitPeering
    from ._models_py3 import ExpressRouteCircuitPeeringConfig
    from ._models_py3 import ExpressRouteCircuitPeeringListResult
    from ._models_py3 import ExpressRouteCircuitRoutesTable
    from ._models_py3 import ExpressRouteCircuitServiceProviderProperties
    from ._models_py3 import ExpressRouteCircuitSku
    from ._models_py3 import ExpressRouteCircuitStats
    from ._models_py3 import ExpressRouteCircuitsArpTableListResult
    from ._models_py3 import ExpressRouteCircuitsRoutesTableListResult
    from ._models_py3 import ExpressRouteCircuitsStatsListResult
    from ._models_py3 import ExpressRouteServiceProvider
    from ._models_py3 import ExpressRouteServiceProviderBandwidthsOffered
    from ._models_py3 import ExpressRouteServiceProviderListResult
    from ._models_py3 import FrontendIPConfiguration
    from ._models_py3 import IPConfiguration
    from ._models_py3 import InboundNatPool
    from ._models_py3 import InboundNatRule
    from ._models_py3 import LoadBalancer
    from ._models_py3 import LoadBalancerListResult
    from ._models_py3 import LoadBalancingRule
    from ._models_py3 import LocalNetworkGateway
    from ._models_py3 import LocalNetworkGatewayListResult
    from ._models_py3 import NetworkInterface
    from ._models_py3 import NetworkInterfaceDnsSettings
    from ._models_py3 import NetworkInterfaceIPConfiguration
    from ._models_py3 import NetworkInterfaceListResult
    from ._models_py3 import NetworkSecurityGroup
    from ._models_py3 import NetworkSecurityGroupListResult
    from ._models_py3 import OutboundNatRule
    from ._models_py3 import Probe
    from ._models_py3 import PublicIPAddress
    from ._models_py3 import PublicIPAddressDnsSettings
    from ._models_py3 import PublicIPAddressListResult
    from ._models_py3 import Resource
    from ._models_py3 import Route
    from ._models_py3 import RouteListResult
    from ._models_py3 import RouteTable
    from ._models_py3 import RouteTableListResult
    from ._models_py3 import SecurityRule
    from ._models_py3 import SecurityRuleListResult
    from ._models_py3 import SubResource
    from ._models_py3 import Subnet
    from ._models_py3 import SubnetListResult
    from ._models_py3 import Usage
    from ._models_py3 import UsageName
    from ._models_py3 import UsagesListResult
    from ._models_py3 import VirtualNetwork
    from ._models_py3 import VirtualNetworkGateway
    from ._models_py3 import VirtualNetworkGatewayConnection
    from ._models_py3 import VirtualNetworkGatewayConnectionListResult
    from ._models_py3 import VirtualNetworkGatewayIPConfiguration
    from ._models_py3 import VirtualNetworkGatewayListResult
    from ._models_py3 import VirtualNetworkGatewaySku
    from ._models_py3 import VirtualNetworkListResult
    from ._models_py3 import VpnClientConfiguration
    from ._models_py3 import VpnClientParameters
    from ._models_py3 import VpnClientRevokedCertificate
    from ._models_py3 import VpnClientRootCertificate
except (SyntaxError, ImportError):
    from ._models import AddressSpace  # type: ignore
    from ._models import ApplicationGateway  # type: ignore
    from ._models import ApplicationGatewayBackendAddress  # type: ignore
    from ._models import ApplicationGatewayBackendAddressPool  # type: ignore
    from ._models import ApplicationGatewayBackendHttpSettings  # type: ignore
    from ._models import ApplicationGatewayFrontendIPConfiguration  # type: ignore
    from ._models import ApplicationGatewayFrontendPort  # type: ignore
    from ._models import ApplicationGatewayHttpListener  # type: ignore
    from ._models import ApplicationGatewayIPConfiguration  # type: ignore
    from ._models import ApplicationGatewayListResult  # type: ignore
    from ._models import ApplicationGatewayPathRule  # type: ignore
    from ._models import ApplicationGatewayProbe  # type: ignore
    from ._models import ApplicationGatewayRequestRoutingRule  # type: ignore
    from ._models import ApplicationGatewaySku  # type: ignore
    from ._models import ApplicationGatewaySslCertificate  # type: ignore
    from ._models import ApplicationGatewayUrlPathMap  # type: ignore
    from ._models import AuthorizationListResult  # type: ignore
    from ._models import AzureAsyncOperationResult  # type: ignore
    from ._models import BackendAddressPool  # type: ignore
    from ._models import BgpSettings  # type: ignore
    from ._models import ConnectionResetSharedKey  # type: ignore
    from ._models import ConnectionSharedKey  # type: ignore
    from ._models import ConnectionSharedKeyResult  # type: ignore
    from ._models import DhcpOptions  # type: ignore
    from ._models import DnsNameAvailabilityResult  # type: ignore
    from ._models import Error  # type: ignore
    from ._models import ErrorDetails  # type: ignore
    from ._models import ExpressRouteCircuit  # type: ignore
    from ._models import ExpressRouteCircuitArpTable  # type: ignore
    from ._models import ExpressRouteCircuitAuthorization  # type: ignore
    from ._models import ExpressRouteCircuitListResult  # type: ignore
    from ._models import ExpressRouteCircuitPeering  # type: ignore
    from ._models import ExpressRouteCircuitPeeringConfig  # type: ignore
    from ._models import ExpressRouteCircuitPeeringListResult  # type: ignore
    from ._models import ExpressRouteCircuitRoutesTable  # type: ignore
    from ._models import ExpressRouteCircuitServiceProviderProperties  # type: ignore
    from ._models import ExpressRouteCircuitSku  # type: ignore
    from ._models import ExpressRouteCircuitStats  # type: ignore
    from ._models import ExpressRouteCircuitsArpTableListResult  # type: ignore
    from ._models import ExpressRouteCircuitsRoutesTableListResult  # type: ignore
    from ._models import ExpressRouteCircuitsStatsListResult  # type: ignore
    from ._models import ExpressRouteServiceProvider  # type: ignore
    from ._models import ExpressRouteServiceProviderBandwidthsOffered  # type: ignore
    from ._models import ExpressRouteServiceProviderListResult  # type: ignore
    from ._models import FrontendIPConfiguration  # type: ignore
    from ._models import IPConfiguration  # type: ignore
    from ._models import InboundNatPool  # type: ignore
    from ._models import InboundNatRule  # type: ignore
    from ._models import LoadBalancer  # type: ignore
    from ._models import LoadBalancerListResult  # type: ignore
    from ._models import LoadBalancingRule  # type: ignore
    from ._models import LocalNetworkGateway  # type: ignore
    from ._models import LocalNetworkGatewayListResult  # type: ignore
    from ._models import NetworkInterface  # type: ignore
    from ._models import NetworkInterfaceDnsSettings  # type: ignore
    from ._models import NetworkInterfaceIPConfiguration  # type: ignore
    from ._models import NetworkInterfaceListResult  # type: ignore
    from ._models import NetworkSecurityGroup  # type: ignore
    from ._models import NetworkSecurityGroupListResult  # type: ignore
    from ._models import OutboundNatRule  # type: ignore
    from ._models import Probe  # type: ignore
    from ._models import PublicIPAddress  # type: ignore
    from ._models import PublicIPAddressDnsSettings  # type: ignore
    from ._models import PublicIPAddressListResult  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import Route  # type: ignore
    from ._models import RouteListResult  # type: ignore
    from ._models import RouteTable  # type: ignore
    from ._models import RouteTableListResult  # type: ignore
    from ._models import SecurityRule  # type: ignore
    from ._models import SecurityRuleListResult  # type: ignore
    from ._models import SubResource  # type: ignore
    from ._models import Subnet  # type: ignore
    from ._models import SubnetListResult  # type: ignore
    from ._models import Usage  # type: ignore
    from ._models import UsageName  # type: ignore
    from ._models import UsagesListResult  # type: ignore
    from ._models import VirtualNetwork  # type: ignore
    from ._models import VirtualNetworkGateway  # type: ignore
    from ._models import VirtualNetworkGatewayConnection  # type: ignore
    from ._models import VirtualNetworkGatewayConnectionListResult  # type: ignore
    from ._models import VirtualNetworkGatewayIPConfiguration  # type: ignore
    from ._models import VirtualNetworkGatewayListResult  # type: ignore
    from ._models import VirtualNetworkGatewaySku  # type: ignore
    from ._models import VirtualNetworkListResult  # type: ignore
    from ._models import VpnClientConfiguration  # type: ignore
    from ._models import VpnClientParameters  # type: ignore
    from ._models import VpnClientRevokedCertificate  # type: ignore
    from ._models import VpnClientRootCertificate  # type: ignore

from ._network_management_client_enums import (
    ApplicationGatewayCookieBasedAffinity,
    ApplicationGatewayOperationalState,
    ApplicationGatewayProtocol,
    ApplicationGatewayRequestRoutingRuleType,
    ApplicationGatewaySkuName,
    ApplicationGatewayTier,
    AuthorizationUseStatus,
    ExpressRouteCircuitPeeringAdvertisedPublicPrefixState,
    ExpressRouteCircuitPeeringState,
    ExpressRouteCircuitPeeringType,
    ExpressRouteCircuitSkuFamily,
    ExpressRouteCircuitSkuTier,
    IPAllocationMethod,
    LoadDistribution,
    NetworkOperationStatus,
    ProbeProtocol,
    ProcessorArchitecture,
    RouteNextHopType,
    SecurityRuleAccess,
    SecurityRuleDirection,
    SecurityRuleProtocol,
    ServiceProviderProvisioningState,
    TransportProtocol,
    UsageUnit,
    VirtualNetworkGatewayConnectionStatus,
    VirtualNetworkGatewayConnectionType,
    VirtualNetworkGatewaySkuName,
    VirtualNetworkGatewaySkuTier,
    VirtualNetworkGatewayType,
    VpnType,
)

__all__ = [
    'AddressSpace',
    'ApplicationGateway',
    'ApplicationGatewayBackendAddress',
    'ApplicationGatewayBackendAddressPool',
    'ApplicationGatewayBackendHttpSettings',
    'ApplicationGatewayFrontendIPConfiguration',
    'ApplicationGatewayFrontendPort',
    'ApplicationGatewayHttpListener',
    'ApplicationGatewayIPConfiguration',
    'ApplicationGatewayListResult',
    'ApplicationGatewayPathRule',
    'ApplicationGatewayProbe',
    'ApplicationGatewayRequestRoutingRule',
    'ApplicationGatewaySku',
    'ApplicationGatewaySslCertificate',
    'ApplicationGatewayUrlPathMap',
    'AuthorizationListResult',
    'AzureAsyncOperationResult',
    'BackendAddressPool',
    'BgpSettings',
    'ConnectionResetSharedKey',
    'ConnectionSharedKey',
    'ConnectionSharedKeyResult',
    'DhcpOptions',
    'DnsNameAvailabilityResult',
    'Error',
    'ErrorDetails',
    'ExpressRouteCircuit',
    'ExpressRouteCircuitArpTable',
    'ExpressRouteCircuitAuthorization',
    'ExpressRouteCircuitListResult',
    'ExpressRouteCircuitPeering',
    'ExpressRouteCircuitPeeringConfig',
    'ExpressRouteCircuitPeeringListResult',
    'ExpressRouteCircuitRoutesTable',
    'ExpressRouteCircuitServiceProviderProperties',
    'ExpressRouteCircuitSku',
    'ExpressRouteCircuitStats',
    'ExpressRouteCircuitsArpTableListResult',
    'ExpressRouteCircuitsRoutesTableListResult',
    'ExpressRouteCircuitsStatsListResult',
    'ExpressRouteServiceProvider',
    'ExpressRouteServiceProviderBandwidthsOffered',
    'ExpressRouteServiceProviderListResult',
    'FrontendIPConfiguration',
    'IPConfiguration',
    'InboundNatPool',
    'InboundNatRule',
    'LoadBalancer',
    'LoadBalancerListResult',
    'LoadBalancingRule',
    'LocalNetworkGateway',
    'LocalNetworkGatewayListResult',
    'NetworkInterface',
    'NetworkInterfaceDnsSettings',
    'NetworkInterfaceIPConfiguration',
    'NetworkInterfaceListResult',
    'NetworkSecurityGroup',
    'NetworkSecurityGroupListResult',
    'OutboundNatRule',
    'Probe',
    'PublicIPAddress',
    'PublicIPAddressDnsSettings',
    'PublicIPAddressListResult',
    'Resource',
    'Route',
    'RouteListResult',
    'RouteTable',
    'RouteTableListResult',
    'SecurityRule',
    'SecurityRuleListResult',
    'SubResource',
    'Subnet',
    'SubnetListResult',
    'Usage',
    'UsageName',
    'UsagesListResult',
    'VirtualNetwork',
    'VirtualNetworkGateway',
    'VirtualNetworkGatewayConnection',
    'VirtualNetworkGatewayConnectionListResult',
    'VirtualNetworkGatewayIPConfiguration',
    'VirtualNetworkGatewayListResult',
    'VirtualNetworkGatewaySku',
    'VirtualNetworkListResult',
    'VpnClientConfiguration',
    'VpnClientParameters',
    'VpnClientRevokedCertificate',
    'VpnClientRootCertificate',
    'ApplicationGatewayCookieBasedAffinity',
    'ApplicationGatewayOperationalState',
    'ApplicationGatewayProtocol',
    'ApplicationGatewayRequestRoutingRuleType',
    'ApplicationGatewaySkuName',
    'ApplicationGatewayTier',
    'AuthorizationUseStatus',
    'ExpressRouteCircuitPeeringAdvertisedPublicPrefixState',
    'ExpressRouteCircuitPeeringState',
    'ExpressRouteCircuitPeeringType',
    'ExpressRouteCircuitSkuFamily',
    'ExpressRouteCircuitSkuTier',
    'IPAllocationMethod',
    'LoadDistribution',
    'NetworkOperationStatus',
    'ProbeProtocol',
    'ProcessorArchitecture',
    'RouteNextHopType',
    'SecurityRuleAccess',
    'SecurityRuleDirection',
    'SecurityRuleProtocol',
    'ServiceProviderProvisioningState',
    'TransportProtocol',
    'UsageUnit',
    'VirtualNetworkGatewayConnectionStatus',
    'VirtualNetworkGatewayConnectionType',
    'VirtualNetworkGatewaySkuName',
    'VirtualNetworkGatewaySkuTier',
    'VirtualNetworkGatewayType',
    'VpnType',
]