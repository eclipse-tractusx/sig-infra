# ********************************************************************************
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
# ********************************************************************************

import requests
import json
import logging
import datetime
from dateutil.relativedelta import relativedelta


# fetch with paging, default=30, max=100
# see https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api?apiVersion=2022-11-28

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def fetchAll(gh_session, url):
    data = []
    while url is not None:
        logger.debug(url)
        response = gh_session.get(url)
        elements = json.loads(response.text)
        data.extend(elements)

        next = response.links.get('next', None)
        more = next is not None
        url = next['url'] if more else None
    return data

# Get the teams in the GitHub Org (public or private ones you are member of):
# Links:
# https://docs.github.com/en/rest/teams/members?apiVersion=2022-11-28#list-team-members
# https://api.github.com/orgs/ORG/teams/TEAM_SLUG/members
def getTeamSlugs(gh_session, org):
    teams_url =  'https://api.github.com/orgs/{ORG}/teams'.format(ORG=org)
    teams = fetchAll(gh_session, teams_url)
    team_slugs = sorted([ t['slug'] for t in teams])
    logger.debug("%s GitHub Org Teams: %s", org, team_slugs)
    return team_slugs



def contribution_interval(nr_of_months):

    now = datetime.datetime.now()
    toDate = now.isoformat()
    toDateCSV = now.date().isoformat()

    # today minus  months
    tmpDate = now.today() + relativedelta(months=nr_of_months*-1)
    fromDate = (datetime.datetime.fromisoformat(tmpDate.isoformat())).isoformat()
    fromDateCSV = tmpDate.date().isoformat()

    logger.info("Contribution interval requested: %s - %s", fromDateCSV, toDateCSV)

    return toDate, toDateCSV, fromDate, fromDateCSV

def getToday():
    today = datetime.datetime.now().date().isoformat()
    return today




