import pandas as pd 
import Bio.SeqIO as SeqIO

## Importar o arquivo para estudo

sars_cov = "C:/Users/Lucas/Downloads/sars_cov2_sequences.fasta"

ids_sequencias = []
comprimentos = []
porcentagens_gc = []

for record in SeqIO.parse(sars_cov, "fasta"):
    print(f"ID da Sequencia:{record.id}")
    print(f"Comprimento da Sequencia: {len(record.seq)}")

    seq_id = record.id # Guarda o ID numa variável
    seq_length = len(record.seq) # Guarda o comprimento numa variável

#### Contar a frequencia dos pares de bases A e T, G e C e calcular a porcentagem de GC ####
    if record.seq.startswith(('A', 'C', 'T', 'G')):
        at_count = record.seq.count('A') + record.seq.count('T')
        gc_count =  record.seq.count('G') + record.seq.count('C')
        print(f"Contagem de A e T: {at_count}")   
        print(f"Contagem de G e C: {gc_count}")
        if (at_count + gc_count) > 0 :
            gc_percentage = (gc_count / (at_count + gc_count)) * 100
            print(f"Porcentagem de GC: {gc_percentage:.2f}%")
        ids_sequencias.append(seq_id)
        comprimentos.append(seq_length)
        porcentagens_gc.append(gc_percentage)
        
    print("="*20)

print("Coleta de dados concluída.")

#Separador da linha de codigo

print("----------------------------------------------------")

#================================================================
##Criacao dos graficos
import matplotlib.pyplot as plt


# --- O BLOCO DE GERAÇÃO DE GRÁFICOS COMEÇA AQUI ---

if ids_sequencias:
    print("Preparando para gerar o gráfico combinado de Composição e Percentagem GC...")

    fig, ax1 = plt.subplots(figsize=(15, 8))
    ax1.set_xlabel("ID da Variantes")

    
    bar_width = 0.8 
    bar_at = ax1.bar(ids_sequencias, at_count, color='salmon',
                      label='Contagem A+T', width=bar_width)
    
    bar_gc = ax1.bar(ids_sequencias, gc_count, bottom=at_count, color='lightgreen', 
                     label='Contagem G+C', width=bar_width)

    
    ax1.set_ylabel("Contagem de Bases (Comprimento da Sequência)", color='black') 
    ax1.tick_params(axis='y', labelcolor='black') 
    ax2 = ax1.twinx()


    line_gc_pct = ax2.plot(ids_sequencias, porcentagens_gc, color='purple'
                           , marker='o', linestyle='-',
                             label='Percentagem de GC (%)')

    ax2.set_ylabel("Percentagem de GC (%)", color='purple') 
    ax2.tick_params(axis='y', labelcolor='purple') 

    fig.autofmt_xdate(rotation=90)

    # Adiciona um título geral para o gráfico.
    plt.title("Composição de Bases e Percentagem de GC por Variante")
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1 + h2, l1 + l2, loc='upper left') 

    fig.tight_layout()
    plt.show()
    print("Gráfico combinado gerado com sucesso!")

else:
    # Mensagem se não foi possível coletar dados.
    print("Nenhum dado de sequência foi encontrado ou processado. Não foi possível gerar o gráfico.")