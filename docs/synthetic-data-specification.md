# Imaging Retrieval Operations — Synthetic Data Specification

## Purpose

This document defines the assumptions used to generate the synthetic dataset for the Imaging Retrieval Operations project.

The dataset is designed to reproduce realistic operational patterns for analysis without representing the data, volumes, performance, or internal processes of any specific healthcare organization.

Synthetic assumptions documented here are analytical design choices and should not be interpreted as historical operational metrics.

## Dataset Scope

- Analysis period: 12 synthetic months
- Cases: approximately 50,000
- Imaging requests: approximately 75,000–85,000
- Healthcare facilities: approximately 400
- SaaS imaging platforms: 6

## Case Complexity Distribution

Cases may require imaging from one or multiple healthcare facilities.

Proposed distribution:

- 60% of cases require imaging from 1 facility
- 28% require imaging from 2 facilities
- 10% require imaging from 3 facilities
- 2% require imaging from 4 facilities

## Facility Request Distribution

Imaging-request volume will vary across healthcare facilities rather than being distributed uniformly.

When imaging requests are generated, facility selection will use randomized weighting so that some facilities naturally receive more requests than others.

The resulting request volume for each facility will not be assigned a predefined high-, medium-, or low-volume classification. Facility volume and any subsequent segmentation will instead be derived during SQL analysis from the generated imaging-request data.

## SaaS Platform Coverage

Facilities vary in whether a SaaS imaging pathway is documented and available for retrieval.

For the synthetic dataset:

- 70% of facilities have a documented SaaS imaging platform.
- 30% have no documented SaaS pathway and primarily rely on physical-media retrieval.
- SaaS platform coverage is not distributed evenly across the six platforms.
- Higher-volume facilities are somewhat more likely to have documented SaaS access than lower-volume facilities.

## Facility-to-Platform Coverage

Facilities may support zero, one, or multiple SaaS imaging platforms.

The number of platforms associated with each facility will be generated randomly using weighted probabilities rather than fixed assignments.

Facility volume tier may influence the probability distribution, with higher-volume facilities more likely to support multiple platforms and lower-volume facilities more likely to support fewer or no SaaS platforms.

The specific platform combination assigned to each facility will also be randomized from the available synthetic SaaS platforms.

## Retrieval Path Generation

Each imaging request will be assigned a retrieval pathway based on the facility's available platform coverage and a randomized operational outcome.

- Facilities with no SaaS platform coverage will use a physical-media retrieval pathway.
- Facilities with one or more SaaS platforms will usually use a digital retrieval pathway.
- A small proportion of requests at SaaS-enabled facilities may still fall back to physical-media retrieval.
- When multiple SaaS platforms are available, the platform used for a specific request will be selected from the facility's documented platform options.
- Retrieval-path assignment will be probabilistic so that the final mix of SaaS and physical retrieval emerges from the generated dataset rather than being fixed in advance.

## Turnaround-Time Generation

Turnaround time will be generated from the retrieval pathway and operational events associated with each imaging request.

- SaaS retrievals will generally complete quickly, often within the same day.
- Physical-media retrievals will have longer and more variable turnaround times.
- Expedited physical shipments will generally complete faster than standard shipping.
- Some requests may remain unresolved or incomplete during the analysis period.
- Turnaround values will be generated probabilistically rather than assigned to produce predetermined averages.

## Follow-Up Generation

Outstanding imaging requests will generate follow-up activity on a 48-hour cycle while the request remains outstanding within the modeled retrieval workflow.

- Follow-up events will occur only while a request remains outstanding.
- Requests completed before the first 48-hour interval will not generate follow-up activity.
- Longer-running requests may generate multiple follow-up events.
- Physical-media retrievals are expected to generate more follow-up activity than fast SaaS retrievals because of their longer turnaround times.
- Follow-up frequency will be derived from request duration rather than assigned as a fixed number per request.

## Physical Shipment and Tracking Generation

Physical-media retrievals may include shipment and tracking activity.

- Physical retrievals may use either an expedited or standard shipping method.
- Expedited shipping will generally produce shorter transit times than standard shipping.
- Tracking information may be available for either shipping method but is not guaranteed.
- Shipment activity will apply only to physical-media retrievals.
- Shipping method and tracking availability will be generated probabilistically.
- Shipping behavior may contribute to variation in overall retrieval turnaround time.

## Request Status at Observation End

Imaging requests may be completed or remain outstanding during the modeled analysis period.

A request is considered complete when the requested imaging has been obtained. Requests for which imaging has not yet been obtained remain outstanding.

Decisions to discontinue retrieval based on clinical, case-management, or other considerations are outside the scope of this project and will not be synthetically modeled.

Because the dataset represents a defined observation period, some requests may remain outstanding when the analysis period ends.

## Temporal Distribution

Cases and imaging requests will be distributed across a 12-month synthetic observation period.

- Case volume will vary naturally from day to day rather than being distributed uniformly.
- Most new case activity will occur on business days.
- Daily volume will be generated probabilistically to create realistic fluctuations in workload.
- Retrieval and follow-up activity may extend beyond the date on which a case first enters the modeled workflow.
- Requests initiated near the end of the observation period may remain outstanding when the dataset ends.

## Facility Behavior Variation

Healthcare facilities will vary in their operational behavior so that retrieval performance is not determined solely by retrieval method.

Synthetic facility-level variation may influence:

- Likelihood of successful SaaS retrieval
- Need for manual contact before retrieval
- Physical-media processing time
- Likelihood of expedited versus standard shipping
- Turnaround-time variability
- Number of follow-up events generated before completion

Facility behavior parameters will be randomized within reasonable ranges rather than assigned uniformly across all facilities.

These differences are synthetic modeling assumptions intended to create realistic operational variation for analysis.

## Patient-to-Case Distribution

Patients may be associated with more than one case during the synthetic observation period.

The synthetic dataset will use a weighted distribution in which most patients are associated with one case, while a smaller proportion have two or three cases.

This distribution is a synthetic modeling assumption used to preserve the one-to-many relationship between patients and cases and should not be interpreted as an observed operational rate.