'''Teste de Shapiro-Wilk'''
from Ciclo_3 import temperatura_biodig, recirculacao, drenagem, producao_biodig, ph_inferior, ph_superior
from scipy import stats

print('\n')
statistic1, p_value1 = stats.shapiro(temperatura_biodig)
print('Estatistica de teste para a primeira variável: ',statistic1)
print('Valor p para a Temperatura do Biodigestor: ',p_value1)
print('\n')

statistic2, p_value2 = stats.shapiro(recirculacao)
print('Estatistica de teste para a primeira variável: ',statistic2)
print('Valor p para a Recirculação: ',p_value2)
print('\n')

statistic3, p_value3 = stats.shapiro(drenagem)
print('Estatistica de teste para a primeira variável: ',statistic3)
print('Valor p para a Drenagem: ',p_value3)
print('\n')

statistic4, p_value4 = stats.shapiro(producao_biodig)
print('Estatistica de teste para a primeira variável: ',statistic4)
print('Valor p para a Produção do Biogás: ',p_value4)
print('\n')

statistic5, p_value5 = stats.shapiro(ph_inferior)
print('Estatistica de teste para a primeira variável: ',statistic5)
print('Valor p para o pH Inferior: ',p_value5)
print('\n')

statistic6, p_value6 = stats.shapiro(ph_superior)
print('Estatistica de teste para a primeira variável: ',statistic6)
print('Valor p para o pH Superior: ',p_value6)