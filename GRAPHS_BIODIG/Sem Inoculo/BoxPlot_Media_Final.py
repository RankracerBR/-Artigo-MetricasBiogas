import Media_FinaL_Sem_Inoculo as mf
import Automatic_Calcs as Acs
import Ciclo_1 as c1
import Ciclo_2 as c2
import Ciclo_3 as c3




##manutenção
if __name__ == "__main__":
    Acs.Calculate.mannwhitneyu_boxplot(c1.temperatura_biodig, c2.temperatura_biodig, c3.temperatura_biodig,mf.temperatura_biodig, 'Temperatura')

    # Recirculação
    Acs.Calculate.mannwhitneyu_boxplot(c1.recirculacao, c2.recirculacao, c3.recirculacao,mf.recirculacao, 'Recirculação')

    # Drenagem
    Acs.Calculate.mannwhitneyu_boxplot(c1.drenagem, c2.drenagem, c3.drenagem,mf.drenagem, 'Drenagem')

    # Produção Biogás
    Acs.Calculate.mannwhitneyu_boxplot(c1.producao_biogas, c2.producao_biogas, c3.producao_biodig, mf.producao_biogas,'Produção Biogás')

    # Ph Inferior
    Acs.Calculate.mannwhitneyu_boxplot(c1.ph_inferior, c2.ph_inferior, c3.ph_inferior, mf.ph_inferior, 'Ph Inferior')

    # Ph Superior
    Acs.Calculate.mannwhitneyu_boxplot(c1.ph_superior, c2.ph_superior, c3.ph_superior, mf.ph_superior, 'Ph Superior')
