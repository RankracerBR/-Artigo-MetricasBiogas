#Libs/Modules
import Automatic_Calcs as Acs
import numpy as np




'''Correlação'''
dias = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
                44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], dtype = float)

temperatura_biodig = np.array([37.5, 36.1, 40.8, 41.0, 40.9, 40.8, 40.7, 40.6, 40.9, 40.8,
                            40.9, 40.8, 40.5, 40.6, 40.8, 40.6, 40.4, 40.7, 40.4, 40.8,
                            40.9, 40.7, 40.6, 40.5, 40.6, 40.6, 40.6, 40.8, 40.9, 40.9,
                            40.6, 40.8, 40.8, 40.6, 40.6, 40.5, 40.8, 40.6, 40.8, 40.8,
                            40.3, 40.8, 40.8, 41.0, 40.7, 40.9, 40.6, 41.0, 41.0, 40.8,
                            41.2, 40.8, 40.7, 40.7, 40.7, 40.8, 41.0, 40.9, 41.1, 40.9,
                            40.9], dtype = float)

recirculacao = np.array([0.977, 5.095, 1.904, 7.108, 12.448, 10.371, 3.726, 5.187,
                  6.505, 7.548, 9.504, 8.874, 8.388, 10.726, 11.628, 9.119,
                  11.158, 11.005, 10.967, 10.333, 9.448, 8.727, 9.110, 9.824,
                  9.692, 10.133, 7.786, 7.058, 8.350, 7.989, 8.068, 7.069,
                  6.898, 7.552, 8.542, 7.235, 6.151, 6.043, 5.911, 5.747,
                  1.947, 1.266, 3.496, 1.998, 1.282, 3.917, 4.395, 4.938,
                  5.361, 5.374, 1.813, 1.859, 1.804, 1.014, 1.074, 1.037,
                  0.899, 1.010, 1.028, 0.931, 0.816], dtype = float)

drenagem = np.array([2.741, 19.092, 5.626, 17.143, 29.468, 19.770, 13.164, 14.893,
                    15.663, 14.547, 12.080, 14.946, 12.509, 15.449, 16.352, 14.270,
                    15.038, 15.307, 19.372, 15.511, 14.724, 13.250, 16.097, 17.722,
                    18.352, 16.647, 12.856, 12.788, 12.517, 13.780, 13.581, 12.020,
                    12.020, 12.706, 16.707, 12.716, 11.751, 12.565, 12.596, 12.465,
                    4.441, 3.275, 5.342, 5.863, 5.595, 5.220, 5.152, 5.222, 6.079,
                    5.611, 3.544, 3.849, 3.767, 2.305, 2.130, 2.255, 2.179, 2.323,
                    2.269, 2.175, 2.031], dtype = float)

producao_biogas = np.array([1.197, 13.997, 3.722, 10.035, 17.020, 16.744, 9.438, 9.706,
                            9.158, 6.999, 6.315, 6.071, 4.121, 4.723, 4.724, 5.151,
                            3.880, 4.302, 8.405, 5.177, 5.276, 4.523, 6.987, 7.899,
                            8.660, 6.514, 5.070, 5.729, 4.167, 5.791, 5.512, 4.950,
                            5.122, 5.154, 8.165, 5.481, 5.599, 6.522, 6.685, 6.718,
                            2.494, 2.009, 1.846, 3.865, 4.313, 1.304, 1.013, 0.888,
                            1.405, 0.651, 1.730, 2.083, 1.984, 1.291, 1.094, 1.219,
                            1.280, 1.313, 1.240, 1.244, 1.215], dtype = float)

ph_inferior = np.array([4.81, 4.59, 4.68, 4.74, 4.66, 4.66, 4.81, 4.74, 4.76, 4.78,
                        4.88, 4.97, 5.01, 4.94, 5.13, 5.18, 5.30, 5.18, 5.19, 5.30,
                        5.17, 5.20, 5.38, 5.41, 5.39, 5.54, 5.55, 5.50, 5.61, 5.59,
                        5.59, 5.58, 5.54, 5.56, 5.51, 5.48, 5.54, 5.65, 5.69, 5.69,
                        5.74, 5.76, 5.62, 5.63, 5.58, 5.64, 5.63, 5.66, 5.65, 5.64,
                        5.63, 5.69, 5.65, 5.67, 5.65, 5.68, 5.69, 5.69, 5.71, 5.71,
                        5.70], dtype = float)

ph_superior = np.array([4.62, 4.42, 4.53, 4.63, 4.89, 5.07, 5.09, 5.00, 5.01, 5.05,
                        5.06, 5.18, 5.29, 5.22, 5.30, 5.39, 5.48, 5.39, 5.40, 5.47,
                        5.37, 5.35, 5.58, 5.54, 5.50, 5.56, 5.59, 5.59, 5.64, 5.61,
                        5.66, 5.67, 5.67, 5.66, 5.55, 5.57, 5.65, 5.68, 5.69, 5.70,
                        5.71, 5.71, 5.60, 5.60, 5.61, 5.64, 5.63, 5.63, 5.64, 5.64,
                        5.63, 5.63, 5.64, 5.65, 5.66, 5.67, 5.67, 5.69, 5.68, 5.69,
                        5.69], dtype = float)



'''Comparação dos dados'''
calculate = Acs.Calculate(days=dias, temp_biodigester=temperatura_biodig, recirculation=recirculacao, drain=drenagem, biogas_prod=producao_biogas, hp_inf=ph_inferior, hp_sup=ph_superior)
calculate.compare()

'''Correlação'''
calculate2 = Acs.Calculate(days=dias, temp_biodigester=temperatura_biodig, recirculation=recirculacao, drain=drenagem, biogas_prod=producao_biogas, hp_inf=ph_inferior, hp_sup=ph_superior)
calculate2.correlation_()

'''Post Hoc'''
calculate3 = Acs.Calculate(days=dias, temp_biodigester=temperatura_biodig, recirculation=recirculacao, drain=drenagem, biogas_prod=producao_biogas, hp_inf=ph_inferior, hp_sup=ph_superior)
calculate3.post_hoc()

'''Spearman'''
calculate4 = Acs.Calculate()
calculate4.spearman_calc(temperatura_biodig, producao_biogas)

calculate5 = Acs.Calculate()
calculate5.spearman_calc(temperatura_biodig, recirculacao)

calculate6 = Acs.Calculate()
calculate6.spearman_calc(temperatura_biodig, ph_inferior)

calculate7 = Acs.Calculate()
calculate7.spearman_calc(temperatura_biodig, ph_superior)



'''Significância'''
# Dados de correlações para o Ciclo 1 (exemplo)
correlation_data_ciclo_1 = [
    [np.nan, 0.121, 0.446, -0.442, -0.503, 0.971, 0.884, -0.447],
    [0.121, np.nan, -0.358, 0.302, 0.352, 0.039, 0.148, -0.452],
    [0.446, -0.358, np.nan, -0.229, -0.421, 0.473, 0.34, 0.371],
    [-0.442, 0.302, -0.229, np.nan, 0.961, -0.192, -0.043, -0.371],
    [-0.503, 0.352, -0.421, 0.961, np.nan, -0.219, -0.063, -0.433],
    [0.971, 0.039, 0.473, -0.192, -0.219, np.nan, 0.901, -0.376],
    [0.884, 0.148, 0.34, -0.043, -0.063, 0.901, np.nan, -0.436],
    [-0.447, -0.452, 0.371, -0.371, -0.433, -0.376, -0.436, np.nan]
]

Acs.plot_correlation_heatmap(correlation_data_ciclo_1, 'Mapa de Calor - Correlações Ciclo 1')

correlation_data_ciclo_2 = [
    [np.nan, -0.015, 0.843, 0.204, -0.168, -0.225, -0.031, -0.371],
    [np.nan, np.nan, 0.112, 0.209, 0.152, -0.329, -0.705, 0.412],
    [np.nan, np.nan, np.nan, 0.357, -0.15, -0.411, -0.188, 0.062],
    [np.nan, np.nan, np.nan, np.nan, 0.686, -0.182, -0.598, 0.371],
    [np.nan, np.nan, np.nan, np.nan, np.nan, 0.006, -0.603, 0.371],
    [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.356, -0.101],
    [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, -0.379],
    [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
]

Acs.plot_correlation_heatmap(correlation_data_ciclo_2, 'Mapa de Calor - Correlações Ciclo 2')

correlation_data_ciclo_3 = [
    [-0.287, np.nan, 0.657, -0.264, -0.457, 0.931, 0.946, -0.371],
    [np.nan, np.nan, -0.213, 0.165, 0.102, -0.171, -0.24, 0.441],
    [0.657, -0.213, np.nan, -0.604, -0.761, 0.593, 0.59, 0.247],
    [-0.264, 0.165, -0.604, np.nan, 0.936, -0.222, -0.249, -0.124],
    [-0.457, 0.102, -0.761, 0.936, np.nan, -0.403, -0.43, -0.124],
    [0.931, -0.171, 0.593, -0.222, -0.403, np.nan, 0.979, -0.372],
    [0.946, -0.24, 0.59, -0.249, -0.43, 0.979, np.nan, -0.435],
    [-0.371, 0.441, 0.247, -0.124, -0.124, -0.372, -0.435, np.nan]
]

Acs.plot_correlation_heatmap(correlation_data_ciclo_3, 'Mapa de Calor - Correlações Ciclo 3')

# Dados de correlações para o Ciclo 4
correlation_data_ciclo_4 = [
    [0.529, np.nan, 0.825, -0.164, -0.489, 0.859, 0.859, -0.371],
    [np.nan, np.nan, 0.391, -0.421, -0.394, 0.405, 0.426, -0.094],
    [0.825, 0.391, np.nan, -0.171, -0.536, 0.703, 0.719, 0.0],
    [-0.164, -0.421, -0.171, np.nan, 0.786, -0.395, -0.329, -0.309],
    [-0.489, -0.394, -0.536, 0.786, np.nan, -0.759, -0.699, 0.062],
    [0.859, 0.405, 0.703, -0.395, -0.759, np.nan, 0.933, -0.404],
    [0.859, 0.426, 0.719, -0.329, -0.699, 0.933, np.nan, -0.373],
    [-0.371, -0.094, 0.0, -0.309, 0.062, -0.404, -0.373, np.nan]
]

Acs.plot_correlation_heatmap(correlation_data_ciclo_4, 'Mapa de Calor - Correlações Ciclo 4')

# Dados de correlações para o Ciclo 5
correlation_data_ciclo_5 = [
    [-0.444, np.nan, 0.389, -0.529, -0.561, 0.821, 0.24, -0.371],
    [np.nan, np.nan, -0.112, 0.329, 0.338, -0.15, 0.386, 0.253],
    [0.389, -0.112, np.nan, 0.011, -0.146, 0.434, 0.157, 0.371],
    [-0.529, 0.329, 0.011, np.nan, 0.964, -0.261, 0.269, 0.309],
    [-0.561, 0.338, -0.146, 0.964, np.nan, -0.313, 0.231, 0.186],
    [0.821, -0.15, 0.434, -0.261, -0.313, np.nan, 0.316, -0.262],
    [0.24, 0.386, 0.157, 0.269, 0.231, 0.316, np.nan, 0.066],
    [-0.371, 0.253, 0.371, 0.309, 0.186, -0.262, 0.066, np.nan]
]

Acs.plot_correlation_heatmap(correlation_data_ciclo_5, 'Mapa de Calor - Correlações Ciclo 5')

# Dados de correlações para o Ciclo 6
correlation_data_ciclo_6 = [
    [-0.103, np.nan, 0.125, 0.679, 0.339, 0.853, 0.936, np.nan],
    [np.nan, np.nan, 0.294, 0.242, -0.014, -0.324, -0.205, np.nan],
    [0.125, 0.294, np.nan, 0.293, -0.486, -0.163, 0.022, np.nan],
    [0.679, 0.242, 0.293, np.nan, 0.496, 0.506, 0.597, np.nan],
    [0.339, -0.014, -0.486, 0.496, np.nan, 0.307, 0.273, np.nan],
    [0.853, -0.324, -0.163, 0.506, 0.307, np.nan, 0.928, np.nan],
    [0.936, -0.205, 0.022, 0.597, 0.273, 0.928, np.nan, np.nan],
    [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
]

Acs.plot_correlation_heatmap(correlation_data_ciclo_6, 'Mapa de Calor - Correlações Ciclo 6')

# Dados de correlações para o Ciclo 7
correlation_data_ciclo_7 = [
    [0.28, np.nan, 0.757, 0.15, -0.118, 0.686, 0.93, np.nan],
    [np.nan, np.nan, 0.275, 0.18, 0.045, 0.555, 0.256, np.nan],
    [0.757, 0.275, np.nan, 0.254, -0.107, 0.559, 0.658, np.nan],
    [0.15, 0.18, 0.254, np.nan, 0.882, 0.005, 0.147, np.nan],
    [-0.118, 0.045, -0.107, 0.882, np.nan, -0.281, -0.134, np.nan],
    [0.686, 0.555, 0.559, 0.005, -0.281, np.nan, 0.697, np.nan],
    [0.93, 0.256, 0.658, 0.147, -0.134, 0.697, np.nan, np.nan],
    [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
]

Acs.plot_correlation_heatmap(correlation_data_ciclo_7, 'Mapa de Calor - Correlações Ciclo 7')

# Dados de correlações para o Ciclo 8
correlation_data_ciclo_8 = [
    [0.343, np.nan, 0.564, 0.107, -0.123, 0.807, 0.425, -0.371],
    [np.nan, np.nan, -0.105, -0.164, -0.422, 0.669, -0.034, -0.378],
    [0.564, -0.105, np.nan, 0.614, 0.47, 0.385, 0.313, -0.309],
    [0.107, -0.164, 0.614, np.nan, 0.899, -0.007, -0.149, -0.371],
    [-0.123, -0.422, 0.47, 0.899, np.nan, -0.272, -0.092, 0.0],
    [0.807, 0.669, 0.385, -0.007, -0.272, np.nan, 0.361, -0.443],
    [0.425, -0.034, 0.313, -0.149, -0.092, 0.361, np.nan, 0.255],
    [-0.371, -0.378, -0.309, -0.371, 0.0, -0.443, 0.255, np.nan]
]

Acs.plot_correlation_heatmap(correlation_data_ciclo_8, 'Mapa de Calor - Correlações Ciclo 8')