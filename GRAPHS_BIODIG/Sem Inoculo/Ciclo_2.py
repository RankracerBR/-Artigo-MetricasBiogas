import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import Automatic_Calcs as Acs

#1
dias = np.array([60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 
                 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 
                 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103,
                 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 
                 116, 117, 118, 119, 120], dtype = float)

temperatura_biodig = np.array([41.2, 30.5, 40.8, 40.5, 40.5, 40.5, 40.7, 40.4, 41.3, 40.7, 40.8,
                            41.3, 40.3, 40.5, 41.2, 40.5, 40.6, 40.4, 40.5, 40.5, 41.3, 40.8,
                            40.4, 40.6, 40.6, 40.7, 40.5, 40.4, 40.4, 40.5, 40.6, 40.6, 40.9,
                            40.5, 40.5, 40.4, 40.8, 40.5, 40.8, 41.2, 40.8, 41.2, 40.7, 41.2,
                            40.7, 41.3, 40.6, 41.3, 41.4, 40.5, 41.3, 40.7, 40.4, 41.3, 40.4,
                            40.6, 41.4, 40.6, 41.2, 40.7, 40.7], dtype = float)

spline = interp1d(dias,temperatura_biodig)

dias_novo = np.linspace(60,120,1000)

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
recirculacao = np.array([0.757, 0.000, 0.000, 12.121, 24.384, 20.633, 0.797, 
                         4.579, 10.073, 10.938, 12.059, 10.500, 12.323, 13.660, 
                         13.102, 9.887, 11.786, 10.245, 9.214, 11.132, 8.519, 6.783, 
                         6.203, 7.583, 7.367, 7.312, 0.000, 0.000, 2.219, 2.524, 2.312, 
                         2.196, 2.059, 4.082, 9.374, 1.727, 1.915, 1.763, 2.060, 1.972, 
                         2.008, 1.839, 1.953, 1.730, 1.604, 1.680, 1.280, 1.624, 3.148, 
                         3.800, 5.003, 4.536, 4.377, 2.182, 2.327, 2.206, 1.817, 2.102, 
                         1.945, 1.817, 1.937], dtype = float)

spline_2 = interp1d(dias,recirculacao)

dias_novo_2 = np.linspace(60,120,1000)

reciculacao_novo = spline_2(dias_novo_2)

plt.scatter(dias,recirculacao)
plt.plot(dias_novo_2,reciculacao_novo, c ='cyan')
plt.xlabel('Dias')
plt.ylabel('Recirculação(L/h)')
plt.grid()
plt.show()

#3
drenagem = np.array([1.068, 0.000, 0.000, 16.202, 39.773, 8.824, 4.780, 
                     11.944, 20.453, 19.908, 7.210, 17.208, 17.480, 16.924,
                     17.570, 17.019, 16.566, 15.265, 16.561, 18.223, 17.160,
                     14.863, 15.800, 16.974, 17.289, 13.118, 0.809, 0.973,
                     4.356, 4.428, 4.708, 4.180, 4.454, 8.164, 16.467, 4.257, 
                     4.414, 3.896, 4.373, 4.145, 4.297, 4.526, 4.508, 4.115, 4.107, 
                     4.106, 4.088, 3.969, 6.984, 5.278, 10.048, 10.225, 10.156, 5.538, 
                     5.331, 5.391, 5.370, 5.508, 5.421, 5.282, 5.217], dtype = float)

spline_3 = interp1d(dias,drenagem)

dias_novo_3 = np.linspace(60,120,1000)

drenagem_novo = spline_3(dias_novo_3)

plt.scatter(dias,drenagem)
plt.plot(dias_novo_3, drenagem_novo, c = 'yellow')
plt.xlabel('Dias')
plt.ylabel('Drenagem(L/h)')
plt.grid()
plt.show()

#4
producao_biogas = np.array([0.312, 0.000, 0.000, 4.081, 15.390, 10.226, 3.983, 7.366, 10.380, 8.970, 6.367,
                            6.708, 5.157, 3.264, 4.469, 7.132, 4.780, 5.020, 7.346, 7.092, 8.641, 8.080, 9.597,
                            9.391, 9.922, 5.806, 0.809, 0.973, 2.137, 1.903, 2.395, 1.985, 2.395, 4.082, 7.094,
                            2.530, 2.498, 2.133, 2.313, 2.173, 2.289, 2.687, 2.554, 2.385, 2.503, 2.426, 2.808,
                            2.345, 3.836, 1.478, 5.045, 5.690, 5.779, 3.357, 3.004, 3.186, 3.553, 3.406, 3.476,
                            3.465, 3.281], dtype = float)

spline_4 = interp1d(dias,producao_biogas, kind='cubic')

dias_novo_4 = np.linspace(60,120,1000)
producao_biogas_novo = spline_4(dias_novo_4)

plt.scatter(dias,producao_biogas)
plt.plot(dias_novo_4, producao_biogas_novo, c = 'purple')
plt.xlabel('Dias')
plt.ylabel('Produção Biogás(L)')
plt.grid()
plt.show()

#5
ph_inferior = np.array([5.14, 4.41, 4.33, 4.49, 4.92, 4.93, 4.83, 4.88, 4.89, 4.91, 4.89,
                        4.91, 4.91, 4.92, 4.92, 4.96, 4.93, 4.99, 4.97, 5.04, 5.11, 5.15,
                        5.17, 5.2 , 5.22, 5.23, 5.24, 5.26, 5.27, 5.26, 5.32, 5.32, 5.35,
                        5.37, 5.4 , 5.41, 5.42, 5.42, 5.44, 5.46, 5.46, 5.47, 5.48, 5.48,
                        5.49, 5.52, 5.52, 5.53, 5.55, 5.55, 5.55, 5.56, 5.58, 5.58, 5.61,
                        5.62, 5.61, 5.62, 5.63, 5.63, 5.62], dtype = float)


ph_superior = np.array([5.16, 4.7 , 4.62, 4.63, 4.71, 4.75, 4.68, 4.74, 4.78, 4.83, 4.85,
                        4.9 , 4.96, 5.06, 5.12, 5.08, 5.03, 5.3 , 5.21, 5.37, 5.44, 5.54,
                        5.62, 5.63, 5.63, 5.66, 5.6 , 5.64, 5.69, 5.66, 5.74, 5.66, 5.55,
                        5.61, 5.64, 5.56, 5.57, 5.6 , 5.61, 5.68, 5.75, 5.73, 5.74, 5.68,
                        5.62, 5.71, 5.7 , 5.73, 5.67, 5.72, 5.72, 5.74, 5.75, 5.75, 5.73,
                        5.78, 5.79, 5.81, 5.81, 5.8 , 5.79], dtype = float)



f_inferior = interp1d(dias, ph_inferior, kind='cubic')
f_superior = interp1d(dias, ph_superior, kind='cubic')

dias_interp = np.linspace(60, 120, 1000)  
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