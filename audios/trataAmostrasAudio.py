import numpy as np
import wave
from audios.Entrada import Entrada
def main():
    lista_arquivos_amostras = []
    lista_arquivos_amostras.append(wave.open('violao1.wav', 'r'))
    lista_arquivos_amostras.append(wave.open('violao2.wav', 'r'))
    lista_arquivos_amostras.append(wave.open('violao3.wav', 'r'))
    lista_arquivos_amostras.append(wave.open('acordeon1.wav', 'r'))
    lista_arquivos_amostras.append(wave.open('acordeon2.wav', 'r'))
    lista_arquivos_amostras.append(wave.open('acordeon3.wav', 'r'))
    lista_entradas = []
    lista_saidas = ['violao', 'violao', 'violao', 'acordeon', 'acordeon', 'acordeon']

    for i in lista_arquivos_amostras:
        numero_canais = i.getnchannels()
        numero_bytes = i.getsampwidth()
        taxa_amostragem = i.getframerate()
        frames = i.readframes(i.getnframes())
        numero_frames = i.getnframes()
        deltaX = 1.0 / i.getframerate()
        tempo = np.arange(start=0, stop=i.getnframes() * deltaX, step=deltaX, dtype=np.float)
        #calcular frequencia e amplitude antes de guardar na lista_entradas
        #Cálculo da Frequência:
        #Cálculo da Amplitude:
        dados_entrada = Entrada(numero_canais, numero_bytes, taxa_amostragem, numero_frames, frames,  deltaX, tempo)
        lista_entradas.append( dados_entrada )
        i.close()

    j = 0
    for e in lista_entradas:
        print('Arquivo ', j+1)
        print('Numero de frames: ', e.numero_frames)
        print('DeltaX: ', e.deltaX)
        print('Tempo: ', e.tempo)
        print('Saida: ', lista_saidas[j])
        print('=============')
        j = j + 1

    return 0

# if __name__ == '__main__':
#     import sys
#
#     sys.exit(main(sys.argv))

main()