
r"""
"""

from setuptools import setup
import versioneer

setup(
    cmdclass=versioneer.get_cmdclass(),
    name='baoab',
    version=versioneer.get_version(),
    description='',
    long_description='',
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
    keywords=[],
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
