# Passo 1 - Coleta e validação dos dados do usuário

nome = input("Digite seu nome completo: ")


print("\n=== VALIDAÇÃO DE DADOS ===")

# Valida se o nome tem pelo menos 3 caracteres e contém espaço (nome e sobrenome)

if len(nome) < 3:
    print("✗ Nome inválido: deve ter pelo menos 3 caracteres.") # Validação de caracteristicas do nome.
elif " " not in nome:
    print("✗ Nome inválido: digite seu nome completo (nome e sobrenome).")
else:
    print("✓ Nome válido (contém nome e sobrenome)")

    # Valida se a idade está entre 0 e 120 anos

    idade = int(input("Digite sua idade: "))

    if idade < 0 or idade > 120: #Validação de idade, aonde o sistema calcula uma idade valida entre 0 a 120 anos.
        print("✗ Idade inválida: deve estar entre 0 e 120 anos.")
    else:
        print("✓ Idade válida")

         # Valida se o mês está entre 1 e 12

        mes = int(input("Digite seu mês de nascimento (1-12): ")) # Validação de mês, sistema deve validar os meses entre 1 e 12

        if mes < 1 or mes > 12:
            print("✗ Mês inválido: deve estar entre 1 e 12.")
        else:
            print("✓ Mês válido (entre 1 e 12)")

            numero = int(input("Digite um número aleatório: "))

# Calcula quantos dias o usuário já viveu (365 dias por ano)
dias_vividos = idade * 365

#Menssagem de boas vidas para o usuario

print(f"""
=== BEM-VINDO ===
Olá, {nome}!
Você tem {idade} anos e seu número aleatório é {numero}.
""")

#Condição para verificar idade impar ou par

if idade % 2 == 0:
    print(f"A sua idade ({idade}) é par.")
else:
    print(f"A sua idade ({idade}) é ímpar.")

    #Classificação de idade do usuário
    #- 0-12: Criança
    #13-17: Adolescente
    # 18-59: Adulto
    #60+: Idoso

if idade <= 12:
    classificacao = "Criança"
    mensagem = "Aproveite sua infância!"
elif idade <= 17:
    classificacao = "Adolescente"
    mensagem = "Fase de descobertas!"
elif idade <= 59:
    classificacao = "Adulto"
    mensagem = "Responsabilidades e conquistas!"
else:
    classificacao = "Idoso"
    mensagem = "Sabedoria e experiência!"

#Classificação da categoria do numero aleatório

print(f"Classificação: {classificacao}") 
print(f"Mensagem: {mensagem}")

if numero < 10:
            categoria_numero = "Muito pequeno"
elif numero <= 50:
            categoria_numero = "Pequeno"
elif numero <= 100:
            categoria_numero = "Médio"
else:
            categoria_numero = "Grande"
print(f"""
=== CLASSIFICAÇÃO DO NÚMERO ===
Seu número aleatório ({numero}) é: {categoria_numero}""")

# Verificação de maioridade
print("\n=== VERIFICAÇÃO DE MAIORIDADE ===")
if idade >= 18:
    print("✓ Você é maior de idade! Suas permissões:")
    print("  - Pode votar")
    print("  - Pode dirigir")
    print("  - Pode assinar contratos")
else:
    print("✗ Você é menor de idade. Permissões restritas:")
    print("  - Não pode votar")
    print("  - Não pode dirigir")
    print("  - Não pode assinar contratos")


#Calculo de ano de nascimento
ano_nascimento = 2026 - idade

# Cálculo do próximo aniversário
mes_atual = 4
if mes == mes_atual:
    mensagem_aniversario = "Parabéns, é seu aniversário!"
elif mes > mes_atual:
    meses_faltando = mes - mes_atual
    if meses_faltando == 1:
        mensagem_aniversario = "Falta 1 mês para seu aniversário!"
    else:
        mensagem_aniversario = f"Faltam {meses_faltando} meses para seu aniversário!"
else:
    meses_faltando = 12 - mes_atual + mes
    if meses_faltando == 1:
        mensagem_aniversario = "Falta 1 mês para seu aniversário!"
    else:
        mensagem_aniversario = f"Faltam {meses_faltando} meses para seu aniversário!"

print(f"""
=== PRÓXIMO ANIVERSÁRIO ===
{mensagem_aniversario}""")

# Estação do ano de nascimento (hemisfério sul)
if mes in [12, 1, 2]:
    estacao = "Verão"
elif mes in [3, 4, 5]:
    estacao = "Outono"
elif mes in [6, 7, 8]:
    estacao = "Inverno"
else:
    estacao = "Primavera"

print(f"""
=== ESTAÇÃO DE NASCIMENTO ===
Você nasceu no: {estacao}""")

import os

# Limpa a tela
os.system('cls' if os.name == 'nt' else 'clear')

# Meses por extenso
meses_extenso = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}

# Paridade da idade
paridade_idade = "par" if idade % 2 == 0 else "ímpar"

# Paridade e sinal do número
paridade_numero = "par" if numero % 2 == 0 else "ímpar"
sinal_numero = "positivo" if numero > 0 else "negativo" if numero < 0 else "zero"

# Status de maioridade
status = "Maior de idade" if idade >= 18 else "Menor de idade"

# Próximo aniversário
if mes == mes_atual:
    aniversario_texto = "é esse mês!"
elif meses_faltando == 1:
    aniversario_texto = "em 1 mês"
else:
    aniversario_texto = f"em {meses_faltando} meses"

print("========================================")
print("           RESUMO COMPLETO              ")
print("========================================")
print(f"Nome:               {nome}")
print(f"Idade:              {idade} anos ({paridade_idade})")
print(f"Nascimento:         {meses_extenso[mes]} de {ano_nascimento} ({estacao})")
print(f"Classificação:      {classificacao}")
print(f"Dias vividos:       ~{dias_vividos} dias")
print(f"Número aleatório:   {numero} ({paridade_numero}, {sinal_numero}, {categoria_numero.lower()})")
print(f"Status:             {status}")
print(f"Próximo aniversário:{aniversario_texto}")
print("========================================")

print(f"""
=== INFORMAÇÕES ADICIONAIS ===
Você nasceu aproximadamente em: {ano_nascimento}
Você já viveu aproximadamente {dias_vividos} dias!
""")

