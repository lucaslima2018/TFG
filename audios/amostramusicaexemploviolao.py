import matplotlib.pyplot as plt
import numpy as np
import wave
import struct

def main():
    '''Abrir o arquivo “exemplo1.wav”, com o comando open do pacote wave no modo leitura'''
    arquivoWave = wave.open('musicaexemploviolao.wav', 'r')

    '''A função “getnchannels()” retorna o número de canais armazenados no arquivo wav. No exemplo
    somente arquivos mono serão processados'''
    print("Número canais: ", arquivoWave.getnchannels())

    '''A função “getsamplewidth()” retorna o numero de bytes por amostra. No exemplo apenas 2 bytes por
    amostra'''
    print("Número bytes: ", arquivoWave.getsampwidth())

    '''A função “getframerate()” retorna a taxa de amostragem (amostras por segundo) com que foram 
    gravados os dados wav.'''
    print("Taxa de amostragem: ", arquivoWave.getframerate())

    '''A função “getnframes” retorna o número de frames, ou seja, a quantidade de dados armazenados.'''
    print("Número de frames: ", arquivoWave.getnframes())

    '''A função “getcompname()” retorna o tipo de compactação. Nenhuma compactação foi usada.'''
    print("Compactação: ", arquivoWave.getcompname())

    '''A função “readFrames(nFrames)” retorna uma string binária com todos os bytes armazenados na 
    área de dados do arquivo wav.'''
    frames = arquivoWave.readframes(arquivoWave.getnframes())

    '''DeltaX é o intervalo de amostragem, em segundos.'''
    deltaX = 1.0 / arquivoWave.getframerate()

    '''Criar array numpy que conterá os pontos de amostragem distribuídos no tempo.'''
    tempo = np.arange(start=0, stop=arquivoWave.getnframes() * deltaX, step=deltaX, dtype=np.float)

    '''Converter string binária lida através de “readframes” para uma lista python.'''
    waveDataList = []
    print('Tamanho da variavel frames: ',len(frames))

    for nLoop in range(0, len(frames), 2):
        waveDataList.append(struct.unpack('<h', (frames[nLoop] + frames[nLoop + 1]).to_bytes(2,'big')))

    #waveDataList = [struct.unpack("<h", frames[nLoop] + frames[nLoop + 1])[0] for nLoop in range(0, len(frames), 2)]

    '''Converter a lista python para um array numpy, mais adequado para processamento matemático.'''
    waveArray = np.array(waveDataList)

    '''Preparar para traçar o gráfico dos primeiros 100 pontos do array. 100 pontos foram selecionados
    para apresentar cerca de dois ciclos completos na tela.'''
    plt.plot(tempo[0:100], waveArray[0:100])

    '''Inserir grade na tela'''
    plt.grid()

    '''Mostrar o gráfico. Para fechar pressione o “x” no canto superior direito.'''
    plt.show()

    '''Fechar arquivo wav.'''
    arquivoWave.close()
    return 0

# if __name__ == '__main__':
#     import sys
#
#     sys.exit(main(sys.argv))

main()