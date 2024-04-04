import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f"\n{nome}, para se vestir adequadamente para uma entrevista, deve usar: Roupas formais, cores neutras, evite muitos acessórios. Boa sorte!\n")
    elif resposta == '2':
        print(f"\n{nome}, para conhecer mais sobre a empresa, faça pesquisas em: Website da empresa, redes sociais, Glassdoor e outros sites de avaliação. Espero ter ajudado!\n")
    elif resposta == '3':
        print(f"\n{nome}, você pode fazer diversos tipos de perguntas para demonstrar interesse, alguns exemplos: Pergunte sobre a empresa, equipe, ambiente de trabalho e sobre feedbacks. Você vai arrasar!\n")
    elif resposta == '4':
        print(f"\n{nome}, você pode perguntar sobre salários e benefícios após ter sido oferecido o cargo, geralmente durante as negociações finais.\n")
    elif resposta == '5':
        print(f"\n{nome}, envie um e-mail de agradecimento logo após a entrevista.\n")
    else:
        print("Digite apenas 1, 2, 3, 4 ou 5!")

def start():
    # Apresentar o chatbot
    print('Olá! Bem-vindo ao EntrevistaPro!')
    # Pedir o nome
    nome = input('Digite seu nome:')
    # Pedir o e-mail
    email = input('Digite seu e-mail:')
    while True:
        # Oferecer o menu de opções
        resposta = input(f'O que gostaria de saber para a sua entrevista, {nome}? Escolha uma opção:\n[1]- Como me vestir adequadamente para entrevista?\n[2]- Como conhecer mais a empresa da qual farei entrevista?\n[3]- Qual tipo de pergunta posso fazer em uma entrevista?\n[4]- Quando devo perguntar sobre salários e benefícios?\n[5]- Qual é o processo de acompanhamento após a entrevista?\n')
    
        # Processar a resposta enviada
        processar_resposta(resposta, nome)

        # Solicitar se o usuário deseja continuar
        continuar = input('Deseja fazer mais alguma pergunta? (s/n): ')
        if continuar.lower() != 's':
            break

    print("Fico muito feliz em ter ajudado, boa sorte na sua entrevista!")

if __name__ == '__main__':
    start()

