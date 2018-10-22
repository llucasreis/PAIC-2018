# Datasets

- Diretório destinado a armazenar as várias versões do *dataset* que serão desenvolvidas.
- Atualmente os dados não estão sendo armazenados em arquivos `.csv` ou em *DataFrame*, apenas está sendo criado *data's providers* e sendo lidos a partir de outros códigos.
- O projeto irá utilizar uma abordagem de filtragem híbrida, ou seja, terá um *dataset* para a filtragem colaborativa e um para filtragem baseada em conteúdo.

## Filtragem Baseada em Conteúdo

### 1ª Versão

Para o primeiro *dataset*, os dados dos candidatos foram obtidos diretamente de suas propostas presentes na pasta `propostas-candidatos` , e o código desenvolvido encontra-se em `algoritmos/data-provider.py` .

A ideia consiste em inicialmente gerar uma lista com todas as palavras presentes no arquivo pdf,  neste processo ocorre uma filtragem de palavras para remover ascentos, caracteres especiais, pontuações, artigos, etc.  Após isso, é criado um dicionário ordenado com a contagens das palvaras. Por fim, a partir das áreas como: saúde, segurança, educação, economia, cultura, tecnologia e meio ambiente, é feito uma busca por palavras relacionadas à àrea somando os valores da contagem feita anteriormente.

Portanto, temos um dicionário por candidato de cada uma área de interesse, com a ocorrência de quantas vezes foi citado alguma palavra relacionada a tal área.

**Problemas**: O maioir problema desta abordagem é que alguns candidatos possuem muitas páginas em suas propostas, Guilherme Boulos possui cerca de 200 páginas, e outros candidatos possuem poucas páginas. Assim, alguns candidatos possuem vários altos para cada área e outros com valores baixos. Além disso, existe uma margem de erros para as palavras que são obtidas, de forma que algumas fazem parte da contagem mas não relacionado a área.

**Obs.:** Não foi possível obter a proposta do candidato Eymael.

## Filtragem Colaborativa

### 1ª Versão

Para o primeiro *dataset*, as linhas corresponderão aos usuários (eleitores) e as colunas irão corresponder aos candidatos. Assim como na filtragem baseada em conteúdo, cada candidato representa um dicionário onde cada um possui as áreas de interesse, mas dessa vez os valores serão notas atribuídas de 1 a 5 por pessoas, atualmente está utilizando uma geração automática de notas de eleitores, criado em `voters_provider.py`  . 

Por fim, após obter as notas individuais de cada área para cada candidato, é feito uma média dessas notas e assim é gerado a nota do eleitor para cada candidato. O código desenvolvido para fazer a leitura desses dados e realizar a recomendação corresponde ao `candidates.py`.

**Problemas**: Como está sendo utilizado a média para o cálculo da nota e os valores não possuem um intervalo alto, grande partes dos valores está tendendo à se estabilizar em 3, prejudicando a recomendação. Como atuamente está sendo utilizado dados fictícios para a recomendação, pode-se acabar não tendo uma visão real da recomendação para cada eleitor.

### 2ª Versão

A segunda versão do *dataset* foi criada em `voters_provider_2.py`, a principal diferença é que as notas agora são atribuídas diretamente aos candidatos, ao invés de suas áreas, para assim evitar o problema dos dados permanecerem na média do intervalo.

**Problemas**: Novamente os dados são fictícios e portanto não é possível obter uma visão real do comportamento da recomendação para eleitores reais.