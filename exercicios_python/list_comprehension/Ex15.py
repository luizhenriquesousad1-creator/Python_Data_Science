#Ex 15
from prompt_toolkit.key_binding.bindings.named_commands import capitalize_word

nomes = ["ana","joao","maria"]

maiusculas = [n.capitalize() for n in nomes]

print(maiusculas)