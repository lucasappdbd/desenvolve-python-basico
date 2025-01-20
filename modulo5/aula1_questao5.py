import emoji

print("Emojis Disponíveis:")
print(((emoji.emojize(':red_heart:'))), "  - :red_heart:")
print(((emoji.emojize(':thumbs_up:'))), " - :thumbs_up:")
print(((emoji.emojize(':thinking_face:'))), " - :thinking_face:")
print(((emoji.emojize(':partying_face:'))), " - :partying_face:")
print()

print("Digite uma frase e ela será emojizada:")
frase = input()
print("Frase emojizada:")
print((emoji.emojize(frase)))