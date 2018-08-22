# Aula 02

## Filtragem Colaborativa

* Entrada
  * uma matriz de avaliações de itens de usuário
* Tipos de Saída
  * Uma previsão (numérica) indicando até que ponto o usuário atual gostará ou não de um determinado item
  * Uma lista top-N de itens recomendados

### Encontrar o usuário mais semelhante

* **Distância de Manhattan**:
  * A métrica de similaridade mais fácil para calcular, além de ser a mais rápida também
  	 Cada pessoa é representada por um ponto (x,y) em um plano 2D	
  * Em python, a distância de Manhattan pode ser calculada por:
  ```python
  dist = abs(x1 - x2) + abs(y1 - y2)
  ```

* **Distância Euclidiana**:
  * Calcular a distância utilizando o teorema de pitagoras
  * Em python, a distância euclidiana pode ser calculada por:
  ```python
  dist = sqrt(pow(x1 - x2,2) + pow(y1 - y2,2))
  ```

Foi feita a implementação da filtragem colaborativa com a distância de Manhattan, junto com a recomendação para o usuário no código `users.py` 