# implementação dos algoritmos de substituição de página FIFO e LRU

import random
from collections import deque

# função para gerar uma string de referência de página aleatória com números de 0 a 9
def gerar_referencia_paginas(tamanho):
    return [random.randint(0, 9) for _ in range(tamanho)]

# algoritmo FIFO
def fifo(referencia, quadros):
    memoria = deque(maxlen=quadros)
    falhas_pagina = 0
    for pagina in referencia:
        if pagina not in memoria:
            falhas_pagina += 1
            memoria.append(pagina)
    return falhas_pagina

# algoritmo LRU
def lru(referencia, quadros):
    memoria = []
    falhas_pagina = 0
    for pagina in referencia:
        if pagina in memoria:
            memoria.remove(pagina)
        else:
            falhas_pagina += 1
            if len(memoria) == quadros:
                memoria.pop(0)
        memoria.append(pagina)
    return falhas_pagina

# função para testar os algoritmos com diferentes números de quadros de página
def testar_algoritmos(tamanho_referencia, max_quadros):
    referencia = gerar_referencia_paginas(tamanho_referencia)
    resultados = []
    
    for quadros in range(1, max_quadros + 1):
        falhas_fifo = fifo(referencia, quadros)
        falhas_lru = lru(referencia, quadros)
        resultados.append({
            'quadros': quadros,
            'falhas_fifo': falhas_fifo,
            'falhas_lru': falhas_lru
        })
    return resultados

# testando os algoritmos com uma string de referência de 20 páginas e até 5 quadros de página
resultados_testes = testar_algoritmos(20, 5)

# mostrando os resultados
for resultado in resultados_testes:
    print(f"Quadros: {resultado['quadros']}, Falhas FIFO: {resultado['falhas_fifo']}, Falhas LRU: {resultado['falhas_lru']}")
