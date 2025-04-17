import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('weather_data.csv')

print(df.head())
print(df.info())
print(df.columns)
print(len(df))

#Wyświetl średnią temperaturę dla każdego miasta oraz medianę i odchylenie standardowe
mean_city_temperature = df.groupby("Location")["Temperature_C"].mean()
print("\n Średnia temperatura \n", mean_city_temperature.head())
median_city_temperature = df.groupby("Location")["Temperature_C"].median()
print("\n Mediana \n",median_city_temperature.head())
standard_deviation = df.groupby("Location")["Temperature_C"].std()
print("\n Odchylenie standardowe \n",standard_deviation.head())



#Znajdź dni o maksymalnej i minimalnej temperaturze w każdym mieście.
hottest_days = df.loc[df.groupby("Location")["Temperature_C"].idxmax()]
print("\n Maksymalna temperatura \n", hottest_days.head(20))
coolest_days = df.loc[df.groupby("Location")["Temperature_C"].idxmin()]
print("\n Minimalna temperatura \n", coolest_days.head(20))



#Narysuj histogram wilgotności powietrza oraz prędkości wiatru. Dobierz odpowiednio typ wykresu, skalę etc.,
#Dodaj do wykresów etykiety osi, legendę oraz tytuł wykresu (w miarę potrzeb) - wykres ma być jasny i czytelny!

# wersja z wykorystaniem losowej próbki danych
df_sample = df.sample(n=5000, random_state=42)  # losujemy 5000 wierszy

plt.figure(figsize=(8, 5))
plt.hist(df_sample["Humidity_pct"], bins=20, color="mediumorchid", edgecolor="black")
plt.title("Histogram wilgotności powietrza (próbka danych)")
plt.xlabel("Wilgotność w %")
plt.ylabel("Liczba dni")
plt.grid(True)
plt.tight_layout()
plt.show()


# Histogram prędkości wiatru
plt.figure(figsize=(8, 5))
plt.hist(df["Wind_Speed_kmh"], bins=20, color="salmon", edgecolor="black")
plt.title("Histogram prędkości wiatru")
plt.xlabel("Prędkość wiatru [km/h]")
plt.ylabel("Liczba dni")
plt.grid(True)
plt.tight_layout()
plt.show()

# wersja z losowymi wierszami
df_sample = df.sample(n=5000, random_state=42)  # losujemy 5000 wierszy

plt.figure(figsize=(8, 5))
plt.hist(df_sample["Wind_Speed_kmh"], bins=20, color="salmon", edgecolor="black")
plt.title("Histogram prędkości wiatru (próbka danych)")
plt.xlabel("Prędkość w km/h")
plt.ylabel("Liczba dni")
plt.grid(True)
plt.tight_layout()
plt.show()


# Znajdź wartości odstające, czyli takie, które przekraczają o 2 
# odchylenia standardowe od średniej dla temperatury, wilgotności powietrza i prędkości wiatru,
temp_mean = df["Temperature_C"].mean()
temp_std = df["Temperature_C"].std()
outliers_temp = df[(df["Temperature_C"] < temp_mean - 2 * temp_std) | 
                   (df["Temperature_C"]  > temp_mean + 2 * temp_std)]

print("\n Temperature \n")
print(temp_mean)
print(temp_std)
print(outliers_temp.head(10))

humidity_mean = df["Humidity_pct"].mean()
humidity_std = df["Humidity_pct"].std()
outliers_humidity = df[(df["Humidity_pct"] < humidity_mean - 2 * humidity_std) |
                       (df["Humidity_pct"] > humidity_mean + 2 * humidity_std)]
print("\n Humidity \n ")
print(humidity_mean)
print(humidity_std)
print(outliers_humidity)

wind_speed_mean = df["Wind_Speed_kmh"].mean()
wind_speed_std = df["Wind_Speed_kmh"].std()
outliers_wind_speed = df[(df["Wind_Speed_kmh"] < wind_speed_mean - 2 * wind_speed_std) |
                       (df["Wind_Speed_kmh"] > wind_speed_mean + 2 * wind_speed_std)]

print("\n Wind Speed \n")
print(wind_speed_mean)
print(wind_speed_std)
print(outliers_wind_speed)

#Oblicz korelację pomiędzy temperaturą i prędkością wiatru,
#Wyświetl wynik oraz interpretację obliczonej korelacji.
correlation = df["Temperature_C"].corr(df["Wind_Speed_kmh"])
print("\n Correlation \n", correlation)


#Korelacja pomiędzy temperaturą a prędkością wiatru jest bardzo zbliżona do zera, co wskazywało by na brak związku między tymi danymi.
#W uproszczeniu, wachania temperatury nie wpływają istotnie na prędkość wiatru.
