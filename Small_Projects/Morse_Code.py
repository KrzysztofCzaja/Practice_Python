import winsound
import time


class MorseCode:
    character_encoding = {
        'A': '10111',
        'B': '111010101',
        'C': '11101011101',
        'D': '1110101',
        'E': '1',
        'F': '101011101',
        'G': '111011101',
        'H': '1010101',
        'I': '101',
        'J': '1011101110111',
        'K': '111010111',
        'L': '101110101',
        'M': '1110111',
        'N': '11101',
        'O': '11101110111',
        'P': '10111011101',
        'Q': '1110111010111',
        'R': '1011101',
        'S': '10101',
        'T': '111',
        'U': '1010111',
        'V': '101010111',
        'W': '101110111',
        'X': '11101010111',
        'Y': '1110101110111',
        'Z': '11101110101',
        'SPACE': '0000',
        'LETTER_SPACE': '000'
    }

    character_decoding = {
        '10111': 'A',
        '111010101': 'B',
        '11101011101': 'C',
        '1110101': 'D',
        '1': 'E',
        '101011101': 'F',
        '111011101': 'G',
        '1010101': 'H',
        '101': 'I',
        '1011101110111': 'J',
        '111010111': 'K',
        '101110101': 'L',
        '1110111': 'M',
        '11101': 'N',
        '11101110111': 'O',
        '10111011101': 'P',
        '1110111010111': 'Q',
        '1011101': 'R',
        '10101': 'S',
        '111': 'T',
        '1010111': 'U',
        '101010111': 'V',
        '101110111': 'W',
        '11101010111': 'X',
        '1110101110111': 'Y',
        '11101110101': 'Z',
    }
    character_dash_dots = {
        '1': '.',
        '111': '-',
        '0000000': '/',
        '000': '|'
    }

    def __init__(self, message):
        self.message = message.upper()

    def encode(self):
        encoded_message = ""
        try:
            for letter in self.message:
                if letter.isspace():
                    encoded_message += self.character_encoding['SPACE']
                    continue
                encoded_message += self.character_encoding[letter]
                encoded_message += self.character_encoding['LETTER_SPACE']

            return encoded_message[:-3]
        except KeyError:
            return "Unallowed characters!"

    def binary_to_dash_dots(self, message):
        try:
            dash_dot_message = ""

            temp_no_space = message.split(self.character_encoding['SPACE'] + self.character_encoding['LETTER_SPACE'])
            for morse_words in temp_no_space:
                morse_words = morse_words.split(self.character_encoding['LETTER_SPACE'])
                for morse_letter in morse_words:
                    morse_letter = morse_letter.split('0')
                    for morse_unit in morse_letter:
                        dash_dot_message += self.character_dash_dots[morse_unit]
                    dash_dot_message += self.character_dash_dots['000']
                dash_dot_message += "/"
            dash_dot_message = dash_dot_message.replace('|/', '/')

            return dash_dot_message
        except KeyError:
            return "Unallowed characters!"

    def decode(self):
        decoded_message = ""
        try:
            temp_nospace = self.message.split(self.character_encoding['SPACE']+self.character_encoding['LETTER_SPACE'])
            for morse_words in temp_nospace:
                morse_words = morse_words.split(self.character_encoding['LETTER_SPACE'])
                for morse_letter in morse_words:
                    decoded_message += self.character_decoding[morse_letter]
                decoded_message += " "

            return decoded_message
        except KeyError:
            return "Unallowed characters!"

    def morse_code_sound(self, encoded=True, frequency=800, duration=100, binary=False):
        if encoded is False:
            message = self.encode()
        else:
            message = self.message

        if binary is True:
            for morse_unit in message:
                print(morse_unit)
                if morse_unit == '1':
                    winsound.Beep(frequency, duration)
                else:
                    time.sleep(duration/1000)
        else:
            message = self.binary_to_dash_dots(message)
            for morse_unit in message:
                print(morse_unit)
                if morse_unit == '.':
                    winsound.Beep(frequency, duration)
                    time.sleep(duration/1000)
                elif morse_unit == '-':
                    winsound.Beep(frequency, 3*duration)
                    time.sleep(duration / 1000)
                elif morse_unit == '|':
                    time.sleep(3*duration / 1000)
                else:
                    time.sleep(7*duration/1000)


binary_ABspaceC = "10111000111010101000000011101011101"
message = "AB C"
code = MorseCode(message)

# print(code.decode())
# print(code.encode())
code.morse_code_sound(encoded=False)