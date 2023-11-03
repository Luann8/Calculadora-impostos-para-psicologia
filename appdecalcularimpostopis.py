# Importa as bibliotecas necessárias
import datetime
import os
import sys

# Define as constantes
BASE_TAXA_INSS = 0.11
BASE_TAXA_IRPF = 7.5
ALIQUOTA_IRPF_1 = 7.5
ALIQUOTA_IRPF_2 = 15
ALIQUOTA_IRPF_3 = 22.5
ALIQUOTA_IRPF_4 = 27.5

# Define as funções
def calcular_inss(valor_faturamento):
    return BASE_TAXA_INSS * valor_faturamento

def calcular_irpf(valor_faturamento, dependentes):
    rendimento_liquido = valor_faturamento - calcular_inss(valor_faturamento)
    if rendimento_liquido <= 1903.98:
        return 0
    elif rendimento_liquido <= 2826.65:
        return rendimento_liquido * ALIQUOTA_IRPF_1
    elif rendimento_liquido <= 3751.05:
        return rendimento_liquido * ALIQUOTA_IRPF_2
    elif rendimento_liquido <= 4664.68:
        return rendimento_liquido * ALIQUOTA_IRPF_3
    else:
        return rendimento_liquido * ALIQUOTA_IRPF_4

def calcular_total_impostos(valor_faturamento, dependentes):
    return calcular_inss(valor_faturamento) + calcular_irpf(valor_faturamento, dependentes)

def mostrar_resultados(valor_faturamento, dependentes, valor_inss, valor_irpf, total_impostos):
    print("Valor do faturamento: R$", valor_faturamento)
    print("Valor do INSS: R$", valor_inss)
    print("Valor do IRPF: R$", valor_irpf)
    print("Valor total dos impostos: R$", total_impostos)

def armazenar_informacoes(valor_faturamento, dependentes, valor_inss, valor_irpf, total_impostos):
    data_hora = datetime.datetime.now()
    nome_arquivo = "informacoes_fiscais.txt"
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(f"Data e Hora: {data_hora}\n")
        arquivo.write(f"Valor do faturamento: R$ {valor_faturamento}\n")
        arquivo.write(f"Número de dependentes: {dependentes}\n")
        arquivo.write(f"Valor do INSS: R$ {valor_inss}\n")
        arquivo.write(f"Valor do IRPF: R$ {valor_irpf}\n")
        arquivo.write(f"Valor total dos impostos: R$ {total_impostos}\n")
        arquivo.write("\n")

def verificar_informacoes():
    try:
        nome_arquivo = "informacoes_fiscais.txt"
        with open(nome_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("O arquivo de informações fiscais não existe.")

# Função do menu principal
def menu_principal():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Calcular Impostos")
        print("2. Verificar Informações")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            # Lê o valor do faturamento do usuário
            valor_faturamento = float(input("Informe o valor do faturamento: "))
            # Lê o número de dependentes do usuário
            dependentes = int(input("Informe o número de dependentes: "))
            # Calcula os impostos
            valor_inss = calcular_inss(valor_faturamento)
            valor_irpf = calcular_irpf(valor_faturamento, dependentes)
            total_impostos = calcular_total_impostos(valor_faturamento, dependentes)
            # Exibe os resultados
            mostrar_resultados(valor_faturamento, dependentes, valor_inss, valor_irpf, total_impostos)
            # Pergunta ao usuário se deseja armazenar as informações
            resposta = input("Deseja armazenar as informações em um arquivo? (S/N): ")
            if resposta.upper() == 'S':
                armazenar_informacoes(valor_faturamento, dependentes, valor_inss, valor_irpf, total_impostos)
        elif opcao == "2":
            verificar_informacoes()
        elif opcao == "3":
            sys.exit("Encerrando o programa.")
        else:
            print("Opção inválida. Escolha novamente.")

# Executa o menu principal
menu_principal()
