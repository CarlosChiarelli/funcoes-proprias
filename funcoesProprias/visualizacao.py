def plotNumVsNum(df, tamanho=1):
    # plota todas colunas Numericas X todas colunas Numericas
    # matriz de dispersao (pontos)
    import matplotlib.pyplot as plt
    from pandas.plotting import scatter_matrix

    scatter_matrix(df, figsize=(12*tamanho,8*tamanho))

    print("TODAS COLUNAS NUMÉRICAS")
    plt.show()

def plotObjCols(df, numColsJuntas=2, tamanho=1):
    # recebe DF apenas com colunas de caracteres
    # e faz CONTAGEM em graficos de BARRA de CADA COLUNA
    # numColsJuntas= quant colunas , tamanho= [-10,10]
    # nada retorna, apenas plota
    import matplotlib.pyplot as plt
    from seaborn import countplot

    colunas = df.columns
    i = 0

    while i <= len(colunas):
        #plotaCont2em2(aux.iloc[:, i:i+numColsJuntas], )

        # selecioando colunas
        aux = df.iloc[:, i:i+numColsJuntas]
        # ajusta subplots
        fig, ax = plt.subplots(1, numColsJuntas, figsize=(12*tamanho,5*tamanho))

        # faz plots
        for j, nomeCol in enumerate(aux.columns):
            countplot(aux[nomeCol], ax=ax[j])
            plt.xticks(rotation = 30)
        # tira descricao
        fig.show()
        # incrementa
        i += numColsJuntas

    print('CONTAGEM DAS COLUNAS OBJECT')
    plt.show()

def plotNumVsNumReg(df):
    # plota matriz de dispersao com regressao
    from scipy.stats import pearsonr
    from seaborn import PairGrid,distplot,regplot
    import matplotlib.pyplot as plt

    def reg_coef(x,y,label=None,color=None,**kwargs):
        ax = plt.gca()
        r,p = pearsonr(x,y)
        ax.annotate('r = {:.2f}'.format(r), xy=(0.5,0.5), xycoords='axes fraction', ha='center')
        ax.set_axis_off()

    print('COLUNAS NUMERICAS - REGRESSÃO')
    g = PairGrid(iris)
    g.map_diag(distplot)
    g.map_lower(regplot)
    g.map_upper(reg_coef)
    plt.show()
