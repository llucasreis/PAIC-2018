# Aula 05

## Similaridade Cosseno

* É uma métrica de similaridade muito popular em Recuperação de Informação, empregada na implementação de máquinas de busca, mineração de texto e técnicas de filtragem de informação

* A similaridade cosseno varia entre -1 e 1

  * 1 indica semelhança perfeita
  * -1 indica semelhança negativa

* Ela trabalha com dois vetores sem zero utilizando o produto interno entre eles para mensurar o cosseno do ângulo entre eles

  ![](https://qph.fs.quoracdn.net/main-qimg-fd48a47fdc134d6fc9b58cd86fdf244b)

  ### Qual medida de similaridade usar?

  * Se os dados estiverem sujeitos a grau de inflação (diferentes usuários podem estar usando diferentes escalas) use **Pearson**
  * Se os dados forem esparsos considere usar **Similaridade Cosseno**
  * Se seus dados forem densos (quase todos os atributos não são nulos valores) use medidas de distância como **euclidiana** ou **Manhattan** 

A implementação da similaridade cosseno foi feita em `users.py` 