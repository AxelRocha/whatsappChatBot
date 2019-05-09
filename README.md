# **WhatsappChatBot**

O programa foi construído com o objetivo de ser um bot para o WhatsApp Web(WAW), o bot se comunicaria com uma interface de Chat que realiza um broadcast para os usuários presentes no mesmo Chat e, posteriormente, os usuários responderiam a uma determinada mensagem enviada e o bot redirecionaria a resposta no WAW para o contato que foi informado pelo usuário.

## Alcançado:

  - Código do servidor para o chat. 
  
  - Código para o usuario participar do Chat. 
  
  - Codigo do Bot que interage com o Chat e o WAW.
  
  - O bot se conecta ao servidor de Chat automaticamente.
  
  - O bot se conecta com o whatsappweb e fica esperando novas mensagens, quando recebe uma mensagem nova, a mensagem é lida e enviada no Chat, no formato "<contato_nome> disse: <contato_mensagem>".
 
## Funcionamento:
 - 1. Server: O servidor espera conexões e gerencia as mensagens de broadcast enviadas no Chat.
 - 2. Cliente/Usuário : Conecta-se ao servidor de forma manual ao executar o código. Depois de conectado o usuário tem acesso ao Chat e as mensagens enviadas pelo mesmo são recebidas por todos os outros usuários presentes no Chat.
 - 3. WAW Bot: Abre o Whats App Web e espera a conexão via QRCODE. Se conecta automaticamente ao servidor do Chat. Com ambas as partes anteriores conectadas, o Bot monitora o WAW e quando recebe um nova mensagem envia esta mensagem no Chat no formato "<contato_nome> disse: <contato_mensagem>".

## Problemas:

  - ~~Server instavel: quando usuário se desconecta, ocorre erro no server.~~

  - Identificação de Contatos diferentes.
  
  - Quebra de linha em mensagens extensas.
  
  - Leitura de mais de uma mensagem de uma só vez.
