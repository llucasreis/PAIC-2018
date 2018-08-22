# Aula 01

## Sistemas de Recomendação

* O **Sistema de Recomendação (SR)** combina várias técnicas computacionais para selecionar itens personalizados com base nos interesses dos usuários e conforme o contexto no qual estão inseridos
* O objetivo dos SR é gerar recomendações válidas de itens que possam interessar aos usuários
* Sistema de Recomendação é um conjunto de algoritmos que utilizam técnicas de **Aprendizagem de Máquina** e **Recuperação da Informação** para gerar recomendações baseadas em algum tipo de filtragem, as mais comuns são:
  * **colaborativa**: considera a experiência de todos os usuários
  * **baseada em conteúdo**: considera a experiência do usuário alvo
  * **híbrida**: as duas abordagens são consideradas
  * **conhecimento**: considera o conhecimento a cerca do usuário alvo

## Filtragem Colaborativa

* São amplamente utilizados no ramo de *e-commerce* e também em Redes Sociais
* O usuário recebe recomendações baseadas nas avaliações passadas de todos os usuários, coletivamente

## Filtragem Baseada em Conteúdo

* Fazem a sugestão de itens que sejam semelhantes aos que o usuário demonstrou interesse no passado, e/ou sobre as configurações de preferência do usuário
* Assim, as recomendações são personalizadas para cada usuário

## Filtragem baseda em Conhecimento

* Utiliza as técnicas de classificação de Aprendizagem de Máquina
* Pode-se prever qual o gênero de filme o usuário gostaria de ver, e também estimar se este filme será ou não apreciado pelo usuário
* Os algoritmos mais utilizados são: KNN, Árvores de Decisão, Bayes Classifier, SVM, Redes Neurais

## Filtragem Híbrida

* Pode-se produzir listas separadas de recomendação (de cada abordagem) e unir seus resultados para produzir uma lista final
* Utilizando pesos para os tipos de filtragem, podemos valorizar itens que receberem mais acessos

## Similaridade de Item/Usuário

* A **similaridade** consiste em descobrir itens similares aos que o usuário já adquiriu ou usuários mais similares entre si (vizinho mais próximo)
* Utilizando as avaliações e preferência de todos os usuários, pode-se calcular a similaridade entre esses usuários e o usuário alvo
* Pode ser determinada por meio dos cálculos de:
  * Distância euclidiana
  * Distância de manhattan
  * Cosseno do ângulo entre vetores
  * Correlação de Pearson, etc

