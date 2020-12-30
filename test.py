from podnuit.jeu import Jeu

if __name__ == "__main__":
    test = Jeu()
    test.setup(["Ben", "Etienne", "Méthieu", "Tony"])
    print(test.get_alive_players())
    for j in test.joueurs.values():
        print(j.get_ident(), j.get_name())
    for killed in ["Tony", "Méthieu"]:
        test.start_round()
        print(test.round_number)
        if "Ben" in set(test.get_alive_players()): test.vote("Ben", killed)
        if "Etienne" in set(test.get_alive_players()): test.vote("Etienne", killed)
        if "Méthieu" in set(test.get_alive_players()): test.vote("Méthieu", killed)
        if "Tony" in set(test.get_alive_players()): test.vote("Tony", killed)
        print(test.vote_is_done())
        print(test.get_dead_folk())
        if test.game_is_done():
            v = test.get_victory()
            print(v.message, v.gagnants)
