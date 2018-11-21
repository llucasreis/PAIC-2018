
# Visualizando *Datasets*

Este arquivo servirá para facilitar a visualização dos *datasets* desenvolvidos, utilizando a biblioteca `pandas`

# Importação das bibliotecas


```python
import pandas as pd
import candidate_provider as cp
import candidate_provider_2 as cp2
import voter_provider as vp
import voter_provider_2 as vp2
import numpy as np
import matplotlib.pyplot as plt
```

## *Dataset* de Candidatos

Foram desenvolvidos dois *datasets* compostos por candidatos para realizar a filtragem baseada em conteúdo

O primeiro *dataset* consiste em uma análise feita nas propostas de cada candidato, gerando um *dataset* da contagem de palavras por área de interesse.

As áreas de interesse são: saúde, segurança, educação, economia, cultura, tecnologia e meio ambiente


```python
candidates = ['alckmin', 'alvaro', 'amoedo', 'bolsonaro', 'boulos', 'ciro', 'daciolo', 'haddad', 'marina', 'meirelles']
```


```python
df_cand = {}
for cand in candidates:
    df_cand[cand] = cp.count_words_from(cand)
```


```python
df_cand = pd.DataFrame(data=df_cand).T
```


```python
df_cand
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cultura</th>
      <th>economia</th>
      <th>educacao</th>
      <th>meio ambiente</th>
      <th>saude</th>
      <th>seguranca</th>
      <th>tecnologia</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>alckmin</th>
      <td>8</td>
      <td>30</td>
      <td>11</td>
      <td>2</td>
      <td>6</td>
      <td>14</td>
      <td>9</td>
    </tr>
    <tr>
      <th>alvaro</th>
      <td>33</td>
      <td>55</td>
      <td>9</td>
      <td>8</td>
      <td>9</td>
      <td>7</td>
      <td>14</td>
    </tr>
    <tr>
      <th>amoedo</th>
      <td>7</td>
      <td>56</td>
      <td>35</td>
      <td>16</td>
      <td>13</td>
      <td>22</td>
      <td>12</td>
    </tr>
    <tr>
      <th>bolsonaro</th>
      <td>17</td>
      <td>128</td>
      <td>47</td>
      <td>15</td>
      <td>28</td>
      <td>40</td>
      <td>44</td>
    </tr>
    <tr>
      <th>boulos</th>
      <td>315</td>
      <td>823</td>
      <td>297</td>
      <td>119</td>
      <td>165</td>
      <td>360</td>
      <td>267</td>
    </tr>
    <tr>
      <th>ciro</th>
      <td>67</td>
      <td>376</td>
      <td>155</td>
      <td>44</td>
      <td>59</td>
      <td>110</td>
      <td>111</td>
    </tr>
    <tr>
      <th>daciolo</th>
      <td>5</td>
      <td>53</td>
      <td>74</td>
      <td>3</td>
      <td>40</td>
      <td>46</td>
      <td>20</td>
    </tr>
    <tr>
      <th>haddad</th>
      <td>180</td>
      <td>534</td>
      <td>195</td>
      <td>84</td>
      <td>76</td>
      <td>125</td>
      <td>177</td>
    </tr>
    <tr>
      <th>marina</th>
      <td>98</td>
      <td>273</td>
      <td>83</td>
      <td>58</td>
      <td>62</td>
      <td>75</td>
      <td>102</td>
    </tr>
    <tr>
      <th>meirelles</th>
      <td>6</td>
      <td>40</td>
      <td>20</td>
      <td>8</td>
      <td>17</td>
      <td>24</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



O segundo *dataset* analisa as mesmas propostas, porém esta abordagem busca verificar o quão importante tal área é importante para o candidato, utilizando a métrica **TF-IDF**. Atualmente este método não consegue analisa todas as propostas em *pdf* por conta da biblioteca utilizada.


```python
candidates = ['bolsonaro', 'ciro', 'daciolo','boulos', 'haddad', 'marina']
```


```python
df_cand_2 = {}
for cand in candidates:
    df_cand_2[cand] = cp2.getCand(cand)
```


```python
df_cand_2 = pd.DataFrame(data=df_cand_2).T
```


```python
df_cand_2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cultura</th>
      <th>economia</th>
      <th>educacao</th>
      <th>meio ambiente</th>
      <th>saude</th>
      <th>seguranca</th>
      <th>tecnologia</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bolsonaro</th>
      <td>1.298674</td>
      <td>2.101016</td>
      <td>2.217653</td>
      <td>0.943479</td>
      <td>2.067089</td>
      <td>1.916048</td>
      <td>1.124516</td>
    </tr>
    <tr>
      <th>ciro</th>
      <td>0.577953</td>
      <td>1.572047</td>
      <td>0.973766</td>
      <td>0.467057</td>
      <td>0.755462</td>
      <td>0.962723</td>
      <td>0.702406</td>
    </tr>
    <tr>
      <th>daciolo</th>
      <td>0.053222</td>
      <td>0.286808</td>
      <td>0.513717</td>
      <td>0.062666</td>
      <td>0.368084</td>
      <td>0.325294</td>
      <td>0.154583</td>
    </tr>
    <tr>
      <th>boulos</th>
      <td>1.929544</td>
      <td>3.294471</td>
      <td>2.777466</td>
      <td>1.666706</td>
      <td>2.350678</td>
      <td>2.757596</td>
      <td>2.078143</td>
    </tr>
    <tr>
      <th>haddad</th>
      <td>0.453759</td>
      <td>1.045867</td>
      <td>0.665708</td>
      <td>0.252479</td>
      <td>0.404181</td>
      <td>0.394746</td>
      <td>0.443712</td>
    </tr>
    <tr>
      <th>marina</th>
      <td>0.163086</td>
      <td>0.434171</td>
      <td>0.229158</td>
      <td>0.100869</td>
      <td>0.257830</td>
      <td>0.163831</td>
      <td>0.200668</td>
    </tr>
  </tbody>
</table>
</div>



## *Dataset* de Eleitores

Atualmente está sendo feito um levantamento de dados da opinião de usuários sobre cada candidato, este *dataset* ainda não foi inserido em algum algoritmo, mas já pode ser visualizado.


```python
df_voter = pd.read_csv('../dados-pesquisa/avaliacao.csv')
```

### Pré-processamento de Dados

Este *dataset* foi obtido diretamente do *Google* formulário, assim precisa inicialmente realizar algumas modificações.


```python
df_voter.drop(['Carimbo de data/hora'],axis=1,inplace=True)
```


```python
voters = [str(i) for i in range(1,len(df_voter)+1)]
```


```python
df_voter.insert(loc=0, column='eleitor', value=voters)
```


```python
df_voter
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>eleitor</th>
      <th>Geraldo Alckmin</th>
      <th>João Amoêdo</th>
      <th>Jair Bolsonaro</th>
      <th>Guilherme Boulos</th>
      <th>Ciro Gomes</th>
      <th>Marina Silva</th>
      <th>Fernando Haddad</th>
      <th>Cabo Daciolo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>4</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>5</td>
      <td>4</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>2</td>
      <td>5</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>1</td>
      <td>4</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>2</td>
      <td>5</td>
      <td>4</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>2</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>3</td>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>1</td>
      <td>5</td>
      <td>4</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>3</td>
      <td>4</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>5</td>
      <td>5</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>1</td>
      <td>3</td>
      <td>5</td>
      <td>1</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>1</td>
      <td>5</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>1</td>
      <td>5</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>2</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_voter_2 = vp2.getVoters()
```


```python
df_voter_2 = pd.DataFrame(data=df_voter_2)
```


```python
df_voter_2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>voter1</th>
      <th>voter2</th>
      <th>voter3</th>
      <th>voter4</th>
      <th>voter5</th>
      <th>voter6</th>
      <th>voter7</th>
      <th>voter8</th>
      <th>voter9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>alckmin</th>
      <td>4.0</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>3</td>
      <td>1.0</td>
      <td>5</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>alvaro</th>
      <td>1.0</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>2</td>
      <td>1.0</td>
      <td>3</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>amoedo</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>2</td>
      <td>NaN</td>
      <td>3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>bolsonaro</th>
      <td>5.0</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>3</td>
      <td>4.0</td>
      <td>3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>boulos</th>
      <td>5.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>5</td>
      <td>5.0</td>
      <td>1</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>ciro</th>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>4</td>
      <td>3.0</td>
      <td>4</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>daciolo</th>
      <td>NaN</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>3</td>
      <td>4.0</td>
      <td>1</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>goulart</th>
      <td>5.0</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>1</td>
      <td>NaN</td>
      <td>5</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>haddad</th>
      <td>4.0</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>4</td>
      <td>4.0</td>
      <td>3</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>marina</th>
      <td>NaN</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>3.0</td>
      <td>5</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>meirelles</th>
      <td>NaN</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>4</td>
      <td>NaN</td>
      <td>3</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



O terceiro *dataset* foi calculado a partir das notas individuais de cada eleitor para cada área de interesse, assim foi realizado uma média, o *dataset* final é semelhante aos anteriores.


```python
def rateOfCandidates(voter):
    for candidate in voter:
        rating = list(voter[candidate].values())
        voter[candidate] = np.median(rating)
    return voter
```


```python
df_voters = vp.getVoters()
```


```python
df_voter_3 = {}
for voter, voter_rate in df_voters.items():
    df_voter_3[voter] = rateOfCandidates(voter_rate)
```


```python
df_voter_3 = pd.DataFrame(data=df_voter_3)
```


```python
df_voter_3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>voter1</th>
      <th>voter2</th>
      <th>voter3</th>
      <th>voter4</th>
      <th>voter5</th>
      <th>voter6</th>
      <th>voter7</th>
      <th>voter8</th>
      <th>voter9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>alckmin</th>
      <td>NaN</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>alvaro</th>
      <td>NaN</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>amoedo</th>
      <td>4.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>bolsonaro</th>
      <td>2.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>boulos</th>
      <td>NaN</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>ciro</th>
      <td>3.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>daciolo</th>
      <td>3.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>goulart</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>haddad</th>
      <td>4.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>marina</th>
      <td>NaN</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>meirelles</th>
      <td>NaN</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
