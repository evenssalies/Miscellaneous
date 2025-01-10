#install.packages("insee")
library(insee)
help(package="insee")

# List of datasets available through a SDMX query
# Check if firm-level variables are available at the sector level; e.g., GFCF. 
# Notes:
#	- sector data names have suffix "BRANCHE"; e.g., CNA-2014-FBCF-BRANCHE
#	- variables' names include base years; e.g., CNA-2020-PIB
get_dataset_list()

# Liste the variables within a group of interest
database <- get_idbank_list("CNA-2020-PIB")
View(database)

# My variable of interest, with filters
data1 <- get_insee_idbank("011779990",
                 startPeriod = 2001,
                 endPeriod = 2020)

# Its values and corresponding years
print(c(data$OBS_VALUE, data$TIME_PERIOD))
