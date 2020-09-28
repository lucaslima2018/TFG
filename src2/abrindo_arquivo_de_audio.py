import matplotlib.pyplot as plt
import numpy as np
import wave
import struct
import math


def main(args):
    arquivoWav = wave.open('../../../Desktop/tri.wav', 'r')
    print("Número canais: ", arquivoWav.getnchannels())

    print("Número bytes: ", arquivoWav.getsampwidth())

    print("Taxa de amostragem: ", arquivoWav.getframerate())

    print("Número de frames: ", arquivoWav.getnframes())

    print("Compactação: ", arquivoWav.getcompname())

    frames = arquivoWav.readframes(arquivoWav.getnframes())

    deltaX = 1.0 / arquivoWav.getframerate()

    tempo = np.arange(start=0, stop=arquivoWav.getnframes() * deltaX, step=deltaX, dtype=np.float)

    wavDataList = [struct.unpack("<h", frames[nLoop] + frames[nLoop + 1])[0] for nLoop in range(0, len(frames), 2)]

    wavArray = np.array(wavDataList)

    plt.plot(tempo[0:100], wavArray[0:100])
    plt.grid()
    plt.show()

    arquivoWav.close()
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))