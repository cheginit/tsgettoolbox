
import os
import datetime
from collections import defaultdict
try:
    import ConfigParser as cp
except ImportError:
    import configparser as cp

from odo import odo, resource, convert
import pandas as pd
import requests

from tsgettoolbox import appdirs

dirs = appdirs.AppDirs('tsgettoolbox', 'tsgettoolbox')

# Forecast.io

class forecast_io_json(object):
    def __init__(self, url, **query_params):
        self.url = url
        self.url_params = {}
        self.url_params['latitude'] = query_params.pop('latitude')
        self.url_params['longitude'] = query_params.pop('longitude')
        self.url_params['time'] = query_params.pop('time')
        self.include_db = query_params.pop('database')
        all_dbs = ['currently', 'minutely', 'hourly', 'daily', 'alerts', 'flags']
        all_dbs.remove(self.include_db)
        query_params['exclude'] = ','.join(all_dbs)
        self.query_params = query_params

@resource.register(r'https://api\.forecast\.io/forecast.*', priority=17)
def resource_usgs(uri, **kwargs):
    return forecast_io_json(uri, **kwargs)

# Function to convert from forecast_io_json type to pd.DataFrame
@convert.register(pd.DataFrame, forecast_io_json)
def forecast_io_json_to_df(data, **kwargs):
    # Read in API key
    if not os.path.exists(dirs.user_config_dir):
        os.makedirs(dirs.user_config_dir)
    configfile = os.path.join(dirs.user_config_dir, 'config.ini')
    if not os.path.exists(configfile):
        with open(configfile, 'w') as fp:
            fp.write('''

[forecast.io]
api_key = ReplaceThisStringWithYourKey

''')
    # Make sure read only by user.
    os.chmod(configfile, 0o600)

    inifile = cp.ConfigParser()
    inifile.readfp(open(configfile, 'r'))

    try:
        api_key = inifile.get('forecast.io', 'api_key')
    except:
        with open(configfile, 'a') as fp:
            fp.write('''

[forecast.io]
api_key = ReplaceThisStringWithYourKey

''')
        api_key = 'ReplaceThisStringWithYourKey'

    inifile.readfp(open(configfile, 'r'))
    api_key = inifile.get('forecast.io', 'api_key')
    if api_key == 'ReplaceThisStringWithYourKey':
        raise ValueError('''
*
*   Need to edit {0}
*   to add your API key that you got from forecast.io.
*
'''.format(configfile))

    urlvar = '{0},{1}'.format(data.url_params['latitude'],
                              data.url_params['longitude'])

    if data.url_params['time'] is not None:
        urlvar = urlvar + ',{0}'.format(data.url_params['time'])

    req = requests.get('/'.join([data.url,
                                 api_key,
                                 urlvar]),
                        data.query_params)
    req.raise_for_status()

    try:
        ndfj = pd.read_json(req.content, orient='index')
    except ValueError:
        return pd.DataFrame()

    ndfj = pd.DataFrame(ndfj.ix[data.include_db, :])

    ndfj = ndfj.transpose()

    ndfj.dropna(inplace=True, how='all')

    if data.include_db not in ['currently', 'flags']:
        ndfj = pd.DataFrame(ndfj.ix[data.include_db, 'data'])

    if data.include_db != 'flags':
        ndfj.index = pd.to_datetime(ndfj['time'], unit='s')
        ndfj.drop('time', axis=1, inplace=True)
        ndfj.sort(inplace=True)

    for datecols in [
                     'apparentTemperatureMinTime',
                     'apparentTemperatureMaxTime',
                     'precipIntensityMaxTime',
                     'sunriseTime',
                     'sunsetTime',
                     'temperatureMaxTime',
                     'temperatureMinTime'
                     ]:
        if datecols in ndfj.columns:
            ndfj[datecols] = pd.to_datetime(ndfj[datecols], unit='s')

    return ndfj


if __name__ == '__main__':
    r = resource(
        r'https://api.forecast.io/forecast',
        latitude=28.45,
        longitude=-81.34,
        database='currently',
        time='2020-01-01T01:00:00',
        )

    as_df = odo(r, pd.DataFrame)
    print('Forecast.io')
    print(as_df)

    r = resource(
        r'https://api.forecast.io/forecast',
        latitude=28.45,
        longitude=-81.34,
        database='minutely',
        time=None,
        )

    as_df = odo(r, pd.DataFrame)
    print('Forecast.io')
    print(as_df)

    r = resource(
        r'https://api.forecast.io/forecast',
        latitude=28.45,
        longitude=-81.34,
        database='hourly',
        time=None,
        )

    as_df = odo(r, pd.DataFrame)
    print('Forecast.io')
    print(as_df)

    r = resource(
        r'https://api.forecast.io/forecast',
        latitude=28.45,
        longitude=-81.34,
        database='daily',
        time=None,
        )

    as_df = odo(r, pd.DataFrame)
    print('Forecast.io')
    print(as_df)

    r = resource(
        r'https://api.forecast.io/forecast',
        latitude=28.45,
        longitude=-81.34,
        database='alerts',
        time=None,
        )

    as_df = odo(r, pd.DataFrame)
    print('Forecast.io')
    print(as_df)

    r = resource(
        r'https://api.forecast.io/forecast',
        latitude=28.45,
        longitude=-81.34,
        database='flags',
        time=None,
        )

    as_df = odo(r, pd.DataFrame)
    print('Forecast.io')
    print(as_df)

