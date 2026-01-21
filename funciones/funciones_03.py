

calorias = [120, 180, 250, 310, 420]

#Map

recomendaciones = list(map(lambda caloria: "Snack Liviano" if caloria < 150 else "Barrita energética" if caloria <= 300 else "Smoothuie o batido" , calorias))

print(recomendaciones)

#Filter

intensos = list(filter(lambda caloria: caloria > 300 , calorias))

print(intensos)