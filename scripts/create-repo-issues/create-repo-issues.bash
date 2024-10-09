#!/usr/bin/env bash

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

# Variables
github_host="github.com"
org="eclipse-tractusx"
issue_title="[Trufflehog Update] Add Trufflehog secret scanning workflow"
issue_body_file="issue-body.md"
repos_file="$1" # Pass the file containing repositories as the first argument

# Check if a repository file is provided, and read from the file if so
if [ -n "$repos_file" ]; then
    if [ -f "$repos_file" ]; then
        echo "Reading repositories from file: $repos_file"
        mapfile -t repos < <(grep -v '^\s*$' "$repos_file" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
    else
        echo "File $repos_file not found!"
        exit 1
    fi
else
    echo "No input file provided!"
    exit 1
fi

# Loop through each repository and create an issue
for repo in "${repos[@]}"; do
    echo "Processing repository: $repo"



    echo "Creating issue in repository: $repo"
       if GH_HOST=$github_host gh issue create --title "$issue_title" --body-file "$issue_body_file" --repo "$repo"; then
        echo "Issue created in repository: $repo"
    else
        echo "Failed to create issue in repository: $repo"
    fi
done

echo "Issues created in all repositories."