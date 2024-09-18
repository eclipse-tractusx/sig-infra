# How to search for files which can or not be found in the repositories in a Github Organization

This script can list the repositories which contain or not contain a list of specific files. It will search in
our `eclipse-tractusx` GitHub organization for the repositories, checking if they contain the target files.

Use cases for such automation could be the tracking of a mandatory change in legal  or security requirements for example.

## Prerequisites

The script described in this how-to is relying on the GitHub CLI (`gh`). See install instructions
on [cli.github.com](https://cli.github.com/).

## Disclaimer

The [search-files-repos.sh](search-files-repos) script is currently designed to work
on [eclipse-tractusx](https://github.com/eclipse-tractusx), but can easily be adapted manually to serve different us
cases.
At the time of this writing, there have not been any attempts to make the script more flexible, to keep things simple
and easy to understand.

## Running the script

```shell
chmod +x ./search-files-repos.sh
./search-files-repos.sh
```

Specify the files in the script in `FILES_TO_SEARCH`. Some file paths were provided as an example:

```shell
FILES_TO_SEARCH=(
    ".github/workflows/trufflehog.yaml"
    ".github/workflows/trufflehog.yml"
    ".github/workflows/secrets-scan.yml"
)
```

Replace them with the path to the files you are interested to target.

The script will query all the non-archive repositories from [eclipse-tractusx](https://github.com/eclipse-tractusx), searching one by one for the files which were specified.

The script will create two files:

- `repos_with_target_files.txt`: Contains the repositories which have the file, there will also be indicated which file was found in the repository.
- `repos_without_target_files.txt`: Contains the list of repositories which do not contain the searched files.
