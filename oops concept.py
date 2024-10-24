#1
class Circle:
    def __init__(self, radii):
        self.radii = radii

    def display_radii(self):
        for radius in self.radii:
            print(f"Circle with radius: {radius}")

# Example usage
radii = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii)
circle.display_radii()
#2
class Circle:
    __pi = 3.141  # Private class variable

    def __init__(self, radii):
        self.radii = radii

    def display_radii(self):
        for radius in self.radii:
            print(f"Circle with radius: {radius}")

    def calculate_area(self):
        for radius in self.radii:
            area = self.__pi * (radius ** 2)
            print(f"Circle with radius {radius} has an area of: {area:.2f}")

    def calculate_circumference(self):
        for radius in self.radii:
            circumference = 2 * self.__pi * radius
            print(f"Circle with radius {radius} has a circumference of: {circumference:.2f}")

# Example usage
radii = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii)
circle.display_radii()
circle.calculate_area()
circle.calculate_circumference()
#3
class Circle:
    __pi = 3.141  # Private class variable

    def __init__(self, radii):
        self.radii = radii

    def display_radii(self):
        for radius in self.radii:
            print(f"Circle with radius: {radius}")

    @classmethod
    def area(cls, radius):
        return cls.__pi * (radius ** 2)

    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.__pi * radius

    def calculate_areas(self):
        for radius in self.radii:
            area = self.area(radius)
            print(f"Circle with radius {radius} has an area of: {area:.2f}")

    def calculate_perimeters(self):
        for radius in self.radii:
            perimeter = self.perimeter(radius)
            print(f"Circle with radius {radius} has a perimeter of: {perimeter:.2f}")

# Example usage
radii = [10, 501, 22, 37, 100, 999, 87, 351]
circle = Circle(radii)
circle.display_radii()
circle.calculate_areas()
circle.calculate_perimeters()
#4
class TV:
    def __init__(self, brand, price, inches):
        self.brand = brand
        self.price = price
        self.inches = inches
        self.channel = 1
        self.volume = 50
        self.on_off_status = False

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

    def toggle_power(self):
        self.on_off_status = not self.on_off_status
        return "TV is On" if self.on_off_status else "TV is Off"

# Example Usage
tv = TV("Panasonic", 300, 42)
print(tv.status())  # Panasonic at channel 1, volume 50
tv.increase_volume()
tv.set_channel(8)
print(tv.status())  # Panasonic at channel 8, volume 51
tv.toggle_power()  # TV is On
#part B
class LedTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        return "Wide Viewing Angle"

    def backlight(self):
        return "LED Backlight"

    def display_details(self):
        return (f"Brand: {self.brand}, Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}W, "
                f"Lifespan: {self.lifespan} hours, Refresh Rate: {self.refresh_rate}Hz, {self.viewing_angle()}, {self.backlight()}")

class PlasmaTV(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        return "Ultra-Wide Viewing Angle"

    def backlight(self):
        return "Plasma Backlight"

    def display_details(self):
        return (f"Brand: {self.brand}, Screen Thickness: {self.screen_thickness}, Energy Usage: {self.energy_usage}W, "
                f"Lifespan: {self.lifespan} hours, Refresh Rate: {self.refresh_rate}Hz, {self.viewing_angle()}, {self.backlight()}")

# Example Usage
led_tv = LedTV("Samsung", 500, 55, "2cm", 150, 40000, 120)
plasma_tv = PlasmaTV("LG", 700, 60, "3cm", 200, 30000, 60)

print(led_tv.display_details())
print(plasma_tv.display_details())
