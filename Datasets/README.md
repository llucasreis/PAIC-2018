# Datasets

Diretório destinado a armazenar as várias versões do *dataset* que serão desenvolvidas

## 1ª versão

Para o primeiro *dataset*, os dados dos candidatos foram obtidos diretamente de suas propostas presentes na pasta `propostas-candidatos` , e o código desenvolvido encontra-se em `algoritmos/data-provider.py` .

A ideia consiste em inicialmente gerar uma lista com todas as palavras presentes no arquivo pdf,  neste processo ocorre uma filtragem de palavras para remover ascentos, caracteres especiais, pontuações, artigos, etc.  Após isso, é criado um dicionário ordenado com a contagens das palvaras. Por fim, a partir das áreas como: saúde, segurança, educação, economia, cultura, tecnologia e meio ambiente, é feito uma busca por palavras relacionadas à àrea somando os valores da contagem feita anteriormente.

Portanto, temos um dicionário por candidato de cada uma área de interesse, com a ocorrência de quantas vezes foi citado alguma palavra relacionada a tal área.

**Problemas**: O maioir problema desta abordagem é que alguns candidatos possuem muitas páginas em suas propostas, Guilherme Boulos possui cerca de 200 páginas, e outros candidatos possuem poucas páginas. Assim, alguns candidatos possuem vários altos para cada área e outros com valores baixos. Além disso, existe uma margem de erros para as palavras que são obtidas, de forma que algumas fazem parte da contagem mas não relacionado a área.

**Obs.:** Não foi possível obter a proposta do candidato Eymael.