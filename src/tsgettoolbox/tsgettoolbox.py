# -*- coding: utf-8 -*-
r"""
tsgettoolbox command line/library tools to retrieve time series.

This program is a collection of utilities to download data from various
web services.
"""
from __future__ import absolute_import, division, print_function

import os.path
import sys
import warnings

import mando

from .functions.cdec import cdec
from .functions.coops import coops
from .functions.cpc import cpc
from .functions.daymet import daymet
from .functions.fawn import fawn
from .functions.ldas import ldas
from .functions.metdata import metdata
from .functions.modis import modis
from .functions.ncei import (
    ncei_annual,
    ncei_ghcnd,
    ncei_ghcnd_ftp,
    ncei_ghcndms,
    ncei_gsod,
    ncei_gsom,
    ncei_gsoy,
    ncei_nexrad2,
    ncei_nexrad3,
    ncei_normal_ann,
    ncei_normal_dly,
    ncei_normal_hly,
    ncei_normal_mly,
    ncei_precip_15,
    ncei_precip_hly,
)
from .functions.ndbc import ndbc
from .functions.nwis import (
    epa_wqp,
    nwis,
    nwis_dv,
    nwis_gwlevels,
    nwis_iv,
    nwis_measurements,
    nwis_peak,
    nwis_site,
    nwis_stat,
)
from .functions.terraclimate import terraclimate
from .functions.twc import twc
from .functions.unavco import unavco
from .functions.usgs_eddn import usgs_eddn
from .functions.usgs_whets import usgs_whets

warnings.filterwarnings("ignore")


@mando.command()
def about():
    r"""Print out information about tsgettoolbox and the system."""
    from tstoolbox import tsutils

    tsutils.about(__name__)


def main():
    r"""Main function."""
    if not os.path.exists("debug_tsgettoolbox"):
        sys.tracebacklimit = 0
    mando.main()


if __name__ == "__main__":
    main()