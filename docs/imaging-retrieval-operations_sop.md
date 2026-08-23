# Imaging Retrieval Operations Workflow SOP

## Purpose

Define a consistent operational workflow for retrieving diagnostic imaging from external healthcare facilities through digital imaging platforms or physical media.

This SOP represents the synthetic operational workflow modeled by the Imaging Retrieval Operations project. It does not reproduce the procedures of any specific organization.

## Scope

This workflow begins after the healthcare facility holding the requested imaging has been identified and the imaging retrieval request has entered the retrieval workflow.

Upstream case intake, facility identification, clinical decision-making, and downstream consultation processes are outside scope.

The workflow applies only to diagnostic imaging retrieval. Medical-records retrieval is not modeled.

## Workflow

### 1. Review Facility Information

Review the facility information available for the imaging request.

Determine whether one or more SaaS imaging platforms are documented for the facility.

A facility may have:

- no documented SaaS platform;
- one documented platform; or
- multiple documented platforms.

### 2. Determine Initial Retrieval Path

If an appropriate SaaS platform is documented, initiate the retrieval using an available digital pathway.

Prior operational knowledge of the facility may inform whether the platform request is initiated directly or accompanied by contact with the facility.

If no appropriate digital pathway is available, initiate physical-media retrieval.

### 3. Initiate Imaging Request

Document initiation of the imaging request and the retrieval pathway used.

For SaaS retrieval, document the platform selected for the request.

For physical-media retrieval, complete the required facility contact and shipment preparation activities.

### 4. Monitor Outstanding Requests

Monitor each imaging request independently.

Requests that remain outstanding enter a 48-hour follow-up cycle.

Document follow-up activity as part of the request's retrieval-event history.

### 5. Monitor Physical Shipments

When physical media is shipped, document shipment information when available.

Shipment information may include:

- shipping method;
- tracking availability;
- shipment date and time; and
- delivery date and time.

Shipping method may be recorded as expedited, standard, or unknown when the method cannot be confirmed.

### 6. Document Imaging Receipt

When the requested imaging is obtained, document the receipt event and completion timestamp.

The individual imaging request is then considered complete from the retrieval perspective.

### 7. Continue Remaining Requests

A case may contain imaging requests associated with multiple facilities.

Each request progresses independently. Completion of one imaging request does not imply completion of other requests associated with the same case.

Determination of whether the available imaging is sufficient for downstream clinical activity is outside the scope of the retrieval workflow.

## Operational Rules

- One patient may be associated with multiple cases.
- One case may contain multiple imaging requests.
- Each imaging request is associated with one healthcare facility.
- A facility may support zero, one, or multiple SaaS imaging platforms.
- Platform availability does not guarantee that a request will ultimately be completed through a digital pathway.
- Outstanding requests are followed up on a 48-hour cycle.
- Physical-media retrieval may require shipment monitoring.
- Imaging-request completion occurs when the requested imaging is obtained.
- Clinical readiness and decisions to discontinue retrieval are outside the scope of this workflow.

## Required Operational Data

The modeled workflow requires visibility into:

- patient identifier;
- case number;
- imaging request identifier;
- facility;
- documented facility-platform relationships;
- initial retrieval pathway;
- selected SaaS platform when applicable;
- request creation timestamp;
- retrieval-event history;
- follow-up activity;
- physical shipment information when applicable;
- request status; and
- completion timestamp.

## Exceptions and Unknowns

Operational information may not always be complete.

Examples include:

- unknown physical shipping method;
- unavailable shipment tracking information;
- incomplete or outdated facility-platform information; and
- imaging requests that remain outstanding at the end of the observation period.

Unknown values should be represented explicitly where they constitute meaningful operational states rather than replaced with fabricated information.

## Workflow Boundary

This SOP describes imaging retrieval operations only.

It does not define:

- patient intake procedures;
- clinical decision-making;
- consultation readiness;
- case-management escalation criteria; or
- downstream clinical workflow.