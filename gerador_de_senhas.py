import random
import string
import pyperclip
import argparse

def gerar_senha(tamanho=12, maiusculas=True, minusculas=True, numeros=True, simbolos=True, evitar_ambiguos=True):
    caracteres = ""
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation
    
    # Remover caracteres ambíguos
    if evitar_ambiguos:
        ambiguos = "O0Il1"
        caracteres = ''.join(c for c in caracteres if c not in ambiguos)
    
    if not caracteres:
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado.")
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    
    # Copiar para área de transferência
    pyperclip.copy(senha)
    
    return senha

def salvar_senha(senha, arquivo="senhas.txt"):
    with open(arquivo, "a") as f:
        f.write(senha + "\n")
    print(f"Senha salva em {arquivo}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerador de senhas seguras.")
    parser.add_argument("-t", "--tamanho", type=int, default=12, help="Tamanho da senha (padrão: 12)")
    parser.add_argument("--sem-maiusculas", action="store_false", help="Excluir letras maiúsculas")
    parser.add_argument("--sem-minusculas", action="store_false", help="Excluir letras minúsculas")
    parser.add_argument("--sem-numeros", action="store_false", help="Excluir números")
    parser.add_argument("--sem-simbolos", action="store_false", help="Excluir símbolos")
    parser.add_argument("--salvar", action="store_true", help="Salvar senha gerada em um arquivo")
    
    args = parser.parse_args()
    senha = gerar_senha(tamanho=args.tamanho, 
                        maiusculas=args.sem_maiusculas, 
                        minusculas=args.sem_minusculas, 
                        numeros=args.sem_numeros, 
                        simbolos=args.sem_simbolos)
    
    print(f"Senha gerada: {senha} (copiada para a área de transferência)")
    
    if args.salvar:
        salvar_senha(senha)