# Current-State Imaging Retrieval Workflow

## Scope

This project examines the operational workflow for retrieving diagnostic imaging from external healthcare facilities for specialist consultation.

The analysis begins when imaging retrieval work reaches the retrieval team and the facility holding the requested imaging has already been identified. Upstream processes such as case creation, patient intake, and identification of the relevant facility are outside the scope of this project.

Although the real operational environment involved retrieval of both medical records and diagnostic imaging, this project models only the imaging retrieval workflow.

## Workflow Entry Point

By the time imaging retrieval work reached the retrieval team, the healthcare facility holding the requested imaging had already been identified.

The worker reviewed existing facility information in the system to determine whether a known SaaS imaging platform was documented for that facility.

If a known SaaS pathway was available, the worker could initiate the imaging request through the platform or contact the facility's radiology department and request that the images be pushed electronically through the documented platform.

If no SaaS pathway was documented, the worker contacted the facility's radiology department, verified the appropriate phone and fax information, and initiated a physical-media retrieval workflow. The ROI was faxed to the facility along with an Express FedEx shipping label for return of the imaging CD.

Although an expedited return label was provided, facilities did not always use it. CDs could instead be returned through USPS, introducing additional and less predictable turnaround time into the retrieval process.

## Retrieval Turnaround

Turnaround time differed substantially depending on the retrieval pathway.

For SaaS-based retrieval, imaging could become available within minutes of the request or facility push. This made the digital pathway substantially faster and more predictable than physical-media retrieval.

For CD-based retrieval, turnaround was more variable and depended partly on facility processing and shipping behavior. When the facility processed the request promptly and used the provided Express FedEx label, imaging could arrive within a few days.

When facilities returned CDs through USPS instead of using the provided expedited shipping label, turnaround could extend to approximately two weeks.

As a result, physical-media retrieval introduced both longer turnaround times and greater variability into a workflow operating against a short consultation target.

## Facility and Platform Information

Facility information served as an operational reference point for determining the appropriate imaging retrieval pathway.

When a facility had a documented SaaS imaging platform, the retrieval workflow could proceed through the available digital pathway. Depending on the platform and facility workflow, imaging could be requested directly through the platform or the facility's radiology department could be contacted to initiate an electronic transfer.

When no SaaS pathway was documented, the retrieval process required additional facility verification and typically proceeded through a physical-media workflow.

The availability and accuracy of facility-level platform information therefore directly affected the number of manual steps required to initiate an imaging request.

## Retrieval Paths

The retrieval pathway depended on both documented platform availability and prior operational knowledge of the facility.

When a SaaS platform was documented, imaging could be requested directly through the platform. For facilities with a known history of responding reliably to platform-based requests, this allowed the retrieval process to begin without additional manual contact.

When the facility's response behavior was unknown, or when prior experience suggested that a platform request alone might not be sufficient, the retrieval workflow could include direct contact with the facility's radiology department before or alongside the electronic request.

When no SaaS pathway was available, retrieval proceeded through a physical-media workflow.

As a result, platform availability alone did not determine workflow efficiency. Facility-specific operational knowledge also influenced how much manual intervention was required to successfully initiate retrieval.

## Follow-Up and Delay Handling

Outstanding imaging requests were followed up on a 48-hour cycle until the required imaging was received.

For physical-media retrieval, shipment tracking was an important part of the workflow. When an expedited return label was created as part of the retrieval process, its tracking number was documented so that the shipment could be monitored.

If the facility used its own shipping method instead, the facility-provided tracking number was documented when available.

The physical retrieval pathway therefore required ongoing monitoring beyond the initial request. Delays could result not only from facility processing time, but also from the time required for physical media to enter and move through the shipping process.

## Multi-Facility Cases

A single case could require imaging from multiple healthcare facilities. Each facility represented a separate retrieval workflow, potentially involving a different imaging platform, retrieval pathway, turnaround time, and follow-up history.

Multiple retrieval requests associated with the same case could therefore progress independently. Imaging from one facility might be received while imaging from another remained outstanding.

The retrieval workflow did not independently determine whether all requested imaging was required before the case could proceed. Decisions about whether the available imaging was sufficient for the next stage of the clinical workflow were outside the retrieval team's responsibility and are outside the scope of this project.

## Retrieval Completion

An individual imaging request was considered complete from the retrieval perspective when the requested imaging had been successfully obtained from the facility.

Because a single case could involve multiple facilities, completion occurred at the imaging-request level rather than necessarily at the overall case level. Individual requests associated with the same case could therefore have different completion dates and statuses.

Determining whether the imaging available for a case was sufficient for the clinical workflow was outside the retrieval team's responsibility and is outside the scope of this project.

## Known Unknowns

This project is based on direct operational experience with imaging retrieval but does not attempt to reconstruct the complete workflow or internal systems of any specific organization.

The modeled workflow begins after the relevant imaging facility has been identified. Upstream processes such as case intake, facility identification, and assignment logic are outside the project scope.

Clinical decisions about whether available imaging was sufficient for a case to proceed are also outside scope.

Where additional data or workflow behavior is required for analysis, the project will use explicitly documented synthetic assumptions rather than presenting those assumptions as historical operational practices.