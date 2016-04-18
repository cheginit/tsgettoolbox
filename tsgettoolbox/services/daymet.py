
import datetime

from odo import odo, resource, convert
import pandas as pd

try:
    import urllib.parse as urlp
except ImportError:
    import urllib as urlp

_units_map = {
    'tmax': 'deg_C',
    'tmin': 'deg_C',
    'srad': 'W/m2',
    'vp': 'Pa',
    'swe': 'kg/m2',
    'prcp': 'mm',
    'dayl': 's',
    }

# Daymet

# pd.read_csv('http://daymet.ornl.gov/data/send/saveData?measuredParams=tmax,tmin,prcp&lat=43.1&lon=-85.3&year=2000,2001',
# skiprows=7,
# date_parser=testp,
# index_col=0,
# parse_dates=[[0,1]])

class Daymet(object):
    def __init__(self, url, **query_params):
        avail_params = ['tmax', 'tmin', 'srad', 'vp', 'swe', 'prcp', 'dayl']
        params = {
            'measureParams': None,
            'year': None,
            }
        params.update(query_params)
        if params['measuredParams'] is not None:
            for testparams in params['measuredParams'].split(','):
                if testparams not in avail_params:
                    raise ValueError('''
*
*   The measuredParams must be 'tmax', 'tmin', 'srad', 'vp', 'swe', 'prcp',
*   and 'dayl'.  You supplied {0}.
*
'''.format(testparams))
        if params['year'] is not None:
            for testyear in params['year'].split(','):
                try:
                    iyear = int(testyear)
                except ValueError:
                    raise ValueError('''
*
*   The year= option must contain a comma separated list of integers.  You
*   supplied {0}.
*
'''.format(testyear))
                last_year = datetime.datetime.now().year - 1
                if iyear < 1980 or iyear > last_year:
                    raise ValueError('''
*
*   The year= option must contain values from 1980 up to and including the last
*   calendar year.  You supplied {0}.
*
'''.format(iyear))

        self.url = url
        self.query_params = params

# Function to make `resource` know about the new Daymet type.
@resource.register(r'http(s)?://daymet\.ornl\.gov.*', priority=17)
def resource_daymet(uri, **kwargs):
    return Daymet(uri, **kwargs)

def _daymet_date_parser(year, doy):
    return pd.to_datetime(year) + pd.to_timedelta(pd.np.int(doy), 'D') - pd.to_timedelta(1, 'D')

# Function to convert from Daymet type to pd.DataFrame
@convert.register(pd.DataFrame, Daymet)
def daymet_to_df(data, **kwargs):
    df = pd.read_csv(
        urlp.unquote('{}?{}'.format(data.url,
                                    urlp.urlencode(data.query_params))),
        skiprows=7,
        sep=",",
        date_parser=_daymet_date_parser,
        header=0,
        index_col=0,
        skipinitialspace=True,
        parse_dates=[[0, 1]])
    df.columns = ['Daymet-{0}'.format(i.replace(' ', '_')) for i in df.columns]
    df.index.name = 'Datetime'
    return df

if __name__ == '__main__':
    r = resource(
        r'http://daymet.ornl.gov/data/send/saveData',
        measuredParams='tmax,tmin',
        lat=43.1,
        lon=-85.2,
        year='2000,2001'
        )

    as_df = odo(r, pd.DataFrame)
    print('Daymet')
    print(as_df)

