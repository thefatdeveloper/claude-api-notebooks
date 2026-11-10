# Halvora Systems — Annual Interdisciplinary Review 2023

*Halvora Systems is a fictional company. This report was written as test material for these notebooks. Every name, number and incident in it is made up.*

Halvora Systems builds software platforms and runs a small life-sciences research unit. This review summarises what each division did during the 2023 financial year, the risks we saw, and our plans for 2024. It is written for the board, for employees, and for our research partners.

## Executive Summary

2023 was a year of stabilisation and focused growth. Revenue grew 14% to $412 million. Operating margin improved from 9.1% to 11.4%, mainly because of lower cloud costs and fewer customer-facing outages.

The research unit made real progress on XDR-47, a previously unknown pathogen. The engineering division finished Project Phoenix, a two-year programme to make our core platform more stable. In the fourth quarter we handled a serious security incident. It was contained within 36 hours and no customer data was confirmed to have left our systems. Details are in the Cybersecurity Analysis section.

We hired 310 people, opened an office in Pune, and cut our data-centre energy use by 18%. For 2024 our priorities are platform reliability, responsible use of AI features, and turning XDR-47 research into a diagnostic product.

## Table of Contents

- Methodology
- Section 1: Medical Research
- Section 2: Software Engineering
- Section 3: Financial Analysis
- Section 4: Product Development
- Section 5: Legal Developments
- Section 6: Human Resources
- Section 7: Marketing and Brand
- Section 8: Supply Chain and Operations
- Section 9: Sustainability
- Section 10: Cybersecurity Analysis
- Section 11: Research Partnerships
- Section 12: Future Outlook

## Methodology

This review combines information from every division. Each division head submitted a written summary, a set of key metrics, and a list of risks. The finance team checked all financial figures against the audited accounts. The research figures come from lab records and peer-reviewed publications where these exist.

We compared 2023 results with 2022 results using the same definitions, unless a section says otherwise. Where a metric changed definition during the year, we explain the change in that section. Employee survey results come from an anonymous survey with a 78% response rate.

Some numbers in this report are estimates. These are marked as estimates in the text. The review was compiled by the Office of Strategy between January and February 2024, and was approved by the executive committee before publication.

## Section 1: Medical Research

This year saw significant strides in our understanding of XDR-47, a "bug" we have not seen before. XDR-47 is a drug-resistant bacterial strain that was first isolated from hospital samples in late 2022. Our team mapped its genome and identified three resistance genes that explain why common antibiotics fail against it.

The team also studied how the infection spreads. Early data suggests two main transmission vectors: contact with contaminated surfaces, and shared medical equipment such as ventilators. We ran 42 controlled lab experiments and found that standard surface disinfectants remove 99.2% of XDR-47 within ten minutes.

A second project tested a slow-release antimicrobial skin patch for patients with long hospital stays. In a small pilot with 60 volunteers, the patch reduced bacterial load on the skin by 64% compared with a placebo. A larger trial needs ethics approval and is planned for 2024.

The research unit published four papers and filed two patent applications. Its budget was $21 million, up from $17 million in 2022.

## Section 2: Software Engineering

This division dedicated significant effort to studying various infection vectors in our distributed systems — the ways a single failing service can spread errors to the services that depend on it. The main programme was Project Phoenix, a two-year effort to improve the stability of our core platform.

Project Phoenix delivered three major stability enhancements. First, every internal service now uses circuit breakers, so one slow service can no longer block the whole platform. Second, we moved our message queues to a new cluster with automatic failover. Third, we added canary releases, so new code reaches 2% of traffic before it reaches everyone.

Engineers fixed 1,284 bugs this year, compared with 1,037 in 2022. The share of bugs found before release rose from 61% to 74%. Customer-facing outages fell from 19 to 7, and average recovery time dropped from 52 minutes to 18 minutes.

The engineering team also supported the response to INC-2023-Q4-011. The root cause was an unpatched authentication library in a legacy reporting service. Engineers patched the library across 140 services within 48 hours, and Project Phoenix's canary system was used to roll out the fix safely.

## Section 3: Financial Analysis

Total revenue for 2023 was $412 million, an increase of 14% over 2022. Subscription revenue made up 81% of the total. Professional services revenue fell slightly as more customers moved to self-service onboarding.

Operating costs grew more slowly than revenue. Cloud infrastructure costs fell by 9% after we moved older workloads to reserved capacity and removed unused storage. Salary costs rose by 11% because of new hiring and an annual pay review.

The fourth-quarter security event created one-off costs of about $3.8 million (estimate). This covers outside forensic experts, legal advice, customer notifications, and extra monitoring tools. We expect a further $1.2 million in 2024 for security improvements. These costs are included in operating expenses.

Cash at year end was $96 million, and the company has no long-term debt. The board approved a $25 million budget for acquisitions in 2024. Our main financial risks are customer concentration (our top ten customers make up 23% of revenue) and exchange-rate changes in our India and Europe operations.

## Section 4: Product Development

The product team launched two major features in 2023: a workflow builder for non-technical users, and an analytics dashboard with natural-language search. Both features were built on the platform improvements delivered by Project Phoenix.

The workflow builder reached 1,900 paying customers within six months of launch. Customers used it mainly to automate approval chains and data imports. The analytics dashboard is in public preview, with 340 customers testing it.

We also introduced a formal product review process. Every new feature now needs a written problem statement, a success metric, and a privacy review before engineering work begins. This slowed down two launches but reduced the number of features we later removed.

In 2024 the team will focus on AI-assisted features, offline support for our mobile app, and better accessibility. Our goal is to meet the WCAG 2.1 AA standard across all customer-facing screens by the end of the year.

## Section 5: Legal Developments

The legal team handled several important matters in 2023. The most significant was the regulatory disclosure that followed the fourth-quarter security incident. We notified data-protection regulators in three countries within the required time limits. None of the regulators has opened a formal investigation so far.

We updated our customer contracts to include clearer terms on data processing, breach notification, and use of AI features. About 70% of enterprise customers signed the new terms by year end.

A patent dispute with a former supplier over a data-compression method was settled out of court. The settlement terms are confidential, and the amount was not material to our results.

The team also prepared for new rules on artificial intelligence in Europe and on digital personal data in India. We created an internal register of all AI features, with their purpose, data sources, and risk level. Legal costs for the year were $4.6 million.

## Section 6: Human Resources

Headcount grew from 1,420 to 1,730 employees. We hired 310 people, most of them in engineering and customer support. Voluntary attrition fell from 16% to 12%.

We opened a new office in Pune with space for 250 people. The office will host engineering, support, and finance teams. Hybrid work remains our default: most teams come to the office two days a week.

The anonymous employee survey had a 78% response rate. Overall engagement rose from 71% to 76%. The lowest scores were for career growth, so we launched a new promotion framework with clear criteria for each level.

Training spend per employee rose to $1,150. Every engineer completed secure-coding training after the fourth-quarter incident, and all managers completed a course on giving feedback.

## Section 7: Marketing and Brand

Marketing focused on reaching mid-sized companies in India, the Middle East, and Southeast Asia. We ran 48 customer events and webinars, which produced 3,200 qualified leads.

Our website traffic grew by 27%. Most new visitors came through search and through technical articles written by our engineers. A customer story series featuring hospitals using our workflow builder was our most-read content of the year.

Brand awareness among target customers rose from 22% to 29%, according to an outside survey. We also redesigned our logo and website for the first time since 2018.

The marketing budget was $18 million, about 4.4% of revenue. In 2024 we will move more spending from events to partner programmes.

## Section 8: Supply Chain and Operations

Halvora is mainly a software company, but our research unit and data centres depend on physical suppliers. In 2023 we faced longer delivery times for lab equipment and server hardware.

We reduced risk by adding a second supplier for key lab reagents and by ordering server hardware six months earlier than usual. Average delivery time for servers improved from 19 weeks to 11 weeks during the year.

Our two data centres achieved 99.98% availability. We completed a full disaster-recovery test in September, moving all production traffic to the backup site for four hours without customer impact.

Procurement savings were $2.1 million, mainly from renegotiated software licences and cloud contracts.

## Section 9: Sustainability

We cut data-centre energy use by 18% by replacing old servers, improving cooling, and shutting down unused machines. 64% of our electricity now comes from renewable sources, up from 41%.

Business travel emissions fell by 12%, mainly because more internal meetings moved online. Our total greenhouse-gas emissions for the year were an estimated 21,400 tonnes of CO2 equivalent.

The research lab started a programme to reduce single-use plastics. It reduced plastic waste by 30% without affecting experiment safety.

Our target is net-zero emissions from our own operations by 2030. In 2024 we will publish our first independently checked emissions report.

## Section 10: Cybersecurity Analysis

**Incident Response Report: INC-2023-Q4-011.** On 14 November 2023 our security monitoring detected unusual login activity on a legacy reporting service. The incident was logged as INC-2023-Q4-011 and classified as severity 1.

Investigation found that an attacker had used a known weakness in an unpatched authentication library. The attacker gained access to internal reporting dashboards for about 31 hours. Forensic experts found no evidence that customer data was copied out of our systems, but we could not rule it out completely, so we notified affected customers and regulators.

The incident was contained within 36 hours. The response team rotated all service credentials, patched the library across 140 services, and shut down the legacy reporting service permanently. A full review of INC-2023-Q4-011 found three main lessons: keep a complete list of third-party libraries, patch critical weaknesses within seven days, and remove legacy services that no team owns.

Outside the incident, we blocked about 2.3 million phishing emails, ran four simulated phishing tests, and passed our annual ISO 27001 surveillance audit.

## Section 11: Research Partnerships

Our research unit worked with four universities and two public hospitals. The largest partnership is with a university medical college, where joint teams study how XDR-47 spreads inside intensive-care units.

We also funded six PhD students working on topics such as antimicrobial resistance, reliable distributed systems, and privacy-preserving data analysis. Partners get access to anonymised lab data under strict agreements.

Two partnerships ended during the year because their projects were completed. Total partnership funding was $3.4 million.

## Section 12: Future Outlook

For 2024 we expect revenue growth of 12% to 15%. Our priorities are platform reliability, AI-assisted features built responsibly, and moving XDR-47 research towards a diagnostic test.

The main risks we see are security threats, changing regulation on AI and personal data, and competition from larger cloud providers. We will keep investing in security after INC-2023-Q4-011, including a dedicated team for third-party library risk.

We thank our customers, partners, and employees for their support during a demanding year.
