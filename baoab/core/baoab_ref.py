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

r"""
This module implements the reference version of the BAOAB Langevin dynamics integrator.
"""

import numpy as np

def baoab_step(q0, p0, dt, kt, damping, hamiltonian):
    p1 = p0 + 0.5 * dt * hamiltonian.potential_gradient(q0)
    q1 = q0 - 0.5 * dt * p1 / hamiltonian.mass
    p1 = np.exp(-damping * dt) * p1 + \
        np.sqrt(kt * (1.0 - np.exp(-2.0 * damping * dt)) / hamiltonian.mass) * \
        np.random.normal(size=p1.shape)
    q1 = q1 - 0.5 * dt * p1 / hamiltonian.mass
    p1 = p1 + 0.5 * dt * hamiltonian.potential_gradient(q1)
    return q1, p1

def baoab_run(n_samples, q0, p0, dt, kt, damping, hamiltonian, skip=1):
    q = []
    p = []
    q1 = q0.copy()
    p1 = p0.copy()
    for _step in range(n_samples):
        for _skip in range(skip):
            q1, p1 = baoab_step(q1, p1, dt, kt, damping, hamiltonian)
        q.append(q1)
        p.append(p1)
    return np.array(q), np.array(p)
