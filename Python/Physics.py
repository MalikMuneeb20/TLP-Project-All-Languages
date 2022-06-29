from typing import final

class Kinematics :
    # speed
    def speed(distance, time):
        _speed = distance / time
        return _speed

    # velocity
    def velocity(displacement, time):
        _velocity = displacement / time
        return _velocity
    
    def velocity_using_initialVelocity_acceleration_time(initial_velocity, acceleration, time):
        _velocity = initial_velocity + (acceleration * time)
        return _velocity

    def velocity_using_initialVelocity_displacement_time(initial_velocity, displacement, time):
        _velocity = 2 * (displacement/time) - initial_velocity
        return _velocity

    def velocity_using_initialVelocity_displacement_acceleration(initial_velocity,displacement ,acceleration):
        _value = initial_velocity**2 + 2 * acceleration * displacement
        _velocity = (_value)**0.5
        return _velocity 

    def change_in_velocity(initial_velocity, final_velocity):
        _velocity = final_velocity - initial_velocity
        return _velocity

    # displacement
    def displacement(velocity, time):
        _displacement = velocity * time
        return _displacement
    
    def displacement_using_initialVelocity_finalVelocity_time(initial_velocity, final_velocity ,time):
        _displacement = ((final_velocity + initial_velocity) / 2) * time
        return _displacement
    
    def displacement_using_initialVelocity_acceleration_time(initial_velocity, acceleration ,time):
        _displacement = (initial_velocity * time) + (0.5 * acceleration * (time**2))
        return _displacement

    def displacement_using_initialVelocity_finalVelocity_acceleration(initial_velocity, final_velocity ,acceleration):
        _displacement = ((final_velocity**2) - (initial_velocity**2)) / (2 * acceleration)
        return _displacement
    
    # time
    def time(displacement, velocity):
        _time = displacement / velocity
        return _time

    def time_using_accleration_velocity(self ,final_velocity, initial_velocity, acceleration):
        _change = self.change_in_velocity(initial_velocity, final_velocity)
        _time = _change / acceleration
        return _time

    def time_using_initialVelocity_finalVelocity_displacement(initial_velocity, final_velocity, displacement):
        _time = (2 * displacement) / (initial_velocity + final_velocity)
        return _time
    
    # acceleration
    def accelration(velocity, time):
        _accelration = velocity / time
        return _accelration
    
    def acceleration_average(self, initial_velocity, final_velocity, time):
        _change = self.change_in_velocity(initial_velocity, final_velocity)
        _acceleration = _change / time
        return _acceleration

    def acceleration_using_displacement_initalVelocity_time(displacement, initial_velocity ,time):
        _acceleration = (2 * (displacement - (initial_velocity * time))) / (time**2)
        return _acceleration
    
    def acceleration_using_displacement_initalVelocity_finalVelocity(self, displacement, initial_velocity ,final_velocity):
        _ivSquare = initial_velocity**2
        _fvSquare = final_velocity**2
        _change = self.change_in_velocity(_ivSquare, _fvSquare) 
        _acceleration = _change / (2 * displacement)
        return _acceleration
    

