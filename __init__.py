"""
ktnumba
==========================================

Package belonging to Karttur´s GeoImagine Framework.

Author
------
Thomas Gumbricht (thomas.gumbricht@karttur.com)

"""
from .version import __version__, VERSION, metadataD

from .tsnumba import InterpolateLinearNaNNumba

#from .tsnumba import  ResampleSeasonalAvg, ResampleToPeriodAvg, ResampleToPeriodSum, MKtestIni,OLSextendedNumba, ResampleToDictPeriodAvgNan, SeasonFill, InterpolateLinearFixedNaNNumba
#from .tsnumba import InterpolatePeriodsLinear, ResampleFixedPeriods, PearsonNrNumba
#from .layernumba import ImageTransform, ImageFgBg, SingleMask, AddToMask, SetMask, ScalarTWIpercent