# import
from botcity.document_processing import *
import pathlib
import pandas as pd

#Variáveis
dados = []


def lerPDF(arquivo): 
    
    # Read the file and instantiate the reader
    # parser = PDFReader().read_file(r"C:\BotProject\ProjetoBot\MyFirstBot\docs\Contoso_INVOICE_TailSpin.pdf")
    parser = PDFReader().read_file(arquivo)
    _date = parser.get_first_entry("Date:")
    date = parser.read(_date, 1.357143, -2.2, 3.571429, 4.3)
    print('Date: ' + date)
    
    # Read the file and instantiate the reader
    
    _bill_to = parser.get_first_entry("Bill to:")
    bill_to = parser.read(_bill_to, 1.222222, -2.3, 4.111111, 4)
    print('Bill to: ' + bill_to)

    _contact = parser.get_first_entry("Contact:")
    contact = parser.read(_contact, 1.197368, -1.4, 4.473684, 3)
    print('Contact: ' + contact)
    
    _balance_due = parser.get_first_entry("Balance due:")
    balance_due = parser.read(_balance_due, 1.093333, -1.75, 1.64, 3.333333)
    print('Balance due: ' + balance_due)
    
    dados.append([date, bill_to, contact, balance_due])
    
#pegar todos os arquivos PDF
arquivos = pathlib.Path(r'C:\BotProject\ProjetoBot\MyFirstBot\docs').glob('*.pdf')

for arquivo in arquivos:
    # print(arquivo)
    lerPDF(arquivo)

#Criando um Data Frame usando a extração de dados dos PDF's
df = pd.DataFrame(dados, columns=['Date', 'Bill too', 'Contact', 'Balance due'])

# Passando o DF para CSV
df.to_csv('Dados_pdf.csv', sep=',', index=False)
