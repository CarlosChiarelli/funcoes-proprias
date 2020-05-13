from setuptools import setup

setup(name='funcoesProprias',
      version='0.1',
      description='funções utilizadas no dia-a-dia de um cientista de dados',
      url='http://github.com/CarlosChiarelli/funcoes-proprias',
      author='Carlos Augusto Chiarelli',
      author_email='ca.chiarelli.97@gmail.com',
      license='MIT',
      packages=['funcoesProprias'],
      # pacotes em uso não adicionados (estão na base): "re", "unicodedata"
      install_requires=['pandas >= 1.0.3', 'numpy >= 1.18.2', 'matplotlib >= 3.2.1',
                        'seaborn >= 0.10.0', 'scipy >= 1.4.1', 'statsmodels >= 0.11.1'],
      zip_safe=False)
