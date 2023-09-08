from abc import ABC, abstractmethod

# Abstract observer class
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float):
        pass

# Abstract subject class
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass
    
    @abstractmethod
    def unregister_observer(self, observer: Observer):
        pass
    
    @abstractmethod
    def notify_observers(self):
        pass

# Concrete subject class
class WeatherStation(Subject):
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.observers = []
    
    def register_observer(self, observer: Observer):
        self.observers.append(observer)
    
    def unregister_observer(self, observer: Observer):
        self.observers.remove(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity)
    
    def set_measurements(self, temperature: float, humidity: float):
        self.temperature = temperature
        self.humidity = humidity
        self.notify_observers()

# Concrete observer class
class TemperatureDisplay(Observer):
    def update(self, temperature: float, humidity: float):
        print(f"Temperature Display - Current temperature: {temperature} degrees Celsius")

# Concrete observer class
class HumidityDisplay(Observer):
    def update(self, temperature: float, humidity: float):
        print(f"Humidity Display - Current humidity: {humidity}%")

# Usage example
if __name__ == '__main__':
    weather_station = WeatherStation()

    temperature_display = TemperatureDisplay()
    humidity_display = HumidityDisplay()

    weather_station.register_observer(temperature_display)
    weather_station.register_observer(humidity_display)

    weather_station.set_measurements(26, 60)