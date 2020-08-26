import minimalmodbus # importa a biblioteca modbus
import serial # importa as funções do SO para acessar as portas de comunicação
import time # importa as funções de tempo (para poder usar o sleep)

instrument = minimalmodbus.Instrument('COM7',1,'rtu') # Configura o "instrumento" que será lido (COM7, endereço do escravo 1, ativa modbus RTU)

# Configurações adicionais da porta serial
#instrument.serial.port # this is the serial port name
#instrument.serial.baudrate = 19200         # Baud
#instrument.serial.bytesize = 8
#instrument.serial.parity   = serial.PARITY_NONE
#instrument.serial.stopbits = 1
#instrument.serial.timeout  = 0.05          # seconds
#instrument.address = 1                     # this is the slave address number
#instrument.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
#instrument.clear_buffers_before_each_transaction = True


time.sleep(2) # Põem o código para dormir por 2s
value =instrument.read_register(5,0,3) # Le o valor do registrador 5,  0 casas decimais, função 3 do modbus (Read Holding Registers)
time.sleep(1) # Põem o código para dormir por 1s
print (value) # Mostra na tela o valor ligo no registrador 5
instrument.write_register(5,520,0,16) # Escreve no registrador 5, 520 valor escrito, 0 casas decimais, função 16 do modbus (Preset Holding Registers)
time.sleep(1) # Põem o código para dormir por 1s

value =instrument.read_register(5,0,3) # Le o valor do registrador 5,  0 casas decimais, função 3 do modbus (Read Holding Registers)
time.sleep(1) # Põem o código para dormir por 1s
print (value) # Mostra na tela o valor ligo no registrador 5