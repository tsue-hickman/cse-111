# water_flow.py
def water_column_height(tower_height, tank_height):
    return tower_height + (3 * tank_height) / 4

def pressure_gain_from_water_height(height):
    water_density = 998.2
    gravity_acceleration = 9.80665
    return (water_density * gravity_acceleration * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    water_density = 998.2
    pressure_loss = -(friction_factor * pipe_length * water_density * fluid_velocity ** 2) / (2000 * pipe_diameter)
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    water_density = 998.2
    pressure_loss = -0.04 * water_density * fluid_velocity ** 2 * quantity_fittings / 2000
    return pressure_loss

def reynolds_number(hydraulic_diameter, fluid_velocity):
    water_density = 998.2
    water_dynamic_viscosity = 0.0010016
    reynolds_num = (water_density * hydraulic_diameter * fluid_velocity) / water_dynamic_viscosity
    return reynolds_num

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    water_density = 998.2
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    pressure_loss = -(k * water_density * fluid_velocity ** 2) / 2000
    return pressure_loss

# test_water_flow.py
from pytest import approx
import pytest
import water_flow

def test_water_column_height():
    assert water_flow.water_column_height(0, 0) == 0
    assert water_flow.water_column_height(0, 10) == approx(7.5)
    assert water_flow.water_column_height(25, 0) == 25
    assert water_flow.water_column_height(48.3, 12.8) == approx(57.9)

def test_pressure_gain_from_water_height():
    assert water_flow.pressure_gain_from_water_height(0) == approx(0, abs=0.001)
    assert water_flow.pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert water_flow.pressure_gain_from_water_height(50) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    assert water_flow.pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == approx(0, abs=0.001)
    assert water_flow.pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == approx(0, abs=0.001)
    assert water_flow.pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == approx(0, abs=0.001)
    assert water_flow.pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert water_flow.pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert water_flow.pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert water_flow.pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)

def test_pressure_loss_from_fittings():
    assert water_flow.pressure_loss_from_fittings(0, 3) == approx(0, abs=0.001)
    assert water_flow.pressure_loss_from_fittings(1.65, 0) == approx(0, abs=0.001)
    assert water_flow.pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    assert water_flow.pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    assert water_flow.pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)

def test_reynolds_number():
    assert water_flow.reynolds_number(0.048692, 0) == approx(0, abs=1)
    assert water_flow.reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert water_flow.reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert water_flow.reynolds_number(0.28687, 1.65) == approx(471729, abs=1)
    assert water_flow.reynolds_number(0.28687, 1.75) == approx(500318, abs=1)

def test_pressure_loss_from_pipe_reduction():
    assert water_flow.pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692) == approx(0, abs=0.001)
    assert water_flow.pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-81.8722, abs=0.001)
    assert water_flow.pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-89.8792, abs=0.001)

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN"])