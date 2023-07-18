# SIG infra

This is the home of Eclipse Tractus-X Special Interest Group (SIG) infra.

## Workflows

This repository contains reusable workflows for the [eclipse-tractusx](https://github.com/eclipse-tractusx) GitHub
organization. Their intent is to make the adoption of Eclipse Tractus-X processes and guidelines easier.

See the [official documentation](https://docs.github.com/en/actions/using-workflows/reusing-workflows) on reusable workflows and specifically the part about
[calling reusable workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows#calling-a-reusable-workflow)
for further information. The following sections describe the reusable workflows provided in this repository and also show
examples on how to use them.

### Quality checks

__Description__:    This workflow runs automated checks, that test for compliance with our [Release Guidelines](https://eclipse-tractusx.github.io/docs/release)

__Workflow file__:  [.github/workflows/quality-checks.yaml](.github/workflows/reusable-quality-checks.yaml)

__Usage__:
```yaml
# Example .github/workflows/quality-checks.yaml in your repo
name: "Quality Checks (Release Guidelines)"

on:
  workflow_dispatch:
  pull_request:
    branches:
      - main

jobs:
  check-quality:
    name: Run quality checks
    runs-on: ubuntu-latest
    steps:
      # Reference the reusable workflow by <org>/<repo>/<path-to-reusable-workflow>@revision
      # We recooment to use the @main branch, since we regularly maintain the quality checks (adding new, enhancing existing) 
      - uses: eclipse-tractusx/sig-infra/.github/workflows/reusable-quality-checks.yaml@main
```

## Actions

This repo also provides some [custom GitHub](https://docs.github.com/en/actions/creating-actions) actions in [.github/actions](.github/actions).

### Check dependencies with [dash-licenses](https://github.com/eclipse/dash-licenses)

__Description__: This action is setting up [dash-licenses](https://github.com/eclipse/dash-licenses) and running it to analyze the project dependencies.
It will check, if the current `DEPENDENCIES` file in the repository is up-to-date and if it contains `restricted` or even `rejected` libs.

__Example Usage__: You can use the action like in the following example. For a complete list of inputs and outputs, refer to [the action docs](.github/actions/run-dash/README.md) 

```yaml
# ...
name: "3rd Party dependency check (Eclipse Dash)"

on:
  workflow_dispatch:
  pull_request:
    branches:
      - main

permissions:
  contents: write

jobs:
  check-dependencies:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Run dash
        id: run-dash
        uses: eclipse-tractusx/sig-infra/.github/actions/run-dash@main
        with:
          dash_version: "1.0.2" # default = 'LATEST'
          dash_input: "package-lock.json" # If your build tool does not have a file, that dash can interpret as-is, add a step to generate it first and reference it here
          dependencies_file: "DEPENDENCIES_FRONTEND"
          fail_on_out_of_date: true # default
          fail_on_rejected: true # default
          fail_on_restricted: false # default
```

