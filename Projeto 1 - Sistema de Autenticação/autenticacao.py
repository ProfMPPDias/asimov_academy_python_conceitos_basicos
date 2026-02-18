# Programa de Autenticação de Usuário

# Credenciais corretas
usuario_correto = "MDias"
senha_correta = "mdias123@"

# Solicitar entrada do usuário
print("=== Sistema de Autenticação ===")
usuario_digitado = input("Digite o usuário: ")
senha_digitada = input("Digite a senha: ")

# Verificar autenticação
if usuario_digitado == usuario_correto and senha_digitada == senha_correta:
    print(f"\nSeja Bem-Vindo(a) {usuario_correto}")
    print("Voce esta logado!")
else:
    # Identificar qual campo está incorreto
    if usuario_digitado != usuario_correto:
        print(f"\nUsuario {usuario_digitado} nao esta cadastrado(a)")
    else:
        print(f"\nUsuario {usuario_digitado} esta com a senha incorreta")