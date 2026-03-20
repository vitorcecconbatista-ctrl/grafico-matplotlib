
import matplotlib.pyplot as plt
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
vendas = [200, 300, 340, 305, 300, 400]
plt.plot(meses, vendas)
plt.title('Vendas no Primeiro Semestre')
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.savefig("grafico_linhas.png")