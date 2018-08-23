# Aula 07

A filtragem colaborativa está comparando um usuário com todos os outros usuários para encontrar as correspondências mais próximas. Existem dois problemas principais com essa abordagem:

* **Escabilidade**
  * O cálculo aumenta à medida que o número de usuários aumenta
  * Os métodos baseados no usuário funcionam bem para centenas de usuários, mas a escabilidade chega a ser um problema quando temos um milhão de usuários
* **Dados esparsos**
  * Embora os sistemas de recomendação tem muitos usuários e muitos produtos, o usuário médio avalia uma pequena fração do total de produtos
  * Por isso, os algoritmos estudados podem não encontrar os vizinhos mais próximos

## Filtragem baseada em item

Para resolver este problema, pode-se utilizar a filtragem baseada em item.

* Nesta filtragem, encontramos os itens mais parecidos e combina-se isso com a avaliação de itens de um usuário para gerar uma recomendação

  * Se estivesse fazendo filtragem baseada em usuários, estaria determinando a similaridade entre linhas. Para a filtragem baseada em item, está sendo determinado a similaridade entre colunas

* Para calcular a similaridade entre itens, será utilizado similaridade de cosseno ajustado:

  ![](/home/lucas/PAIC-2018/Estudos/anotacoes/slides/cosine-adjust.png)
  * *U* é o conjunto de todos os usuários que classificaram os itens *i* e *j* . Significa que a avaliação *R* do usuário *u* dá ao item *i* menos a avaliação média que o usuário deu para todos os itens que avaliou.

* Antes de poder fazer a recomendação, precisa-se prever a avaliação que um usuário dará a um certo item. Utilizando a fórmula abaixo:

  ![](/home/lucas/PAIC-2018/Estudos/anotacoes/slides/prevision.png)

  * *N* é cada um dos itens que o usuário *u* avaliou que são similares ao item *i*

    * Por similar, quer dizer que há um valor de similaridade entre *N* e *i* em nossa matriz de similaridade

  * *Si,N* é a similaridade entre *i* e *N* (da matriz de similaridade)

  * *Ru,N* é a avaliação que o usuário *u* deu para o item *N*

    * Para obter melhores resultados, este valor deve estar na faixa de -1 a 1. Como as avaliações estão na faixa de 1 a 5, precisa-se de uma equação para converter ou normalizar as avaliações: 

      * **Normalizar**

      ![](/home/lucas/PAIC-2018/Estudos/anotacoes/slides/normalize.png)

      * **Desnormalizar**

        ![](/home/lucas/PAIC-2018/Estudos/anotacoes/slides/unnormalize.png)


A implementação da similaridade cosseno ajustada e a recomendação do usuário foram implementadas em `usersitem.py`.