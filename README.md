# Road Accidents in India: ETL Pipeline and Tableau Dashboard

An ETL project on state-wise road accident data for India (2018-2024).

**Dashboard:** https://public.tableau.com/app/profile/vaishnavi.kulkarni6683/viz/RoadAccidentsDashboard_17935234853090/RoadAccidentsinIndia2018-2024?publish=yes

## Tools
Python, pandas, SQLAlchemy, PostgreSQL, SQL, Tableau Public

## Pipeline
1. **Extract:** read the state-wise accident CSV (NCRB open data via India Data Portal) with pandas.
2. **Transform:** dropped the id column, trimmed text, converted number columns, checked for missing values and duplicates.
3. **Load:** loaded the cleaned table into PostgreSQL with SQLAlchemy (783 rows).
4. **Analyse:** SQL queries on accident totals by year and state, then a road-accidents-only CSV for Tableau.

## Data quality findings
- **2023 excluded:** the 2023 figures were about 3x higher than every other year (for example Tamil Nadu: about 200,000 cases in 2023 against 45,000-68,000 in other years). The cause is unclear, so 2023 is left out of the dashboard.
- **Severity** is deaths per 100 recorded accidents. States with under 10,000 recorded cases are hidden because small counts gave unreliable ratios (for example, Mizoram had more deaths than recorded accidents).

## How to run
1. Install: `pip install pandas sqlalchemy psycopg2-binary`
2. Create a PostgreSQL database named `road_accidents`.
3. Run `python etl.py` and enter your port and password when asked. No password is stored in the code.

## Files
- `etl.py`: the ETL script
- `accidents.csv`: original data
- `accidents_clean.csv`: cleaned data
- `accidents_road.csv`: road accidents only, 2023 removed (used in Tableau)
