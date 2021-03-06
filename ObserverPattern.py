# class WeatherData:
#
#     def get_temp(self):
#         pass
#
#     def get_humidity(self):
#         pass
#
#     def get_wind_force(self):
#         pass
#
#     def update(self):
#
#         Display1.update(self.temp, self.humidity, self.wind_force)
#         Display3.update(self.temp, self.humidity, self.wind_force)
#         Display2.update(self.temp, self.humidity, self.wind_force)

import abc


class SubjectInterface(abc.ABC):

    @abc.abstractmethod
    def register(self, obj):
        pass

    @abc.abstractmethod
    def remove(self, obj):
        pass

    @abc.abstractmethod
    def notify(self):
        pass


class WeatherData(SubjectInterface):
    def __init__(self):
        self.temp = None
        self.humidity = None
        self.wind_force = None
        self.subscriber_list = []

    def register(self, obj):
        self.subscriber_list.append(obj)

    def remove(self, obj):
        self.subscriber_list.remove(obj)

    def notify(self):
        for subscriber in self.subscriber_list:
            subscriber.update(self.temp, self.humidity, self.wind_force)

    def get_measurements(self, temp, humidity, wind_force):
        self.temp = temp
        self.humidity = humidity
        self.wind_force = wind_force

        self.notify()


class SubscriberInterface(abc.ABC):

    @abc.abstractmethod
    def update(self, temp, humidity, wind_force):
        pass


class CityDisplay(SubscriberInterface):

    def update(self, temp, humidity, wind_force):
        self.temp = temp
        self.humidity = humidity
        self.wind_force = wind_force

        print(f'CityDisplay - Temp: {self.temp}, humidity: {self.humidity}, wind_force: {self.wind_force}')


class RoadDisplay(SubscriberInterface):

    def update(self, temp, humidity, wind_force):
        self.temp = temp
        self.humidity = humidity
        self.wind_force = wind_force

        print(f'RoadDisplay - Temp: {self.temp}, humidity: {self.humidity}, wind_force: {self.wind_force}')


class VillageDisplay(SubscriberInterface):

    def update(self, temp, humidity, wind_force):
        self.temp = temp
        self.humidity = humidity
        self.wind_force = wind_force

        print(f'VillageDisplay - Temp: {self.temp}, humidity: {self.humidity}, wind_force: {self.wind_force}')


display_1 = CityDisplay()
display_2 = RoadDisplay()
display_3 = VillageDisplay()

weather_data = WeatherData()
weather_data.get_measurements(1, 84, 34)
weather_data.register(display_1)
weather_data.get_measurements(2, 84, 34)
weather_data.register(display_2)
weather_data.get_measurements(3, 24, 35)
weather_data.register(display_3)

weather_data.get_measurements(4, 84, 34)
