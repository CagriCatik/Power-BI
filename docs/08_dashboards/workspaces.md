# App Workspaces

## Overview

A **workspace** in the Power BI Service is a collaborative container for storing, managing, and sharing reports, semantic models, dashboards, and dataflows. Workspaces are the primary unit of organisation for team-based Power BI development and distribution.

> **Reference:** [Publish an app in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-create-distribute-apps)

---

## Workspace Types

| Type | Description |
| --- | --- |
| **My Workspace** | Personal, private workspace — content cannot be shared unless you have a Pro license |
| **Workspace (team)** | Shared workspace for collaboration with role-based access control |
| **Premium workspace** | Same as team workspace but backed by dedicated capacity (Premium) |

For any content that needs to be shared with colleagues, use a **team workspace** — not My Workspace.

---

## Creating a Workspace

1. In the Power BI Service left navigation, click **Workspaces**.
2. Click **Create a workspace**.
3. Enter a **Name** and optional **Description**.
4. Set the **License mode**: Pro, Premium per user, or Premium capacity.
5. Add a workspace image (optional) for visual identification.
6. Click **Save**.

---

## Workspace Roles

| Role | Permissions |
| --- | --- |
| **Admin** | Full control: add/remove members, publish apps, delete workspace |
| **Member** | Create, edit, and delete content; publish apps |
| **Contributor** | Create and edit content; cannot publish apps |
| **Viewer** | View published content only; cannot edit or publish |

### Assigning Roles

1. Open the workspace in the Power BI Service.
2. Click **Access** (top-right of the workspace view).
3. Type a user's email or AAD group name.
4. Select the role from the dropdown.
5. Click **Add**.

---

## Workspace Content

A workspace can contain:

* **Reports** — built in Power BI Desktop or the Service.
* **Semantic models** — the data model backing reports.
* **Dashboards** — single-page monitoring views with pinned tiles.
* **Dataflows** — reusable ETL pipelines built in the Service.
* **Paginated reports** — pixel-perfect printable reports (requires Premium).

---

## Workspace Settings

Under **Settings** (gear icon in the workspace):

* Change workspace name, description, and image.
* Set the license type.
* Enable **Git integration** (for version control with Azure DevOps or GitHub).
* Enable **Deployment pipeline** assignment.

---

## Deployment Pipelines

**Deployment Pipelines** enable a structured Dev → Test → Production promotion workflow:

1. Assign workspaces to pipeline stages.
2. Develop and test content in Dev and Test workspaces.
3. Promote content to Production with a single click — no re-publishing required.
4. Differences between stages are highlighted before each promotion.

This feature requires a **Premium** or **Fabric** capacity.

---

## Monitoring Workspace Usage

Admins can view workspace **usage metrics**:

1. Click the **Usage metrics report** option in the workspace.
2. See which reports are viewed most, by whom, and how often.
3. Use this data to identify unused content and prioritise maintenance.

---

## Best Practices

* Create **separate workspaces** for different business domains (Finance, Sales, HR) — avoid a single shared workspace for everything.
* Use **Contributor** role for developers who should not publish apps.
* Use **Viewer** role for end consumers — they cannot modify content.
* Assign **AAD security groups** instead of individual users for easier role management at scale.
* Use **Deployment Pipelines** for any production-grade content to maintain a safe promotion workflow.

---

## References

* [Publish an app in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-create-distribute-apps)
* [Share and Collaborate on Power BI Reports and Dashboards – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-share-dashboards)
