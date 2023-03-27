import os

# Chemin des dossiers à renommer
dossiers = ['Bus', 'Fleche', 'Pieton', 'Virage']
# Nouveau nom de fichier à utiliser
nouveau_nom = 'nouveau_nom_'

# Parcourir chaque dossier
for dossier in dossiers:
    i = 1
    # Parcourir chaque fichier dans le dossier
    for filename in os.listdir(dossier):
        # Vérifier si le fichier est un fichier et non un dossier
        if os.path.isfile(os.path.join(dossier, filename)):
            # Créer le nouveau nom de fichier
            nouveau_nom_fichier = dossier.upper()+'_'+str(i)
            # Renommer le fichier
            os.rename(os.path.join(dossier, filename), os.path.join(dossier, nouveau_nom_fichier))
            i = i + 1