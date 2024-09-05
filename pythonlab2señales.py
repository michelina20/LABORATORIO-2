import librosa
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter



# Creación del filtro pasa bajo
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


# Aplicación del filtro pasa bajo
def lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y



#AISLAR PARA SEÑAL 1:

audio_file = '1MICHEL Y ELI.wav'
y, sr = librosa.load(audio_file, sr=None, mono=False)

if y.ndim > 1:
    y = librosa.to_mono(y)

cutoff_freq = 800.0  
y_filtered = lowpass_filter(y, cutoff_freq, sr, order=12)
output_file = 'voz_grave_filtrada1.wav'
sf.write(output_file, y_filtered, sr)
print(f"Archivo guardado: {output_file}")



#AISLAR PARA SEÑAL 2:

audio_file2 = '2MICHEL Y ELI.wav'
y2, sr2 = librosa.load(audio_file2, sr=None, mono=False)

if y2.ndim > 1:
    y2 = librosa.to_mono(y2)

cutoff_freq2 = 800.0  
y2_filtered = lowpass_filter(y2, cutoff_freq2, sr2, order=12)
output_file2 = 'voz_grave_filtrada_2.wav'
sf.write(output_file2, y2_filtered, sr2)
print(f"Archivo guardado: {output_file2}")




#AISLAR PARA SEÑAL 3:
    
audio_file3 = '3MICHEL Y ELI.wav'
y3, sr3 = librosa.load(audio_file3, sr=None, mono=False)

if y3.ndim > 1:
    y3 = librosa.to_mono(y3)

cutoff_freq3 = 800.0  
y3_filtered = lowpass_filter(y3, cutoff_freq3, sr3, order=12)
output_file3 = 'voz_grave_filtrada_3.wav'
sf.write(output_file3, y3_filtered, sr3)
print(f"Archivo guardado: {output_file3}")




#SUMA DE SEÑALES AISLADAS:

    
min_length = min(len(y_filtered), len(y2_filtered), len(y3_filtered))
y_filtered = y_filtered[:min_length]
y3_filtered = y3_filtered[:min_length]
y2_filtered = y2_filtered[:min_length]

summed_signal = y_filtered + y2_filtered + y3_filtered

#Se normaliza la señal
summed_signal = summed_signal / np.max(np.abs(summed_signal))

output_file_summed = 'voz_grave_sumada.wav'
sf.write(output_file_summed, summed_signal, sr)
print(f"Archivo guardado: {output_file_summed}")




#SNR PARA PRIMERA SEÑAL:

ruido_1 = '1SILENCIO.wav'
ruido_y, sr = librosa.load(audio_file, sr=None, mono=False)

min_length = min(len(y), len(ruido_y))
y = y[:min_length]
ruido_y = ruido_y[:min_length]


PRIMERA_squared = np.square(y)
sumatoria_PRIMERA = np.sum(PRIMERA_squared)
resultado_potencia_PRIMERA = sumatoria_PRIMERA / len(y)


ruido_squared = np.square(ruido_y)
sumatoria_ruido = np.sum(ruido_squared)
resultado_potencia_ruido = sumatoria_ruido / len(ruido_y)

SNR=10*np.log10(resultado_potencia_PRIMERA/resultado_potencia_ruido)

print("SNR PARA PRIMER MICRÓFONO (dB):", SNR)




#SNR PARA SEGUNDA SEÑAL:

ruido_2 = '2SILENCIO.wav'
ruido2_y, sr = librosa.load(audio_file, sr=None, mono=False)


SEGUNDA_squared = np.square(y2)
sumatoria_SEGUNDA = np.sum(SEGUNDA_squared)
resultado_potencia_SEGUNDA = sumatoria_SEGUNDA / len(y2)


ruido2_squared = np.square(ruido2_y)
sumatoria_ruido2 = np.sum(ruido2_squared)
resultado_potencia_ruido2 = sumatoria_ruido2 / len(ruido2_y)

SNR_2=10*np.log10(resultado_potencia_SEGUNDA/resultado_potencia_ruido2)

print("SNR PARA SEGUNDO MICRÓFONO (dB):", SNR_2)




#SNR PARA TERCERA SEÑAL:

ruido_3 = '3SILENCIO.wav'
ruido3_y, sr = librosa.load(audio_file, sr=None, mono=False)


TERCERA_squared = np.square(y3)
sumatoria_TERCERA = np.sum(TERCERA_squared)
resultado_potencia_TERCERA = sumatoria_TERCERA / len(y3)


ruido3_squared = np.square(ruido3_y)
sumatoria_ruido3 = np.sum(ruido3_squared)
resultado_potencia_ruido3 = sumatoria_ruido3 / len(ruido3_y)

SNR_3=10*np.log10(resultado_potencia_TERCERA/resultado_potencia_ruido3)

print("SNR PARA TERCER MICRÓFONO (dB):", SNR_3)




#COMPARACIÓN DE SEÑAL AISLADA CON LA ORIGINAL DE CADA MICRÓFONO

#Para micrófono 1:
    
y_filtered_squared = np.square(y_filtered)
sumatoria_y_filtered = np.sum(y_filtered_squared)
resultado_potencia_y_filtered = sumatoria_y_filtered / len(y_filtered)

SNR_Aislada_1= 10*np.log10(resultado_potencia_y_filtered/resultado_potencia_PRIMERA)

print("COMPARACIÓN SNR SEÑAL AISLADA 1 CON SEÑAL 1  (dB):", SNR_Aislada_1)


#Para micrófono 2:
    
y2_filtered_squared = np.square(y2_filtered)
sumatoria_y2_filtered = np.sum(y2_filtered_squared)
resultado_potencia_y2_filtered = sumatoria_y2_filtered / len(y2_filtered)

SNR_Aislada_2= 10*np.log10(resultado_potencia_y2_filtered/resultado_potencia_SEGUNDA)

print("COMPARACIÓN SNR SEÑAL AISLADA 2 CON SEÑAL 2  (dB):", SNR_Aislada_2)


#Para micrófono 3:
    
y3_filtered_squared = np.square(y3_filtered)
sumatoria_y3_filtered = np.sum(y3_filtered_squared)
resultado_potencia_y3_filtered = sumatoria_y3_filtered / len(y3_filtered)

SNR_Aislada_3= 10*np.log10(resultado_potencia_y3_filtered/resultado_potencia_TERCERA)

print("COMPARACIÓN SNR SEÑAL AISLADA 3 CON SEÑAL 3  (dB):", SNR_Aislada_3)




#COMPARACIÓN DE SEÑAL AISLADA FINAL CON LA ORIGINAL DE CADA MICRÓFONO

#Para micrófono 1:
    
summed_signal = np.square(summed_signal)
sumatoria_summed_signal = np.sum(summed_signal)
resultado_potencia_summed_signal = sumatoria_summed_signal / len(summed_signal)

SNR_Aislada_FIN1= 10*np.log10(resultado_potencia_summed_signal/resultado_potencia_PRIMERA)

print("COMPARACIÓN SNR SEÑAL AISLADA FINAL CON SEÑAL 1  (dB):", SNR_Aislada_FIN1)


#Para micrófono 2:
    
summed_signal = np.square(summed_signal)
sumatoria_summed_signal = np.sum(summed_signal)
resultado_potencia_summed_signal = sumatoria_summed_signal / len(summed_signal)

SNR_Aislada_FIN2= 10*np.log10(resultado_potencia_summed_signal/resultado_potencia_SEGUNDA)
print("COMPARACIÓN SNR SEÑAL AISLADA FINAL CON SEÑAL 2  (dB):", SNR_Aislada_FIN2)


#Para micrófono 3:
    
summed_signal = np.square(summed_signal)
sumatoria_summed_signal = np.sum(summed_signal)
resultado_potencia_summed_signal = sumatoria_summed_signal / len(summed_signal)

SNR_Aislada_FIN3= 10*np.log10(resultado_potencia_summed_signal/resultado_potencia_TERCERA)

print("COMPARACIÓN SNR SEÑAL AISLADA FINAL CON SEÑAL 3  (dB):", SNR_Aislada_FIN3)





#ANÁLISIS TEMPORAL Y ESPECTRAL DE LA SEÑAL 1 :
    


#Análisis Temporal:

plt.figure(figsize=(12, 6))
plt.title('Señal Micrófono 1')
plt.xlabel('Tiempo (Segundos)')
plt.ylabel('dB')
librosa.display.waveshow(y, sr=sr)
plt.tight_layout()
plt.show()


#Análisis Espectral:


N = len(y)  
Y = np.fft.fft(y) 
frequencies = np.fft.fftfreq(N, 1/sr)  

half_N = N // 2
Y_half = Y[:half_N] 
frequencies_half = frequencies[:half_N]  

magnitude = np.abs(Y_half)

plt.figure(figsize=(14, 5))
plt.plot(frequencies_half, magnitude)
plt.title('Espectro de Frecuencia de la Señal 1')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.xlim(0, sr/2)  
plt.grid()
plt.show()



#ANÁLISIS TEMPORAL Y ESPECTRAL DE LA SEÑAL 2 :



#Análisis Temporal Micrófono 2:

plt.figure(figsize=(12, 6))
plt.title('Señal Micrófono 2')
plt.xlabel('Tiempo (Segundos)')
plt.ylabel('dB')
librosa.display.waveshow(y2, sr=sr)
plt.tight_layout()
plt.show()


#Análisis Espectral Micrófono 2:

N2 = len(y2)  
Y2 = np.fft.fft(y2)  
frequencies2 = np.fft.fftfreq(N2, 1/sr) 

half_N2 = N2 // 2
Y_half2 = Y2[:half_N2]  
frequencies_half2 = frequencies2[:half_N2]  

magnitude2 = np.abs(Y_half2)

plt.figure(figsize=(14, 5))
plt.plot(frequencies_half2, magnitude2)
plt.title('Espectro de Frecuencia de la Señal 2')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.xlim(0, sr/2) 
plt.grid()
plt.show()



#ANÁLISIS TEMPORAL Y ESPECTRAL DE LA SEÑAL 2 :

    
#Análisis Temporal Micrófono 3:

plt.figure(figsize=(12, 6))
plt.title('Señal Micrófono 3')
plt.xlabel('Tiempo (Segundos)')
plt.ylabel('dB')
librosa.display.waveshow(y3, sr=sr)
plt.tight_layout()
plt.show()


#Análisis Espectral Micrófono 3:

N3 = len(y3)  
Y3 = np.fft.fft(y3)  
frequencies3 = np.fft.fftfreq(N3, 1/sr) 

half_N3 = N3 // 2
Y_half3 = Y3[:half_N3]  
frequencies_half3 = frequencies3[:half_N3]  

magnitude3 = np.abs(Y_half3)

plt.figure(figsize=(14, 5))
plt.plot(frequencies_half3, magnitude3)
plt.title('Espectro de Frecuencia de la Señal 3')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.xlim(0, sr/2) 
plt.show()
