# Signing Up for Power BI

## Introduction

Power BI is a cloud-based business intelligence platform by Microsoft that supports real-time analytics, reporting, and data visualization. This documentation focuses on **Power BI Service**, the SaaS component accessed via a web browser, and how users can effectively sign up, navigate, create, and manage content in a scalable, enterprise-compliant manner.

---

## Signing Up for Power BI Service

### Website Access

* Navigate to: `https://powerbi.microsoft.com`
* Entry points available:

  * **"Sign In"** (top-right, mid-screen, and footer)
  * **"Try Free"** for new registrations

### Account Prerequisites

| Requirement         | Detail                                                                 |
| ------------------- | ---------------------------------------------------------------------- |
| **Email Type**      | Must use a **work or organizational email** (e.g., `name@company.com`) |
| **Personal Emails** | Domains such as Gmail, Yahoo, or Outlook.com are not supported         |
| **Tenant Access**   | Power BI requires an Azure Active Directory (AAD) tenant association   |

### Registration Flow

1. Click “Try Free”
2. Provide a valid organizational email
3. Complete Microsoft account setup (if needed)
4. Verify email address
5. Gain access to Power BI Service as a Free or Pro trial user

---

## Understanding the Power BI Service UI

### Primary Sections

| Section              | Description                                                               |
| -------------------- | ------------------------------------------------------------------------- |
| **Home**             | Personalized content overview: recent, recommended reports, usage trends  |
| **Favorites**        | Quick access to starred reports and dashboards                            |
| **Create**           | Interface to initiate new report building from datasets or files          |
| **Browse**           | File system-like navigation across user content, shared content, and apps |
| **Workspaces**       | Core collaboration units for storing and managing reports/datasets        |
| **Apps**             | Packaged BI content published to targeted user groups                     |
| **Metrics**          | KPI and scorecard building area                                           |
| **Data Hub**         | Listing of semantic models (datasets) available for reporting             |
| **Learning**         | Access to tutorials, Microsoft Learn, and training materials              |
| **Admin/Monitoring** | For Power BI Admins to track activity, usage, and permissions             |

---

## Navigating the Power BI Service

### Home Screen Overview

* Displays “**Recommended**” content based on usage frequency
* Lists “**Recent Reports**” across workspaces
* Provides quick-access actions (e.g., add to **Favorites**, open, share)

### Favorites Management

* Mark any report, dashboard, or dataset as a **favorite** via the star icon
* Favorites appear in the dedicated “Favorites” section in the navigation pane
* Toggling the star removes it from favorites

### Browse View

* Filters:

  * Recent
  * Favorites
  * Shared with Me
  * Owned by Me
* Allows:

  * Sorting by type (reports, datasets, dashboards)
  * Searching across titles and metadata

---

## Creating Content in the Power BI Service

### Report Creation from Existing Datasets

Steps:

1. Click **Create** > **Pick a published semantic model**
2. Select an available dataset (published to your workspace or shared)
3. Enter the web-based report editor
4. Drag fields into the canvas, configure visuals

### Uploading and Connecting Data

Supported methods (covered later in detail):

* Upload `.pbix` files from Power BI Desktop
* Import Excel files
* Connect to cloud services (SharePoint, Azure SQL, Salesforce)
* Use **Dataflows** for ETL within the service

---

## Workspaces in Power BI

### Definition

A **workspace** is a logical container used for:

* Group collaboration
* Content separation by department/function
* Role-based access control (Admin, Member, Contributor, Viewer)

### My Workspace

* **Private** to each user
* Available on both free and paid licenses
* Intended for:

  * Personal development
  * Local testing
* Limitations:

  * No sharing unless on a Pro license
  * No access delegation

### Creating a Workspace

1. Go to `Workspaces > Create a workspace`
2. Define:

   * Name
   * Description
   * Image (optional)
   * License type (Pro / Premium per user / Premium capacity)
3. Add users and assign roles

### Use Cases

| Workspace Type    | Use Case Example                                  |
| ----------------- | ------------------------------------------------- |
| Sales Workspace   | CRM dashboards, lead tracking reports             |
| Finance Workspace | Budget reports, variance analysis dashboards      |
| Project Workspace | Sprint tracking, timeline burndown visualizations |

---

## Data Models and Semantic Layers

### Semantic Model (Dataset)

* Defines structured, reusable data
* Published once, consumed by multiple reports
* Governed through Power BI Service

### Creating and Publishing Models

* Created in **Power BI Desktop**
* Published to:

  * My Workspace (for personal use)
  * Shared Workspace (for collaborative use)

### Supported Model Features

* Relationships
* Measures (DAX)
* Calculated columns
* Row-level security (RLS)
* Incremental refresh

---

## Report Sharing, Licensing & Access Control

### Licensing Rules

| Action                    | License Required                     |
| ------------------------- | ------------------------------------ |
| Create Report             | Free / Pro                           |
| Publish to Workspace      | Pro                                  |
| Share with Other Users    | Pro (both sender and recipient)      |
| Consume App Content       | Free (if hosted in Premium capacity) |
| Collaborate in Workspaces | Pro / Premium per user               |

### Sharing Options

* Share report link (restricted by licensing)
* Publish to app
* Embed in Microsoft Teams
* Add to Power BI App navigation pane

### Access Roles in Workspaces

| Role        | Permissions                                        |
| ----------- | -------------------------------------------------- |
| Admin       | Full control over workspace content and membership |
| Member      | Edit reports and datasets                          |
| Contributor | Upload new content but cannot publish apps         |
| Viewer      | View-only access                                   |

---

## Supplementary Power BI Features

### Apps

* **Definition**: Bundled dashboards, reports, datasets
* Used for packaging business content and distributing securely
* Published from Workspaces
* End users cannot modify app contents

### Metrics (Scorecards)

* Create visual summaries of key indicators
* Combine values, goals, and status indicators
* Ideal for executive dashboards and KPI tracking

### Monitoring (Admin Portal)

* For capacity and usage monitoring
* Audit logs, dataset refresh monitoring
* Role-based access: Admin only

### Learning Hub

* Direct link to Microsoft training
* Includes interactive modules, certification guides

---

## Best Practices for Enterprise Usage

### Content Organization

* Use dedicated workspaces per department or function
* Avoid using My Workspace for anything that needs collaboration

### Security

* Implement Row-Level Security (RLS) on datasets
* Monitor access and sharing permissions regularly

### Data Model Governance

* Encourage reuse of semantic models
* Centralize dataset ownership for consistency

---

## Appendix: Terminology Reference

| Term                     | Description                                                          |
| ------------------------ | -------------------------------------------------------------------- |
| `.pbix` File             | Power BI Desktop report file                                         |
| Dataset (Semantic Model) | Data structure containing tables, relationships, and DAX definitions |
| RLS                      | Row-level Security, filters data by user                             |
| Workspace                | Container for reports, dashboards, and datasets                      |
| Dashboard                | Aggregated view of visuals from one or more reports                  |
| App                      | Packaged and published content from a workspace                      |
| Metric                   | KPI element with status, target, and trendline                       |
