from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import Automatic_Calcs as Acs
import numpy as np

#1
dias = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
                44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], dtype = float)

temperatura_biodig = np.array([30.7, 40.6, 40.7, 41.2, 40.9, 40.8, 40.7, 40.6, 40.7, 40.5, 41.2, 40.5, 40.4, 40.8,
                                40.6, 40.5, 40.3, 40.6, 40.4, 40.5, 40.6, 40.6, 40.8, 40.5, 40.7, 40.4, 40.8, 41.2,
                                41.3, 40.9, 40.3, 40.6, 41.2, 40.7, 40.5, 40.6, 40.9, 40.7, 40.8, 40.6, 39.2, 40.5,
                                40.9, 41.3, 40.9, 40.7, 40.6, 40.5, 40.8, 40.5, 41.2, 40.9, 41.2, 40.4, 40.8, 40.8,
                                40.7, 41.3, 41.2, 41.3, 41.2], dtype = float)

spline = interp1d(dias,temperatura_biodig, kind='cubic')

dias_novo = np.linspace(0,60,1000)

temperatura_biodig_novo = spline(dias_novo)

fig = plt.figure(figsize=(5, 6))  # Define o tamanho da figura

ax1 = fig.add_subplot(1, 1, 1)
ax1.scatter(dias, temperatura_biodig, c='red')
ax1.plot(dias_novo, temperatura_biodig_novo, c='green')
ax1.set_xlabel('Dias')
ax1.set_ylabel('Temperatura Biodigestor', color='red')
ax1.tick_params(axis='y', labelcolor='red')

# Criando um segundo eixo y
ax2 = ax1.twinx()
ax2.set_ylabel('Outro Eixo Y', color='blue')
ax2.plot([], [])  # Para criar uma linha vazia apenas para incluir no gráfico
ax2.tick_params(axis='y', labelcolor='blue')

# Define os limites do eixo y
ax1.set_ylim(0, 60)
ax2.set_ylim(0, 60)
ax1.grid(axis='both')

plt.grid(True)
plt.show()

#2
recirculacao = np.array([0.000, 0.044, 6.655, 5.791, 11.232, 10.991, 10.879, 9.836, 4.973, 10.634, 12.441,
                        8.468, 6.049, 12.008, 19.274, 9.113, 16.627, 19.624, 23.617, 23.615, 24.968, 25.874,
                        21.684, 22.592, 22.544, 23.810, 22.364, 23.953, 23.855, 24.742, 23.469, 23.174, 21.284,
                        21.114, 15.752, 21.054, 16.176, 14.644, 14.007, 14.032, 6.889, 3.506, 16.150, 8.103,
                        3.955, 19.154, 22.889, 25.303, 24.764, 23.482, 0.450, 1.791, 1.673, 1.284, 1.468, 1.328,
                        1.450, 1.387, 1.902, 1.657, 0.757], dtype = float)

spline_2 = interp1d(dias,recirculacao, kind='cubic')

dias_novo_2 = np.linspace(0,60,1000)

reciculacao_novo = spline_2(dias_novo_2)

plt.scatter(dias,recirculacao)
plt.plot(dias_novo_2,reciculacao_novo, c ='cyan')
plt.xlabel('Dias')
plt.ylabel('Recirculação(L/h)')
plt.grid()
plt.show()

#3
drenagem = np.array([0.000, 21.628, 18.169, 36.029, 65.759, 74.179, 42.418, 40.287, 27.513, 32.649, 24.361,
                    19.244, 19.259, 23.515, 27.540, 16.250, 20.154, 25.386, 35.861, 31.684, 31.404, 29.977,
                    29.432, 31.458, 34.927, 31.981, 32.632, 31.399, 30.924, 31.811, 28.943, 30.353, 29.178,
                    25.256, 28.496, 26.921, 24.243, 27.862, 26.049, 28.102, 15.465, 9.618, 21.604, 25.375,
                    23.182, 21.077, 21.400, 21.785, 20.764, 21.077, 0.495, 1.246, 1.544, 1.365, 1.245, 1.456,
                    1.575, 1.424, 1.988, 1.782, 1.068], dtype = float)

spline_3 = interp1d(dias,drenagem, kind='cubic')

dias_novo_3 = np.linspace(0,60,1000)

drenagem_novo = spline_3(dias_novo_3)

plt.scatter(dias,drenagem)
plt.plot(dias_novo_3, drenagem_novo, c = 'yellow')
plt.xlabel('Dias')
plt.ylabel('Drenagem(L/h)')
plt.grid()
plt.show()

#4
producao_biogas = np.array([0.000, 21.584, 11.514, 30.238, 54.527, 63.188, 31.538, 30.451, 22.540, 22.014, 11.920,
                            10.777, 13.210, 11.506, 8.266, 7.137, 3.527, 5.762, 12.244, 8.069, 6.436, 4.103, 7.747,
                            8.866, 12.384, 8.171, 10.268, 7.446, 7.068, 7.069, 5.473, 7.179, 7.894, 4.143, 12.744,
                            5.867, 8.068, 13.218, 12.042, 14.070, 8.576, 6.112, 5.455, 17.273, 19.227, 1.923, 0.000,
                            0.000, 0.000, 0.000, 0.045, 0.000, 0.000, 0.080, 0.000, 0.128, 0.124, 0.037, 0.086, 0.124,
                            0.312], dtype = float)

spline_4 = interp1d(dias,producao_biogas, kind='cubic')

dias_novo_4 = np.linspace(0,60,1000)
producao_biogas_novo = spline_4(dias_novo_4)

plt.scatter(dias,producao_biogas)
plt.plot(dias_novo_4, producao_biogas_novo, c = 'purple')
plt.xlabel('Dias')
plt.ylabel('Produção Biogás(L/h)')
plt.grid()
plt.show()

#5

ph_inferior = np.array([3.80, 3.30, 3.40, 3.63, 3.21, 3.23, 3.77, 3.52, 3.52, 3.54, 3.82, 4.12, 4.10, 3.80, 4.29,
                        4.45, 4.85, 4.22, 4.33, 4.49, 4.01, 3.98, 4.40, 4.52, 4.48, 4.92, 4.97, 4.78, 5.06, 5.02,
                        4.95, 4.96, 4.96, 4.97, 4.76, 4.79, 4.97, 5.25, 5.35, 5.27, 5.33, 5.35, 4.95, 5.00, 4.95,
                        5.02, 4.97, 5.01, 5.03, 4.97, 4.91, 5.04, 4.94, 4.95, 4.92, 4.94, 4.97, 4.97, 5.01, 4.99,
                        4.98], dtype = float)


ph_superior = np.array([3.70, 3.51, 3.54, 3.65, 3.94, 4.47, 4.64, 4.31, 4.33, 4.43, 4.48, 4.83, 5.08, 4.87, 5.11,
                        5.29, 5.60, 5.27, 5.30, 5.43, 5.04, 4.95, 5.58, 5.44, 5.29, 5.46, 5.55, 5.49, 5.63, 5.56,
                        5.65, 5.64, 5.62, 5.58, 5.18, 5.22, 5.45, 5.56, 5.58, 5.57, 5.58, 5.56, 5.23, 5.21, 5.21,
                        5.23, 5.21, 5.19, 5.20, 5.17, 5.16, 5.16, 5.15, 5.16, 5.15, 5.16, 5.18, 5.20, 5.18, 5.20, 5.21], dtype = float)



f_inferior = interp1d(dias, ph_inferior, kind='cubic')
f_superior = interp1d(dias, ph_superior, kind='cubic')

dias_interp = np.linspace(0, 60, 1000)  
ph_inferior_interp = f_inferior(dias_interp)
ph_superior_interp = f_superior(dias_interp)

# Plot dos dados originais e das curvas interpoladas
plt.plot(dias, ph_inferior, 'ro', label='pH Inferior')
plt.plot(dias, ph_superior, 'bo', label='pH Superior')
plt.plot(dias_interp, ph_inferior_interp, 'r-', label='pH Inferior (Interpolado)')
plt.plot(dias_interp, ph_superior_interp, 'b-', label='pH Superior (Interpolado)')
plt.xlabel('Dias')
plt.ylabel('pH')
plt.legend()
plt.grid(True)
plt.show()



'''Comparação dos dados'''
calculate = Acs.Calculate(days=dias, temp_biodigester=temperatura_biodig, recirculation=recirculacao, drain=drenagem, biogas_prod=producao_biogas, hp_inf=ph_inferior, hp_sup=ph_superior)
calculate.compare()


#Ajeitar na classe
'''Correlação'''
calculate2 = Acs.Calculate(days=dias, temp_biodigester=temperatura_biodig, recirculation=recirculacao, drain=drenagem, biogas_prod=producao_biogas, hp_inf=ph_inferior, hp_sup=ph_superior)
calculate2.correlation_()

'''Spearman'''
calculate4 = Acs.Calculate()
calculate4.spearman_calc(temperatura_biodig, producao_biogas)

calculate5 = Acs.Calculate()
calculate5.spearman_calc(temperatura_biodig, recirculacao)

calculate6 = Acs.Calculate()
calculate6.spearman_calc(temperatura_biodig, ph_inferior)

calculate7 = Acs.Calculate()
calculate7.spearman_calc(temperatura_biodig, ph_superior)