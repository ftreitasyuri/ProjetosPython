# Import for the Desktop Bot
from botcity.core import DesktopBot, Backend

''' Notas importantes
    Necessário criar a pasta app ou com qualquer outro nome para colocar o executável
    da aplicação que será aberta pela código;
    Nesse caso criamos a pasta app e colocamo o exe do myCRM nela;
    Para localizar o exe basta clicar no aplicativo com o botão direito e copiar o caminho
'''

bot = DesktopBot()
path = r"C:\BotProject\ProjetoBot\MeuCRM\app\MyCRM.exe"

bot.execute(path)
bot.wait(2000)
bot.connect_to_app(backend=Backend.UIA, path=path)
# Códgio para abrir o app
janelaPrincipal = bot.find_app_window(title='My CRM (Sample App)')
 
# Código para selecionar file e limpar os dados
janelaPrincipal.menu_select('File -> Clear Fields')
bot.wait(2000)
# Código para escrever o nome
janelaPrincipal.type_keys('%{t} Yuri')
bot.wait(2000)
# Código para escrever o sobrenome
janelaPrincipal.type_keys('%{l} Freitas')

janelaPrincipal.menu_select('File -> Open')
# Comando para ver todos os ID's dos campos da janela
# janelaPrincipal.CustumerLookup.print_control_identifiers()

# Comando para escrever no campo Edit2
janelaPrincipal.CustomerLookup.Edit2.type_keys('Outro teste')
# Comando para escrever no campo Edit0
janelaPrincipal.CustomerLookup.Edit0.type_keys('00012')
# Comando para clicar em OK no Button3
janelaPrincipal.CustomerLookup.Button3.click()
bot.wait(1500)
# Código para fechar o app
janelaPrincipal.FecharButton2.click()

print('Código finalizado')

# janelaPrincipal.print_control_identifiers()
