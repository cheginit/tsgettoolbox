## v23.15.8 (2021-08-01)

## v23.15.7 (2021-07-25)

## v23.15.6 (2021-07-24)

## v23.14.6 (2021-07-22)

### Fix

- netcdf4 dep., docs

## v23.13.6 (2021-07-07)

### Fix

- Finished some part of terraclimate
fix: rename ncdc to ncei
fix: ldas deprecated "variable" in favor of "variables"
fix: ncei 1/10 degC to full degC
fix: ncei allow for prefix or no prefix for variables
fix: ncei add units to column header.
docs: misc.

### Refactor

- Apply all tests in .pre-commmit-config.yaml
feat: Add metdata.

## v23.11.5 (2021-06-10)

### Fix

- various small fixes.

## v23.10.5 (2021-05-19)

### Feat

- Added usgs_whets pull from USGS-CIDA
fix: Minor fixes for ncei and fawn

## v22.10.5 (2021-05-14)

### Fix

- The rolling download feature of ncdc/ncei now works correctly.
refactor: Renamed all "ncdc" to "ncei" to match name change from
National Climatic Data Center, to National Centers for Environmental
Information.
docs: Small fixes for the ncdc -> ncei name change
style: Removed all trailing spaces and used "black" to reformat.

## v22.9.4 (2021-05-12)

### Fix

- Better defaults in xr.open_dataset
- Made metdata variables a keyword.

## v22.8.4 (2021-05-07)

### Feat

- Added metdata download.

## v21.8.4 (2021-03-14)

### Fix

- Now will co

## v21.7.4 (2021-03-06)

### Feat

- Allow for multiple variables in ldas.

## v21.6.4 (2021-03-06)

### Fix

- Make Literal work with Python 3.6.7.

## v21.5.4 (2021-03-06)

### Fix

- Requests now retries. Better docs. typic.al
- Removing remnants of "odo".

### Perf

- Removed dependence on "odo".

## v21.4.4 (2021-02-11)

### Fix

- fawn-handled empty responses.

## v21.3.4 (2021-02-11)

### Fix

- Fixed start and end dates in fawn.
- Testing of station names was incorrect.

## v21.2.3 (2021-02-01)

### Fix

- Spelling errors/mechanize is new dependency

### Feat

- Added FAWN support.

## v21.1.2 (2020-09-05)

### Fix

- Bunch of miscellaneous fixes.
- Added units to column names for cpc.
- Updated to latest URL for cdec
- COOPS now uses https.

## v21.1.1 (2020-04-30)

## v20.42.11.23 (2020-03-28)

## v20.42.11.22 (2020-03-09)

## v20.42.11.21 (2020-03-09)

## v20.41.11.21 (2019-11-20)

## v18.39.11.21 (2019-11-02)

## v17.38.11.21 (2019-10-21)

## v17.38.11.20 (2019-10-03)

## v17.38.11.18 (2019-09-18)