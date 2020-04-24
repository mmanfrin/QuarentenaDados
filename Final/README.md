#Regulamento Desafio QuarentenaDados

**Como funcionará? **

A partir do desafio proposto na Aula 5, criar um modelo de Machine Learning para prever as notas da prova Linguagens e códigos, ENEM 2018, com base na nota das outras provas incluindo a redação.

Será utilizado o Erro Quadrático Médio como métrica de avaliação. O modelo vencedor será o que tiver o menor erro.

**Prêmio**

O aluno ou aluna que enviar o modelo vencedor ganhará 1 Nintendo Switch (Modelo Console Nintendo Switch 32GB ou de valor equivalente). O prêmio não poderá ser dividido ou revertido em dinheiro;

**Quem pode participar?**

 A competição é exclusiva para participantes inscritos na #QuarentenaDados até o dia 23/04. Colaboradores do grupo Caelum Alura não poderão participar.

**Prazo**

-   A competição terá inicio do dia 24/04/2020 até o dia 01/05/2020, sexta-feira, até às 23h59 horário de Brasília.

Sobre os dados para realizar o Desafio:
---------------------------------------

O dados serão uma amostra aleatória dos Microdados ENEM 2018, os quais podem ser acessados neste notebook do [Google Colab](https://colab.research.google.com/drive/1YVEM0uwtGBkm6EydYMqP0tyJN49Cm7XF), contendo a URL para os datasets e toda a informação necessária para criação do modelo.

Estão disponíveis no notebook os seguintes Dados:

-   dados_treino.csv - Contendo as notas das 4 provas mais nota da redação.

-   dados_teste.csv - Contendo as notas das 4 provas mais nota da redação

-   dados_desafioqt.csv Contendo a nota de 3 provas mais redação, a nota que deve ser prevista (linguagens e códigos) não estará disponível até o dia do resultado.

Sobre o envio do Desafio
------------------------

Você deve submeter seu resultado [neste link do Google Forms](https://docs.google.com/forms/d/e/1FAIpQLSdxEljb6lbw9vDRqLYXVNAs7F8PAZoJOG4guIkDDuChqeFiag/viewform).  O arquivo que será enviado deve ter o nome de PREDICAO_DESAFIOQT.csv e deve estar no seguinte padrão, Id e NU_NOTA_LC (Nota de predição) separados por vírgula:

id, NU_NOTA_LC

0, 620.00

1, 756.00

2, 564.00

[No colab notebook](https://colab.research.google.com/drive/1YVEM0uwtGBkm6EydYMqP0tyJN49Cm7XF) que você recebeu tem instruções detalhadas de como salvar e baixar seu arquivo de predição.

Regras para envio do desafio 
=============================

-   É necessário informar o mesmo e-mail que foi utilizado no cadastrado da #QuarentenaDados.

-   Não será permitido o uso de modelos pré-treinados.

-   Ganha quem tiver o Erro Quadrático Médio mais próximo de zero.

-   Em caso de empate vence quem submeteu o resultado primeiro, conforme horário registrado no envio do formulário. 

-   O resultado será divulgado até o dia 8/05/2020 e o envio do prêmio será feito em até 30 dias úteis após essa data.

-   Seja gentil :). É um desafio criado de última hora e usaremos o senso comum para qualquer ponto que esteja cinzento. 

-   Não teremos ranking automático, mas no twitter da Alura vamos falando os melhores resultados que recebemos com o tempo!
