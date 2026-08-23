# Imaging Retrieval Operations — Data Model

## Purpose

This document defines the relational data model required to support the documented imaging retrieval workflow and synthetic dataset.

The model is derived from the operational requirements documented in the project rather than from the project's original database schema.

## Entity Review

### Imaging Platforms

Represents the synthetic SaaS imaging platforms available within the modeled retrieval environment.

Proposed attributes:

* `platform_id` — unique platform identifier
* `platform_name` — synthetic platform name

A platform may be associated with multiple healthcare facilities, and a facility may support multiple platforms.

### Facilities

Represents healthcare facilities from which imaging may be requested.

Proposed attributes:

* `facility_id` — unique facility identifier
* `facility_name` — synthetic facility name
* `address` — synthetic facility address
* `phone_number` — synthetic contact number
* `radiology_contact` — synthetic radiology contact information
* `last_updated_date` — date the facility reference information was last updated

A facility may support zero, one, or multiple SaaS imaging platforms.

Platform relationships will therefore not be stored directly on the `facilities` table.

### Facility Platforms

Represents the many-to-many relationship between healthcare facilities and SaaS imaging platforms.

Proposed attributes:

* `facility_platform_id` — unique relationship identifier
* `facility_id` — healthcare facility
* `platform_id` — SaaS imaging platform
* `documented_date` — date the platform relationship was documented
* `last_verified_date` — most recent date the relationship was verified

Each row represents one documented facility-to-platform relationship.

A single facility may therefore have multiple rows in this table when multiple SaaS platforms are available.

### Patients

Represents the synthetic patients associated with cases in the modeled retrieval workflow.

Proposed attributes:

* `patient_id` — unique synthetic patient identifier

A patient may be associated with one or multiple cases.

Patient demographic and clinical attributes are not included unless they become necessary for a defined analytical question.

The synthetic patient table intentionally excludes personally identifying and demographic attributes because patient identity resolution is outside the analytical scope of this project.

In a production imaging retrieval system, additional patient-identification fields would be required to support accurate patient matching and retrieval operations. The simplified synthetic model uses `patient_id` only to preserve the relationship between patients, cases, and imaging requests without modeling protected health information.

### Cases

Represents an individual case associated with a patient and one or more imaging retrieval requests.

Proposed attributes:

* `case_number` — unique synthetic case reference
* `patient_id` — patient associated with the case
* `assigned_at` — date and time the case entered the modeled retrieval workflow

`case_number` serves as the unique identifier for the case.

A patient may have multiple cases, and each case may be associated with one or multiple imaging requests.

The `cases` table does not determine whether the case is clinically ready to proceed. Clinical readiness and downstream case-management decisions are outside the scope of this project.

### Imaging Requests

Represents one imaging retrieval request for one healthcare facility within a case.

Proposed attributes:

* `request_id` — unique imaging request identifier
* `case_number` — parent case
* `facility_id` — healthcare facility holding the requested imaging
* `request_created_at` — date and time the retrieval request entered the modeled workflow
* `initial_retrieval_path` — initial retrieval approach, such as SaaS or physical media
* `selected_platform_id` — SaaS platform selected for the request when applicable
* `request_status` — current retrieval status, such as outstanding or completed
* `completed_at` — date and time the requested imaging was obtained

Each imaging request belongs to one case and one facility.

A case may therefore contain multiple imaging requests when imaging is required from multiple facilities.

The selected SaaS platform must be one of the platforms documented for that facility when a digital retrieval pathway is used.

### Imaging Retrieval Events

Represents individual operational events that occur during the lifecycle of an imaging request.

Proposed attributes:

* `event_id` — unique event identifier
* `request_id` — imaging request associated with the event
* `event_timestamp` — date and time the event occurred
* `event_type` — type of retrieval activity or workflow event
* `retrieval_method` — method associated with the event when applicable
* `platform_id` — SaaS platform involved in the event when applicable
* `notes` — optional synthetic operational context

One imaging request may generate multiple retrieval events.

Events may include activities such as:

* SaaS request submitted
* facility contacted
* physical-media request submitted
* follow-up performed
* shipment initiated
* imaging received

The event history preserves how a request progressed through the retrieval workflow rather than storing only its final outcome.

### Physical Shipments

Represents shipment activity associated with physical-media imaging retrieval.

Proposed attributes:

* `shipment_id` — unique shipment identifier
* `request_id` — imaging request associated with the shipment
* `shipping_method` — shipping method used for the physical-media return, such as expedited, standard, or unknown when the method cannot be confirmed
* `tracking_available` — whether tracking information was available
* `shipped_at` — date and time the shipment entered transit
* `delivered_at` — date and time the physical media was delivered
* `shipment_status` — current shipment state when applicable

A physical-media imaging request may have zero or one associated shipment record.

Shipment details are modeled separately from retrieval events because shipping has its own lifecycle and timing characteristics.

## Relationship Summary

The proposed relational model is:

* One patient may have many cases.
* Each case belongs to one patient.
* One case may have many imaging requests.
* Each imaging request belongs to one case.
* Each imaging request belongs to one facility.
* One facility may support zero, one, or multiple SaaS imaging platforms.
* One SaaS imaging platform may be associated with many facilities.
* Facility-to-platform relationships are stored in `facility_platforms`.
* One imaging request may generate many imaging retrieval events.
* A physical-media imaging request may have zero or one physical shipment record.

Conceptually:

```text
patients
   ↓
cases
   ↓
imaging_requests
   ├── imaging_retrieval_events
   └── physical_shipments

facilities
   ↓
facility_platforms
   ↑
imaging_platforms
```

## Current Schema Changes Required

The original schema will require revision before synthetic data generation.

Planned changes include:

* Add a `patients` table.
* Remove `case_id` from the case model.
* Use `case_number` as the unique case identifier.
* Add `patient_id` to `cases`.
* Replace `date_assigned` with a date-and-time field such as `assigned_at`.
* Remove `platform_id` from `facilities`.
* Add a `facility_platforms` junction table.
* Remove `platform_type` from `imaging_platforms` if all rows represent SaaS platforms.
* Replace `retrieval_log` with `imaging_retrieval_events`.
* Add `physical_shipments`.
* Replace date-only workflow fields with date-and-time fields where operational timing may occur within the same day.
* Remove fields that depend on upstream or clinical workflow assumptions outside the project scope.