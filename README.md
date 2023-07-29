# Objetivo
O objetivo deste projeto é mostrar como é possível criar uma interface amigável no Kivy que se conecta ao Node-RED para receber mensagens em tempo real e exibi-las para o usuário. A comunicação entre o Node-RED e o Kivy é realizada usando requisições HTTP.

# Integração Kivy com Node-RED para Captar Mensagens
Este projeto demonstra como integrar o framework Kivy com o Node-RED para captar mensagens enviadas pelo Node-RED e exibi-las em uma interface gráfica criada no Kivy.

# Como usar o aplicativo Kivy:
1. Clone este repositório em seu ambiente local.
2. Certifique-se de ter o Kivy e a biblioteca requests instalados (pip install kivy requests).
3. Execute o aplicativo Kivy usando o arquivo main.py.
4. O aplicativo mostrará uma interface gráfica que aguarda mensagens do Node-RED. Para buscar a mensagem, basta clicar no botão "Buscar Conteúdo".
5. Configure o Node-RED para enviar mensagens para o aplicativo Kivy usando requisições HTTP.
6. O aplicativo Kivy captará as mensagens enviadas pelo Node-RED e exibirá em tempo real na interface gráfica.

# Como usar o Node-RED Flow:
1. Certifique-se de ter o Node-RED instalado em sua máquina.
2. Abra o Node-RED em seu navegador (geralmente em http://localhost:1880).
3. Importe os fluxos Node-RED fornecidos neste repositório.
4. Configure os fluxos de saída para enviar mensagens para o aplicativo Kivy através de requisições HTTP.

Este projeto é apenas uma demonstração de conceito e pode ser estendido e adaptado para atender às necessidades específicas do seu projeto. Sinta-se à vontade para explorar, modificar e contribuir para o repositório!

Importante: Este repositório contém apenas fins educacionais e para demonstrar a integração entre o Kivy e o Node-RED. Certifique-se de não incluir informações sensíveis em suas aplicações e fluxos de produção.
