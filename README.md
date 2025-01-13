# Mini Curso IoT - UFC 2025.
Repositório com scripts para o mini curso de IoT na UFC.

> Abaixo estão algumas orientações para realização da prática que será realizada no mini curso, seguidas dos scripts que serão utilizados. Para realização da Prática I deve-se seguir a orientação que está no script .ino no wifimanager.

## Práticas
### Prática I

> Faça um gerenciador de Wi-Fi no seu ESP32 para gerenciar o login em redes sem fio em seus projetos IoT. Para isso, abre a pasta "PRÁTICA_I" e siga as instruções do script.

### Prática II

> Nessa prática, iremos desenvolver um medidor de nível sem fio para reservatórios  (silos, caixas dágua e tanques) utilizando sensor ultrassônico. Além disso, a verificação do nível terá acesso remoto e também vamos realizar a automação de notificações via e-mail de forma gratuita.

OBS: Para realização das práticas, faça as instalações necessárias e crie credenciais de usuário nas plataformas gratuitas abordadas.

## Instalações Necessárias
### Instalando a IDE do arduino

Na Arduino IDE, abra a janela de Preferências e digite as URLs abaixo no campo “URLs adicionais de Gerenciadores de Placas” (clique no ícone lateral) e selecione OK para retornar para a tela principal. Você pode acrescentar mais links separando-os com uma vírgula ou quebra de linha.

Link ESP32 board: https://dl.espressif.com/dl/package_esp32_index.json

Agora clique em Ferramentas → Placa → Gerenciador de Placas e busque por ESP32. Em seguida, clique em Instalar. Reinicie o arduino IDE. Agora vá em Ferramentas → Placa e selecione a placa Node MCU ESP32.

### Crie uma conta no ThinksPeak

1. Criar uma conta no site: https://thingspeak.mathworks.com/;
2. Crie um novo canal (Channel) e crie uma variável para receber os dados de profundidade do reservatório;
3. Vá para a aba API Keys e copie a chaves de API;

### Criar conta no GitHub e criar um repositório para o Projeto
1. Criar conta, siga tutorial: https://docs.github.com/pt/get-started/start-your-journey/creating-an-account-on-github;
2. Criar repositório, subir página .html disponibilizada com as modificações personalizadas realizadas.

### Criar conta na VERCEL e puxar repositório do GitHub
1. Criar conta na VERCEL, seguir tutorial: https://vercel.com/docs/accounts/create-an-account;
2. Vincular GitHub com a VERCEL e puxar repositório com página .html.

### Automatizar e-mails de alerta
1. Configure o script send_email com as configurações do e-mail;
2. Leve o script para um servidor linux e altere o nível de acesso do usuário com o comando: sudo chmod +x /send_email.py;
2. Crie um script com extensão .sh e insira os comandos a seguir:
    
    #!/bin/bash

    python3 send_email.py
    echo "E-mail enviado via tarefas agendadas em: $(date)" > ~/

3. Salve o arquivo .sh e altera o nível de acesso com o comando sudo chmod +x arquivo.sh
4. Digite o comando: crontab -e
5. Navegue até a ultima linha do arquivo e insira o comando a seguir para que seja efetuada a leitura da variável a cada 30 minutos: 

    */30 * * * * ~/./arquivo.sh

6. Salve o arquivo e execute o comando: sudo systemctl restart cron
7. Pronto, sua aplicação está rodando com link para visualização e alertas automatizados via e-mail.


