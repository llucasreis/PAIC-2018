# Aula 04

## Coeficiente de Correlação Pearson

* É uma métrica de similaridade entre duas variáveis (neste caso específico, a correlação entre os usuários X e Y).
* Ele varia entre -1 e 1 inclusive
  * 1 indica acordo perfeito
    * Um gráfico com uma linha reta tem um Pearson de 1
  * -1 indica desentendimento perfeito
* É usado quando usuários seguem um padrão de avaliação diferentes, criando uma variabilidade não esperada de dados, podendo criar problemas com um sistema de recomendaçao
* Podemos encontrar o indíviduo que é mais parecido com a pessoa que somos interessados em:

![](http://onlinestatbook.com/2/describing_bivariate_data/graphics/comp_formula.gif)

* Onde o somatório vai de *i* = 1 até *n* 

A correlação de Pearson foi implementada em em `users.py` 