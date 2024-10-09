# How to create an issue on each repo in `eclipse-tractusx`

This How-To shows an automated approach to create a pre-defined issue on a list of  repositories in
our `eclipse-tractusx` GitHub organization.

Use cases for such automation could be the tracking of a mandatory change in legal documentation for example.

## Prerequisites

The script described in this how-to is relying on the GitHub CLI (`gh`). See install instructions
on [cli.github.com](https://cli.github.com/).

## Disclaimer

The [create-repo-issues.bash](create-repo-issues.bash) script is currently designed to work
on [eclipse-tractusx](https://github.com/eclipse-tractusx), but can easily be adapted manually to serve different use
cases.
At the time of this writing, there have not been any attempts to make the script more flexible, to keep things simple
and easy to understand.

## Running the script

```shell
chmod +x ./create-repo-issues.bash
./create-repo-issues.bas repo.txt
```

The `repo.txt` needs to be updated with the desired repositories to create the issue. Another file can also be indicated by passing the path as parameter instead of `repo.txt`.

The repositories need to be listed in the following way (Example):


```
eclipse-tractusx/SSI-agent-lib
eclipse-tractusx/eclipse-tractusx.github.io.largefiles
eclipse-tractusx/testdata-provider
eclipse-tractusx/tractusx-profiles
eclipse-tractusx/app-dashboard
```

It will query all the selected non-archive repositories from [eclipse-tractusx](https://github.com/eclipse-tractusx) and create an
issue of all of them, with a pre-defined title and body.
The title is currently defined in the script directly. As issue body, the contents of [issue-body.md](issue-body.md)
are used.

> [!WARNING]
> After creating a certain amount of repositories, depending on the ammount of repos in the list, GITHUB will give a timeout of some seconds, to prevent uses to create issues as a attack form.
>
> Remove the repos from the list which the issues were created and wait for the timeout to pass then re-execute the script with the missing repos.
