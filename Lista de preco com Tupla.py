objetos = 'lâmpada', 'caneta', 'celular', 'notebook',\
          'ventilador', 'televisão', 'janela', 'violão', 'cama'
preços = 1.00, 0.80, 2199.99, 3499.99, 359.99,\
        4199.90, 400.00, 1999.00, 2700.00
quantidade = 2, 3, 1, 1, 2, 1, 3, 1, 2

print('=' * 53)
print(f'{"> TABELA DE PREÇO E QUANTIDADE <":-^52}')
print('=' * 53)
print(f'\tITENS {"PREÇO":>19} {"QUANTIDADE":>20}')
print('=' * 53)

índice = 0
for posição, obj in enumerate(objetos):  #Imprimindo os itens e valores da tupla
    print(f'{posição + 1}º {obj.capitalize():<20} R${preços[índice]:<20.2f}'
          f' {quantidade[índice]}')
    índice += 1
    print('-' * 53)

TotalQ = TotalP = 0  #Total de quantidade; Total de preço
for soma in quantidade:
    TotalQ = TotalQ + soma  #Somando quantidade
for soma in preços:
    TotalP = TotalP + soma  #Somando os gastos

print(f'\t{"TOTAL:":<19} R${TotalP:<21.2f}{TotalQ}')  #Mostrar o total
print('=' * 53)
