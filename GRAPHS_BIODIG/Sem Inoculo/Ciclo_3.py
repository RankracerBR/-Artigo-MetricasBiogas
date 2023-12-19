from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import Automatic_Calcs as Acs
import numpy as np




#1
dias = np.array([120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130,
                 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141,
                 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152,
                 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164,
                 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176,
                 177, 178, 179, 180], dtype = float)

temperatura_biodig = np.array([40.7, 37.2, 40.8, 41.4, 41.2, 41.2, 40.8, 40.8,
                               40.8, 41.2, 40.7, 40.7, 40.9, 40.6, 40.7, 40.9,
                               40.4, 41.2, 40.4, 41.3, 40.9, 40.8, 40.5, 40.4,
                               40.6, 40.6, 40.6, 40.7, 40.9, 41.2, 40.9, 41.3,
                               40.4, 40.6, 40.9, 40.6, 40.7, 40.5, 40.9, 40.5, 40.8,
                               40.6, 40.8, 40.4, 40.6, 40.7, 40.5, 41.2, 40.9, 41.3,
                               41.2, 40.9, 40.4, 40.4, 40.9, 40.9, 40.8, 40.7, 40.8,
                               40.8, 40.8], dtype = float)

spline = interp1d(dias, temperatura_biodig, kind='cubic')

dias_novo = np.linspace(120, 180, 1000)
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
recirculacao = np.array([2.174, 15.262, 2.285, 6.220, 7.175, 4.819,
                         4.779, 5.917, 6.881, 6.231, 10.046, 11.762,
                         9.725, 12.332, 11.854, 12.776, 13.126, 12.664,
                         11.523, 7.706, 6.965, 6.072, 9.958, 10.251, 10.097,
                         10.824, 11.840, 8.838, 10.545, 8.700, 9.804, 7.076,
                         7.674, 7.699, 8.138, 9.135, 8.207, 8.824, 8.460, 8.041,
                         0.286, 0.154, 0.217, 0.090, 0.205, 0.206, 0.116, 0.159,
                         0.182, 0.227, 0.205, 0.120, 0.174, 0.198, 0.139, 0.220,
                         0.133, 0.214, 0.161, 0.123, 0.122], dtype = float)

spline_2 = interp1d(dias,recirculacao, kind='cubic')

dias_novo_2 = np.linspace(120,180,1000)
recirculacao_novo = spline_2(dias_novo_2)

plt.scatter(dias,recirculacao)
plt.plot(dias_novo_2, recirculacao_novo, c = 'green' )
plt.xlabel('Dias')
plt.ylabel('Recirculação(L/h)')
plt.grid()
plt.show()


#3
drenagem = np.array([7.154, 46.136, 7.521, 16.671, 14.763, 12.281, 12.866,
                     11.985, 12.366, 6.918, 16.484, 17.717, 10.127, 17.312,
                     17.300, 17.422, 18.169, 17.582, 23.086, 11.990, 10.838, 9.448,
                     17.333, 19.990, 19.777, 20.351, 20.952, 21.218, 17.268, 20.529,
                     21.128, 16.246, 16.580, 16.946, 18.976, 20.026, 18.352, 19.448,
                     20.000, 18.776, 1.061, 0.347, 0.391, 0.405, 0.740, 0.700, 0.347,
                     0.477, 0.560, 0.701, 0.328, 0.679, 0.349, 0.673, 0.416, 0.624, 0.355,
                     0.728, 0.362, 0.327, 0.325], dtype = float)

spline_3 = interp1d(dias,drenagem, kind='cubic')

dias_novo_3 = np.linspace(120,180,1000)
drenagem_novo = spline_3(dias_novo_3)

plt.scatter(dias,drenagem)
plt.plot(dias_novo_3,drenagem_novo, c = 'purple')
plt.xlabel('Dias')
plt.ylabel('Drenagem')
plt.grid()
plt.show()

#4 
producao_biodig = np.array([3.281, 30.874, 5.235, 10.451, 7.588,
                            7.463, 8.087, 6.068, 5.485, 0.688, 6.438,
                            5.955, 0.402, 4.980, 5.445, 4.646, 5.043, 4.918,
                            11.563, 4.284, 3.873, 3.376, 7.375, 9.739, 9.680, 9.527,
                            9.111, 12.380, 6.723, 11.829, 11.323, 9.169, 8.906, 9.247,
                            10.837, 10.891, 10.144, 10.624, 11.540, 10.735, 0.776, 0.193,
                            0.174, 0.315, 0.534, 0.494, 0.232, 0.318, 0.378, 0.474, 0.123,
                            0.559, 0.174, 0.475, 0.277, 0.404, 0.222, 0.514, 0.201, 0.204,
                            0.203], dtype = float)

spline_4 = interp1d(dias, producao_biodig, kind='cubic')

dias_novo_4 = np.linspace(120,180,1000)
producao_biogas_novo = spline_4(dias_novo_4)

plt.scatter(dias,producao_biodig)
plt.plot(dias_novo_4,producao_biogas_novo, c = 'orange' )
plt.xlabel('Dias')
plt.ylabel('Produção Biogás(L)')
plt.grid()
plt.show()

#5
ph_inferior = np.array([5.46, 5.76, 6.03, 5.97, 6.05, 6.01, 5.99, 5.96, 5.97, 5.97, 5.98, 5.90, 5.98, 5.97,
                        5.98, 6.00, 6.01, 6.01, 6.02, 6.05, 6.07, 6.07, 6.11, 6.09, 6.06, 6.04, 6.07, 6.08,
                        6.08, 6.10, 6.09, 6.11, 6.11, 6.11, 6.12, 6.08, 6.09, 6.09, 6.12, 6.12, 6.15, 6.20,
                        6.18, 6.22, 6.17, 6.20, 6.21, 6.24, 6.24, 6.24, 6.27, 6.28, 6.27, 6.30, 6.29, 6.32,
                        6.31, 6.28, 6.31, 6.33, 6.32], dtype = float)

ph_superior = np.array([5.02, 5.35, 5.73, 5.76, 5.80, 5.80, 5.80, 5.80, 5.81, 5.81, 5.82, 5.81, 5.87, 5.88,
                        5.88, 5.91, 5.92, 5.91, 5.94, 5.93, 5.96, 5.95, 5.98, 5.98, 5.98, 5.99, 5.99, 6.01,
                        6.02, 6.01, 6.01, 6.04, 6.03, 6.03, 6.07, 6.07, 6.07, 6.07, 6.06, 6.07, 6.09, 6.09,
                        6.10, 6.12, 6.12, 6.16, 6.15, 6.16, 6.17, 6.20, 6.18, 6.18, 6.20, 6.21, 6.22, 6.22,
                        6.22, 6.24, 6.24, 6.25, 6.24], dtype = float)


f_inferior = interp1d(dias, ph_inferior, kind='cubic')
f_superior = interp1d(dias, ph_superior, kind='cubic')


dias_interp = np.linspace(120, 180, 1000)  
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
calculate = Acs.Calculate(days=dias, temp_biodigester=temperatura_biodig, recirculation=recirculacao, drain=drenagem, biogas_prod=producao_biodig, hp_inf=ph_inferior, hp_sup=ph_superior)
calculate.compare()


#Ajeitar na classe
'''Correlação'''
calculate2 = Acs.Calculate(days=dias, temp_biodigester=temperatura_biodig, recirculation=recirculacao, drain=drenagem, biogas_prod=producao_biodig, hp_inf=ph_inferior, hp_sup=ph_superior)
calculate2.correlation_()

'''Spearman'''
calculate4 = Acs.Calculate()
calculate4.spearman_calc(temperatura_biodig, producao_biodig)

calculate5 = Acs.Calculate()
calculate5.spearman_calc(temperatura_biodig, recirculacao)

calculate6 = Acs.Calculate()
calculate6.spearman_calc(temperatura_biodig, ph_inferior)

calculate7 = Acs.Calculate()
calculate7.spearman_calc(temperatura_biodig, ph_superior)