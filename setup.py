#from setuptools import setup#, find_packages

# setup(
#     name='funcoesProprias',
#     version='1.0.0',
#     url='https://github.com/CarlosChiarelli/funcoes-proprias.git',
#     author='Carlos Augusto Chiarelli',
#     author_email='ca.chiarelli.97@gmail.com',
#     description='funções utilizadas no dia-a-dia de um cientista de dados',
#     #packages=find_packages(),
#     #packages=find_packages(include=['manipulacaoDados']),
#     packages=['manipulacaoDados'],
#     install_requires=['pandas >= 1.0.3', 'numpy >= 1.18.2']
#     #include_package_data=True
#     #scripts=['manipulacaoDados/manipulacaoDados.py']
# )

from setuptools import setup

setup(name='funcoesProprias',
      version='0.1',
      description='funções utilizadas no dia-a-dia de um cientista de dados',
      url='http://github.com/CarlosChiarelli/funcoes-proprias',
      author='Carlos Augusto Chiarelli',
      author_email='ca.chiarelli.97@gmail.com',
      license='MIT',
      packages=['funcoesProprias'],
      install_requires=['pandas >= 1.0.3', 'numpy >= 1.18.2', 'matplotlib >= 3.2.1', 'seaborn >= 0.10.0'],
      zip_safe=False)

# from setuptools import setup
#
# setup(name='funniest',
#       version='0.1',
#       description='The funniest joke in the world',
#       url='http://github.com/storborg/funniest',
#       author='Flying Circus',
#       author_email='flyingcircus@example.com',
#       license='MIT',
#       packages=['funniest'],
#       zip_safe=False)
