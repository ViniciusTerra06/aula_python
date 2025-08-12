"""
1 - Colocar uma forma de voltar ao menu principal e de encerrar o programa a qualquer momento 

"""
import sys

def exibir_menu():
  menu = """
    ╔═══════════════════════════════╗
    ║     ⭐ MENU PRINCIPAL ⭐      ║
    ╠═══════════════════════════════╣
    ║                               ║
    ║ 1 - ➕ Adicionar tarefa       ║
    ║ 2 - 📋 Listar tarefas         ║
    ║ 3 - ✏️  Editar tarefas         ║
    ║ 4 - ✅ Marcar como concluída  ║
    ║ 5 - 🗑️  Remover tarefa         ║
    ║ 6 - 🚪 Sair                   ║
    ║                               ║
    ╚═══════════════════════════════╝
  """
  
  print(menu)
  
#========================================================

# Dicionário onde serão armazenados os valores
tarefas =  []

# Variável que armazena o status de conclusão das tarefas
status_conclusao = "Concluída ✅"

#=========================================================

# Função para adicionar tarefas
def adicionar_tarefas():
  texto_tarefa = voltar_menu_principal("\n➕ Digite a tarefa que você deseja incluir: ")
  if texto_tarefa is None:
    return

  nome_tarefa = voltar_menu_principal("\n➕ Digite o nome da tarefa que você deseja incluir: ")
  if nome_tarefa is None:
    return

  tarefa = {
    'nome': nome_tarefa.upper(),
    'texto': texto_tarefa.lower(),
    'concluida ✅': False
  }


  tarefas.append(tarefa)
  print(f"\nTarefa '{tarefa['nome']}' adicionada com sucesso!")

#=========================================================

# Função para listar tarefas
def listar_tarefas():
  if not tarefas:
    print("Nenhuma tarefa encontrada.")
  else:
    for i, tarefa in enumerate (tarefas, 1):
      status = status_conclusao if tarefa.get('concluida ✅', False) else ("pendente ⏳")
      print(f"\n[{i}] {tarefa['nome']}: {tarefa['texto']} - [{status}]")
      
#=========================================================

# Função para editar tarefas
def editar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    
    listar_tarefas()
    
    opcao = voltar_menu_principal("\n✏️  Digite o número da tarefa que você deseja editar: ")
    if opcao is None:
        return
    
    try:
        indice = int(opcao) - 1
        
        if 0 <= indice < len(tarefas):
            tarefa = tarefas[indice]
            print(f"\n📝 Editando tarefa: {tarefa['nome']}")
            
            # Editar nome da tarefa
            novo_nome = voltar_menu_principal(f"\n✏️  Digite o novo nome (atual: {tarefa['nome']}): ")
            if novo_nome is None:
                return
            if novo_nome.strip():
                tarefa['nome'] = novo_nome.upper()
            
            # Editar texto da tarefa 
            novo_texto = voltar_menu_principal(f"\n✏️  Digite o novo texto (atual: {tarefa['texto']}): ")
            if novo_texto is None:
                return
            if novo_texto.strip():
                tarefa['texto'] = novo_texto.lower()  # CORRIGIDO: era novo_nome.lower()
            
            print(f"\n✅ Tarefa '{tarefa['nome']}' editada com sucesso!")
            
        else: 
            print("\n❌❌❌ ERRO: O NÚMERO INFORMADO NÃO CORRESPONDE A UMA TAREFA EXISTENTE. ❌❌❌")
            
    except ValueError:
        print("\n❌❌❌ ERRO: ENTRADA INVÁLIDA! DEVE SER INFORMADO UM NÚMERO INTEIRO CORRESPONDENTE A UMA TAREFA. ❌❌❌")



#=========================================================

# Função para definir a conclusão da tarefa
def marcar_conclusao():
  if not tarefas:
    print("Nenhuma tarefa encontrada.")
    return
  
  listar_tarefas()

  opcao = voltar_menu_principal("\n🔍 Digite o número da tarefa para marcar como concluída: ")
  if opcao is None:
    return

  try: 
    indice = int(opcao) - 1
    if 0 <= indice < len(tarefas):
      tarefas[indice]['concluida ✅'] = True
      print(f"A tarefa '{tarefas[indice]['nome']}' foi marcada como concluída ✅")
    else: 
      print("\n❌❌❌ ERRO: O NÚMERO INFORMADO NÃO CORRESPONDE A UMA TAREFA EXISTENTE. ❌❌❌")
  except ValueError:
    print("\n❌❌❌ ERRO: ENTRADA INVÁLIDA! DEVE SER INFORMADO UM NÚMERO INTEIRO CORRESPONDENTE A UMA TAREFA. ❌❌❌")

#=========================================================

# Função para remover tarefas
def remover_tarefas():
  if not tarefas:
    print("Nenhuma tarefa encontrada")
    return
  
  listar_tarefas()

  opcao = voltar_menu_principal("\n🗑️  Digite o número da tarefa que você deseja remover: ")
  if opcao is None:
    return
  

  
  try:
    indice = int(opcao) - 1
    if 0 <= indice < len(tarefas):
      tarefa_removida = tarefas.pop(indice)
      print(f"\n 🗑️  A tarefa '{tarefa_removida['nome']}' foi removida com sucesso 🗑️")
    else:
      print("\n❌❌❌ ERRO: NÚMERO INFORMADO NÃO CORRESPONDE A NENHUMA TAREFA. ❌❌❌")
  except ValueError:
    print("\n❌❌❌ ERRO: INFORME APENAS NÚMEROS INTEIROS. ❌❌❌")

#=========================================================
  
# Função que define o fluxo principal
def fluxo_principal():

  while True:
    exibir_menu()
    
    try:
      opt = int(input("🌟 Digite a opção correlata à sua necessidade: "))
      
      if opt == 1:
        adicionar_tarefas()
      elif opt == 2:
        listar_tarefas()
      elif opt == 3:
        editar_tarefas()
      elif opt == 4:
        marcar_conclusao()
      elif opt == 5:
        remover_tarefas()
      elif opt == 6:
        print("\n 🏆 Programa encerrado! 🏆")
        break
      else:
        print("\n❌❌❌ERRO: ENTRADA INVÁLIDA, INFORME APENAS NÚMEROS ENTRE 1 E 6.❌❌❌")
    except ValueError:
      print("\n ❌❌❌ ERRO: ENTRADA INVÁLIDA! DIGITE APENAS NÚMEROS INTEIROS ENTRE 1 E 6! ❌❌❌")
    
#===================================

# Função que retorna ao menu principal ou encerra o programa sempre que solicitado
def voltar_menu_principal(PROMPT):
  entrada = input(PROMPT).strip().lower()
  if entrada.lower() == 'menu':
    return None
  elif entrada in ['sair','exit', 'quit']:
    sys.exit("\n ⏳ PROGRAMA SENDO ENCERRADO. ⏳")
  return entrada

#===================================

# O programa está iniciando aqui

if __name__ == "__main__":
    fluxo_principal()
#===================================