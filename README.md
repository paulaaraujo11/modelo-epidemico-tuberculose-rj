# modelo-epidemico-tuberculose-rj
Algoritmo SEIR para simular epidemia de tuberculose no Rio de Janeiro com dados reais do SUS

# Dados do kaggle - Dados RIO 20 ANOS

Município	Casos confirmados (I0)	População total (N)	Taxa de incidência (tx_100mil)
Angra dos Reis	2.231	210.171	1.061,52
"Revista Nature Medicine em 2014 estimou que o valor de e0 para a tuberculose pulmonar ativa na África do Sul era de 0,23 por ano." Fonte: Artigo específico:

Título: "The global epidemiology of latent tuberculosis: a systematic review and meta-analysis" Autores: Dye, C., et al. Publicação: Nature Medicine, 20(12): 1287-1298, 2014. Link para o artigo: https://www.nature.com/articles/nm.3738

#Ajustando as equações do modelo SEIR aos dados de Angra dos Reis: Definição das variáveis:

- S(t): População suscetível ao longo do tempo (estimada em 207.940 - E no início da epidemia).
- E(t): População exposta ao longo do tempo (0,23 ao ano).
- I(t): População infectada ao longo do tempo (informada como 2.231 no início da epidemia).
- R(t): População recuperada ao longo do tempo (assumida como 0 no início da epidemia).
- N: População total de Angra dos Reis (210.171).
- β: Taxa de propagação da doença (a ser estimada).
- α: Taxa de transição de exposto para infectado (a ser estimada).
- γ: Taxa de recuperação (assumindo um período de infecção de 2 anos, γ = 0,5).
- β ≈ 19.4 -> β = I0 / (E0 * γ) e α ≈ -18.2 -> α = (1/duração do período de latência) - β
