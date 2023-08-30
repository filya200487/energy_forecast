import tkinter as tk
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from main_class import EnergyForecast

class EnergyForecastApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Прогноз потребления энергии')
        
        self.file_label = tk.Label(root, text = "Загрузите файл с данными:")
        self.file_label.pack()
        
        self.load_button = tk.Button(root, text = "Загрузить файл", command = self.load_data)
        self.load_button.pack()
        
        self.years_label = tk.Label(root, text = "Введите количество лет для прогноза:")
        self.years_label.pack()
        
        self.years_entry = tk.Entry(root)
        self.years_entry.pack()
        
        self.forecast_button = tk.Button(root, text = "Сделать прогноз", command = self.make_forecast)
        self.forecast_button.pack()
        
        self.canvas = FigureCanvasTkAgg(Figure(), master = root)
        self.canvas.get_tk_widget().pack()
        self.energy_forecast = EnergyForecast(self.canvas)
        
    def load_data(self):
        file_path = filedialog.askopenfilename()
        self.energy_forecast.load_data(file_path)
        
    def make_forecast(self):
        years = int(self.years_entry.get())
        self.energy_forecast.make_forecast(years)
        self.energy_forecast.plot_forecast()
        
    def run(self):
        self.root.mainloop()
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = EnergyForecastApp(root)
    app.run()

