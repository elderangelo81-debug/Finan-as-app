print('=== Meu Organizador Financeiro Diario ===')
ganhos = float(input("Digite o total de ganhos de hoje (R$):"))
total_gastos = 0
quantidade_gastos = int(input("Quantos gastos separados voce teve hoje?"))
print("\n--- digite o valor de cada gasto ---")
for i in range(quantidade_gastos):
    valor_gasto = float(input(f"valor do gasto {i+1} (R$):"))
    total_gastos = total_gastos + valor_gasto
    saldo_final = ganhos - total_gastos
print("\n=== Resumo do dia ===")
print(f"ganhos totais: R${ganhos:.2f}")
print(f"gastos totais: R${total_gastos:.2f}")
if saldo_final > 0:
    print(f"parabens! hoje sobrou R${saldo_final:.2f}.")
elif saldo_final == 0:
    print(f"ficou no zero a zero. voce gastou exatamente o que ganhou.")
else:
    print(f" atençao! voce fechou o dia no vermelho em R${abs(saldo_final):.2f}.")
