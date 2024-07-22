# Creating statistics for committer and contributor activities

This script creates a csv file with information about member activities and the membership in teams for one GitHub organization.

This a an example of the data structure for the [Eclipse Tractus-X GitHub organization](https://github.com/eclipse-tractusx) and the [teams](https://github.com/orgs/eclipse-tractusx/teams).

| Column                                     | Content                                                         |
|-----------------------------------------|-----------------------------------------------------------------|
| GitHub Login                            | the GitHub login of the user                                    |
| totalCommitContributions (*)            | How many commits were made by the user in this time span.       |
| totalIssueContributions (*)             | How many issues the user opened.                                |
| totalPullRequestContributions (*)       | How many pull requests the user opened.                         |
| totalPullRequestReviewContributions (*) | How many pull request reviews the user left.                    |
| sum_contributions                       | The sum of the contributions listed before.                     |
| login (**)                              | The GitHub login                                                |
| id (**)                                 | The GitHub user id                                              |
| profile (**)                            | The GitHub user profile URL                                     |
| automotive-tractusx-committers (**)     | Indicates whether the user is a member of this team.            |
| automotive-tractusx-contributors (**)   | Indicates whether the user is a member of this team.            |
| automotive-tractusx-project-leads (**)  | Indicates whether the user is a member of this team.            |
| < more teams ...> (**)                  | Indicates whether the user is a member of this team.            |


(*) from API: https://docs.github.com/en/graphql/reference/objects#organizationmemberconnection

(**) Empty if the user is member of the organization, but not of any teams.

__Note:__
Only teams of the configured GitHub organization that are public or that you are a member of will be retrieved

## Prerequisites

- a Jupyter Notebook environment
- the Python libraries declared in the file "requirements.in" have to be installed


## Configuration

Configure the properties in the file `config.py`.

| Property                   | Description                                                               |
|----------------------------|---------------------------------------------------------------------------|
| username                   | GitHub user name.                                                         |
| token                      | GitHub Personal Access Token with scope: repo, read:org, read:user scoped |
| organizationName           | GitHub organization name.                                                 |
| organizationID             | GitHub organization ID.                                                   |
| contrib_nr_of_months       | Number of last months in which the activity is retrieved.                 |
| fname_github_contributions | Name of the output file.                                                  |


## Creating the DEPENDENCIES file (Eclipse projects only)

If the use of the external libraries is changed, e.g. by extending or updating the scripts, the `DEPENDENCIES` file (at root level of your repository) also have to be updated.

For all directly imported libraries, using the `import` statement in the scripts, do:

- Add new libraries to the file `requirements.in` with the concrete version number used.
- When updating libraries, then also update the version number in the file `requirements.in`
- Generate the file `requirements.txt` via `pip-compile requirements.in`
- Use the file `requirements.txt` as input for the Dash Tool, see [here](https://github.com/eclipse-dash/dash-licenses/blob/master/README.md#example-python)
- update the `DEPENDENCIES` file in your repository

## Disclaimer

The script is currently designed to work and tested
on [eclipse-tractusx](https://github.com/eclipse-tractusx), but can easily be adapted to serve different use cases.

## NOTICE

This work is licensed under the [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0).

- SPDX-License-Identifier: Apache-2.0
- SPDX-FileCopyrightText: 2024 Contributors to the Eclipse Foundation
- Source URL: https://github.com/eclipse-tractusx/sig-infra/tree/main/scripts