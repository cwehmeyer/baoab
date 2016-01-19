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
This class implements a harmonic potential with arbitrary dimensionality which should act as an
example how to write Hamiltonian classes fur usage with BAOAB.
"""

class HarmonicPotential(object):
    r"""Hamiltonian for a single particle in a harmonic potential"""
    def __init__(self, strength=1.0, mass=1.0):
        r"""
        Set up the Hamiltonian for a single particle in a harmonic potential or arbitrary dimension
            
        Parameters
        ----------
        strength : float
            force constant of the harmonic potential in arbitrary units
        mass : float
            mass of the particle in arbitrary units

        Notes
        -----
        The potential has the form

        .. math:
            U(\mathbf{q}) = 0.5 * \textrm{strength} * \left\Vert\mathbf{q}\right\Vert_2^2.

        Its gradient reads

        .. math:
            \nabla U(\mathbf{q}) = \textrm{strength} * \mathbf{q}.

        """
        self.strength = strength
        self.mass = mass
    def potential_energy(self, q):
        r"""
        Compute the potential energy of configuration q.

        Parameters
        ----------
        q : numpy.ndarray()
            configuration of arbitrary shape and units

        Returns
        -------
        epot : float
            potential energy
        """
        return 0.5 * self.strength * (q**2).sum()
    def potential_gradient(self, q):
        r"""
        Compute the gradient of potential at configuration q.

        Parameters
        ----------
        q : numpy.ndarray()
            configuration of arbitrary shape and units

        Returns
        -------
        epot : numpy.ndarray(shape=q.shape)
            gradient of the potential
        """
        return self.strength * q
    def kinetic_energy(self, p):
        r"""
        Compute the kinetic energy of momentum p.

        Parameters
        ----------
        p : numpy.ndarray()
            momentum of arbitrary shape and units

        Returns
        -------
        ekin : float
            kinetic energy
        """
        return 0.5 * (p**2).sum() / self.mass
    def total_energy(self, q, p):
        r"""
        Compute the sum of potential and kinetic energy for configuration q and momentum p.

        Parameters
        ----------
        q : numpy.ndarray()
            configuration of arbitrary shape and units
        p : numpy.ndarray(shape=q.shape)
            momentum of arbitrary shape and units

        Returns
        -------
        etot : float
            total energy
        """
        return self.potential_energy(q) + self.kinetic_energy(p)
