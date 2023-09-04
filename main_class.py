import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor


class EnergyForecast:
    def __init__(self, canvas):
        self.data = None   #данные по годам
        self.forecast = None  # данные прогноза
        self.canvas = canvas  # для графика
        
    def load_data(self, file_path): #функция для импорта файла с данными (расширение файла)
        file_extension = file_path.split('.')[-1].lower()
        
        if file_extension == 'csv':
            self.data = pd.read_csv(file_path, sep = ';')
            self.data['electricity_generation'] = self.data['electricity_generation'].str.replace(',', '.').astype(float) 
            self.data = self.data.dropna(subset = ['electricity_generation'])   #Pandas df.dropna () — это встроенный метод DataFrame, которая используется для удаления строк и столбцов со значениями Null/None/NaN из DataFrame в Python.
        
        elif file_extension == 'xlsx':
            self.data = pd.read_excel(file_path)
            self.data = self.data.dropna(subset = ['electricity_generation']) #subset: Это массив, который ограничивает процесс отбрасывания переданными строками/столбцами через список.
                
        elif file_extension == 'json':
            self.data = pd.read_json(file_path)
            self.data = self.data.dropna(subset = ['electricity_generation'])

    def make_forecast(self, years):  #параметры для графика
        if self.data is not None:
            X = self.data['year'].values.reshape(-1,1)
            Y = self.data['electricity_generation'].values
            model = RandomForestRegressor(n_estimators=100, random_state=0) #параметр n_estimators определяет количество деревьев в случайном лесу.
            model.fit(X, Y) #Подгонка модели 
            
            future_years = np.arange(self.data['year'].max() +1, self.data['year'].max() + 1 + years)
            forecast = model.predict(future_years.reshape(-1, 1)) #прогноз
            self.forecast = pd.DataFrame({'year': future_years, 'forecast': forecast})
            
        else:
            print("Данные не загружены.")
            
    def plot_forecast(self): #построение фигуры графика
        if self.forecast is not None:
            figure = plt.figure(figsize = (6, 6))
            ax = figure.add_subplot(1,1,1)
            ax.plot(self.data['year'], self.data['electricity_generation'], label = 'Исходные данные')
            ax.plot(self.forecast['year'], self.forecast['forecast'], label = 'Прогноз')
            ax.set_xlabel('Год')
            ax.set_ylabel('Потребление энегргии')
            ax.legend()
            
            self.canvas.future = figure
            self.canvas.draw()
        
        else:
            print("Ошибка. Прогноз не сделан.")
            
            
            
        
    
        
