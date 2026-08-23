# Import Python's random module for synthetic value generation
import random
from datetime import date, datetime, time, timedelta

# Set a fixed seed so the same synthetic dataset is generated each time
random.seed(42)


# --------------------------------------------------
# IMAGING PLATFORMS
# --------------------------------------------------

# Define the six synthetic SaaS imaging platforms used in the dataset
platforms = [
    "ImageBridge",
    "CloudPACS",
    "RadLink",
    "MedExchange",
    "ScanShare",
    "ImagingConnect"
]

# Create records that mirror the imaging_platforms MySQL table
imaging_platforms = []

for platform_id, platform_name in enumerate(platforms, start=1):
    imaging_platforms.append({
        "platform_id": platform_id,
        "platform_name": platform_name
    })


# --------------------------------------------------
# FACILITIES
# --------------------------------------------------

# Synthetic street names used to construct facility addresses
street_names = [
    "Oak Street",
    "Maple Avenue",
    "Pine Road",
    "Cedar Boulevard",
    "Lake Drive",
    "Willow Lane",
    "Park Avenue",
    "River Road"
]

# Define the date range for synthetic facility reference updates
update_start_date = date(2025, 1, 1)
update_end_date = date(2026, 8, 1)

# Calculate the total number of days available in the update-date range
days_in_update_range = (update_end_date - update_start_date).days

# Generate 400 synthetic healthcare facility records
facilities = []

for facility_id in range(1, 401):

    # Create sequential facility names: Facility 001 through Facility 400
    facility_name = f"Facility {facility_id:03d}"

    # Generate a synthetic 555 phone number
    phone_number = (
        f"555-{random.randint(100, 999)}-"
        f"{random.randint(1000, 9999)}"
    )

    # Generate a synthetic street address
    street_number = random.randint(100, 9999)
    street_name = random.choice(street_names)
    address = f"{street_number} {street_name}"

    # Generate a synthetic radiology department contact
    radiology_contact = f"radiology{facility_id:03d}@example.org"

    # Generate a random date when the facility information was last updated
    last_updated_date = update_start_date + timedelta(
        days=random.randint(0, days_in_update_range)
    )

    # Add one facility record to the facilities list
    facilities.append({
        "facility_id": facility_id,
        "facility_name": facility_name,
        "address": address,
        "phone_number": phone_number,
        "radiology_contact": radiology_contact,
        "last_updated_date": last_updated_date
    })

# --------------------------------------------------
# PATIENTS
# --------------------------------------------------

# Generate synthetic patients.
# Most patients will have one case, while a smaller number will have two or three.
patients = []

patient_id = 1
case_slots_remaining = 50000

while case_slots_remaining > 0:

    cases_for_patient = random.choices(
        [1, 2, 3],
        weights=[90, 8, 2]
    )[0]

    # Prevent the final patient from creating more cases than needed
    cases_for_patient = min(cases_for_patient, case_slots_remaining)

    patients.append({
        "patient_id": patient_id,
        "case_count": cases_for_patient
    })

    patient_id += 1
    case_slots_remaining -= cases_for_patient

# --------------------------------------------------
# CASES
# --------------------------------------------------

# Define the synthetic 12-month observation period
case_start_date = date(2025, 9, 1)
case_end_date = date(2026, 8, 31)

days_in_case_range = (case_end_date - case_start_date).days

cases = []

case_sequence = 1

for patient in patients:

    for _ in range(patient["case_count"]):

        # Generate a case assignment date, with most activity occurring on business days
        while True:
            assigned_date = case_start_date + timedelta(
                days=random.randint(0, days_in_case_range)
            )

            # weekday(): Monday = 0 through Sunday = 6
            if assigned_date.weekday() < 5:
                break

            # Allow a smaller proportion of weekend case activity
            if random.random() < 0.15:
                break

        # Generate a synthetic assignment time
        assigned_hour = random.randint(7, 18)
        assigned_minute = random.randint(0, 59)

        assigned_at = datetime.combine(
            assigned_date,
            time(assigned_hour, assigned_minute)
        )

        # Create sequential case numbers
        case_number = f"CASE-{case_sequence:05d}"

        # Add one case record to the cases list
        cases.append({
            "case_number": case_number,
            "patient_id": patient["patient_id"],
            "assigned_at": assigned_at
        })

        case_sequence += 1

# --------------------------------------------------
# FACILITY PLATFORMS
# --------------------------------------------------

facility_platforms = []

facility_platform_id = 1

for facility in facilities:

    # Randomly decide how many SaaS platforms this facility supports.
    # Most facilities will have fewer platforms; some may have several.
    platform_count = random.choices(
        [0, 1, 2, 3, 4, 5, 6],
        weights=[18, 30, 22, 14, 8, 5, 3]
    )[0]

    # Randomly select unique platforms for this facility
    selected_platforms = random.sample(
        imaging_platforms,
        k=platform_count
    )

    for platform in selected_platforms:

        facility_platforms.append({
            "facility_platform_id": facility_platform_id,
            "facility_id": facility["facility_id"],
            "platform_id": platform["platform_id"]
        })

        facility_platform_id += 1

# --------------------------------------------------
# VALIDATION OUTPUT
# --------------------------------------------------

# Print record counts so we can confirm generation worked as expected
print(f"Generated {len(imaging_platforms)} imaging platforms.")
print(f"Generated {len(facilities)} facilities.")
print(f"Generated {len(patients)} patients.")
print(f"Planned {sum(patient['case_count'] for patient in patients)} cases.")
print(f"Generated {len(cases)} cases.")
print(f"Generated {len(facility_platforms)} facility-platform relationships.")

facilities_with_saas = len({
    row["facility_id"]
    for row in facility_platforms
})

print(f"Facilities with at least one SaaS platform: {facilities_with_saas}")
print(f"Facilities with no SaaS platform: {len(facilities) - facilities_with_saas}")