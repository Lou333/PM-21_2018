gueltige_nukleotide = ['A', 'T', 'G', 'C', 'a', 't', 'g', 'c']

# Molekulargewichte in mg/mol
# Nukleotidmonophosphate ohne 3'-OH-Gruppe
mw_a = 313210
mw_t = 304200
mw_g = 329210
mw_c = 289180
# freie OH-Gruppe am 3'-Ende eines DNA-Fragments
mw_oh = 17010


def hole_dna_sequenz():
    """Liefere eine vom Nutzer erfragte und validierte DNA-Sequenz.

    Um gültig zu sein, darf die Sequenz nur aus den Buchstaben
    A, G, T, C, a, g, t, c bestehen.
    """
    # Hinweis: Verwende eine while-Schleife, innerhalb derer Du eine
    # Sequenz vom Nutzer erfragst und die Eingabe validierst.
    # Nur wenn die Validierung klappt, brichst Du die Schleife ab
    # und lieferst die Sequenz zurück.
    while True:
        sequence = input('Gib eine DNA-Sequenz ein: ')
        for nucleotid in sequence:
            if nucleotid in gueltige_nukleotide:
                erfolgreiche_validierung = True
            else:
                erfolgreiche_validierung = False
                
        if erfolgreiche_validierung:
            break
        else:
            # Dieser Teil wird ausgeführt wenn die Bedingung hinter if
            # nicht erfüllt war.
            print()
            print(
                'Bei der Eingabe handelt es sich nicht um eine gültige '
                'DNA-Sequenz!'
                )
            print()
            print()
        
    return sequence


seq = hole_dna_sequenz()

Anzahl_G = seq.count('G') + seq.count('g')
Anzahl_A = seq.count('A') + seq.count('a')
Anzahl_T = seq.count('T') + seq.count('t')
Anzahl_C = seq.count('C') + seq.count('c')

print()
print('Eingelesene Sequenz:', seq)
print()
print('Länge:', len(seq))
print()
print('Base', '   ', 'Häufigkeit')
print('G', '      ', Anzahl_G)
print('A', '      ', Anzahl_A)
print('T', '      ', Anzahl_T)
print('C', '      ', Anzahl_C)
print()

GC_Gehalt = (100*(Anzahl_G + Anzahl_C)/(Anzahl_G + Anzahl_A + Anzahl_T + Anzahl_C))

print('% GC-Gehalt:', GC_Gehalt,)
print()
Molgewicht = 0.001*(Anzahl_G * mw_g + Anzahl_A * mw_a + Anzahl_T * mw_t + Anzahl_C * mw_c + mw_oh)

print('Molekulargewicht:', Molgewicht, 'g/mol')


