init python:
    def setup(): 
        #     /!\ A CHANGER EN FONCTION DE L'IMAGE /!\                                                         !!!
        #
        #
        start_x = 500 # Début de la zone de placement des pièces en X
        start_y = 500 # Début de la zone de placement des pièces en Y
        end_x = 500 # fin en X
        end_y = 500 # fin en Y
        rand_spots = (renpy.random.randint(start_x, end_x),renpy.random.randint(start_y, end_y)) # randomise les placements des morceaux dans les intervalles donnés
        starting_pieces_coords.append(rand_spots) # ajoute les coordonnées à la liste

    def dropping(slot, piece):
        global correctly_placed

        if piece[0].drag_name==slot.drag_name:
            piece[0].snap(slot.x, slot.y)
            piece[0].draggable=False
            correctly_placed+=1

        if correctly_placed == report_pieces:
            renpy.jump("Fin_du_mini_jeu")


screen completing_puzzle:
    #image "background_autopsie.png" # image de fond du mini jeu
    frame:                          # encadrement où le joueur mettra les pièces du puzzle
        background "puzzle_frame.png"
        xysize report_size
        anchor(0.5,0.5)
        #  /!\ A CHANGER EN FONCTION DE L'IMAGE /!\                                                             !!!
        #
        #
        pos(1000,1000)  

    draggroup:
        for i in range(report_pieces):
            drag:
                drag_name i 
                pos starting_pieces_coords[i]
                anchor(0.5,0.5)
                focus_mask True
                drag_raise True
                image "Pieces/piece-%s.png" %(i+1)

        for i in range(report_pieces):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped dropping
                pos pieces_coords[i]
                anchor(0.5,0.5)
                focus_mask True
                image "Pieces/piece-%s.png" %(i+1) alpha 0.0


default report_pieces = 1 #Nombre de pièces du rapport
default report_size = (800,300) #taille du rapport entier en pixels
default pieces_coords = [(500,500)] # liste de positions correctes de chaque pièce
default starting_pieces_coords = [] #liste de positions de départ de chaque pièce
default correctly_placed = 0 # nombre de pièces correctement placées



define e = Character("Eileen")






label start:
    e "Salut zézuberzeketufé"
    $setup()
    
    call screen completing_puzzle
    return













label Fin_du_mini_jeu :
    e "Bien joué"
    return



















