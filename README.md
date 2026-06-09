# projetopython
Projeto de um sistema escolar simples em python 
sem banco de dados, todas as alterações serão feitas localmente

## Linha de raciocínio do código

O programa começa criando listas vazias para `cursos`, `disciplinas`, `professores`, `alunos` e `notas`; depois define funções de busca para encontrar curso, disciplina, aluno e professor.

Em seguida vem a parte das funcoes de cadastro:
1. cadastrar curso
2. cadastrar disciplina (associada a um curso existente)
3. cadastrar aluno (associado a um curso existente)
4. cadastrar professor (associado a disciplina e curso)
5. cadastrar nota (associada a aluno e disciplina)

Depois há funções de relatório e validação:
- verificar situação do aluno pela média das notas
- relatório geral de cursos/disciplinas/professores/alunos
- relatórios de alunos por curso, por disciplina e notas de um aluno
- emitir certificado se o aluno tiver disciplinas aprovadas suficientes

Por fim, o `while True` exibe um menu que permite ao usuário escolher cada operação e executa a função correspondente.

## destaque para as proteções contra erros acidentais no código:

### 1. Verificações antes de cadastrar
- Cada `cadastrar_*` verifica se o registro já existe:
  - `cadastrar_curso()` checa `buscar_curso(codigo)`
  - `cadastrar_disciplina()` checa `buscar_disciplina(codigo)`
  - `cadastrar_aluno()` checa `buscar_aluno(matricula)`
  - `cadastrar_professor()` checa `buscar_professor(matricula)`
- Isso evita duplicatas e entradas conflitantes.

### 2. Busca e validação de dependências
- `cadastrar_disciplina()` exige que o curso exista antes de cadastrar a disciplina.
- `cadastrar_aluno()` exige que o curso do aluno exista.
- `cadastrar_professor()` exige disciplina e curso válidos, e ainda confirma que a disciplina pertence ao curso.
- `cadastrar_nota()` só segue se o aluno e a disciplina forem encontrados e a disciplina pertencer ao curso do aluno.

### 3. Tratamento de entrada inválida
- Em `cadastrar_nota()`, o código usa:
  - `try/except ValueError` para capturar quando o usuário digita algo que não é número.
- Também verifica se a nota está no intervalo correto:
  - `0 <= nota <= 10`
- Isso evita que valores inválidos sejam salvos.

### 4. Proteção em relatórios e consultas
- Antes de calcular média ou mostrar dados, o código confirma que:
  - o aluno existe (`buscar_aluno`)
  - o curso existe (`buscar_curso`)
  - a disciplina existe (`buscar_disciplina`)
- Se não existir, ele imprime mensagem de erro e não continua em operação inválida.

### 5. Menus e opções inválidas
- No laço principal (`while True`), uma opção fora do menu exibe:
  - `Opção inválida! Tente novamente.`
- Isso evita que o programa tente executar uma ação inexistente e perca o progresso.
