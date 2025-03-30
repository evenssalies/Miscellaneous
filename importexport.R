# install.packages("foreign")
# install.packages("xlsx")
# install.packages("readstata13")

# Importer

#	.RData
file("C:/Users/evens/Documents/Synth/data/synth.data.RData")
load("C:/Users/evens/Documents/Synth/data/synth.data.RData")
View(synth.data)

#	.raw
DATA <- read.table(file = "http://www.evens-salies.com/KIELMC.raw", header = FALSE)
View(DATA)

# 	.csv
DATA <- read.csv2("http://www.evens-salies.com/electric.company.csv")
View(DATA)

#	.xlsx
# Installer Java : https://java.com/en/download/manual.jsp
# Mettre le fichier "cardkrueger1994_short.xlsx" dans votre PC, et modifier le
#  chemin ci-dessous
library(xlsx)
DATA <- read.xlsx("C:/Users/evens/Documents/cardkrueger1994_short.xlsx", "Feuil2")
View(DATA)

# 	.dta (Stata 5 à 12)
library(foreign)
STAR <- read.dta("http://www.evens-salies.com/webstar.dta")
View(STAR)

# 	.dta (Stata 13 à ?)
library(readstata13)
STAR <- read.dta13("http://www.evens-salies.com/rd_e_gerdfund.dta")
STAR = STAR[order(STAR$PAYSCODE, STAR$YEAR),]
View(STAR)

# Epurer, fusionner, etc.

# Exporter 
#	.dta  
DATA <- read.table(file = "http://www.evens-salies.com/KIELMC.raw", header = FALSE)
str(DATA)
View(DATA)
write.dta(DATA, file = "C:/Users/evens/Documents/kielmc_temp.dta")


