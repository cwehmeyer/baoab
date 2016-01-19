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
This module implements a class for the BAOAB Langevin dynamics integrator.
"""

from .core import run_ref
from .core import run_opt

import numpy as _np

class BAOAB(object):
    r"""This class implements the BAOAB Langevin dynamics integrator."""
    def __init__(self, hamiltonian, dt, kt, damping, skip=1, method='optimized'):
        r"""
        Set up the Hamiltonian for a single particle in a harmonic potential or arbitrary dimension
            
        Parameters
        ----------
        hamiltonian : object
            an object which represents the Hamiltonian of the system of interest
        dt : float
            time step for the BAOAB integrator
        kt : float
            energy scale (Boltzmann's constant times temperature)
        damping : float
            damping constant
        skip : int
            output only every skip time steps
        method : string
            use optimized or reference

        Notes
        -----
        The BAOAB [1]_ Langevin dynamics integrator was developed by Benedict Leimkuhler and
        Charles Matthews.

        .. [1] Leimkuhler, B. and Matthews, C.: Robust and efficient configurational molecular
            sampling via Langevin dynamics. J. Chem. Phys. 138: 174102 (2013)

        """
        self.hamiltonian = hamiltonian
        self.dt = dt
        self.kt = kt
        self.damping = damping
        self.skip = skip
        self.method = method
        # compute factors for optimized version
        self.dth = 0.5 * self.dt
        self.factor_a = _np.exp(-self.damping * self.dt)
        self.factor_b = self.kt * (1.0 - _np.exp(-2.0 * self.damping * self.dt))
        # compute derived values
        self.effective_dt = self.dt * self.skip
    def run(self, q0, p0, n_samples):
        r"""
        Perform a BAOAB run.
            
        Parameters
        ----------
        q0 : numpy.ndarray()
            initial configuration
        p0 : numpy.ndarray(shape=q0.shape)
            initial momenta
        n_samples : int
            number of samples with effective time step dt * skip

        Returns
        -------
        q : numpy.ndarray(shape=(n_samples, q0.shape))
            trajectory of configurations
        p : numpy.ndarray(shape=(n_samples, p0.shape))
            trajectory of momenta

        """
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
            return None, None
    def epot(self, q_traj):
        r"""
        Compute the potential energies along a given trajectory of configurations.
            
        Parameters
        ----------
        q_traj : numpy.ndarray()
            trajectory of configurations

        Returns
        -------
        epot : numpy.ndarray(shape=(q_traj.shape[0],))
            trajectory of potential energies

        """
        return _np.array(
            [self.hamiltonian.potential_energy(q_traj[i, :]) for i in range(q_traj.shape[0])])
    def ekin(self, p_traj):
        r"""
        Compute the kinetic energies along a given trajectory of momenta.
            
        Parameters
        ----------
        p_traj : numpy.ndarray()
            trajectory of momenta

        Returns
        -------
        ekin : numpy.ndarray(shape=(p_traj.shape[0],))
            trajectory of kinetic energies

        """
        return _np.array(
            [self.hamiltonian.kinetic_energy(p_traj[i, :]) for i in range(p_traj.shape[0])])
