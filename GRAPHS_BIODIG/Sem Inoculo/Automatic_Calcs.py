#Libs/modules
from matplotlib.animation import FuncAnimation, PillowWriter
from scipy.interpolate import interp1d
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import numpy as np


##Maintenance
#Class
class Calculate:
    '''Calculate the variables related to the Biodigester'''
    def __init__(self, **kwargs):
        self.days = kwargs.get('days')
        self.temp_biodigester = kwargs.get('temp_biodigester')
        self.recirculation = kwargs.get('recirculation')
        self.biogas_prod = kwargs.get('biogas_prod')
        self.drain = kwargs.get('drain')
        self.hp_inf = kwargs.get('hp_inf')
        self.hp_sup = kwargs.get('hp_sup')


    def compare(self):
        '''Data Comparison'''
        # Check lengths of arrays
        arrays = [self.days, self.temp_biodigester, self.recirculation, self.biogas_prod, self.drain, self.hp_inf, self.hp_sup]
        lengths = [len(arr) for arr in arrays]
        
        if len(set(lengths)) != 1:
            raise ValueError("Arrays have different lengths!")
        else:
            print("Arrays have consistent lengths.")

        x_new = np.linspace(min(self.days), max(self.days), 10000)

        if np.any(self.hp_sup) and np.any(self.hp_inf):
            f_temp = interp1d(self.days, self.temp_biodigester, kind='cubic')
            f_rec = interp1d(self.days, self.recirculation, kind='cubic')
            f_biogas = interp1d(self.days, self.biogas_prod, kind='cubic')
            f_drain = interp1d(self.days, self.drain, kind='cubic')
            f_hp_inf = interp1d(self.days, self.hp_inf, kind='cubic')
            f_hp_sup = interp1d(self.days, self.hp_sup, kind='cubic')

            # Plotar os dados interpolados
            plt.figure(figsize=(10, 6))
            plt.plot(x_new, f_temp(x_new), label='Temperatura do Biodigestor')
            plt.plot(x_new, f_rec(x_new), label='Recirculação')
            plt.plot(x_new, f_biogas(x_new), label='Produção de Biogás')
            plt.plot(x_new, f_drain(x_new), label='Drenagem')
            plt.plot(x_new, f_hp_inf(x_new), label='hp Inferior')
            plt.plot(x_new, f_hp_sup(x_new), label='hp Superior')

            plt.scatter(self.days, self.temp_biodigester, c='red')
            plt.scatter(self.days, self.recirculation, c='red')
            plt.scatter(self.days, self.biogas_prod, c='red')
            plt.scatter(self.days, self.drain, c='red')
            plt.scatter(self.days, self.hp_inf, c='red')
            plt.scatter(self.days, self.hp_sup, c='red')

            # Adicionar legendas e título
            plt.xlabel('Days')
            plt.ylabel('Data')
            plt.title('Biogas Data')

            # Mostrar a legenda
            plt.legend()
            plt.grid()

        elif not np.any(self.hp_inferior) and not np.any(self.hp_superior):
            f_temp = interp1d(self.days, self.temp_biodigester, kind='cubic')
            f_rec = interp1d(self.days, self.recirculation, kind='cubic')
            f_biogas = interp1d(self.days, self.biogas_prod, kind='cubic')
            f_drenagem = interp1d(self.days, self.drain, kind='cubic')
            f_hp_inf = interp1d(self.days, self.hp_superior, kind='cubic')
            f_hp_sup = interp1d(self.days, self.hp_superior, kind='cubic')

            # Plotar os dados interpolados
            plt.figure(figsize=(10, 6))
            plt.plot(x_new, f_temp(x_new), label='Temperatura do Biodigestor')
            plt.plot(x_new, f_rec(x_new), label='Recirculação')
            plt.plot(x_new, f_biogas(x_new), label='Produção de Biogás')
            plt.plot(x_new, f_drenagem(x_new), label='Drenagem')


            plt.scatter(self.days, self.temp_biodigester, c='red')
            plt.scatter(self.days, self.recirculation, c='red')
            plt.scatter(self.days, self.biogas_prod, c='red')
            plt.scatter(self.days, self.drain, c='red')
            
            # Adicionar legendas e título
            plt.xlabel('Days')
            plt.ylabel('Results')
            plt.title('Biogas Data')

            # Mostrar a legenda
            plt.legend()
            plt.grid()
        
        # Exibir o gráfico
        plt.show()


    def correlation_(self):
        '''Correlation'''
        if self.hp_inf is not None and self.hp_sup is not None:
            # When hp_inferior and hp_superior are present
            correlation, p_value = spearmanr([self.temp_biodigester, self.recirculation, self.biogas_prod, self.hp_inf, self.hp_sup, self.drain])

            # Variable names and labels
            variable_names = ['Biodogester Temp', 'Recirculation', 'Biogas Prod', 'hp Inf', 'hp Sup', 'Drain']
            variable_names_2 = ['Biodig Temp', 'Rerc.', 'Prod. Bio', 'hp Inf', 'hp Sup', 'Drain']
        else:
            # When hp_inferior and hp_superior are absent
            correlation, p_value = spearmanr([self.temp_biodigester, self.recirculation, self.biogas_prod, self.drain])

            # Variable names and labels
            variable_names = ['Biodigeste Temp', 'Recirculation', 'Biogas Prod', 'Drain']
            variable_names_2 = ['Temp. B', 'Rerc.', 'Prod. Bio', 'Drain']

        # Printing Spearman correlation coefficient
        print(f"Spearman correlation coefficient: {correlation}")

        # Create correlation matrixs
        data = np.array([self.temp_biodigester, self.recirculation, self.biogas_prod, self.drain])
        if self.hp_inf is not None and self.hp_sup is not None:
            data = np.array([self.temp_biodigester, self.recirculation, self.biogas_prod, self.hp_inf, self.hp_sup, self.drain])
        correlation_matrix, _ = spearmanr(data, axis=1)

        # Create correlation heatmap
        plt.figure(figsize=(8, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True,
                    xticklabels=variable_names_2, yticklabels=variable_names)

        # Add title
        plt.title('Correlation Matrix')

        # Exibir o gráfico
        plt.show()
        

    def compare_animation(self):
        '''Data Comparison with Animation'''
        arrays = [self.days, self.temp_biodigester, self.recirculation, self.biogas_prod, self.drain, self.hp_inf, self.hp_sup]
        lengths = [len(arr) for arr in arrays]
        
        if len(set(lengths)) != 1:
            raise ValueError("Arrays have different lengths!")
        else:
            print("Arrays have consistent lengths.")

        f_temp = interp1d(self.days, self.temp_biodigester, kind='cubic')
        f_rec = interp1d(self.days, self.recirculation, kind='cubic')
        f_biogas = interp1d(self.days, self.biogas_prod, kind='cubic')
        f_drain = interp1d(self.days, self.drain, kind='cubic')

        fig, ax = plt.subplots(figsize=(10, 6))


        def update(frame):
            ax.clear()

            x_new = np.linspace(min(self.dias), max(self.dias), 1000)  # Definir o linspace dentro da função update

            if frame < 1000:
                ax.plot(x_new[:frame], f_temp(x_new)[:frame])
                ax.plot(x_new[:frame], f_rec(x_new)[:frame], label='Recirculation', color='green')
                ax.plot(x_new[:frame], f_biogas(x_new)[:frame], label='Biogas Prod', color='orange')
                ax.plot(x_new[:frame], f_drain(x_new)[:frame], label='Drain', color='purple')

                for i in range(frame):
                    if i % 100 == 0:  # Mostrar apenas a cada 100 pontos (ajuste conforme necessário)
                        ax.scatter(x_new[i], f_temp(x_new[i]), c='red')
                        ax.scatter(x_new[i], f_rec(x_new[i]), c='red')
                        ax.scatter(x_new[i], f_biogas(x_new[i]), c='red')
                        ax.scatter(x_new[i], f_drain(x_new[i]), c='red')

                ax.set_xlabel('Days')
                ax.set_ylabel('Data')
                ax.set_title('Biogas Data')

                ax.legend()
                ax.grid()

        ani = FuncAnimation(fig, update, frames=1000, interval=1, repeat=False)
        plt.show()## mudar para que o usuário coloque o nome do arquivo
        ani.save('animacao_grafico_ciclo_120.gif', writer=PillowWriter(fps=30))
    
    def post_hoc(self):
        median_temp_biogas = np.median(self.temp_biodigester)
        median_recirculation = np.median(self.recirculation)
        median_drain = np.median(self.drain)
        median_biogas_prod = np.median(self.biogas_prod)
        median_hp_inf = np.median(self.hp_inf)
        median_hp_sup = np.median(self.hp_sup)

        # Imprimir os resultados
        print("Mediana - Temperature Biodigester:", median_temp_biogas)
        print("Mediana - Recirculation:", median_recirculation)
        print("Mediana - Drain:", median_drain)
        print("Mediana - Biogas Prod:", median_biogas_prod)
        print("Mediana - hp Inf:", median_hp_inf)
        print("Mediana - hp Sup:", median_hp_sup)

        # Dados das medianas
        variaveis = ['Temperatura Biodigestor', 'Recirculação', 'Drenagem', 'Produção de Biogás', 'hp Inferior', 'hp Superior']
        medianas = [median_temp_biogas, median_recirculation, median_drain, median_biogas_prod, median_hp_inf, median_hp_sup]

        # Criar o gráfico de barras
        plt.bar(variaveis, medianas)

        # Adicionar rótulos aos eixos e título ao gráfico
        plt.xlabel('Variáveis')
        plt.ylabel('Mediana')
        plt.title('Medianas das Variáveis')

        # Exibir o gráfico
        plt.show()
    
    ##Maintenance
    def spearman_calc(self, x, y):
       '''Calculate Spearman correlation and plot scatter with regression line'''
       correlation, p_value = spearmanr(x,y)
       plt.figure(figsize=(8,6))
       sns.regplot(x=x, y=y, color='b')
       plt.xlabel('Temperatura Biodigestor')
       plt.ylabel('Produção Biogás')
       plt.title('Gráfico de Dispersão e Regressão Linear')
       plt.text(0.5, 0.9, f"Coeficiente de correlação: {correlation:.4f}, Valor-p: {p_value:.4f}", fontsize=9, color='r', transform=plt.gca().transAxes)
       plt.show()       
    
    def shapiro_will():
        pass      

    def mannwhitneyu_boxplot(self, variable_name, *datasets):
        results = []
        labels = []
        colors = ['lightblue', 'lightgreen', 'lightpink', 'lightyellow']

        # Validate datasets
        for dataset in datasets:
            if not isinstance(dataset, (list, np.ndarray)):
                raise ValueError("Os conjuntos de dados devem ser listas ou arrays.")

        lengths = [len(dataset) for dataset in datasets]
        if len(set(lengths)) != 1:
            raise ValueError("Os conjuntos de dados devem ter o mesmo comprimento.")

        # Calculate Mann-Whitney U and collect results
        for i in range(len(datasets)):
            for j in range(i + 1, len(datasets)):
                statistic, pvalue = stats.mannwhitneyu(datasets[i], datasets[j])
                results.append((statistic, pvalue))
                labels.append(f'Ciclo {i + 1} vs Ciclo {j + 1}')

        # Plotting
        plt.boxplot(datasets, labels=['Ciclo 1', 'Ciclo 2', 'Ciclo 3', 'Média Final'])

        for patch, color in zip(plt.boxplot(datasets, patch_artist=True)['boxes'], colors):
            patch.set_facecolor(color)

        plt.title(variable_name)

        # Calculate significant outliers
        significant_outliers = [
            dataset[outlier] for dataset, (statistic, pvalue) in zip(datasets, results)
            if pvalue < 0.05 for outlier in np.where(stats.zscore(dataset) > 3)[0]
        ]

        plt.plot([], marker='*', linestyle='none', color='red', markersize=10, label='Outliers Significativos')
        plt.legend()
        plt.show()



#Functions
def plot_correlation_heatmap(data, title):
    plt.figure(figsize=(8, 6))

    # Mostra os valores somente quando as posições são diferentes
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i][j] is not None and i != j:
                plt.text(j, i, f'{data[i][j]:.2f}', ha='center', va='center', color='black')
            else:
                plt.text(j, i, 'N/A', ha='center', va='center', color='black')

    plt.imshow(data, cmap='coolwarm', interpolation='nearest')
    plt.colorbar(label='Correlation')
    plt.title(title)
    plt.xticks(np.arange(len(data)), ['Dias', 'T. Biod.', 'Recirc.', 'Dren.', 'Biogás', 'pH sup.', 'pH inf.', 'Alcalin.'])
    plt.yticks(np.arange(len(data)), ['Dias', 'T. Biod.', 'Recirc.', 'Dren.', 'Biogás', 'pH sup.', 'pH inf.', 'Alcalin.'])
    plt.tight_layout()
    plt.show()

