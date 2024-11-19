from services.models import Component, Vehicle, Issue
from django.utils.timezone import now, timedelta
import random

# Generate a large dataset
NUM_COMPONENTS = 50
NUM_VEHICLES = 200
NUM_ISSUES = 1000

# Helper function to generate random dates
def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

# Create Components
component_objs = []
for i in range(NUM_COMPONENTS):
    obj, created = Component.objects.get_or_create(
        name=f"Component {i + 1}",
        repair_price=random.uniform(500, 5000),
        purchase_price=random.uniform(1000, 15000),
    )
    component_objs.append(obj)

print(f"{len(component_objs)} components added.")

# Create Vehicles
vehicle_objs = []
for i in range(NUM_VEHICLES):
    obj, created = Vehicle.objects.get_or_create(
        name=f"Vehicle {i + 1}",
        registration_number=f"REG{i + 1:04d}",
    )
    vehicle_objs.append(obj)

print(f"{len(vehicle_objs)} vehicles added.")

# Create Issues
issues = []
start_date = now() - timedelta(days=365)  # 1 year ago
end_date = now()

for _ in range(NUM_ISSUES):
    vehicle = random.choice(vehicle_objs)
    component = random.choice(component_objs)
    is_new = random.choice([True, False])
    created_at = random_date(start_date, end_date)
    issue = Issue.objects.create(
        vehicle=vehicle,
        component=component,
        is_new=is_new,
        created_at=created_at,
    )
    issues.append(issue)

print(f"{len(issues)} issues added.")
