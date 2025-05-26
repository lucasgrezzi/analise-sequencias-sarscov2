# Análise de Sequências de SARS-CoV-2: Frequência de Pares de Bases e Porcentagem de GC

Este projeto consiste em um script Python que analisa sequências genômicas do SARS-CoV-2 presentes em um arquivo no formato FASTA. O objetivo principal é calcular a frequência dos pares de bases Adenina (A), Timina (T), Guanina (G) e Citosina (C), bem como determinar a porcentagem de Guanina e Citosina (GC) em cada sequência. Além disso, o script gera uma visualização gráfica combinando a composição das bases e a porcentagem de GC para cada variante analisada.

## Funcionalidades

O script realiza as seguintes etapas:

1.  **Importação de Dados:** Lê sequências genômicas de um arquivo FASTA.
2.  **Análise de Sequências:** Para cada sequência, identifica o ID e calcula o comprimento.
3.  **Contagem de Bases:** Determina a frequência dos pares de bases A-T e G-C.
4.  **Cálculo da Porcentagem de GC:** Calcula a proporção de bases G e C no total da sequência.
5.  **Visualização:** Gera um gráfico que exibe a composição das bases (A+T e G+C como barras empilhadas) e a porcentagem de GC (como uma linha sobreposta) para cada sequência identificada.

## Pré-requisitos

Para executar este script, você precisará ter o Python instalado e as seguintes bibliotecas:

* **pandas:** Embora não seja extensivamente usado no código atual, é uma biblioteca fundamental para análise de dados em Python e pode ser útil para futuras extensões.
* **Biopython (Bio.SeqIO):** Utilizada para ler e manipular arquivos no formato FASTA.
* **matplotlib:** Empregada para a criação de gráficos e visualizações.

Você pode instalar essas bibliotecas usando o `pip`:

```bash
pip install pandas biopython matplotlib

Como Usar
Salve o script: Salve o código Python em um arquivo com a extensão .py (por exemplo, analise_sequencias.py).

Prepare o arquivo FASTA: Certifique-se de ter o arquivo contendo as sequências do SARS-CoV-2 no formato FASTA.

Edite o caminho do arquivo: No script Python, localize a linha que define o caminho para o arquivo FASTA e atualize-o com o caminho correto para o seu arquivo:

Python

sars_cov = "C:/Users/Lucas/Downloads/sars_cov2_sequences.fasta" # <--- MODIFIQUE ESTE CAMINHO
Execute o script: Abra o terminal ou prompt de comando, navegue até o diretório onde você salvou o arquivo .py e execute o script:

Bash

python analise_sequencias.py
ou

Bash

python3 analise_sequencias.py
Saída Esperada
Ao executar o script, você verá no console informações sobre cada sequência processada, incluindo seu ID, comprimento, contagem de bases A+T, contagem de bases G+C e a porcentagem de GC. Além disso, uma janela com um gráfico será exibida, mostrando visualmente a composição das bases e a porcentagem de GC para cada variante.

Exemplo do Gráfico
(![Texto alternativo para a imagem]("C:/Users/Lucas/Desktop/ProjetosVSC/analise-sequencias-sarscov2/Figure_1.png"))

Próximos Passos e Melhorias Potenciais
Análise Estatística: Adicionar cálculos estatísticos como média, mediana, desvio padrão da porcentagem de GC entre as variantes.
Comparação de Variantes: Implementar funcionalidades para comparar a composição de bases e a porcentagem de GC entre diferentes grupos de variantes.
Salvar Resultados: Permitir que os resultados da análise (tabelas de dados, gráfico) sejam salvos em arquivos (por exemplo, CSV, PNG).
Tratamento de Erros: Adicionar um tratamento de erros mais robusto para lidar com arquivos FASTA mal formatados ou sequências inválidas.
Argumentos de Linha de Comando: Permitir que o caminho do arquivo FASTA seja fornecido como um argumento de linha de comando para maior flexibilidade.
Autor
LUCAS GREZZI (@lucasgrezzi)