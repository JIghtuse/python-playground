def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing information about a car."""
    car = {
        manufacturer: manufacturer,
        model: model,
    }
    car.update(car_info)
    return car
