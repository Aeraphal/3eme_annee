# ProjetJeu

Le principe du jeu : 

Le joueur manipule une entité qui doit se diriger d'un point A à un point B
en esquivant les obstacles se dressant sur son chemin.

Les règles : 

Le joueur peut se déplacer à l'aide des flèches et sauter grâce à la barre espace.
Le joueur ne peux pas quitter la plateforme de départ. 
Le joueur peut sprinter
Des obstacles se déplacent linéairement sur la plateforme mais ne peuvent pas aller au spawn du joueur.

Détails sur le jeu

Le Jeu : 
    Joueur : 
        Entité :
            Déplacement : 
                - Avec les flèches pour un déplacement horizontal sur la plateforme(done). 
                - Avec la barre espace pour sauter.(done mais ameliorable)
            Caméra : 
                - Suit toujours l'utilisateur par derrière.(done)
            Hitbox :
                - Création d'une hitbox qui suit l'utilisateur lors de ses déplacement.

    Environnement :
        Terrain : 
            Sol : 
                - Délimiter le terrain à une certaine surface.
            Mur : 
                - Visibilité de l'interface.
                - Limitation visible du joueur.  (done)
        Plateforme : 
            - Plateforme surélevé qui permet au joueur de se protéger des obstacles.

    Objectifs : 
        Départ :
            - Point de spawn et respawn de l'utilisateur.
            - Un espace délimité protégé des obstacles et des plateformes.
        Arrivée : 
            - Un espace qui termine la partie une fois qu'il est franchit
            
    Obstacles : 
        Entité :
            Déplacement :
                - Déplacement aléatoire depuis sa position initial.
                - Vitesse uniforme tout au long du jeu.
            Hitbox : 
                Collision :
                    Utilisateur :
                        - L'utilisateur meurt et recommence au départ.
                    Obstacle : 
                        - Repart dans une trajectoire perpendiculaire par rapport à l'obstacle ou le mur. 
        Spawn : 
            - Spawn prédéfini par l'application.

    


















