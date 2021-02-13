from podnuit.jeu import Jeu

if __name__ == "__main__":
    test = Jeu()
    test.setup({"1":"Ben", "2":"Etienne", "3":"Méthieu", "4":"Tony"})
    print(test.get_alive_players())
    for j in test.joueurs.values():
        print(j.get_ident(), j.get_name())
    for killed in ["4", "3"]:
        test.start_round()
        print(test.round_number)
        if "1" in set(test.get_alive_players()): test.vote("1", killed)
        if "2" in set(test.get_alive_players()): test.vote("2", killed)
        if "3" in set(test.get_alive_players()): test.vote("3", killed)
        if "4" in set(test.get_alive_players()): test.vote("4", killed)
        print(test.vote_is_done())
        print(test.get_dead_folk())
        if test.game_is_done():
            v = test.get_victory()
            print(v.message, v.gagnants)
