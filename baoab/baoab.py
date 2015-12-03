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

from core.baoab_ref import baoab_run as run_ref
from core.baoab_opt import baoab_run as run_opt

import numpy as np

class BAOAB(object):
    def __init__(self, hamiltonian, dt, kt, damping, skip=1, method='optimized'):
        self.hamiltonian = hamiltonian
        self.dt = dt
        self.kt = kt
        self.damping = damping
        self.skip = skip
        self.method = method
        # compute factors for optimized version
        self.dth = 0.5 * self.dt
        self.factor_a = np.exp(-self.damping * self.dt)
        self.factor_b = self.kt * (1.0 - np.exp(-2.0 * self.damping * self.dt))
        # compute derived values
        self.effective_dt = self.dt * self.skip
    def run(self, q0, p0, n_samples):
        if self.method == 'reference':
            return run_ref(
                n_samples, q0, p0,
                self.dt, self.kt, self.damping, self.hamiltonian, skip=self.skip)
        elif self.method == 'optimized':
            return run_opt(
                n_samples, q0, p0,
                self.dth, self.factor_a, self.factor_b, self.hamiltonian, skip=self.skip)
        else:
            print "method <%s> is not implemented" % self.method
    def ekin(self, p_traj):
        return np.array(
            [self.hamiltonian.kinetic_energy(p_traj[i, :]) for i in range(p_traj.shape[0])])
    def epot(self, q_traj):
        return np.array(
            [self.hamiltonian.potential_energy(q_traj[i, :]) for i in range(q_traj.shape[0])])
