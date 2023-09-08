
# Subject class
class WeatherStation:
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity)

    def set_measurements(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.notify_observers()


# Observer classes
class TemperatureDisplay:
    def update(self, temperature, humidity):
        print("Temperature Display - Current temperature: {} degrees Celsius".format(temperature))


class HumidityDisplay:
    def update(self, temperature, humidity):
        print("Humidity Display - Current humidity: {}%".format(humidity))


# Usage example
if __name__ == '__main__':
    weather_station = WeatherStation()

    temperature_display = TemperatureDisplay()
    humidity_display = HumidityDisplay()

    weather_station.register_observer(temperature_display)
    weather_station.register_observer(humidity_display)

    weather_station.set_measurements(26, 60)