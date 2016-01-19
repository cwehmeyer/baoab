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
The BAOAB Langevin dynamics integrator by B. Leimkuhler and C. Matthews.
"""

from setuptools import setup
import versioneer

long_description = r"""
This package provides a Python version of the BAOAB Langevin dynamics integrator by
Benedict Leimkuhler and Charles Matthews.
"""

setup(
    cmdclass=versioneer.get_cmdclass(),
    name='baoab',
    version=versioneer.get_version(),
    description='The BAOAB Langevin dynamics integrator by B. Leimkuhler and C. Matthews.',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: C',
        'Programming Language :: Cython',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics'],
    keywords=[
        'BAOAB',
        'Langevin dynamics',
        'molecular dynamics',
        'MD',
        'NVT'],
    url='https://github.com/cwehmeyer/baoab',
    maintainer='Christoph Wehmeyer',
    maintainer_email='christoph.wehmeyer@fu-berlin.de',
    license='LGPLv3+',
    setup_requires=[
        'numpy>=1.7',
        'setuptools>=0.6'],
    tests_require=[
        'numpy>=1.7',
        'nose>=1.3'],
    install_requires=[
        'numpy>=1.7',],
    packages=['baoab', 'baoab.core'],
    test_suite='nose.collector',
    scripts=[]
)
