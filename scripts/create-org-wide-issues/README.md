# How to create an issue on each repo in `eclipse-tractusx`

This How-To shows an automated approach to create a pre-defined issue on every single repository in
our `eclipse-tractusx` GitHub organization.

Use cases for such automation could be the tracking of a mandatory change in legal documentation for example.

## Prerequisites

The script described in this how-to is relying on the GitHub CLI (`gh`). See install instructions
on [cli.github.com](https://cli.github.com/).

## Disclaimer

The [create-org-issues.bash](create-org-issues.bash) script is currently designed to work
on [eclipse-tractusx](https://github.com/eclipse-tractusx), but can easily be adapted manually to serve different use
cases.
At the time of this writing, there have not been any attempts to make the script more flexible, to keep things simple
and easy to understand.

## Running the script

```shell
chmod +x ./create-org-issues.bash
./create-org-issues.bash
```

It will query all non-archive repositories from [eclipse-tractusx](https://github.com/eclipse-tractusx) and create an
issue of all of them, with a pre-defined title and body. 
The title is currently defined in the script directly. As issue body, the contents of [issue-body.md](issue-body.md)
are used.
