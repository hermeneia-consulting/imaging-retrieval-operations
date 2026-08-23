# Imaging Retrieval Operations — Business Rules

## Purpose

This document defines the operational rules used to model the imaging retrieval workflow. Rules derived from direct operational experience are separated from synthetic assumptions introduced for analytical purposes.

These rules will guide the future data model, synthetic dataset, SQL analysis, and visualization layer.

## Core Workflow Rules

### BR-01 — Facility Identification
Each imaging request is associated with a healthcare facility that has already been identified before the modeled retrieval workflow begins.

### BR-02 — Case-to-Request Relationship
A case may require imaging from one or multiple healthcare facilities. Each facility retrieval is represented as a separate imaging request.

### BR-03 — Independent Request Progress
Imaging requests associated with the same case progress independently and may have different retrieval pathways, follow-up histories, turnaround times, and completion dates.

### BR-04 — Facility Platform Knowledge
A facility may or may not have a documented SaaS imaging platform available at the time a request is initiated.

### BR-05 — Retrieval Pathway
Imaging may be retrieved through a SaaS imaging platform or through a physical-media workflow when an appropriate digital pathway is unavailable or not used.

### BR-06 — Platform Availability Does Not Guarantee Platform Use
A documented SaaS platform does not guarantee that an imaging request will ultimately be completed through that platform.

### BR-07 — Facility-Specific Operational Knowledge
Prior knowledge of facility behavior may influence whether a worker initiates a SaaS request directly or contacts the facility before or alongside the electronic request.

### BR-08 — Follow-Up Cycle
Outstanding imaging requests are subject to follow-up on a 48-hour cycle until the requested imaging is obtained or the request reaches another defined terminal status.

### BR-09 — Physical Shipment Monitoring
Physical-media retrieval may require shipment monitoring. Tracking information is documented when available so that the return shipment can be monitored.

### BR-10 — Request-Level Completion
An imaging request is complete from the retrieval perspective when the requested imaging has been successfully obtained from the facility.

### BR-11 — Case Status Is Outside Retrieval Determination
Completion of an individual imaging request does not determine whether the overall case is clinically ready to proceed. Clinical sufficiency decisions are outside the scope of the modeled retrieval workflow.