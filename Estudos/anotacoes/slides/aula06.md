# Aula 06

Existe a probabilidade do usuário mais similar ao usuário que queremos realizar a recomendação apresentar certos gostos opostos, e assim será feito a recomendação para o usuário, pois o algoritmo não verifica esta situação, apenas analisa se os usuários são similares

Para contornar esta situação, podemos usar a abordagem do k vizinhos mais próximos na filtragem colaborativa

## K-Nearest Neighbor

* Técnica de aprendizagem de máquina que pode ser empregada de duas formas para implementar a filtragem colaborativa:
  * Usa-se o KNN para obter as pessoas mais semelhantes para determinar as recomendações, onde k é o número de pessoas
  * Usa-se o KNN como um classificador para classificar se um determinado item, por exemplo, uma música, é revelante ou irrelevante para uma pessoa se baseando nas k pessoas mais próximas

### 1ª abordagem

* O valor de k é específico para cada aplicação, precisa-se realizar vários testes para determinar o número de pessoas que deseja-se utilizar
* Cada pessoa irá influenciar as recomendações, mas como determinar a influência de cada pessoa?
  * Em uma aplicação utilizando a correlação de Pearson, pode-se dividir o valor de cada pessoa pelo soma das pontuações Pearson, assim resultando na porcentagem de influência de cada pessoa
  * Após isso, somar as multiplicações das porcentagens pelas notas dada paras os itens

### 2ª abordagem

* Para utilizar o KNN é necessário:
  * Um conjunto de instâncias conhecidas (registros classifcados)
  * Definir uma métrica para calcular a distância (ou similaridade) entre a instância desconhecida e as instâncias conhecidas
    * A distância entre as instâncias pode ser calculada pela distância euclidiana ou outras métricas
  * Definir o valor de K (o número de vizinhos mais próximos que serão considerados pelo algoritmo)

* Predizer a classe para uma instância desconhecida com o KNN consiste nas seguintes atividades:
  * Calcular a distância entre a instância desconhecida e outras instâncias do conjunto de treinamento
  * Identificar os K vizinhos mais próximos (registros mais similares)
  * Utilizar o rótulo da classe dos vizinhos mais próximos para determinar o rótulo de classe da instância desconhecida
* **Vantagens**
  * Técnica simples e facilmente implementada
  * Bastante flexível

* **Desvantagens**
  * Pode ser um processo computacionalmente complexo
  * Requer um cálculo de distância para cada instância
  * A precisão pode ser degradada pela presença de atributos ou características irrelevantes