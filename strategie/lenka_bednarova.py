def tah_pocitace(pole, symbol):
    if symbol == 'o':
        symbol_protihrac = 'x'
    else:
        symbol_protihrac = 'o'

    if '-' not in pole:
        raise ValueError('Pole je plne.')

    if len(pole) == 0:
        raise ValueError('Pole neni nastaveno.')
    
    if symbol and symbol_protihrac not in pole:
        pocitac_odpoved = int(len(pole)/2)

    elif symbol not in pole:
         pocitac_odpoved = pole.index(symbol_protihrac) + 1

    elif symbol * 2 + '-' in pole:
        pocitac_odpoved = pole.rfind(symbol * 2 + '-') + 2
    
    elif '-' + symbol * 2 in pole:
        pocitac_odpoved = pole.find('-' + symbol * 2 )

    elif symbol_protihrac * 2 + '-' in pole:
        pocitac_odpoved = pole.rfind(symbol_protihrac * 2 + '-') + 2
 
    elif '-' + symbol_protihrac * 2 in pole:
        pocitac_odpoved = pole.find('-' + symbol_protihrac * 2)
    
    elif symbol + '-' + symbol in pole:
        pocitac_odpoved = pole.find(symbol + '-' + symbol) + 1
    
    elif symbol_protihrac + '-' + symbol_protihrac in pole:
        pocitac_odpoved = pole.find(symbol_protihrac + '-' + symbol_protihrac) + 1

    elif symbol + '-' in pole:
        if symbol + '-' in pole[-2:] and symbol + '-' in pole[:-2]:
            pocitac_odpoved = pole[:-2].rfind(symbol + '-') + 1
        else:
            pocitac_odpoved = pole.rfind(symbol + '-') + 1
    
    elif '-' + symbol in pole:
        if '-' + symbol in pole[:2] and '-' + symbol in pole[2:]:
            pocitac_odpoved = pole.find('-' + symbol,2)
        else:
            pocitac_odpoved = pole.find('-' + symbol)  
    
    elif symbol_protihrac + '-' in pole:
        if symbol_protihrac + '-' in pole[-2:] and symbol_protihrac + '-' in pole[:-2]:
            pocitac_odpoved = pole[:-2].rfind(symbol_protihrac + '-') + 1
        else:
            pocitac_odpoved = pole.rfind(symbol_protihrac + '-') + 1

    elif '-' + symbol_protihrac in pole:
        if '-' + symbol_protihrac in pole[:2] and '-' + symbol_protihrac in pole[2:]:
            pocitac_odpoved = pole.find('-' + symbol_protihrac, 2)
        else:
            pocitac_odpoved = pole.find('-' + symbol_protihrac)

    pole = pole[:pocitac_odpoved] + symbol + pole[pocitac_odpoved + 1:]
    return pole
