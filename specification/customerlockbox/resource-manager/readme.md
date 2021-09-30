# customerlockbox

> see https://aka.ms/autorest

This is the AutoRest configuration file for customerlockbox.

## Getting Started

To build the SDKs for My API, simply install AutoRest via `npm` (`npm install -g autorest`) and then run:

> `autorest readme.md`

To see additional help and options, run:

> `autorest --help`

For other options on installation see [Installing AutoRest](https://aka.ms/autorest/install) on the AutoRest github page.

---

## Configuration

### Basic Information

These are the global settings for the customerlockbox.

```yaml
openapi-type: arm
tag: package-2018-02-28-preview
```

### Tag: package-2018-02-28-preview

These settings apply only when `--tag=package-2018-02-28-preview` is specified on the command line.

```yaml $(tag) == 'package-2018-02-28-preview'
input-file:
  - Microsoft.CustomerLockbox/preview/2018-02-28-preview/customerlockbox.json
```

---

# Code Generation

## CSharp

See configuration in [readme.csharp.md](./readme.csharp.md)


