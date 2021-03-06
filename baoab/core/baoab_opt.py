# This file is part of baoab.
#
# Copyright 2015 Computational Molecular Biology Group, Freie Universitaet Berlin (GER)
#
# baoab is free software: you can redistribute it and/or modify
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
This module implements a slighty optimized version of the BAOAB Langevin dynamics integrator.
"""

import numpy as _np

def baoab_run(n_samples, q0, p0, dth, factor_a, factor_b, hamiltonian, skip=1):
    # factor_a = _np.exp(-damping * dt)
    # factor_b = kt * (1.0 - _np.exp(-2.0 * damping * dt))
    q = []
    p = []
    q1 = q0.copy()
    p1 = p0.copy()
    g1 = hamiltonian.potential_gradient(q1)
    for _step in range(n_samples):
        for _skip in range(skip):
            p1 = p1 + dth * g1
            q1 = q1 - dth * p1 / hamiltonian.mass
            p1 = factor_a * p1 + \
                _np.sqrt(factor_b / hamiltonian.mass) * \
                _np.random.normal(size=p1.shape)
            q1 = q1 - dth * p1 / hamiltonian.mass
            g1 = hamiltonian.potential_gradient(q1)
            p1 = p1 + dth * g1
        q.append(q1)
        p.append(p1)
    return _np.array(q), _np.array(p)
