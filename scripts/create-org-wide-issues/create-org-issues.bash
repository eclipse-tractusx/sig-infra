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

github_host="github.com"
org="eclipse-tractusx"

issue_title="Mandatory change in licensing and legal documentation"
issue_body_file="issue-body.md"

readarray -t repos < <(GH_HOST=$github_host gh repo list "$org" --limit 1000 --no-archived --json nameWithOwner --jq '.[].nameWithOwner')

for repo in "${repos[@]}"; do
    GH_HOST=$github_host gh issue create --title "$issue_title" --body-file "$issue_body_file" --repo "$repo"
done
