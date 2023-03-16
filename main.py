import re
import os

# Pergunta ao usuário qual é o separador
separador = input("Qual é o separador que você gostaria de usar? (Pressione enter se não quiser usar nenhum) ")

# Lê o arquivo "input.txt" e separa as palavras-chave com base no separador fornecido
with open('input.txt', 'r') as f:
    # lê o conteúdo do arquivo em uma string
    conteudo_arquivo = f.read().strip()

    # verifica se o conteúdo do arquivo não é vazio
    if conteudo_arquivo:
        # divide as palavras-chave com base no separador fornecido
        palavras_chave = re.split(f'[{separador}]', conteudo_arquivo)
    else:
        # se o conteúdo do arquivo for vazio, define a lista de palavras-chave como vazia
        palavras_chave = []

    # Remove espaços em branco e linhas vazias da lista de palavras-chave
    palavras_chave = [palavra.strip() for palavra in palavras_chave if palavra.strip()]

    # Verifica se existem palavras-chave para processar
    if not palavras_chave:
        print("Nenhuma palavra-chave foi encontrada no arquivo 'input.txt'. O programa será encerrado.")
        exit()

    # Pergunta ao usuário qual tipo de correspondência deseja utilizar
    print("Selecione um tipo de correspondência:")
    print("1 - Correspondência Ampliada")
    print("2 - Correspondência Ampliada Modificada")
    print("3 - Correspondência de Frase")
    print("4 - Correspondência Exata")
    print("5 - Ver explicação dos tipos de correspondência e link para leitura mais detalhada")

    opcao_correspondencia = input("Opção selecionada: ")

    # Verifica qual tipo de correspondência foi selecionado
    if opcao_correspondencia == "1":
        padrao_correspondencia = "+"
    elif opcao_correspondencia == "2":
        padrao_correspondencia = re.compile(r'(?<=\S)\+(?=\S)')
    elif opcao_correspondencia == "3":
        padrao_correspondencia = '"{}"'
    elif opcao_correspondencia == "4":
        padrao_correspondencia = "[{}]".format(''.join([re.escape(c) for c in palavras_chave]))
    elif opcao_correspondencia == "5":
        print("Os tipos de correspondência disponíveis são:")
        print(
            "1. Correspondência ampla (Broad Match): A palavra-chave pode aparecer em qualquer ordem e pode incluir palavras relacionadas.")
        print(
            "2. Correspondência ampla modificada (Modified Broad Match): A palavra-chave deve aparecer na pesquisa, mas as palavras relacionadas podem ser inseridas antes ou depois da palavra-chave.")
        print(
            "3. Correspondência de frase (Phrase Match): A palavra-chave deve aparecer exatamente como digitada, mas outras palavras podem aparecer antes ou depois dela.")
        print(
            "4. Correspondência exata (Exact Match): A palavra-chave deve aparecer exatamente como digitada, sem outras palavras.")

        print(
            "\nLeia mais sobre correspondência de palavras-chave do Google Ads em: https://support.google.com/google-ads/answer/7478529?hl=pt-BR")
        exit()
    else:
        print("Opção inválida. O programa será encerrado.")
        exit()

    # Aplica o padrão de correspondência às palavras-chave
    palavras_chave_correspondencia = [padrao_correspondencia.format(palavra) for palavra in palavras_chave]

    # Salva as palavras-chave com o padrão de correspondência desejado no arquivo "output.txt"
    with open('output.txt', 'w') as f:
        f.write("\n".join(palavras_chave_correspondencia))

    print("Palavras-chave salvas com sucesso!")
    os.system("open output.txt")
