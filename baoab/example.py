# This file is part of baoab.
#
# Copyright 2015 Computational Molecular Biology Group, Freie Universitaet Berlin (GER)
#
# thermotools is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np

class HarmonicPotential(object):
    def __init__(self, strength=1.0, mass=1.0):
        self.strength = strength
        self.mass = mass
    def potential_energy(self, q):
        return 0.5 * self.strength * (q**2).sum()
    def potential_gradient(self, q):
        return self.strength * q
    def kinetic_energy(self, p):
        return 0.5 * (p**2).sum() / self.mass
    def total_energy(self, q, p):
        return self.potential_energy(q) + self.kinetic_energy(p)
