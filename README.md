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
