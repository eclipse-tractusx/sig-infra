## QG checks
Please keep this issue open until QG X is concluded and will be managed by the Issue Creator!  
We will inform you about finding and proposals in separated issues, this issue here is for the Overview of the Checks!

### Please keep this issue open until QG4 is concluded!

Product Name:
Product Owner:
Dev SPOC:
Helm Chart Version:
App Version:
QG4 Approval: yes/no

#### TRG 1 Documentation
##### TRG 1.01
https://eclipse-tractusx.github.io/docs/release/trg-1/trg-1-1
- [ ] an appropriate `README.md` file
###### TRG 1.02
https://eclipse-tractusx.github.io/docs/release/trg-1/trg-1-2
- [ ] an appropriate `INSTALL.md`
###### TRG 1.03
https://eclipse-tractusx.github.io/docs/release/trg-1/trg-1-3
- [ ] an appropriate `CHANGELOG.md`
    - [ ] the versioning itself follows [semantic versioning](https://semver.org/)
#### TRG 2 Git
##### TRG 2.01
https://eclipse-tractusx.github.io/docs/release/trg-2/trg-2-1
- [ ] default branch is named `main`
##### TRG 2.03
https://eclipse-tractusx.github.io/docs/release/trg-2/trg-2-3
- [ ] `/docs` directory contains detailed product related documentation for the Tractus-X product
- [ ] `/charts` directory contains the Helm chart for the Tractus-X product IF available
- [ ] `AUTHORS.md` file (optional)
- [ ] `CODE_OF_CONDUCT.md` file
- [ ] `CONTRIBUTING.md` file
- [ ] `DEPENDENCIES` file(s) with up to date content (Dash tool generated)
- [ ] `LICENSE` file
- [ ] `NOTICE.md` file
- [ ] `SECURITY.md` file
##### TRG 2.04
https://eclipse-tractusx.github.io/docs/release/trg-2/trg-2-4
- [ ] a Leading product repository
- [ ] repository name must be _productname_ without prefix or suffix
- [ ] should contain the release
- [ ] references/urls to the product's other repositories
- [ ] might contain product helm chart
- [ ] README.md: contains the urls for the backend and frontend applications
##### TRG 2.05
https://eclipse-tractusx.github.io/docs/release/trg-2/trg-2-5
- [ ] `.tractusx` metafile is present in the root of the repository
- [ ] file has a proper format
#### TRG 3 Kubernetes
##### TRG 3.02
https://eclipse-tractusx.github.io/docs/release/trg-3/trg-3-2
- [ ] if data persistence is needed in Kubernetes the use of PersistentVolume and PersistentVolumeClaim resource
#### TRG 4 container
##### TRG 4.01
https://eclipse-tractusx.github.io/docs/release/trg-4/trg-4-1
- [ ] All images must be tagged following [semantic versioning](https://semver.org/)
- [ ] container is labeled correctly additionally to the latest tag
##### TRG 4.02
https://eclipse-tractusx.github.io/docs/release/trg-4/trg-4-2
- [ ] must add a section to your top level `README.md` file, that contains information about the used base image
- [ ] Java, Kotlin, ... if JVM based language use base image from [Eclipse Temurin](https://hub.docker.com/_/eclipse-temurin)
##### TRG 4.03
https://eclipse-tractusx.github.io/docs/release/trg-4/trg-4-3
- [ ] image has `USER` command to specify a non-root user to run the container
- [ ] `deployment.yaml` has `runAsUser` and `allowPrivilegeEscalation: false` properly set
##### TRG 4.05
https://eclipse-tractusx.github.io/docs/release/trg-4/trg-4-5
- [ ] released image must be present on `GitHub Package registry` or `Dockerhub`
#### TRG 5 Helm
##### TRG 5.01
https://eclipse-tractusx.github.io/docs/release/trg-5/trg-5-01
- [ ] Helm chart must be released
- [ ] appropriate semantic versioning for `version` and `appVersion` has to be used in `Chart.yaml`
- [ ] must not contain any environment specific `values-xyz.yaml`
- [ ] `values.yaml` file must contain proper default values/placeholders
- [ ] No hostname provided for ingress
- [ ] Ingress is disabled
- [ ] No references to any secret engine service (e.g.: Hashicorp Vault)
- [ ] Dependencies should be prefixed with the nameOverride and/or fullnameOverride properties
- [ ] Image tag is set to the `Chart.yaml` `appVersion` property
- [ ] must be deployable to any environment without overwriting default values with a simple helm install command
- [ ] dependencies have to be declared in Chart.yaml NOT requirements.yml
##### TRG 5.02
https://eclipse-tractusx.github.io/docs/release/trg-5/trg-5-02
- [ ] Helm chart location inside Git repository in `/charts` directory
- [ ] chart file structure
``` markdown
charts/ 
    chartNameA/
      Chart.yaml
      ... 
    chartNameB/
      Chart.yaml
      ...
AUTHORS.md 
DEPENDENCIES.md 
LICENCE 
README.md 
```
- [ ] each file must contain the [Apache 2.0 Licence](https://github.com/catenax-ng/foss-example/blob/main/general/LICENSE)
- [ ] latest tag is not used in helm chart be default
##### TRG 5.04
https://eclipse-tractusx.github.io/docs/release/trg-5/trg-5-04
- [ ] CPU and memory limits and requests are properly set
##### TRG 5.06
https://eclipse-tractusx.github.io/docs/release/trg-5/trg-5-06
- [ ] every startup configuration aspect of your application must be configurable through the Helm chart (ingress class, tls, labels, annotations, database, secrets, persistence, env variables)
##### TRG 5.07
https://eclipse-tractusx.github.io/docs/release/trg-5/trg-5-07
- [ ] if dependencies are present in the `Chart.yaml` they are properly configured
##### TRG 5.08
https://eclipse-tractusx.github.io/docs/release/trg-5/trg-5-08
- [ ] a product has a single deployable helm chart that contains all components (backend, frontend, etc.)
- [ ] name of the Chart should be just the product-name without prefix or suffix
- [ ] values file should contain all available variables (even from subcharts) with default values and comments about what they do
- [ ] helm install command should successfully install the chart to any supported Kubernetes version cluster (without overwriting default values)
- [ ] helm test runs without errors

#### Testing
- [ ] installed and running on pre-prod without errors

#### Hints

#### Information Sharing
