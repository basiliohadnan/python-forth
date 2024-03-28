
# [Solução A](#https://exercism.org/tracks/python/exercises/forth/solutions/tugrul): tugrul's solution

# [Solução B](#https://exercism.org/tracks/python/exercises/forth/solutions/pythonSnake): pythonSnake's solution

  

## Resumo da comparação

  

A Solução A é mais organizada, legível e tem uma maior preocupação na tratativa de erros e aproveitamento das funções inatas do Python, facilitando manutenção e reaproveitamento. Além disso, a solução A tende a ser mais performática, por ser mais eficaz em uso de memória, tempo de execução e escalabilidade, devido à implementação de list comprehensions e generator expressions.

  

### Pontos de melhoria na Solução A

  

- Na linha 23, há um nome de classe incorreto e o código não utilizado.

- Na linha 39, há um print desnecessário.

  

### Detalhes a serem considerados

  

1.  **Organização do código**: A Solução A separa em funções, melhorando a legibilidade e permitindo o reuso do código, enquanto a Solução B entrega um grande bloco de função.

  

2.  **Tratativa de erros**: Na Solução A, são definidas exceções customizadas, respeitando a regra da mensagem clara de erro, colaborando para um melhor entendimento do código, centralizando as chamadas e facilitando sua manutenção. Já na Solução B, por repetir-se diversas vezes as chamadas da exceção customizada, dificulta-se a manutenção e abre margem para erros nas chamadas.

  

3.  **Estrutura de dados**: A Solução A prioriza o uso de dicionários, facilitando o entendimento e a manutenção. A Solução B trata os dados inseridos diretamente, sem armazená-los de forma estruturada.

  

4.  **Tratativa de inserções**: A Solução A faz o parse e processamento de cada linha, separando a lógica para cada operação e avaliando as expressões. Usa list comprehension e generator expressions, melhorando a legibilidade e mantendo o código mais conciso. A Solução B processa tudo em um bloco de loop, o que faz o código ficar verboso e menos legível.

  

5.  **Boas práticas**: Dentro da Solução A, vemos maior preocupação em seguir convenções como nomes de variáveis descritivos (PEP-8), aproveitamento de funções internas e uso de estrutura de dados de forma efetiva. A Solução B, embora funcional, carece de organização, legibilidade e capricho na tratativa de erros.

  
  

## Testes

Para rodar os testes, digitar comando **pytest**, no terminal.

  

Testes efetuados manualmente:

  

1.  **Teste de multiplicação**: O resultado esperado de uma multiplicação de 5 por 2 é 10. Ambas as soluções retornam corretamente.

  

2.  **Teste de soma**: O resultado esperado de uma soma de 5 com 2 é 7. Ambas as soluções retornam corretamente.

  

3.  **Teste de subtração**: O resultado esperado de uma subtração de 5 por 2 é 3. Ambas as soluções retornam corretamente.

  

4.  **Teste de divisão**: O resultado esperado de uma divisão de 10 por 2 é 5. Ambas as soluções retornam corretamente.

  

5.  **Teste de erro de pilha vazia**: Ambas as soluções retornam corretamente um erro quando há uma operação em uma pilha vazia.

6.  **Teste de dup**: Ambas as soluções retornam corretamente após a execução do comando "dup".

  

7.  **Teste de drop**: Ambas as soluções retornam corretamente após a execução do comando "drop".

  

8.  **Teste de swap**: Ambas as soluções retornam corretamente após a execução do comando "swap".

  

9.  **Teste de over**: Ambas as soluções retornam corretamente após a execução do comando "over".