import os

produtos = {'Lapis':'R$0,99','Caneta':'R$1,20','Caderno':'R$8,99','Calculadora':'R$19,99'}
carrinho = []

def exibir_titulo():
    print('***Papelaria da Julia***')
    print('Bem-vindo à papelaria da Julia, como podemos ajudar?')
    print(' 1-Comprar produtos\n','2-Verificar carrinho\n','3-Finalizar compra\n','4-Sair do programa\n')

def escolher_opcoes():
    opcao_escolhida = int(input('O que deseja fazer?: '))
    try:
        if opcao_escolhida == 1:
            comprar_produtos()
        elif opcao_escolhida == 2:
            verificar_carrinho()
        elif opcao_escolhida == 3:
            finalizar_compra()
        elif opcao_escolhida == 4:
            print('Sistema finalizado')
        else:
            opcao_invalida()
    except:
        opcao_invalida()         

def comprar_produtos():
    print('Obrigado por escolher a nossa loja! Aqui estão nossas opções: ')
    print(produtos, '\n')
    
    comprando = int(input('O que deseja fazer?\n (1)- Adicionar itens ao carrinho\n (2)- Voltar ao menu principal\n'))
    if comprando == 1:
        comprando_itens()
    elif comprando == 2:
        print('Voltando ao menu principal')
        voltar_menu()
    else:
        print('Opção inválida')
        comprar_produtos()

def verificar_carrinho():
    print('Verificando carrinho')
    print(carrinho)

    opcao_carrinho = int(input('O que gostaria de fazer?\n (1)-Excluir item\n (2)-Limpar carrinho\n (3)-Voltar ao menu principal\n'))
    if opcao_carrinho == 1:
        exclui_produto()
    elif opcao_carrinho == 2:
        limpar_carrinho()
    elif opcao_carrinho == 3:
        voltar_menu()
    else:
        print('Opção Inválida')
        verificar_carrinho()

def finalizar_compra():
    print('Finalizando compra! Deseja continuar?')
    opcao_finalizar= int(input('(1)-Sim, finalize minha compra\n(2)-Não, quero continuar comprando: '))
    if opcao_finalizar == 1:
        for i in carrinho:
         if i in produtos:
               print(i, produtos[i].split('R$')[1])
    else:
        voltar_menu()


    valor_total = []
    for i in carrinho:
         if i in produtos:
            valor_total.append(produtos[i].split('R$')[1])
    
    print(valor_total)
    valores = []
    for val in valor_total:
        valores.append(float(val))
    print(valores)
    pass


    #exibir valor dos produtos
    #calcular frete
    #exibir valor total
    #solicitar metodo de pagamento e confirmar pagamento
    #limpar carrinho quando finalizado

def voltar_menu():
    os.system('cls')
    print('Voltando ao menu')
    main()

def exclui_produto():
    produto_excluido = (input('Qual produto gostaria de retirar?')).title()
    if produto_excluido in carrinho:
        carrinho.remove(produto_excluido)
        print('Produto removido com êxito!')
        verificar_carrinho()
    else:
        print('Produto inexistente no carrinho!')
        verificar_carrinho()

def limpar_carrinho():
    limpar_carrinho = (input('Confirma limpar carrinho? Y/N')).upper()
    if limpar_carrinho == Y:
        carrinho = []
        print('Carrinho limpo com sucesso!\n')
        verificar_carrinho()
    elif limpar_carrinho == N:
        print('Voltando ao menu\n')
        verificar_carrinho()
    else:
        print('Opção inválida\n')
        verificar_carrinho()

def comprando_itens():
    item_escolhido = input('Qual item deseja comprar?: ').title()
    if item_escolhido in produtos:
        confirmacao = int(input(f'Confirma adição de {item_escolhido} no carrinho? 1 - Sim / 2 - Não: '))
        if confirmacao == 1:
            carrinho.append(item_escolhido)
            print('Item adicionado ao carrinho com êxito!\n')
            comprar_produtos()
        elif confirmacao == 2:
            print('Retornando ao menu de compras\n')
            comprar_produtos()
        else:
            print('Opção inválida, retornando ao menu de compras\n')
            comprar_produtos()
    else:
        print('Item inexistente!\n')
        comprar_produtos()

def opcao_invalida():
    print('Opção Inválida')
    verificar_carrinho()

def main():
    exibir_titulo()
    escolher_opcoes()

main()