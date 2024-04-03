
  
  

# [Solução A](https://exercism.org/tracks/python/exercises/forth/solutions/tugrul) - tugrul's solution

  

  

# [Solução B](https://exercism.org/tracks/python/exercises/forth/solutions/pythonSnake) - pythonSnake's solution

  

  

## Resumo da comparação

  

  

  

A solução A é mais organizada, legível, tem maior preocupação na tratativa de erros e uso das funções inatas do Python, o que facilita na manutenção e reaproveitamento de código.

Além disso, a solução A tende a ser mais performática, por ser mais eficaz em uso de memória, tempo de execução e escalabilidade, devido à implementação de _list comprehensions_ e _generator expressions_.

  

**Observação**: Embora a tendência fosse de que a solução A tivesse um desempenho melhor em termos de performance, após rodar o teste comparativo, a solução B se mostrou mais rápida.

Minha sugestão de alteração do script ficou em segundo lugar e a solução A teve a execução mais lenta.

  

| Script| Average Execution Time (seconds) |

|-------------|----------------------------------|

| solution_a | 0.0145 |

| solution_b | 0.0 |

| forth | 0.0008 |

  

  

  

### Pontos de melhoria na solução A

  

  

  

- Na linha 23, há um nome de classe incorreto e o código não utilizado.

  

  

- Na linha 39, há um print desnecessário.

  

### Melhorias realizadas, com base na solução A

  

- Exceção customizada _'DivisionByZero'_ removida, aproveitando exceção inata.

- Função _'is_number'_ uso de _regex_, melhor legibilidade.

- Função _'apply'_, removido _print_ desnecessário

- Função _'substitute'_ uso de _list comprehension_ no lugar de _generator expression_ dentro de _chain_ (removido), performance e legibilidade.

  
  

### Detalhes a serem considerados

  

  

  

1.  **Organização do código**: A solução A separa em funções, melhorando a legibilidade e permitindo o reuso do código, enquanto a solução B entrega um grande bloco de função.

  

  

  

2.  **Tratativa de erros**: Na solução A, são definidas exceções customizadas, respeitando a regra da mensagem clara de erro, colaborando para um melhor entendimento do código, centralizando as chamadas e facilitando sua manutenção. Já na solução B, por repetir-se diversas vezes as chamadas da exceção customizada, dificulta-se a manutenção e abre margem para erros nas chamadas.

  

  

  

3.  **Estrutura de dados**: A solução A prioriza o uso de dicionários, facilitando o entendimento e a manutenção. A solução B trata os dados inseridos diretamente, sem armazená-los de forma estruturada.

  

  

  

4.  **Tratativa de inserções**: A solução A faz o _parse_ e processamento de cada linha, separando a lógica para cada operação e avaliando as expressões. Usa _list comprehension_ e _generator expressions_, melhorando a legibilidade e mantendo o código mais conciso. A solução B processa tudo em um bloco de loop, o que faz o código ficar verboso e menos legível.

  

  

  

5.  **Boas práticas**: Dentro da solução A, vemos maior preocupação em seguir convenções como nomes de variáveis descritivos (_PEP-8_), aproveitamento de funções internas e uso de estrutura de dados de forma efetiva. A solução B, embora funcional, carece de organização, legibilidade e capricho na tratativa de erros.

  

  

  

## Testes

  

  

Para rodar os testes de aceitação do Forth, executar comandos:

  

1.  **_pip install pytest_**

  

2.  **_pytest_**

  

Para rodar o teste de performance, executar comando:

1.  **_python "path"/performance-test.py_**

  

  

  

Testes efetuados manualmente:

  

  

  

1.  **Teste de multiplicação**: O resultado esperado de uma multiplicação de 5 por 2 é 10. Ambas as soluções retornam corretamente.

  

  

  

2.  **Teste de soma**: O resultado esperado de uma soma de 5 com 2 é 7. Ambas as soluções retornam corretamente.

  

  

  

3.  **Teste de subtração**: O resultado esperado de uma subtração de 5 por 2 é 3. Ambas as soluções retornam corretamente.

  

  

  

4.  **Teste de divisão**: O resultado esperado de uma divisão de 10 por 2 é 5. Ambas as soluções retornam corretamente.

  

  

  

5.  **Teste de erro de pilha vazia**: Ambas as soluções retornam corretamente um erro quando há uma operação em uma pilha vazia.

  

  

6.  **Teste de _dup_**: Ambas as soluções retornam corretamente uma lista com o último item duplicado, após a execução do comando "_dup_".

  

  

  

7.  **Teste de _drop_**: Ambas as soluções retornam corretamente uma lista com o último item removido, após a execução do comando "_drop_".

  

  

  

8.  **Teste de _swap_**: Ambas as soluções retornam corretamente uma lista com o último item trocado de índice com o penúltimo item, após a execução do comando "_swap_".

  

  

  

9.  **Teste de _over_**: Ambas as soluções retornam corretamente uma lista com o segundo item duplicado e posicionado no final, após a execução do comando "_over_".