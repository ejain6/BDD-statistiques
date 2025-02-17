import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


Colleges2DF = pd.read_csv("colleges2_stats.csv", delimiter=';')

Colleges2DF = Colleges2DF.dropna()
Colleges2AR = Colleges2DF.to_numpy()

for ligne in Colleges2AR:

    if ligne[1] == "Dans QP         ":
        ligne[1] = 3

    elif ligne[1] == "Dans QP+200m    ":
        ligne[1] = 2

    elif ligne[1] == "Dans QP+200-300m":
        ligne[1] = 1

    # La valeur des QP non renseignés sera de 0 (comme pour Hors QP)
    else:
        ligne[1] = 0


def centrerReduire(arr):
    arr=np.array(arr,dtype=np.float64)

    nv_arr = np.zeros((len(arr),len(arr[1])))
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            nv_arr[i,j] = (arr[i,j] - np.average(arr[:,j])) / np.std(arr[:,j])
    return nv_arr

Colleges2AR_CR = centrerReduire(Colleges2AR)

def DiagBatons(Colonne, nom_col, num_bins=50):
    m = np.min(Colonne)  # m contient la valeur minimale de la colonne
    M = np.max(Colonne)  # M contient la valeur maximale de la colonne
    inter = np.linspace(m, M, num_bins)  # liste de num_bins valeurs allant de m à M

    # Calcul des fréquences pour chaque intervalle
    hist, bins = np.histogram(Colonne, bins=inter)

    plt.figure()
    # Tracé du diagramme pour les intervalles inter
    plt.bar(bins[:-1], hist, width=np.diff(bins), align="edge")
    plt.xlabel(nom_col)
    plt.ylabel('Nombre de collèges')
    plt.title('Statistiques ' + nom_col)
    plt.show()


#Décommenter pour afficher les diagrammes souhaités

#DiagBatons(Colleges2AR[:,0], 'nb de 3ème filles par collège')
#DiagBatons(Colleges2AR[:,1], 'qp a proximité par collège')
#DiagBatons(Colleges2AR[:,2], 'nb de candidats brevet général collège')
#DiagBatons(Colleges2AR[:,3], 'taux de réussite brevet général par collège')
#DiagBatons(Colleges2AR[:,4], 'nb mentions TB au brevet général par collège')
#DiagBatons(Colleges2AR[:,5], 'taux d accès 6è 3è par collège')



MatriceCov = np.cov(Colleges2AR_CR,rowvar=False)


Y = Colleges2AR[:,0]
X = Colleges2AR[:,1:]

Colleges2LR = LinearRegression()
Colleges2LR.fit(X, Y)

coefficients = Colleges2LR.coef_
resultat = Colleges2LR.intercept_

print("Coefficients:", coefficients)
print("Intercept:", resultat)


coef_corr_multiple = Colleges2LR.score(X, Y)
print("CCM: ", coef_corr_multiple)