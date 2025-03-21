#	Package mapdata
#
#		Beautiful code by:
#			Code Allard Natane et Cahuzac Thomas
#			Data: "Covid-19 in Europe – Latest Data" (europe_covid.csv)
#			Source: https://www.kaggle.com/datasets/anandhuh/latest-covid19-data-of-european-countries
#			Original source: WorldOMeters.info

#	Remove all objects from the workspace
rm(list = ls())

#	Get the data
datacovid <- read.csv("europe_covid.csv", sep=",")

library(dplyr)
library(readr)
library(tidyverse)
library(ggplot2)
library(eurostat)

#remove the na
na.omit(datacovid)

#rename variable of countries
datacovid=
  datacovid %>%
  rename(
    geo = Country.Other
  )

#	Creation of a variable with country codes

datacovid$codepays <- character(47)
datacovid$codepays[datacovid$geo == "Albania"] <- "AL"
datacovid$codepays[datacovid$geo == "Andorra"] <- "AD"
datacovid$codepays[datacovid$geo == "Austria"] <- "AT"
datacovid$codepays[datacovid$geo == "Belarus"] <- "BY"
datacovid$codepays[datacovid$geo == "Belgium"] <- "BE"
datacovid$codepays[datacovid$geo == "Bosnia and Herzegovina"] <- "BA"
datacovid$codepays[datacovid$geo == "Bulgaria"] <- "BG"
datacovid$codepays[datacovid$geo == "Channel Islands"] <- "JE"
datacovid$codepays[datacovid$geo == "Croatia"] <- "HR"
datacovid$codepays[datacovid$geo == "Czechia"] <- "CZ"
datacovid$codepays[datacovid$geo == "Denmark"] <- "DK"
datacovid$codepays[datacovid$geo == "Estonia"] <- "EE"
datacovid$codepays[datacovid$geo == "Faeroe Islands"] <- "FO"
datacovid$codepays[datacovid$geo == "Finland"] <- "FI"
datacovid$codepays[datacovid$geo == "France"] <- "FR"
datacovid$codepays[datacovid$geo == "Germany"] <- "DE"
datacovid$codepays[datacovid$geo == "Gibraltar"] <- "GI"
datacovid$codepays[datacovid$geo == "Greece"] <- "EL"
datacovid$codepays[datacovid$geo == "Hungary"] <- "HU"
datacovid$codepays[datacovid$geo == "Iceland"] <- "IS"
datacovid$codepays[datacovid$geo == "Ireland"] <- "IE"
datacovid$codepays[datacovid$geo == "Isle of Man"] <- "IM"
datacovid$codepays[datacovid$geo == "Italy"] <- "IT"
datacovid$codepays[datacovid$geo == "Latvia"] <- "LV"
datacovid$codepays[datacovid$geo == "Liechtenstein"] <- "LI"
datacovid$codepays[datacovid$geo == "Lithuania"] <- "LT"
datacovid$codepays[datacovid$geo == "Luxembourg"] <- "LU"
datacovid$codepays[datacovid$geo == "Malta"] <- "MT"
datacovid$codepays[datacovid$geo == "Moldova"] <- "MD"
datacovid$codepays[datacovid$geo == "Monaco"] <- "MC"
datacovid$codepays[datacovid$geo == "Montenegro"] <- "ME"
datacovid$codepays[datacovid$geo == "Netherlands"] <- "NL"
datacovid$codepays[datacovid$geo == "North Macedonia"] <- "MK"
datacovid$codepays[datacovid$geo == "Norway"] <- "NO"
datacovid$codepays[datacovid$geo == "Poland"] <- "PL"
datacovid$codepays[datacovid$geo == "Portugal"] <- "PT"
datacovid$codepays[datacovid$geo == "Romania"] <- "RO"
datacovid$codepays[datacovid$geo == "Russia"] <- "RU"
datacovid$codepays[datacovid$geo == "San Marino"] <- "SM"
datacovid$codepays[datacovid$geo == "Serbia"] <- "RS"
datacovid$codepays[datacovid$geo == "Slovakia"] <- "SK"
datacovid$codepays[datacovid$geo == "Slovenia"] <- "SI"
datacovid$codepays[datacovid$geo == "Spain"] <- "ES"
datacovid$codepays[datacovid$geo == "Sweden"] <- "SE"
datacovid$codepays[datacovid$geo == "Switzerland"] <- "CH"
datacovid$codepays[datacovid$geo == "UK"] <- "UK"
datacovid$codepays[datacovid$geo == "Ukraine"] <- "UA"

#rename variables
datacovid=
  datacovid %>%
  rename(
    pays = geo
  )

datacovid=
  datacovid %>%
  rename(
    geo = codepays
  )

#map of Total Cases per 1 million of the population

install.packages("giscoR")
library(giscoR) 
install.packages("viridis")
library(viridis)

mapdata = get_eurostat_geospatial(nuts_level = 0)
list_countries = mapdata$geo

datacovid_match =
  datacovid %>%
  filter(geo %in% list_countries)

mapdata_plot = mapdata %>% right_join(datacovid_match, by ='geo')

mapdata_plot %>%
  ggplot() + aes(fill = Tot.Cases..1M.pop)  +
  geom_sf()+
  xlim(c(-23, 35)) + ylim(c(35,70)) +   
  labs(title = "Total number of cases per 1 million of the population",
       fill = "Cases/1M pop") +
 theme_bw() + scale_fill_viridis(option = "rocket", direction = -1) #we changed the colors and the direction of shades with viridis (rocket)


