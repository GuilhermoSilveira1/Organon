# Organon
## Aplicativo de Organização Pessoal

Organon é um projeto pessoal e experimental, criado a partir do interesse em desenvolver uma ferramenta de organização simples, funcional e com aparência de aplicativo nativo. O foco principal está no uso do Django como base para toda a lógica e estrutura do app, mantendo a stack enxuta e acessível.

# Objetivo do Projeto
Criar um aplicativo desktop de organização pessoal com funcionalidades úteis como gerenciamento de tarefas, sistema de recompensas e integração com serviços externos. Tudo isso utilizando:

Django para backend e frontend
HTML, CSS e JavaScript para a interface
PyWebView para transformar a aplicação web em um app desktop com aparência nativa

💡 Embora o Electron tenha sido considerado, optou-se pelo PyWebView para evitar a necessidade de empacotar o Node.js, mantendo a simplicidade da stack.

# 🚀 Como Utilizar

1 - Clone o repositório ou baixe o .zip:
git clone https://github.com/seu-usuario/organon.git

2 - Acesse a pasta do projeto:
cd organon

3 - Instale as dependências:
Certifique-se de estar na mesma pasta onde está o arquivo requirements.txt, e execute:
pip install -r requirements.txt

4 - Execute o servidor Django:
Navegue até a pasta onde está o manage.py e rode:

Windows: python manage.py runserver
Linux/Mac: python3 manage.py runserver

5 - Acesse o app:
Abra o navegador e vá até http://127.0.0.1:8000 para começar a usar o Organon.
- ⚠️ O aplicativo ainda não está empacotado como um executável. Ele roda localmente via navegador por enquanto.

# Sugestões
Caso tenha alguma sugestão ou tenha percebido um bug ou qualquer outra coisa, se sinta à vontade para abrir uma nova issue sobre o assunto.
Vou ler e ver se é viável/faz sentido para o projeto, e irei ajustar.

# 🧩 Funcionalidades Atuais e Futuras
- ✅ Timer Pomodoro
- ✅ Painel de Tarefas
- 🔜 Sistema de Recompensas por conclusão de tarefas e subtarefas
- 🔜 Integração com Spotify (para controle de música)
- 🔜 Backup em Nuvem via Google Drive

# 🛠️ Tecnologias Utilizadas
- Python
- Django
- HTML, CSS, JavaScript
- PyWebView (para exibição como app desktop)
