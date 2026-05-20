from datetime import datetime
#LISTAS----
cursos = []
disciplinas = []
professores = []
alunos = []
notas = []
# Cadastro de cursos – código, nome
# Cadastro de disciplinas – código, nome
# Cadastro de professores – matrícula, nome, disciplina, curso
# Cadastro de aluno – matrícula, nome, curso
# Cadastro de notas – aluno, disciplina, nota

#BUSCAR ---------------------------------------------
def buscar_curso(codigo):
#procura pra ver se tem um curso com esse codigo
    for curso in cursos:
        if curso["codigo"] == codigo:
            return curso
    return None

def buscar_disciplina(codigo):
# Procurar uma disciplina com esse código.
    for disciplina in disciplinas:
        if disciplina["codigo"] == codigo:
            return disciplina
    return None
#retorna o nome e o codigo de uma diciplina

def buscar_aluno(matricula):
    # Procurar um aluno com uma matrícula.
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            return aluno
    return None

def buscar_professor(matricula):
    # Procurar um professor pela matrícula.
    # usada em cadastrar_professor()
    for professor in professores:
        if professor["matricula"] == matricula:
            return professor
    return None

#NOTAS --------------------------------------------------

def notas_do_aluno(matricula):
    # Criar uma lista apenas com as notas de um aluno específico
    # ele pega a nota pela matricula do aluno que vai estar no dicionario dentro da lista
    lista_notas = []
    for nota in notas:
        if nota["aluno"] == matricula:
            lista_notas.append(nota)
    return lista_notas

def calcular_media_aluno(matricula):
# Calcular a média das notas de um aluno.
    lista_notas = notas_do_aluno(matricula)
# Pega somente as notas do aluno informado
    if len(lista_notas) == 0:
        return 0
    
    soma = 0
    for nota in lista_notas:
        soma += nota["nota"]
    media = soma / len(lista_notas)
    return media

def contar_disciplinas_aprovadas(matricula):
    # Contar em quantas disciplinas o cara passou pela matrícula
    # usada para emitir_certificado
    quantidade = 0
    for nota in notas:
        if nota["aluno"] == matricula and nota["nota"] >= 7:
            quantidade += 1
    return quantidade

#CADASTRAR CURSO -------------------------------------
def cadastrar_nota():
    # Cadastrar uma nota para um aluno em uma disciplina.
    matricula_aluno = input("Digite a matrícula do aluno: ")
    aluno = buscar_aluno(matricula_aluno)
    
    
    if aluno is None:
        print("Aluno não encontrado!")
        return
    codigo_disciplina = input("Digite o código da disciplina: ")
    disciplina = buscar_disciplina(codigo_disciplina)
    if disciplina["curso"] != aluno["curso"]:
        print("Essa disciplina não pertence ao curso do aluno!")
        return
    if disciplina is None:
        print("Disciplina não encontrada!")
        return
    # pra ver se existe o aluno e disciplina ^
    try:
        nota_aluno = float(input("Digite a nota do aluno: "))
    # tente rodar o que o usuário digitou em número
    # se não conseguir, mostre erro e pare a função, sem quebrar o código
    
    except ValueError: #se der erro do tipo valuEerror, digite invalido
        print("Nota inválida!")
        return
    
    if nota_aluno < 0 or nota_aluno > 10:
        print("A nota deve estar entre 0 e 10!")
        return
    nova_nota = {
        "aluno": matricula_aluno,
        "disciplina": codigo_disciplina,
        "nota": nota_aluno
    }
    notas.append(nova_nota)
    print("Nota cadastrada com sucesso!")
    
def cadastrar_curso():
 #CODIGO E NOME
    codigo = input("Digite o código do curso: ")
    if buscar_curso(codigo) is not None:
        print("Curso já cadastrado!")
        return
#ve se ja existe esse codigo
    nome = input("Digite o nome do curso: ")
    curso = {
        "codigo": codigo,
        "nome": nome
    }

    cursos.append(curso)
    print("Curso cadastrado com sucesso!")

#CADASTRAR DISCIPLINA ------------------------------------
#CODIGO CURSO E NOME
def cadastrar_disciplina():
    codigo = input("Digite o código da disciplina: ")
    if buscar_disciplina(codigo) is not None:
        print("Disciplina já cadastrada!")
        return
    nome = input("Digite o nome da disciplina: ")
    codigo_curso = input("Digite o código do curso da disciplina: ")
    curso = buscar_curso(codigo_curso)
    if curso is None:
        print("Curso não encontrado!")
        return
   
    disciplina = {
        "codigo": codigo,
        "nome": nome,
        "curso": codigo_curso
    }

    disciplinas.append(disciplina)
    print("Disciplina cadastrada com sucesso!")

#CADASTRAR ALUNOS ----------------------------------------

def cadastrar_aluno():
 #ALUNO -> CURSO
    matricula = input("Digite a matrícula do aluno: ")
    if buscar_aluno(matricula) is not None:
        print("Aluno já cadastrado!")
        return

    nome = input("Digite o nome do aluno: ")
    codigo_curso = input("Digite o código do curso do aluno: ")
    curso = buscar_curso(codigo_curso)
    if curso is None:
        print("Curso não encontrado!")
        return
    aluno = {
        "matricula": matricula,
        "nome": nome,
        "curso": codigo_curso
    }
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")
    
#CADASTRAR PROFESSOR --------------------------------------------------------

def cadastrar_professor():
 #PROFESSOR -> DISCIPLINA -> CURSO
    matricula = input("Digite a matrícula do professor: ")
    if buscar_professor(matricula) is not None:
        print("Professor já cadastrado!")
        return

    nome = input("Digite o nome do professor: ")
    codigo_disciplina = input("Digite o código da disciplina do professor: ")
    disciplina = buscar_disciplina(codigo_disciplina)
    if disciplina is None:
        print("Disciplina não encontrada!")
        return
    codigo_curso = input("Digite o código do curso do professor: ")
    curso = buscar_curso(codigo_curso)
    if curso is None:
        print("Curso não encontrado!")
        return
    if disciplina["curso"] != codigo_curso:
        print("Essa disciplina não pertence a esse curso!")
        return
    
    professor = {
        "matricula": matricula,
        "nome": nome,
        "disciplina": codigo_disciplina,
        "curso": codigo_curso
    }
    professores.append(professor)
    print("Professor cadastrado com sucesso!")
    
#VERIFICAR SITUACAO --------------------------------------------------------------
def verificar_situacao_aluno():
    # Verificar se o aluno foi aprovado, está em recuperação ou foi reprovado.
    
    matricula = input("Digite a matrícula do aluno: ")
    aluno = buscar_aluno(matricula)
    if aluno is None:
        print("Aluno não encontrado!")
        return

    lista_notas = notas_do_aluno(matricula)
    if len(lista_notas) == 0:
        print("Esse aluno ainda não possui notas cadastradas.")
        return

    media = calcular_media_aluno(matricula)
    print(f"Aluno: {aluno['nome']}")
    print(f"Média: {media}")

    if media >= 7:
        print("Situação: APROVADO")

    elif media >= 4:
        print("Situação: RECUPERAÇÃO")
        print("Disciplinas com nota abaixo de 7:")

        disciplinas_baixas = []

        for nota in lista_notas:
            if nota["nota"] < 7:
                disciplina = buscar_disciplina(nota["disciplina"])
                disciplinas_baixas.append(nota)
                if disciplina is not None:
                    print(f"- {disciplina['nome']} | Nota atual: {nota['nota']}")

    else:
        print("Situação: REPROVADO NO CURSO")

# RELATORIO GERAL --------------------------------------------------------------------

def relatorio_geral():
#mostra cursos, disciplinas, professores e alunos cadastrados.
    print("========== RELATÓRIO GERAL ==========")
    
    print("\n--- CURSOS CADASTRADOS ---")
    if len(cursos) == 0:
        print("Nenhum curso cadastrado.")
    else:
        for curso in cursos:
            print(f"Código: {curso['codigo']} | Nome: {curso['nome']}")

    print("\n--- DISCIPLINAS CADASTRADAS ---")
    if len(disciplinas) == 0:
        print("Nenhuma disciplina cadastrada.")
    else:
        for disciplina in disciplinas:
            print(f"Código: {disciplina['codigo']} | Nome: {disciplina['nome']}")

    print("\n--- PROFESSORES CADASTRADOS ---")
    if len(professores) == 0:
        print("Nenhum professor cadastrado.")
    else:
        for professor in professores:
            disciplina = buscar_disciplina(professor["disciplina"])
            curso = buscar_curso(professor["curso"])
            if disciplina is not None:
                nome_disciplina = disciplina["nome"]
            else:
                nome_disciplina = "Não encontrada"
            if curso is not None:
                nome_curso = curso["nome"]
            else:
                nome_curso = "Não encontrado"

            print(
                f"Matrícula: {professor['matricula']} | "
                f"Nome: {professor['nome']} | "
                f"Disciplina: {nome_disciplina} | "
                f"Curso: {nome_curso}"
            )
            
    print("\n--- ALUNOS MATRICULADOS ---")
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            curso = buscar_curso(aluno["curso"])
            if curso is not None:
                nome_curso = curso["nome"]
            else:
                nome_curso = "Não encontrado"

            print(
                f"Matrícula: {aluno['matricula']} | "
                f"Nome: {aluno['nome']} | "
                f"Curso: {nome_curso}"
            )

#RELATORIO DE ALUNOS/CURSO -------------------------------------------------------

def relatorio_alunos_por_curso():
# Mostrar os alunos e matricula de cada curso
    print("\n========== ALUNOS POR CURSO ==========")

    if len(cursos) == 0:
        print("Nenhum curso cadastrado.")
        return

    for curso in cursos:
        print(f"\nCurso: {curso['nome']}")
        
        encontrou = False
        for aluno in alunos:
            if aluno["curso"] == curso["codigo"]:
                print(f"- {aluno['nome']} | Matrícula: {aluno['matricula']}")
                encontrou = True
        if encontrou == False:
            print("Nenhum aluno matriculado neste curso.")
            
#ALUNOS POR DICIPLINA-----------------------------------------------------------------

def relatorio_alunos_por_disciplina():
    print("\n========== ALUNOS POR DISCIPLINA ==========")
    if len(disciplinas) == 0:
        print("Nenhuma disciplina cadastrada.")
        return

    for disciplina in disciplinas:
        print(f"\nDisciplina: {disciplina['nome']}")
        
        encontrou = False
        for nota in notas:
            if nota["disciplina"] == disciplina["codigo"]:
                aluno = buscar_aluno(nota["aluno"])
                if aluno is not None:
                    print(f"- {aluno['nome']} | Matrícula: {aluno['matricula']} | Nota: {nota['nota']}")
                    encontrou = True
        if encontrou == False:
            print("Nenhum aluno matriculado nesta disciplina.")
#EXEMPLO;
#nota = {
#     "aluno": "101",
#     "disciplina": "MAT",
#     "nota": 8
# }
#disciplina = {
#     "codigo": "MAT",
#     "nome": "Matemática"
# } ESSE ALUNO E NOTA ESTARIA NO RELATORIO


# NOTAS DE UM UNICO ALUNO--------------------------------------------------------------------------------
def relatorio_notas_aluno():
    matricula = input("Digite a matrícula do aluno: ")
    aluno = buscar_aluno(matricula)
    if aluno is None:
        print("Aluno não encontrado!")
        return

    curso = buscar_curso(aluno["curso"])
    lista_notas = notas_do_aluno(matricula)
#é uma lista com matricula do aluno e disciplina
    if curso is not None:
        print(f"Curso: {curso['nome']}")
    else:
        print("Curso: Não encontrado")

    if len(lista_notas) == 0:
        print("Esse aluno ainda não possui notas cadastradas.")
        return
    
    print("\n========== RELATÓRIO DE NOTAS ==========")
    print(f"Aluno: {aluno['nome']}")
    print("\nNotas:")

    for nota in lista_notas:
        disciplina = buscar_disciplina(nota["disciplina"])
        if disciplina is not None:
            print(f"Disciplina: {disciplina['nome']} | Nota: {nota['nota']}")
        else:
            print(f"Disciplina não encontrada | Nota: {nota['nota']}")

    media = calcular_media_aluno(matricula)
    print(f"\nMédia geral: {media}")

# CERTIFICADO-----------------------------------------------------------------------------------

def emitir_certificado():
    matricula = input("Digite a matrícula do aluno: ")
    aluno = buscar_aluno(matricula)
    
    if aluno is None:
        print("Aluno não encontrado!")
        return
    curso = buscar_curso(aluno["curso"])
    if curso is None:
        print("Curso do aluno não encontrado!")
        return

    aprovadas = contar_disciplinas_aprovadas(matricula)
    if aprovadas >= 10:
        data_emissao = datetime.now().strftime("%d/%m/%Y")
        print("\n====================================")
        print("       CERTIFICADO DE CONCLUSÃO      ")
        print("====================================")
        print(f"Certificamos que o aluno {aluno['nome']}")
        print(f"concluiu o curso de {curso['nome']}.")
        print(f"Data de emissão: {data_emissao}")
        print("====================================")

    else:
        print("O aluno ainda não pode receber o certificado.")
        print(f"Disciplinas aprovadas: {aprovadas}")
        print("Para concluir o curso, o aluno precisa ser aprovado em pelo menos 10 disciplinas.")


#Menu do sistema(final da pagina)-----------------

def mostrar_menu():
    print("\n========== SISTEMA ESCOLAR ==========")
    print("1 - Cadastrar curso")
    print("2 - Cadastrar disciplina")
    print("3 - Cadastrar aluno")
    print("4 - Cadastrar professor")
    print("5 - Cadastrar nota")
    print("6 - Verificar situação do aluno")
    print("7 - Relatório geral")
    print("8 - Relatório de alunos por curso")
    print("9 - Relatório de alunos por disciplina")
    print("10 - Relatório de notas de um aluno")
    print("11 - Emitir certificado")
    print("0 - Sair")
    
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_curso()
    elif opcao == "2":
        cadastrar_disciplina()
    elif opcao == "3":
        cadastrar_aluno()
    elif opcao == "4":
        cadastrar_professor()
    elif opcao == "5":
        cadastrar_nota()
    elif opcao == "6":
        verificar_situacao_aluno()
    elif opcao == "7":
        relatorio_geral()
    elif opcao == "8":
        relatorio_alunos_por_curso()
    elif opcao == "9":
        relatorio_alunos_por_disciplina()
    elif opcao == "10":
        relatorio_notas_aluno()              
    elif opcao == "11":
        emitir_certificado()
    elif opcao == "0":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida! Tente novamente.")