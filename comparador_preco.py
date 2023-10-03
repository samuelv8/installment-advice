def calcular_rendimento(investimento_inicial, taxa_anual, meses):
    imposto = 0.225  # Imposto de 22,5% sobre o lucro
    total_bruto = 0.0 + investimento_inicial
    parcela = investimento_inicial / meses

    for _ in range(meses):
        total_bruto = total_bruto * pow((1 + taxa_anual), (1 / 12))
        total_bruto -= parcela

    rendimento_liquido = total_bruto * (1 - imposto)
    return rendimento_liquido

def vale_a_pena_prazo_ou_vista(preco_vista, preco_prazo, taxa_anual, num_parcelas):
    desconto = abs(preco_vista - preco_prazo)
    valor_investido = preco_prazo
    rendimento_liquido = calcular_rendimento(valor_investido, taxa_anual, num_parcelas - 1)

    resposta = f"Vale a pena pagar { 'a prazo' if rendimento_liquido >= desconto else 'à vista' }" \
                f"O rendimento do valor a prazo será de R$ {rendimento_liquido:.2f}, enquanto o desconto é de R$ {desconto:.2f}."
    return resposta

preco_a_vista = float(input("Digite o preço à vista: "))
preco_a_prazo = float(input("Digite o preço à prazo: "))
taxa_anual = float(input("Digite a taxa de juros anual (em %): ")) / 100
num_parcelas = int(input("Digite o número de parcelas: "))

resultado = vale_a_pena_prazo_ou_vista(preco_a_vista, preco_a_prazo, taxa_anual, num_parcelas)
print(resultado)
