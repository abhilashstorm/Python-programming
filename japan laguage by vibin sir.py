japan={
    'a':'ka',
    'b':'tu',
    'c':'mi',
    'd':'te',
    'e':'ku',
    'f':'lu',
    'g':'ji',
    'h':'ri',
    'i':'ki',
    'j':'zu',
    'k':'me',
    'l':'ta',
    'm':'rin',
    'n':'to',
    'o':'mo',
    'p':'no',
    'q':'ke',
    'r':'shi',
    's':'ari',
    't':'chi',
    'u':'do',
    'v':'ru',
    'w':'mei',
    'x':'na',
    'y':'fu',
    'z':'zi'
}
def conversion():
   string=input("\nenter: ")
   for letters in string:
       print(japan.get(letters," "),end ="")
   conversion()
conversion()