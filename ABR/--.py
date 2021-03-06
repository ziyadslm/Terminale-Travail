from visualisation_arbre import *

class ABR:
    def __init__(self, valeur, gauche, droit):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
    
    def get_data(self):
        return self.valeur
    
    def get_SAG(self):
        return self.gauche
    
    def get_SAD(self):
        return self.droit
    
    def set_SAG(self, arbre):
        self.gauche = arbre
    
    def set_SAD(self, arbre):
        self.droit = arbre
        
    def __repr__(self):
        chaine = ''
        for val in parcours_infixe(self):
            chaine += str(val) + ' ' 
        return chaine

def est_vide(abr):
    return abr is None      
    
def parcours_infixe(arbre):
    def parcours_infixe2(arbre, liste):
        if est_vide(arbre):
            liste = []
            return

        gauche = arbre.get_SAG()
        if not(est_vide(gauche)):
            parcours_infixe2(gauche, liste)

        liste.append(arbre.get_data())

        droit = arbre.get_SAD()    
        if not(est_vide(droit)):
            parcours_infixe2(droit, liste)
    
    l = []
    parcours_infixe2(arbre, l)
    return l

#2
##get_data : 
##get_SAG : recupérer tout larbre gauche de l ABR
##get_SAD : recupérer tout larbre droit de l ABR
##set_SAG : modifier larbre gauche de lABR
##set_SAD : modifier larbre droit de lABR

#3
A = ABR(1,None,None)
show_tree(A)