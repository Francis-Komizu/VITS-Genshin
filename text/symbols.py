""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''
_pad        = '_'
_punctuation = '；：，。！？-“”《》、（）…—~ '
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
_numbers = '01234567890'

# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_numbers)

# Special symbol ids
SPACE_ID = symbols.index(" ")
