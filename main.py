import asyncio, asyncvnc, os

import ctypes

img1 = r"C:\Users\47316025808\Downloads\unisal.png"
ipMaquina = '10.10.30.5'

import time

from screeninfo import get_monitors

async def run_client():
   resultado = os.system(f'.\sendBg.bat {ipMaquina} {img1}')

   if (resultado != 0): print('erro ao enviar')


#    async with asyncvnc.connect('10.10.30.5', password='vncAdmin') as client:
#         #print(client.video.)
        
        
#         monitor=get_monitors()



#         altura=monitor[0].height   
#         largura=monitor[0].width

#         print(largura, altura)

#         if altura==900 and largura==1440:

#                 #ctypes.windll.user32.SystemParametersInfoW(20,0,img1,0)

#                 client.keyboard.write ('super', 'r')

#                 client.keyboard.write ('reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d {caminho} /f')

#                 print('Executado')


#         else: print('Falha')



        

        

        

asyncio.run(run_client()) 