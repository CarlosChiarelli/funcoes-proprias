# funções em Python 3 para manipulação de dados
def mostrarTodasColsJupyter(nCols=1000, nLinhas=1000):
    # essa função permite que o jupyter mostre todas colunas
    # além de configurar outras coisas
    from pandas import set_option

    options = {
    'display': {
        'max_columns': nCols,
        #'max_colwidth': 25,
        #'expand_frame_repr': False,  # Don't wrap to multiple pages
        'max_rows': nLinhas#,
        #'max_seq_items': 50,         # Max length of printed sequence
        #'precision': 2,
        #'show_dimensions': False
    }#,
    #'mode': {
    #    'chained_assignment': None   # Controls SettingWithCopyWarning
    #}
}
    for category, option in options.items():
        for op, value in option.items():
            set_option(f'{category}.{op}', value)  # Python 3.6+

def temaPlot():
    # configura um tema dos graficos para o fundo dark do jupyter notebook
    import matplotlib.pyplot as plt
    from matplotlib import style
    plt.style.use('classic')

def configuraJupyter():
    # seta mostrar numero de colunas e tema plots para fundo dark
    mostrarTodasColsJupyter()
    temaPlot()

def dfExploracao(df):
    # retorna df com nomes, tipos, percentual de NAs e contagem unicos da coluna
    from pandas import DataFrame
    explora = DataFrame(data = {'colunas':list(df.columns),
                        'tipos':list(df.dtypes),
                        'na_perct':df.isna().sum() / df.shape[0],
                        'quantUnicos': df.nunique()})
    # removendo indice
    explora.reset_index(inplace=True)
    explora.drop('index', axis=1, inplace=True)
    return explora

def limpaNomesCols(df, subEspacoUnderl = False):
    # retorna lista das colunas limpas
    # minusculas, espaços por _ , sem espaços nas pontas
    #df.columns = [x.lower().lstrip().rstrip().replace(' ','_', regex=False) for x in df.columns]
    if not subEspacoUnderl:
        nomesCols = [x.lower().lstrip().rstrip() for x in df.columns]
    else:
        nomesCols = [x.lower().lstrip().rstrip().replace(' ','_') for x in df.columns]

    return nomesCols

def removeAcento(text):
    # recebe uma string, remove acentuação e retorna ela
    import unicodedata

    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text)

def limpaNomesColsPart2(listaNomesCols):
    # recebe uma lista com nome das colunas
    # remove caracteres especiais
    from re import sub

    # lista com nomes das colunas corrigidos
    nomesLimpos = []

    for x in listaNomesCols:
        aux = removeAcento(x).replace('%','porcent').replace(' ','_')
        aux = sub('\W','',aux)
        nomesLimpos.append(aux)

    return nomesLimpos
