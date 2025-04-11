from flask import jsonify, request

cars = []
next_id = 0  # To keep track of the next car ID


def register_routes(app):
    global next_id

    @app.route('/')
    def home():
        return 'hello'

    @app.get('/cars')
    def get_cars():
        return jsonify(cars)

    @app.post('/cars')
    def add_car():
        global next_id
        car = request.json
        car['id'] = next_id
        next_id += 1
        cars.append(car)
        return jsonify(car), 201

    @app.get('/cars/<int:id>')
    def get_car(id):
        car = next((car for car in cars if car['id'] == id), None)
        if car is None:
            return jsonify({'error': 'Car not found'}), 404
        return jsonify(car)

    @app.put('/cars/<int:id>')
    def update_car(id):
        updated_car = request.json
        for i, car in enumerate(cars):
            if car['id'] == id:
                updated_car['id'] = id  # Preserve the ID
                cars[i] = updated_car
                return jsonify(updated_car)
        return jsonify({'error': 'Car not found'}), 404

    @app.delete('/cars/<int:id>')
    def delete_car(id):
        del cars[id]
        return {"message" : "deleted"}, 200