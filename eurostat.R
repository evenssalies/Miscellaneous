#	Package: eurostat
# 		
#		Merci à Gaston Aurélien,
#		M1 EADE, Université Côte d'Azur, promotion 2021-2022

#	Installer le package si ce n'est pas déjà fait
install.packages("eurostat")
library(eurostat)

#	Recherche de données dans le pattern environment
BASE <- search_eurostat(pattern="environment",type="table", fixed=FALSE)

#	Garde la variable id ten00135
#		Choix des pays à étudier et chargement de la base de données
PAYS <- c("DE","ES","FR","IT")
DATA <- get_eurostat(id="ten00135",filter=list(geo=PAYS,unit="MIO_EUR"))

#	On enlève les lignes avec NA
DATA=DATA[complete.cases(DATA),]

#	On garde les trois variables clés
DATA=DATA[4:6]

#	Jette un oeil
View(DATA)
