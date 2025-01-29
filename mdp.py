import random
import curses
def generate(length:int):
    pwd = ""
    if length == 0:
        length = random.choice(range(7, 15))
    for _ in range(length):
        current = random.choice(range(33, 126))
        pwd += chr(current)
    return pwd

def main(stdscr):
    curses.curs_set(0)  # Masquer le curseur
    stdscr.clear()
    stdscr.refresh()

    while True:
        stdscr.clear()
        stdscr.addstr(2, 2, "🔑 Générateur de mot de passe")
        stdscr.addstr(4, 2, "Entrez la longueur du mot de passe (0 pour aléatoire) :")
        stdscr.refresh()

        # Saisie utilisateur
        curses.echo()
        length_str = stdscr.getstr(5, 2, 10).decode("utf-8")
        curses.noecho()

        try:
            length = int(length_str) if length_str else 0
            password = generate(length)

            stdscr.addstr(7, 2, f"✅ Mot de passe : {password}")
            stdscr.addstr(9, 2, "Appuyez sur une touche pour recommencer, ou 'q' pour quitter.")
            stdscr.refresh()

            key = stdscr.getch()
            if key == ord('q'):
                break

        except ValueError:
            stdscr.addstr(7, 2, "❌ Erreur : Entrez un nombre valide !")
            stdscr.refresh()
            stdscr.getch()  # Attendre une touche avant de continuer

curses.wrapper(main)