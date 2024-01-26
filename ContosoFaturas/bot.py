# Import for the Desktop Bot
from http.client import NOT_FOUND
from botcity.core import DesktopBot
import pandas as pd


bot = DesktopBot()
# Caminho do contoso exe
path_app = r"C:\Program Files (x86)\Contoso, Inc\Contoso Invoicing\LegacyInvoicingApp.exe"
    
# Abrindo o contoso
bot.execute(path_app)
bot.wait(2000)

#Maximizando a tela
if not bot.find( "Maximo", matching=0.97, waiting_time=10000):
    NOT_FOUND("Maximo")
bot.click()


bot.wait(2000)


dados = pd.read_excel('DadosContoso.xlsx')

if not bot.find( "invoices", matching=0.97, waiting_time=10000):
    NOT_FOUND("invoices")
bot.click()

def cadastraFaturas(data, conta, contato, valor, status):

    if not bot.find( "novo-registro", matching=0.97, waiting_time=10000):
        NOT_FOUND("novo-registro")
    bot.click()
    
    #Iniciando o preenchimento do novo resgistro
     
    if not bot.find( "date", matching=0.97, waiting_time=10000):
         NOT_FOUND("date")
    bot.click_relative(69, 13)
    
    #Deletando informações do campo Date:
    bot.type_keys(['home'])
    bot.type_keys(['shift', 'end'])
    
    
    # Inserindo a data
    bot.paste(data)
    # Pulando para o próximo campo
    bot.tab()    
        
    # Nova conta
        
    bot.paste(conta)
    bot.tab()
    
    # Novo contato 
    
    bot.paste(contato)
    bot.tab()    
    
    # Novo amount
    
    bot.paste(valor)   
    
    # Novo Status
    
    if not bot.find( "status-inicio", matching=0.97, waiting_time=10000):
        NOT_FOUND("status-inicio")
    bot.click_relative(117, 9)
    
    # Lógica de onde clicar
    
    coluna = status
    
    if coluna == "Univoiced":
            
        if not bot.find( "Univoiced", matching=0.97, waiting_time=10000):
            NOT_FOUND("Univoiced")
        bot.click_relative(89, 35)
    elif coluna == "Invoiced":
            
        if not bot.find( "invoiced", matching=0.97, waiting_time=10000):
            NOT_FOUND("invoiced")
        bot.click_relative(100, 53)
        
    else:
    
        if not bot.find( "paid", matching=0.97, waiting_time=10000):
            NOT_FOUND("paid")
        bot.click_relative(104, 80)
        
    # Salvando o registro
    if not bot.find( "save", matching=0.97, waiting_time=10000):
        NOT_FOUND("save")
    bot.click()
    
        
    
        
# print('Cadastro concluido com sucesso')
    
    
# print(dados)
# # 
# 
for coluna in dados.itertuples():
    cadastraFaturas(str(coluna[1]), str(coluna[2]), str(coluna[3]), str(coluna[4]), str(coluna[5]))

if not bot.find( "fecharPrograma", matching=0.97, waiting_time=10000):
    NOT_FOUND("fecharPrograma")
bot.click()



print("Missão cumprida :)")