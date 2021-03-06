# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Downloads the FITS files that are used in image testing and for building documentation.
"""
from astropy.utils.data import download_file
from astropy.io import fits

__all__ = ['fetch_msx_hdu',
           'fetch_rosat_hdu',
           'fetch_twoMASS_k_hdu',
           'fetch_l1448_co_hdu',
           'fetch_bolocam_hdu',
           ]

URL = 'http://astrofrog.github.io/wcsaxes-datasets/'


def fetch_hdu(filename, cache=True):
    """Download a FITS file to the cache and open HDU 0.
    """
    path = download_file(URL + filename, cache=cache)
    return fits.open(path)[0]


def fetch_msx_hdu(cache=True):
    """Fetch the MSX example dataset HDU.

    Returns
    -------
    hdu : `~astropy.io.fits.ImageHDU`
        Image HDU
    """
    return fetch_hdu('msx.fits', cache=cache)


def fetch_rosat_hdu(cache=True):
    return fetch_hdu('rosat.fits', cache=cache)


def fetch_twoMASS_k_hdu(cache=True):
    return fetch_hdu('2MASS_k.fits', cache=cache)


def fetch_l1448_co_hdu(cache=True):
    return fetch_hdu('L1448_13CO_subset.fits', cache=cache)


def fetch_bolocam_hdu(cache=True):
    return fetch_hdu('bolocam_v2.0.fits', cache=cache)
