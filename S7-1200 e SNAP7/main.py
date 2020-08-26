import snap7
import sys
import time

# Atribui o caminho da Classe Client() que contem os metodos de acesso, leitura e escrita no CLP
plc = snap7.client.Client()

# Atribui o caminho da Classe Util que contém os 
# métodos para tratar os dados na leitura ou escrita para o CLP.
# A troca de dados é feita através de um Array de bytes do tipo bytearray.
data_edit = snap7.util

#Configuração de conexão com o CLP
ip = '192.168.0.1' #Enderço IP do CLP.
rack = 0 # Número do Rack que o CLP está (para os S7-1200 geralmente 0)
slot = 1 # Númro do slot no rack que o CPL está (para os S7-1200 geralmente 0).

try:
	plc.connect(ip, rack, slot) # Metódo da Classe Client() que cria a conexão com o CLP
except:
	print('Erro na conexão com o CLP')
	sys.exit()

time.sleep(1) #Pausa em segundos na execução do programa

status_connect = plc.get_connected() # get_connected() retorna um boleano com o status da conexão com o CLP true = ok, false = erro.
print(status_connect)
print()
status_clp = plc.get_cpu_state() # get_cpu_state() retorna uma string com o status do CLP.
print(status_clp)
print()
time.sleep(1) #Pausa em segundos na execução do programa

n_db = 1 # Número do DB que será acessado.
n_offset = 0 # Número do Offset do DB. (Endereço de inico)
n_size = 1 # Número de bytes a ser lidos.
array_data = bytearray(b'\x00') # Array de bytes necessário para troca de dados com o CLP

#Tratamento dos bits dentro do bytearray para escrever em um bit especifico da DB
byte_index = 0 # Indice do Array bytearray (indece do byte a ser modificado)
bool_index = 0 # Bit do Byte a ser modificado.
value = 1 # Valor que será atribuido ao bit 

# Seta um valor em um bit especifico dentro do bytearray
# Será configurado para setar o DB1.DBX0.1
data_edit.set_bool(array_data, byte_index, bool_index, value)
print('Byte array configurado para escrever em DB1.DBX0.1')
time.sleep(1)

#Endereço da area interna de memória do CLP :
# 132 = DB
# 131 = Merkers
# 130 = Outputs
# 129 = Inputs
# 29 = Timers
# 28 = Contadores
area_memoria = 132 # Indica a area de memoria DB.

# Escrita de valor em uma determinada area de memória (neste caso em um DB).
# Será passado o Array configurado anteriormente para fazer escrever em DB1.DBX0.1
plc.write_area(area_memoria, n_db, n_offset, array_data)
print('Escrito com sucesso em DB1.DBX0.1')
time.sleep(1)

# Leitura de valor em uma determinada area de memória (neste caso em um DB).
# Retorno da função é um array do tipo bytearray.
return_data = plc.read_area(area_memoria, n_db, n_offset, n_size)
print('Leitura do DB1')
time.sleep(1)

# Leitura de um bit especico dentro de um bytearray.
# Será configurada a função get_bool para ler o DB1.DBX0.2
bool_index = 2 # Muda o indice para 2 para ler o segundo bit do primeiro byte do bytearray
value_bit = data_edit.get_bool(return_data, byte_index, bool_index)
print('Valor do DB1.DBX0.2 = ')
print(value_bit)

# Desfaz a conexão com o CLP.
plc.disconnect() 


