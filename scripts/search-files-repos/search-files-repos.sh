#!/bin/bash

# #############################################################################
# Copyright (c) 2024 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0
# #############################################################################
# Generated using Artificial Intelligence (ChatGPT 3.5) and refined/debugged by Human Committers
# Requires the installation of the github cli: https://cli.github.com/
# This script can search for different files in different repositories, indicating if they contain the files or not.

# Organization name (change this to your organization)
ORG_NAME="eclipse-tractusx"

# List of target files to search for
FILES_TO_SEARCH=(
    ".github/workflows/trufflehog.yaml"
    ".github/workflows/trufflehog.yml"
    ".github/workflows/secrets-scan.yml"
)

# Output files to store results
FOUND_FILE="repos_with_target_files.txt"
NOT_FOUND_FILE="repos_without_target_files.txt"

# Clear the output files if they exist
> "$FOUND_FILE"
> "$NOT_FOUND_FILE"

# Check if 'gh' command is available
if ! command -v gh &> /dev/null
then
    echo "'gh' command not found. Please install the GitHub CLI."
    exit 1
fi

# Check if user is authenticated
if ! gh auth status &> /dev/null
then
    echo "You are not authenticated to GitHub CLI. Run 'gh auth login' to authenticate."
    exit 1
fi

# Get list of repositories in the organization, including their archived status
repos=$(gh repo list $ORG_NAME --limit 1000 --json name -q '.[] | .name')

# Loop through each repository
for repo in $repos; do
    echo "Checking repository: $ORG_NAME/$repo"
    
    # Get repository details to check if it's archived
    archived=$(gh api repos/$ORG_NAME/$repo --jq '.archived')
    
    # Skip archived repositories
    if [ "$archived" = "true" ]; then
        echo "$ORG_NAME/$repo is archived. Skipping."
        continue
    fi

    # Flag to check if the file is found in the current repo
    file_found=false

    # Loop through each file in the list
    for file in "${FILES_TO_SEARCH[@]}"; do
        # Check if the file exists in the repository
        if gh api repos/$ORG_NAME/$repo/contents/$file &> /dev/null; then
            echo "Found $file in $ORG_NAME/$repo"
            echo "$ORG_NAME/$repo contains $file" >> "$FOUND_FILE"
            file_found=true
            break  # If one file is found, skip checking others
        fi
    done

    # If no file was found, write the repo to the "not found" file
    if [ "$file_found" = false ]; then
        echo "$ORG_NAME/$repo" >> "$NOT_FOUND_FILE"
    fi
done

echo "Repositories with target files have been saved to $FOUND_FILE."
echo "Repositories without target files have been saved to $NOT_FOUND_FILE."