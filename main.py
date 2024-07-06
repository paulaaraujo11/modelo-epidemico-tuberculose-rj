import numpy as np
import matplotlib.pyplot as plt

def simulacao_seir(beta, alpha, gamma, S0, E0, I0, R0, t_start, t_end, dt):
  """
  Simula o modelo SEIR com as equações e parâmetros fornecidos.

  Argumentos:
    beta: Taxa de propagação da doença.
    alpha: Taxa de expostos para infectados.
    gamma: Taxa de recuperação.
    S0: Número inicial de indivíduos suscetíveis.
    E0: Número inicial de indivíduos expostos.
    I0: Número inicial de indivíduos infectados.
    R0: Número inicial de indivíduos recuperados.
    t_start: Tempo inicial da simulação.
    t_end: Tempo final da simulação.
    dt: Passo de tempo da simulação.

  Retorno:
    S, E, I, R: Vetores com os valores das variáveis ao longo do tempo.
  """

  # Vetores para armazenar os valores ao longo do tempo
  S = np.zeros(int((t_end - t_start) / dt))
  E = np.zeros(int((t_end - t_start) / dt))
  I = np.zeros(int((t_end - t_start) / dt))
  R = np.zeros(int((t_end - t_start) / dt))

  # Condições iniciais
  S[0] = S0
  E[0] = E0
  I[0] = I0
  R[0] = R0

  for i in range(1, int((t_end - t_start) / dt)):
    # Cálculo das taxas de variação
    if S[i-1] == 0 or I[i-1] == 0:
        # Evitar divisão por zero
        dSdt = 0
        dEdt = 0
        dIdt = 0
        dRdt = 0
    else:
        dSdt = -beta * (S[i-1] * I[i-1]) / S[i-1]
        dEdt = beta * (S[i-1] * I[i-1]) / S[i-1] - alpha * E[i-1]
        dIdt = alpha * E[i-1] - gamma * I[i-1]
        dRdt = gamma * I[i-1]

    # Limitar os valores para evitar overflow
    S[i] = max(0, min(S[i-1] + dSdt * dt, S0))
    E[i] = max(0, min(E[i-1] + dEdt * dt, E0))
    I[i] = max(0, min(I[i-1] + dIdt * dt, I0))
    R[i] = max(0, min(R[i-1] + dRdt * dt, R0))

  return S, E, I, R

# Exemplo de uso da função
beta = 19.4
alpha = 18.2
gamma = 0.0714
S0 = 207.940
E0 = 0.23
I0 = 10
R0 = 0
t_start = 0
t_end = 365
dt = 0.1

S, E, I, R = simulacao_seir(beta, alpha, gamma, S0, E0, I0, R0, t_start, t_end, dt)

# Plotar os resultados
plt.plot(np.arange(t_start, t_end, dt), S, label="Suscetíveis")
plt.plot(np.arange(t_start, t_end, dt), E, label="Expostos")
plt.plot(np.arange(t_start, t_end, dt), I, label="Infectados")
plt.plot(np.arange(t_start, t_end, dt), R, label="Recuperados")
plt.legend()
plt.xlabel("Tempo (dias)")
plt.ylabel("Número de indivíduos")
plt.show()
