# Trabalhos Relacionados

Para auxiliar o desenvolvimento do trabalho, procurou-se por trabalhos ou projetos relacionados à recomendação e análise de candidatos à orgãos públicos.

O [Portal da Transparência](https://www.transparencia.org.br/) possui um repositório de informações públicas sobre obras, projetos e políticos. O site pode ajudar a obter dados (através de *data mining*) para o *dataset* .

O site Iceberg disponibilizou no [site](https://oiceberg.com.br/calculadora/)  a **Calculadora de Afinidade Eleitoral 2018** um sistema ao que será desenvolvido para o projeto, onde para cada área deve-se responder uma pergunta, a diferença é que para o projeto será colocado a afinidade para cada área. O site também disponibilizou os dados que utilizaram, tanto o [dataset](https://n6f4c4k8.stackpathcdn.com/wp-content/uploads/2018/08/mapeamento-presidenciaveis-2018-v4-1024x576.png) quanto os [links](https://docs.google.com/spreadsheets/d/1IzuNdR6IBP0f3oBTfkyIGvS9TSWloqfuC_5b5WOyQoQ/edit#gid=107546370)  utilizados para minerar os dados e a [ideia](https://www.facebook.com/lacerda8000/posts/2044465275563986) original.

### Critérios - Calculadoradora - Iceberg

Para calcular a afinidade entre o usuário e os presidenciáveis adotou-se a seguinte abordagem. Se o candidato ou o usuário estão divididos no assunto, ou se a posição do candidato ainda não foi mapeada, soma-se 0,5. Quando as posições são idênticas, adiciona-se 1 ponto. Quando são divergentes - a posição do usuário e do candidato são opostas - não se soma nada. Por fim, calcula-se o percentual de afinidade tendo como base o total dos 23 pontos disponíveis. As frases foram ajustadas visando maior clareza e coesão.	



O artigo [Ferramentas tecnológicas para ajudar a decidir o seu voto](https://tecnoblog.net/163880/eleicoes-aplicativos-votos/) publicado na web reuniu diversas ferramentas que fazem análises e recomendações de candidatos. Em específico, o **Projeto Brasil** apresenta uma proposta semelhante ao que será desenvolvido. Atualmente o projeto aparenta ter sido cancelado (assim como outras ferramentas mostradas) mas o seu [repositório do Github](https://github.com/ProjetoBrasil) ainda está disponível para consultas.

No site Época, publicou-se o artigo [10 aplicativos e sites que ajudam a decidir em quem votar](https://epocanegocios.globo.com/Informacao/Acao/noticia/2014/10/10-aplicativos-e-sites-que-ajudam-decidir-em-quem-votar.html) que também reuniu ferramentas, a maioria *mobiles*, para a análise de candidatos. Novamente algumas ferramentas não encontram-se mais disponíveis. Além dos dez aplicativos, também foi citado as ferramentas [Appoie](https://www.appoie.com/) e [#Temmeuvoto](https://temmeuvoto.com/) 

O artigo web [Aplicativos e sites ajudam a esmiuçar a vida dos candidadtos nas eleições](https://www.em.com.br/app/noticia/tecnologia/2014/09/25/interna_tecnologia,572574/aplicativos-e-sites-ajudam-a-esmiucar-a-vida-dos-candidatos-nas-eleicoes.shtml) também apresentou alguams ferramentas que podem ser utilizadas

