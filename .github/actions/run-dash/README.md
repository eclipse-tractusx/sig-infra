# Run-dash action

The `run-dash` action is setting up the [Eclipse Dash](https://github.com/eclipse/dash-licenses) tool and its
prerequisites.
Given the dependency list as input, it will analyze it and create a temporary `DEPENDENCIES` file, that is compared
against the current file in the repository. The action will check, if the current file is up-to-date and if it does
contain
`restricted` or `rejected` libraries. The results are provided as boolean action outputs.

## Usage

The following examples show different usage of the action for different build systems and programming languages.

### Analyze golang application

Golang defines detailed dependency and version info in a file called `go.sum`. The Eclipse Dash tool can interpret that file
as-is. Therefore, a minimal set of config for the `run-dash` action is needed.

```yaml
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
          dash_input: "go.sum"
```

## Inputs

| input name            | description                                                            | required |     default      |
|:----------------------|------------------------------------------------------------------------|:--------:|:----------------:|
| `dash_version`        | The version of dash to download                                        |  `true`  |     "LATEST"     |
| `dash_input`          | The dependencies list to analyze                                       |  `true`  |        -         |
| `dependencies_file`   | The path to the `DEPENDENCIES` file in the repo                        |  `true`  | "./DEPENDENCIES" |
| `fail_on_out_of_date` | If set to 'true', the action fails, if `DEPENDENCIES` out of date      |  `true`  |      "true"      |
| `fail_on_rejected`    | If set to 'true', the action fails, if `rejected` dependencies found   |  `true`  |      "true"      |
| `fail_on_out_of_date` | If set to 'true', the action fails, if `restricted` dependencies found |  `true`  |     "false"      |

## Outputs

| output name               | description                                                                                                              |
|:--------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `dependencies_up_to_date` | Boolean flag, that indicates, if the temporarily generated DEPENDENCIES match the one in the repository                  |
| `restricted_deps_found`   | Boolean flag, that indicates, if the temporarily generated DEPENDENCIES contain `restricted` libs                        |
| `rejected_deps_found`     | Boolean flag, that indicates, if the temporarily generated DEPENDENCIES contain `rejected` libs these have to be removed |
