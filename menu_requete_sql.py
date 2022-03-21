class Menu:
    
    liste_menu = [
        "Lister les tous les agences",
        "Lister tous les caissiers par ordre croissant de leur nom",
        "Lister tous chef d'agence ainsi que l'addresse de l'agence",
        "Lister les comptes de transaction de l'agence Plateau par ordre croissant du solde",
        "Lister la somme des montants déposés par un caissier dans un compte de transaction de l'agence dont le chef est moussa dop par ordre croissant du montant",
        "Lister les utilisateurs de l'agence Plateau",
        "Lister le nombre de compte par agence",
        "Lister les comptes affectés à l'utilisateur DUERDIN durant le mois de Mai 2021",
        "Lister les utilisateurs à qui on a affecté le compte numéro 001 durant année 2021"
    ]
    
    requetes_sql_correspondants = {
        "Lister les tous les agences": "SELECT * FROM AGENCE",
        "Lister tous les caissiers par ordre croissant de leur nom": "SELECT u.nom_USER FROM PROFIL p, USERS u WHERE p.libelle_PROFIL = 'caissier'",
        "Lister tous chef d'agence ainsi que l'addresse de l'agence": "SELECT nom_USER FROM USERS, AGENCE, PROFIL WHERE libelle_PROFIL LIKE '%chef agence%' AND id_USER = id_USER_USER;",
        "Lister les comptes de transaction de l'agence Plateau par ordre croissant du solde": "SELECT DISTINCT numero, solde_COMPTE_TRANSACTION, adresse_AGENCE FROM COMPTE_TRANSACTION, AGENCE, TRANSACTIONS WHERE numero_AGENCE_AGENCE AND adresse_AGENCE like '%American%' ORDER BY solde_COMPTE_TRANSACTION;",
        #"Lister la somme des montants déposés par un caissier dans un compte de transaction de l'agence dont le chef est moussa dop par ordre croissant du montant": """
        #"""
}
