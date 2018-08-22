# Sistemas de Recomendação

Anotações do curso Inteligência Artificial: Sistemas de Recomendação em Python da Udemy.

Um sistema de recomendação tem como objetivo selecionar itens personalizados com base nos interesses dos usuários

Alguns tipos de sistemas de recomendação:

* Recuperação direta da informação
  * Os mais vendidos, os mais clicados, etc.
* Filtragem por conteúdo
  * Conteúdo dos itens
  * Comparação da descrição dos itens
* Filtragem colaborativa
  * Perguntar para amigos
  * Prever o grau de interesse sobre um item baseado nas avaliações feitas por esse cliente e as avaliações feitas por outros clientes com perfil semelhante
  * Tarefa cooperativa entre um ou mais usuários

Alguns modos usuais de calcular a similaridade entre usuários (preferências similares):

* Escala de distância euclidiana
* Escala de correlação de Pearson

Para o cálculo de similiaridade pode-se utilizar uma escala de porcentagem, assim variando entre 0 e 1.

 ## Recomendando filmes

* Encontrar alguém semelhante para ler as avaliações
  * Problemas:
    * Pessoas que não tenham feito avaliações sobre filmes que pode ser de interesse
    * Pessoas que tenham gostado de filmes mal avaliados por todos os demais
  * Para resolver esses problemas, pode-se atribuir notas usando média ponderada (**peso**).
    * Pessoas mais parecidas com você, terão mais peso na avaliação e pessoas menos parecidas, terão um peso menor.
* Para cada campo, é cálculo uma similiaridade para eles, multiplicando-se a nota dada no filme pela similaridade com o usuário

### Filtragem baseada em itens

* **Problemas ** :
  * Um sistema com muitos produtos pode apresentar pouca semelhança entre usuários
  * Conjunto de dados podem ser muito grandes

* Esse tipo de filtragem permite que os cálculos sejam feitos **antecipadamente** para retornar recomendações mais rapidamente
* Comparações entre itens não mudarão com tanta frequência quanto comparações entre usuários

## Filtragem baseada em Usuários x Itens

* **Usuários**:
  * Mais simples para implementar
  * Indicada para conjuntos de dados menores (mantido integralmente em memória)
  * Somente o cálculo de similaridade já pode ser útil
* **Itens**:
  * Mais rápida
  * Indicada para grandes conjunto de dados
  * Necessita manter a tabela de similaridade de itens

## Conjunto de dados

* **Denso**
  * As pessoas deram notas para quase todos os produtos
* **Esparso**
  * As pessoas deram notas para produtos diferentes (grupo de pessoas)
* Recomendação baseada em itens possui desempenho melhor com dados esparsos
* Ambas as recomendações possuem desempenho similar com dados densos