#!/usr/bin/env python3
#
# This file is part of warwick.observatory.
#
# warwick.observatory is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# warwick.observatory is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with warwick.observatory.  If not, see <http://www.gnu.org/licenses/>.

"""
Common helper functions
"""

import Pyro4

def pyro_client_matches(ip_whitelist):
    """Returns true if the current pyro client IP is included in the given white list"""
    client_ip = Pyro4.current_context.client.sock.getpeername()[0]
    return client_ip in ip_whitelist

def sexagesimal(angle):
    """Formats a decimal number in sexagesimal format"""
    negative = angle < 0
    angle = abs(angle)

    degrees = int(angle)
    angle = (angle - degrees) * 60
    minutes = int(angle)
    seconds = (angle - minutes) * 60

    if negative:
        degrees *= -1

    return '{:d}:{:02d}:{:05.2f}'.format(degrees, minutes, seconds)
