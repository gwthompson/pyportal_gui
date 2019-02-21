#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18

"""`TG-Modules.TG-RGB.rgb`
a dictionary of bytes organised to create basic text, just the templates
Author(s):Jonah Yolles-Murphy
imspiration for base letter style from Ben Gelb"""
__version__ = "1.0"


text_dict = {
    'Height' : 7,
    'Width' : 5,
    "A" :(0b10111111,
          0b11000100,
          0b11000100,
          0b11000100,
          0b10111111),

    "B" :(0b11111111,
          0b11000001,
          0b11001001,
          0b11001001,
          0b10110110),
    
    "C" :(0b10111110,
          0b11000001,
          0b11000001,
          0b11000001,
          0b10100010),

    "D" :(0b11111111,
          0b11000001,
          0b11000001,
          0b10100010,
          0b10011100),

    "E" :(0b11111111,
          0b11001001,
          0b11001001,
          0b11001001,
          0b11000001),

    "F" :(0b11111111,
          0b11001000,
          0b11001000,
          0b11000000,
          0b11000000),

    "G" :(0b10111110,
          0b11000001,
          0b11001001,
          0b11001001,
          0b10101110),

    "H" :(0b11111111,
          0b10001000,
          0b10001000,
          0b10001000,
          0b11111111),

    "I" :(0b11000001,
          0b11000001,
          0b11111111,
          0b11000001,
          0b11000001),

    "J" :(0b11000110,
          0b11000001,
          0b11111110,
          0b11000000,
          0b11000000),

    "K" :(0b11111111,
          0b10001000,
          0b10001000,
          0b11110100,
          0b10000011),

    "L" :(0b11111111,
          0b10000001,
          0b10000001,
          0b10000001,
          0b10000001),

    "M" :(0b11111111,
          0b10100000,
          0b10010000,
          0b10100000,
          0b11111111),

    "N" :(0b11111111,
          0b10100000,
          0b10011100,
          0b10000010,
          0b11111111),

    "O" :(0b10111110,
          0b11000001,
          0b11000001,
          0b11000001,
          0b10111110),

    "P" :(0b11111111,
          0b11001000,
          0b11001000,
          0b11001000,
          0b10110000),

    "Q" :(0b10111110,
          0b11000001,
          0b11000101,
          0b11000010,
          0b10111101),

    "R" :(0b11111111,
          0b11001000,
          0b11001100,
          0b11001010,
          0b10110001),

    "S" :(0b10110010,
          0b11001001,
          0b11001001,
          0b11001001,
          0b10100110),

    "T" :(0b11000000,
          0b11000000,
          0b11111111,
          0b11000000,
          0b11000000),

    "U" :(0b11111110,
          0b10000001,
          0b10000001,
          0b10000001,
          0b11111110),

    "V" :(0b11110000,
          0b10001110,
          0b10000001,
          0b10001110,
          0b11110000),

    "W" :(0b11111100,
          0b10000011,
          0b10000100,
          0b10000011,
          0b11111100),

    "X" :(0b11100011,
          0b10010100,
          0b10001000,
          0b10010100,
          0b11100011),

    "Y" :(0b11100000,
          0b10010000,
          0b10001111,
          0b10010000,
          0b11100000),

    "Z" :(0b11000011,
          0b11000101,
          0b11001001,
          0b11010001,
          0b11100001),

    "0" :(0b10111110,
          0b11000101,
          0b11001001,
          0b11010001,
          0b10111110),

    "1" :(0b10010001,
          0b10100001,
          0b11111111,
          0b10000001,
          0b10000001),

    "2" :(0b10100001,
          0b11000011,
          0b11000101,
          0b11001001,
          0b10110001),

    "3" :(0b11000110,
          0b11000001,
          0b11010001,
          0b11101001,
          0b11000110),

    "4" :(0b11111000,
          0b10001000,
          0b10001000,
          0b10001000,
          0b11111111),

    "5" :(0b11110010,
          0b11010001,
          0b11010001,
          0b11010001,
          0b11001110),

    "6" :(0b10011110,
          0b10101001,
          0b11001001,
          0b11001001,
          0b10000110),

    "7" :(0b11000000,
          0b11000111,
          0b11001000,
          0b11010000,
          0b11100000),

    "8" :(0b10110110,
          0b11001001,
          0b11001001,
          0b11001001,
          0b10110110),

    "9" :(0b10110000,
          0b11001001,
          0b11001001,
          0b11001010,
          0b10111100),

    
    
    ")" :(0b10000000,
          0b11000001,
          0b10111110,
          0b10000000,
          0b10000000),
    
    "(" :(0b10000000,
          0b10000000,
          0b10111110,
          0b11000001,
          0b10000000),
    
    "[" :(0b10000000,
          0b10000000,
          0b11111111,
          0b11000001,
          0b10000000),
    
    "]" :(0b10000000,
          0b11000001,
          0b11111111,
          0b10000000,
          0b10000000),
    
    "." :(0b10000000,
          0b10000011,
          0b10000011,
          0b10000000,
          0b10000000),
    
    "'" :(0b10000000,
          0b10000000,
          0b10110000,
          0b10000000,
          0b10000000),
    
    ":" :(0b10000000,
          0b10000000,
          0b10110110,
          0b10110110,
          0b10000000),
    
    "__?__" :(0b11111111,
          0b11011111,
          0b11010010,
          0b11000111,
          0b11111111),
    
    "!" :(0b10000000,
          0b11111011,
          0b11111011,
          0b10000000,
          0b10000000),

    "?" :(0b10100000,
          0b11000000,
          0b11000101,
          0b11001000,
          0b10110000),
    
    "," :(0b10000000,
          0b10000101,
          0b10000110,
          0b10000000,
          0b10000000),
    
    ";" :(0b10000000,
          0b10110101,
          0b10110110,
          0b10000000,
          0b10000000),
    
    "/" :(0b10000001,
          0b10000110,
          0b10001000,
          0b10110000,
          0b11000000),
    
    ">" :(0b11000001,
          0b11100011,
          0b10110110,
          0b10011100,
          0b10001000),
    
    "<" :(0b10001000,
          0b10011100,
          0b10110110,
          0b11100011,
          0b11000001),
    
    "%" :(0b11100001,
          0b11100110,
          0b10001000,
          0b10110011,
          0b11000011),
    
    "@" :(0b10100110,
          0b11001001,
          0b11001111,
          0b11000001,
          0b10111110),
    
    "#" :(0b10010100,
          0b11111111,
          0b10010100,
          0b11111111,
          0b10010100),
    
    "$" :(0b10110010,
          0b11001001,
          0b11111111,
          0b11001001,
          0b10100110),
    
    "&" :(0b10110110,
          0b11001001,
          0b11010101,
          0b10100010,
          0b10000101),
    
    "*" :(0b10101000,
          0b10010000,
          0b11111100,
          0b10010000,
          0b10101000),
    
    "-" :(0b10000000,
          0b10001000,
          0b10001000,
          0b10001000,
          0b10000000),
    
    "_" :(0b10000001,
          0b10000001,
          0b10000001,
          0b10000001,
          0b10000001),
    
    "+" :(0b10001000,
          0b10001000,
          0b10111110,
          0b10001000,
          0b10001000),
    
    "=" :(0b10000000,
          0b10010100,
          0b10010100,
          0b10010100,
          0b10000000),
    
    '"' :(0b10000000,
          0b11110000,
          0b10000000,
          0b11110000,
          0b10000000),
    
    "`" :(0b10000000,
          0b10000000,
          0b10100000,
          0b10010000,
          0b10000000),
    
    "~" :(0b10001000,
          0b10010000,
          0b10001000,
          0b10000100,
          0b10001000),
    
    " " :(0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000),
    
    "^" :(0b10010000,
          0b10100000,
          0b11000000,
          0b10100000,
          0b10010000),
    
    "__NONE__" :(),
    
    "BLANK" :(0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000),

    "__BATA0__" :(0b11111111,#1
          0b11000001,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11111111,
          0b10011100,),#11

    "__BATA1__" :(0b11111111,#1
          0b11000001,
          0b11011101,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11111111,
          0b10011100,),#11

    "__BATA2__" :(0b11111111,#1
          0b11000001,
          0b11011101,
          0b11011101,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11111111,
          0b10011100,),#11

    "__BATA3__" :(0b11111111,#1
          0b11000001,
          0b11011101,
          0b11011101,
          0b11011101,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11111111,
          0b10011100,),#11

    "__BATA4__" :(0b11111111,#1
          0b11000001,
          0b11011101,
          0b11011101,
          0b11011101,
          0b11011101,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11111111,
          0b10011100,),#11

    "__BATA5__" :(0b11111111,#1
          0b11000001,
          0b11011101,
          0b11011101,
          0b11011101,
          0b11011101,
          0b11011101,
          0b11000001,
          0b11000001,
          0b11111111,
          0b10011100,),#11

    "__BATA6__" :(0b11111111,#1
          0b11000001,
          0b11011101,
          0b11011101,
          0b11011101,
          0b11011101,
          0b11011101,
          0b11011101,
          0b11000001,
          0b11111111,
          0b10011100,),#11

     "__BATACHRG__" :(0b11111111,#1
          0b11000001,
          0b11001001,
          0b11011001,
          0b11111001,
          0b11001111,
          0b11001101,
          0b11001001,
          0b11000001,
          0b11111111,
          0b10011100,),#11

    "__BATB0__" :(0b11111111,#1
          0b11000001,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11000001,
          0b11111111,
          0b10011100,),#11
    
    
    "__FULL__" :(0b11111111,
          0b11111111,
          0b11111111,
          0b11111111,
          0b11111111),

    "BLANK" :(0b10000000,
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000),

    '''
'''         :(0b10000000, # this is the enter / paragraph character
          0b10000000,
          0b10000000,
          0b10000000,
          0b10000000),
    
    "__DEGREESIGN__" :(0b10011000,
          0b10100100,
          0b10100100,
          0b10011000,
          0b10000000),
    
    }