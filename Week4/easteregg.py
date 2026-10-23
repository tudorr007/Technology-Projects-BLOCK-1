import matplotlib.pyplot as plt

with open("temperature.txt") as f:
	temps = [float(line.strip()) for line in f]

plt.plot(temps, marker="o")
plt.title("Temperature over time")
plt.xlabel("Measurement number")
plt.ylabel("Temperature (C)")
plt.grid(True)
plt.show()
plt.savefig("temperature_plot.png")
