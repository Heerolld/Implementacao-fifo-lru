
# Algoritmos de Substituição de Página FIFO e LRU

Este projeto implementa os algoritmos de substituição de página FIFO e LRU para simular o gerenciamento de memória.

## Requisitos
- Python 3.8 ou superior
- Nenhuma dependência externa necessária

## Exemplo de Saída
```
Quadros: 1, Falhas FIFO: 19, Falhas LRU: 19
Quadros: 2, Falhas FIFO: 17, Falhas LRU: 17
Quadros: 3, Falhas FIFO: 16, Falhas LRU: 16
Quadros: 4, Falhas FIFO: 15, Falhas LRU: 16
Quadros: 5, Falhas FIFO: 15, Falhas LRU: 14
```

## Descrição do Código
O código consiste na implementação dos dois algoritmos de substituição de páginas:

- **FIFO (First-In-First-Out)**: Substitui a página mais antiga em memória quando ocorre uma falha de página.
- **LRU (Least Recently Used)**: Substitui a página que foi usada há mais tempo quando ocorre uma falha de página.

### Funcionamento
1. A string de referência de página é gerada aleatoriamente com números de página entre 0 e 9.
2. Tanto o algoritmo FIFO quanto o LRU são aplicados a essa string, e o número de falhas de página é calculado.
3. Os resultados são mostrados para diferentes números de quadros de página (entre 1 e 5).

## Autor
Este projeto foi desenvolvido como parte de um exercício de implementação de algoritmos de gerenciamento de memória.
