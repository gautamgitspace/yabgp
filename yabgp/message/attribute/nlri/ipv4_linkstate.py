# Copyright 2015 Cisco Systems, Inc.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""IPv4 BGP linkstate NLRI
"""
import struct
import math
import binascii

import netaddr

from yabgp.common import constants as bgp_cons

LOG = logging.getLogger(__name__)

class IPv4LinkState(object):

    @classmethod
    def parse(cls, value):
        """
        IPv4 BGP linkstate NLRI
        """
        nlri_list = []
        while value:
            nlri_dict = {}
            nlri_list.append(nlri_dict)
        return nlri_list

    @classmethod
    def contruct(cls, value):
        pass