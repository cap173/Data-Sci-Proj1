# COSC-287, Fall 2019
> **- Project 1 _Luc Nikiema, Aleida Olvera, Christian Paniagua_**


### Data Science Problem
Gentrification is sometimes seen as a sign of economic growth and investment in a neighborhood, but that "investment" inevitably changes the demographics and character of the neighborhood's community. Lower-income residents who have leases on apartments are now faced with rent price increases, which inevitably leads to many of these residents being displaced. Prior to gentrification, these neighborhoods were not being invested into, but when the affluent population joins the neighborhood, money is poured into it. Therefore, the main goal of the project is to investigate this phenomena. We plan to investigate this through changes in the demographics as well as the rising median household income and funding in different neighborhoods that are being gentrified.

### Potential Analyzes that Can Be Conducted Using Collected Data
First we plan to collect data on median household income, population age, and the number of occupied and non-occupied housing units. We will also look into the changes in population (most specifically race and age) among different neighborhoods in DC. Because we will be comparing census data from 2000 and 2010, we can visualize the impact gentrification made over the DC neighborhoods during this 10 year time frame. This data will contribute to answering our question because it is divided into tracts, which is a census designated area of the city. The variables that are most useful are the occupied and vacant housing units as well as the adjusted income of each household.

Some questions and possible directions we could ask and answer with this data are the following:
- Do changes in a neighborhood's median household income drastically impact the number of vacant housing units in neighborhoods?
- Do changes in a neighborhood's median household income cause changes in the racial demographics of the neighborhood?
- Is there a correlation between the increase of adults in the population and the increase in median household income?

### Data Issues
The biggest issue with the data was there were missing values on a few rows. The data was completely clean, and the only change that needed to be made was renaming the variable headers. The variable headers to be renamed were as follows:
- `P0010001` was renamed to `Total Population`
- `P0010002` was renamed to `Total Pop of 1 Race`
- `P0010003` was renamed to `Pop of 1 race: White`
- `P0010004` was renamed to `Pop of 1 race: Black`
- `P0010005` was renamed to `Pop of 1 race: American Indian Alaskan`
- `P0010006` was renamed to `Pop of 1 race: Asian`
- `P0010007` was renamed to `Pop of 1 race: Native Hawaiian Pacific Islander`
- `P0010008` was renamed to `Pop of 1 race: Other Race`
- `OP000001` was renamed to `Pop 2 or more races: Black and`
- `OP000002` was renamed to `Pop 2 or more races: American Indian Alaskan and`
- `OP000003` was renamed to `Pop 2 or more races: Asian and`
- `OP000004` was renamed to `Pop 2 or more races: Native Hawaiian Pacific Islander and`
- `P0020002` was renamed to `Total Hispanic Population`
- `P0020005` was renamed to `Total Non-Minority Population (White Not Hispanic)`
- `P0020006` was renamed to `Not Hispanic Pop of 1 race: Black`
- `P0020007` was renamed to `Not Hispanic Pop of 1 race: American Indian Alaskan`
- `P0020008` was renamed to `Not Hispanic Pop of 1 race: Asian`
- `P0020009` was renamed to `Not Hispanic Pop of 1 race: Native Hawaiian Pacific Islander`
- `P0020010` was renamed to `Not Hispanic Pop of 1 race: Other Race`
- `OP00005` was renamed to `Not Hispanic Pop 2 or more races: Black and`
- `OP00006` was renamed to `Not Hispanic Pop 2 or more races: American Indian Alaskan and`
- `OP00007` was renamed to `Not Hispanic Pop 2 or more races: Asian and`
- `OP00008` was renamed to `Not Hispanic Pop 2 or more races: Native Hawaiian Pacific Islander and`
- `P0030001` was renamed to `Total Pop 18+`
- `P0030003` was renamed to `18+ Pop 1 race: White`
- `P0030004` was renamed to `18+ Pop 1 race: Black`
- `P0030005` was renamed to `18+ Pop 1 race: American Indian Alaskan`
- `P0030006` was renamed to `18+ Pop 1 race: Asian`
- `P0030007` was renamed to `18+ Pop 1 race: Native Hawaiian Pacific Islander`
- `P0030008` was renamed to `18+ Pop 1 race: Other race`
- `OP00009` was renamed to `18+ Pop 2 or more races: Black and`
- `OP00010` was renamed to `18+ Pop 2 or more races: American Indian Alaskan and`
- `OP00011` was renamed to `18+ Pop 2 or more races: Asian and`
- `OP00012` was renamed to `18+ Pop 2 or more races: Native Hawaiian Pacific Islander`
- `P0040002` was renamed to `Hispanic 18+ Pop`
- `P0040005` was renamed to `Non-Minority 18+ Pop (White Non-Hispanic)`
- `P0040006` was renamed to `Not Hispanic 18+ Pop 1 race: Black`
- `P0040007` was renamed to `Not Hispanic 18+ Pop 1 race: American Indian Alaskan`
- `P0040008` was renamed to `Not Hispanic 18+ Pop 1 race: Asian`
- `P0040009` was renamed to `Not Hispanic 18+ Pop 1 race: Native Hawaiian Pacific Islander`
- `P0040010` was renamed to `Not Hispanic 18+ Pop 1 race: Other race`
- `OP000013` was renamed to `Not Hispanic 18+ Pop 2 or more races: Black and`
- `OP000014` was renamed to `Not Hispanic 18+ Pop 2 or more races: American Indian Alaskan and`
- `OP000015` was renamed to `Not Hispanic 18+ Pop 2 or more races: Asian and`
- `OP000016` was renamed to `Not Hispanic 18+ Pop 2 or more races: Native Hawaiian Pacific Islander and`
- `H0010001` was renamed to `Total Housing Units`
- `H0010002` was renamed to `Occupied Housing Units`
- `H0010003` was renamed to `Vacant Housing Units`

### Files in Project
- `getData.py`: This file pulls 2000 and 2010 DC Census data from the OpenData API. It then cleans the data and spits out the original and clean data into separate files.
    - `census_2010.csv`: As the name suggests, this is the 2010 DC Census. It is important to note this is the data before it gets cleaned.
    - `census_2010_CLEAN.csv`: This contains the clean 2010 DC Census data.
    - `census_2000.csv`: This file is the same as the 2010 csv file, except this reflects 2000 DC Census data.
    - `census_2000_CLEAN.csv`: This file is the clean data extracted from the 2000 DC Census file.
