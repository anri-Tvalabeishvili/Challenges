SELECT SUM(CITY.POPULATION) FROM CITY
WHERE CITY.COUNTRYCODE IN (SELECT COUNTRY.CODE FROM COUNTRY WHERE COUNTRY.CONTINENT = "Asia");

-- OR

SELECT SUM(CITY.POPULATION) FROM CITY,COUNTRY
WHERE COUNTRY.CONTINENT = "Asia" AND CITY.COUNTRYCODE = COUNTRY.CODE;