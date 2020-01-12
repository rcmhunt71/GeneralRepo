# Weekly Update - 01/13/2020

> Note: Please be concise and brief. List what has been accomplished, what is planned, and what is blocking. Provide concise, brief detail about the effort's value-add or the blocking issue's impacts and mitigations. Add links to supporting documentation if needed.

> General format: **Name**: Component: Description of activity and key dates or required actions.

# PROGRESS
> **Progress** is made up of two sections:
> * What is "completed"?
> * What is "in progress"?

## Completed
**SATURN**
* **DEV**
  * Resolved [MDBACKLOG-9876](https://www.fiserv.com) (Showstopper). Impact: *\<Briefly explain issue and impact to customer/revenue>* 
    * Targeted hot patch Release: 19.11.01.05
  * Completed development assessment of design criteria for next generation of LOS/MD. Accepted: 23 req., clarification on: 9 req., added: 11 req. This assessment will allow development to start design and implementation planning. 

* **QE**
  * Validated [MDBACKLOG-9876](https://www.fiserv.com) (ShowStopper). Issue resolution verified, QA signed off; ready for hot patch release.
  * **FFB**: Validated and signed off on 8 defects specific to FFB. Fixes to be deployed to FFB UAT env for customer validation on 01/14/20. 
  * Worked with dev in assessing design criteria for MDng. Assessed design, architecture, and testing requirements.

  
**MERCURY**
* **DEV** - Completed implementation of Feature-X, which will provide increased efficiency in processing by pre-populating additional required documentation. In code-review. 
* **QE** - Finished initial test automation of Feature-X. Integrated into CI/CD; ready for testing when feature is added to build.

  
**PRICE APis**
* **DEV** - RTB. Resolved 4 defects (0/0/3/1). In code review. 
* **QE** - No updates - focused on other products (see problems).

-------------------------------------------------------------------

## In Progress
> List work in progress and the expected date of completion.

**SATURN**
* **DEV**
  * Started code design and implementation meetings for accepted requirements. Target date for completion: 01/27/20.
  * Resolving issues (0/0/5/0) for FFB not required for 19.11.02 release. Target date for completion: 02/07/20.
  
* **QE**
  * Working with dev in review of design requirements and design meetings. Scoping testing requirements: tools, frameworks, environments, acceptance criteria.
  * QA Team is moving quickly to validate all defects ([Sharepoint Document Link](https://www.fiserv.com)). On schedule to have all defects required for 01/14/20 release validated by EOD 01/13/20 PST.

**PRICE APIs**
* **DEV** - Resolving FFB issue [MDBACKLOG-5378](https://www.fiserv.com) - found and logged late last week.
* **QE** 
   * **SDKs** - Completed approx 66% of API response models + unittests, base client, and request mock. This SDK will allow testers to significantly reduce the time required to implement API test automation time by removing concern to API request/response format and reduces the amount of test updates required when an API changes.

-------------------------------------------------------------------

# Plans
> List work to be started/continued, and if known, the expected date of completion.

**SATURN**
* **DEV**
  * Complete and document initial code design for component X (requirements A-F)
  * Start initial code design for Component Y (requirements G-J)
  * Resolve FFB defects (See In Progress)
  
* **QE**
  * Complete initial testing effort assessment for Component X.
  * Start assessment for Component Y 
  * Start to verify defects prioritized for post-19.11.05 release. 

**GENERAL**
* **JIRA** 
   * Implementing new work flow for defects to allow coordination between dev and QE efforts without creating additional subtasks. This will allow dashboards to show proper status for all teams without external updating or intervention. Target delivery: mid-next week (01/22/20).
   * Creating new dashboard for leadership to show planned releases, issues included in release, and current state of the identified issues. Target delivery: end of week (01/17/20).
   
* **TRAINING**
  * Development and QE receiving additional training about \<domain XYZ>; this will increase the team's understanding of the customer experience and corresponding pain points.

* **QE Resources**
  * **FYI**: *Two resources* will be joining the week of 01/19/20. Plan to onboard the week they start and focus on automation for *\<insert initial product focus here>*. 

# Problems

> Provide a brief description of the issue, the impact it has on the team or business, and steps being taken for mitigation/resolution.

**SATURN**
* **DEV** - None
* **QE** - None

**MERCURY**
* **DEV** - None 
* **QE** - None
  
**General**
* **DEV**
    * Having issues with tracking code changes being integrated into build pipeline. Looking into integration hooks into pipeline to provide feedback and reporting of integrations. [MDENGLT-123](https://www.fiserv.com)
* **QE**
    * Need more resources. Currently leveraging BAs and others from other groups. Currently interviewing candidates, but few are meeting the required expectations. Working with recruitment team to enhance the minimum requirements. 
    * Need training on US Mortgage process and how MD is used by customers. Looking into applicable courses and talking with BA/Dev leaders about who might be a good resource. [MDENGLT-456](https://www.fiserv.com)
 