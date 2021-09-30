# azureactivedirectory

> see https://aka.ms/autorest

This is the AutoRest configuration file for azureactivedirectory.

## Getting Started

To build the SDKs for My API, simply install AutoRest via `npm` (`npm install -g autorest`) and then run:

> `autorest readme.md`

To see additional help and options, run:

> `autorest --help`

For other options on installation see [Installing AutoRest](https://aka.ms/autorest/install) on the AutoRest github page.

---

## Configuration

### Basic Information

These are the global settings for the azureactivedirectory.

``` yaml
openapi-type: arm
tag: package-preview-2017-04
```


### Tag: package-preview-2017-04

These settings apply only when `--tag=package-preview-2017-04` is specified on the command line.

```yaml $(tag) == 'package-preview-2017-04'
input-file:
  - Microsoft.Aadiam/preview/2017-04-01-preview/azureactivedirectory.json
```
### Tag: package-preview-2020-07

These settings apply only when `--tag=package-preview-2020-07` is specified on the command line.

``` yaml $(tag) == 'package-preview-2020-07'
input-file:
  - Microsoft.Aadiam/preview/2020-07-01-preview/azureADMetrics.json
```

### Tag: package-preview-2020-03

These settings apply only when `--tag=package-preview-2020-03` is specified on the command line.

``` yaml $(tag) == 'package-preview-2020-07'
input-file:
  - Microsoft.Aadiam/preview/2020-03-01-preview/privateLinkForAzureAD.json
  - Microsoft.Aadiam/preview/2020-03-01-preview/privateLinkResources.json
```

### Tag: package-2020-03

These settings apply only when `--tag=package-2020-03` is specified on the command line.

```yaml $(tag) == 'package-2020-03'
input-file:
  - Microsoft.Aadiam/stable/2020-03-01/privateLinkForAzureAD.json
  - Microsoft.Aadiam/stable/2020-03-01/privateLinkResources.json
  - Microsoft.Aadiam/stable/2020-03-01/privateEndpointConnections.json
```

### Tag: package-2017-04-01

These settings apply only when `--tag=package-2017-04-01` is specified on the command line.

``` yaml $(tag) == 'package-2017-04-01'
input-file:
  - Microsoft.Aadiam/stable/2017-04-01/azureactivedirectory.json
```

## Suppression

``` yaml
directive:
  - suppress: BodyTopLevelProperties
    from: azureADMetrics.json
    where: $.definitions.azureADMetricsConfig.properties
  - suppress: BodyTopLevelProperties
    from: privateLinkForAzureAD.json
    where: $.definitions.privateLinkPolicy.properties
  - suppress: RequiredPropertiesMissingInResourceModel
    from: azureADMetrics.json
    where: $.definitions.azureADMetricsConfig
  - suppress: RequiredPropertiesMissingInResourceModel
    from: privateLinkForAzureAD.json
    where: $.definitions.privateLinkPolicy
  - suppress: R3020
  - suppress: R3023
  - suppress: RequiredDefaultResponse
    where: '$.paths["/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.aadiam/privateLinkForAzureAd/{policyName}/privateLinkResources"].get.responses'
    from: privateLinkResources.json
    reason: 'If I make this change, it is marked as a breaking change between api versions and I can''t complete the resultant PR.'
  - suppress: RequiredDefaultResponse
    where: '$.paths["/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.aadiam/privateLinkForAzureAd/{policyName}/privateLinkResources/{groupName}"].get.responses'
    from: privateLinkResources.json
    reason: 'If I make this change, it is marked as a breaking change between api versions and I can''t complete the resultant PR.'
```

---

# Code Generation

## Swagger to SDK

This section describes what SDK should be generated by the automatic system.
This is not used by Autorest itself.

``` yaml $(swagger-to-sdk)
swagger-to-sdk:
  - repo: azure-sdk-for-net
  - repo: azure-sdk-for-python-track2
  - repo: azure-sdk-for-java
  - repo: azure-sdk-for-go
  - repo: azure-sdk-for-js
  - repo: azure-sdk-for-ruby
    after_scripts:
      - bundle install && rake arm:regen_all_profiles['azure_mgmt_azureactivedirectory']
  - repo: azure-resource-manager-schemas
```

## Go

See configuration in [readme.go.md](./readme.go.md)

## Python

See configuration in [readme.python.md](./readme.python.md)

## Ruby

See configuration in [readme.ruby.md](./readme.ruby.md)

## TypeScript

See configuration in [readme.typescript.md](./readme.typescript.md)

## CSharp

See configuration in [readme.csharp.md](./readme.csharp.md)