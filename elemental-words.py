# recursive method
def elemental_forms(word):
    res = []
    
    for i in range(len(word)+1):
        symbol = word[0:i].capitalize()
        if symbol in ELEMENTS:
            element = ELEMENTS[symbol]
            if len(symbol) == len(word):
                res.append(["{} ({})".format(element, symbol)])
                return res
            recursive_results = elemental_forms(word[i:])
            for result in recursive_results:
                res.append(["{} ({})".format(element, symbol)]+result)

    return res


# iterative version
def elemental_forms_iterative(word):
    final_result = []
    stack = []
    
    for i in range(len(word)+1)[::-1]:
        symbol = word[i:].capitalize()
        if symbol in ELEMENTS:
            element = ELEMENTS[symbol]
            stack.append(["{}".format(word[0:i]),[["{} ({})".format(element, symbol)]]])

    while stack:
        word, results = stack.pop()
        
        if not word:
            for res in results:
                final_result.append(res)
    
        for i in range(len(word)+1)[::-1]:
            symbol = word[i:].capitalize()
            if symbol in ELEMENTS:
                element = ELEMENTS[symbol]
                new_res = []
                for res in results:
                    new_res.append(["{} ({})".format(element, symbol)]+res)
                stack.append(["{}".format(word[0:i]),new_res])
            
    return final_result


ELEMENTS = {
    'H': 'Hydrogen',
    'He': 'Helium',
    'Li': 'Lithium',
    'Be': 'Beryllium',
    'B': 'Boron',
    'C': 'Carbon',
    'N': 'Nitrogen',
    'O': 'Oxygen',
    'F': 'Fluorine',
    'Ne': 'Neon',
    'Na': 'Sodium',
    'Mg': 'Magnesium',
    'Al': 'Aluminium',
    'Si': 'Silicon',
    'P': 'Phosphorus',
    'S': 'Sulfur',
    'Cl': 'Chlorine',
    'Ar': 'Argon',
    'K': 'Potassium',
    'Ca': 'Calcium',
    'Sc': 'Scandium',
    'Ti': 'Titanium',
    'V': 'Vanadium',
    'Cr': 'Chromium',
    'Mn': 'Manganese',
    'Fe': 'Iron',
    'Co': 'Cobalt',
    'Ni': 'Nickel',
    'Cu': 'Copper',
    'Zn': 'Zinc',
    'Ga': 'Gallium',
    'Ge': 'Germanium',
    'As': 'Arsenic',
    'Se': 'Selenium',
    'Br': 'Bromine',
    'Kr': 'Krypton',
    'Rb': 'Rubidium',
    'Sr': 'Strontium',
    'Y': 'Yttrium',
    'Zr': 'Zirconium',
    'Nb': 'Niobium',
    'Mo': 'Molybdenum',
    'Tc': 'Technetium',
    'Ru': 'Ruthenium',
    'Rh': 'Rhodium',
    'Pd': 'Palladium',
    'Ag': 'Silver',
    'Cd': 'Cadmium',
    'In': 'Indium',
    'Sn': 'Tin',
    'Sb': 'Antimony',
    'Te': 'Tellurium',
    'I': 'Iodine',
    'Xe': 'Xenon',
    'Cs': 'Caesium',
    'Ba': 'Barium',
    'La': 'Lanthanum',
    'Ce': 'Cerium',
    'Pr': 'Praseodymium',
    'Nd': 'Neodymium',
    'Pm': 'Promethium',
    'Sm': 'Samarium',
    'Eu': 'Europium',
    'Gd': 'Gadolinium',
    'Tb': 'Terbium',
    'Dy': 'Dysprosium',
    'Ho': 'Holmium',
    'Er': 'Erbium',
    'Tm': 'Thulium',
    'Yb': 'Ytterbium',
    'Lu': 'Lutetium',
    'Hf': 'Hafnium',
    'Ta': 'Tantalum',
    'W': 'Tungsten',
    'Re': 'Rhenium',
    'Os': 'Osmium',
    'Ir': 'Iridium',
    'Pt': 'Platinum',
    'Au': 'Gold',
    'Hg': 'Mercury',
    'Tl': 'Thallium',
    'Pb': 'Lead',
    'Bi': 'Bismuth',
    'Po': 'Polonium',
    'At': 'Astatine',
    'Rn': 'Radon',
    'Fr': 'Francium',
    'Ra': 'Radium',
    'Ac': 'Actinium',
    'Th': 'Thorium',
    'Pa': 'Protactinium',
    'U': 'Uranium',
    'Np': 'Neptunium',
    'Pu': 'Plutonium',
    'Am': 'Americium',
    'Cm': 'Curium',
    'Bk': 'Berkelium',
    'Cf': 'Californium',
    'Es': 'Einsteinium',
    'Fm': 'Fermium',
    'Md': 'Mendelevium',
    'No': 'Nobelium',
    'Lr': 'Lawrencium',
    'Rf': 'Rutherfordium',
    'Db': 'Dubnium',
    'Sg': 'Seaborgium',
    'Bh': 'Bohrium',
    'Hs': 'Hassium',
    'Mt': 'Meitnerium',
    'Ds': 'Darmstadtium',
    'Rg': 'Roentgenium',
    'Cn': 'Copernicium',
    'Uut':'Ununtrium',   # Nihonium (Nh)
    'Fl':'Flerovium',
    'Uup':'Ununpentium', # Moscovium (Mc)
    'Lv':'Livermorium',
    'Uus':'Ununseptium', # Tennessine (Ts)
    'Uuo':'Ununoctium',  # Oganesson (Og)
}