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
__Workflow file__:  [.github/workflows/reusable-quality-checks.yaml](.github/workflows/reusable-quality-checks.yaml)
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
      # We recommend to use the @main branch, since we regularly maintain the quality checks (adding new, enhancing existing) 
      - uses: eclipse-tractusx/sig-infra/.github/workflows/reusable-quality-checks.yaml@main
```

### Generate static PlantUML files 

__Description__:    This workflow generates static .svg files form .puml-files and push this to main branch
__Workflow file__:  [.github/workflows/reusable-generate-puml-svg.yaml](.github/workflows/reusable-generate-puml-svg.yaml)
__Usage__:
```yaml
# Example .github/workflows/add-static-puml-files.yaml in your repo
name: "Render static puml files"
# trigger on push to main branch with changed **.puml files in your repository structure
on:
  push:
    branches:
      - 'main'
    paths:
      - '**/*.puml'
jobs:
  render-images:
    uses: eclipse-tractusx/sig-infra/.github/workflows/reusable-generate-puml-svg.yaml@main

```

### Generate static Mermaid files

__Description__:    This workflow generates static .svg files form .mmd/.mermaid-files and push this to main branch
__Workflow file__:  [.github/workflows/reusable-generate-mermaid-svg.yaml](.github/workflows/reusable-generate-mermaid-svg.yaml)
__Usage__:
```yaml
# Example .github/workflows/add-static-mermaid-files.yml in your repo
name: "Render static mermaid files"
# trigger on push to main branch with changed *.mermaid or *.mmd  files in your repository structure
on:
  push:
    branches:
      - 'main'
    paths:
      - '**/*.mermaid'
      - '**/*.mmd'
jobs:
  render-images:
    uses: eclipse-tractusx/sig-infra/.github/workflows/reusable-generate-mermaid-svg.yaml@main

```