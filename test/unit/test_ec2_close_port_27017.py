# Copyright (c) 2020 VMware Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

from remediation_worker.jobs.ec2_close_port_27017.ec2_close_port_27017 import EC2ClosePort27017


@pytest.fixture
def valid_payload():
    return """
{
    "notificationInfo": {
        "FindingInfo": {
            "ObjectId": "i-00347a2be30cf1a15",
            "Region": "us-east-1"
        }
    }
}
"""


class TestEC2ClosePort27017:
    def test_parse_payload(self, valid_payload):
        obj = EC2ClosePort27017()
        param, region = obj.parse(valid_payload)
        assert "instance_id" in param
        assert param["instance_id"] == "i-00347a2be30cf1a15"