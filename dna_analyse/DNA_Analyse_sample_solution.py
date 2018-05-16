gueltige_nukleotide = ['A', 'T', 'G', 'C']

# Molekulargewichte in mg/mol
# Nukleotidmonophosphate ohne 3'-OH-Gruppe
# freie OH-Gruppe am 3'-Ende eines DNA-Fragments
mol_gewicht = {'a': 313210, 't': 304200, 'g': 329210, 'c': 289180, 'oh': 17010}



def ist_valide_sequenz(seq, alphabet, match_case=False):
    """Prüfe, ob eine Sequenz nur Buchstaben des erlaubten Alphabets enthält.

    Als Alphabet kann als iterierbare Buchstabenfolge beliebigen Typs
    übergeben werden.
    Mit match_case=True muss die Groß-/Kleinschreibung der des Alphabets
    entsprechen.
    """

    if match_case == False:
        # Groß-/Kleinschreibung soll keine Rolle spielen.
        # Deshalb wandeln wir die Sequenz und das Alphabet in Großbuchstaben
        # um. Für das Alphabet ist das am einfachsten, wenn wir es zuerst
        # in einen string verwandeln.
        seq = seq.upper()
        alphabet = ''.join(alphabet).upper()
    for c in seq:
        if c not in alphabet:
            return False
    return True


def hole_dna_sequenz(erlaubte_nukleotide):
    """Liefere eine vom Nutzer erfragte und validierte DNA-Sequenz.

    Um gültig zu sein, darf die Sequenz nur aus den Buchstaben
    aus erlaubte_nukleotide (in Groß- oder Kleinschreibung) bestehen.
    """

    while True:
        sequence = input('Gib eine DNA-Sequenz ein: ')

        if ist_valide_sequenz(sequence, erlaubte_nukleotide):
            return sequence

        # Dieser Teil wird ausgeführt wenn die Bedingung hinter if
        # nicht erfüllt war.
        print()
        print(
            'Bei der Eingabe handelt es sich nicht um eine gültige '
            'DNA-Sequenz!'
            )
        print()
        print()


if __name__ == '__main__':
    # Sequenz einlesen
    # ----------------
    seq = hole_dna_sequenz(gueltige_nukleotide)

    # Berechnungen
    # ------------

    # Sequenzlänge
    seqlen = len(seq)
    # Basenhäufigkeiten
    n_g = 0
    n_a = 0
    n_t = 0
    n_c = 0
    for c in seq.upper():
        if c == 'G':
            n_g += 1
        elif c == 'A':
            n_a += 1
        elif c == 'T':
            n_t += 1
        elif c == 'C':
            n_c += 1
    # GC-Gehalt
    gc_gehalt = 100 * (n_g+n_c) / seqlen
    # Molekulargewicht
    mw_gesamt = n_g * mol_gewicht['g'] + n_a * mol_gewicht['a'] + n_t * mol_gewicht['t'] + n_c*mol_gewicht['c'] + mol_gewicht['oh']  # in mg/mol

    #Komplementaerstrang
    comp_bases = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    comp_dna = []
    for b in seq.upper():
            comp_dna.append(comp_bases[b])

    compdna_string = ''.join(comp_dna)

    #Reversekomplementaerstrang
    string_length = len(compdna_string)
    reversed_string = compdna_string[-1:-(string_length + 1):-1]


    # Ausgabe
    # -------
    print()
    print('Eingelesene Sequenz:', seq)
    print()
    print('Länge:', seqlen)
    print()
    print('Base\tHäufigkeit')
    print('G', n_g, sep='\t')
    print('A', n_a, sep='\t')
    print('T', n_t, sep='\t')
    print('C', n_c, sep='\t')
    print()
    print('% GC-Gehalt:', gc_gehalt)
    print()
    print('Molekulargewicht:', mw_gesamt/1000, 'g/mol')
    print('Die Komplementaersequenz lautet:', compdna_string)
    print('Die reverse Komplementaersequenz lautet:', reversed_string)
