# Publishing an App

## Overview

A **Power BI app** is a packaged collection of dashboards and reports published from a workspace to a large audience. Apps provide a clean, consumer-friendly entry point to BI content — consumers install the app once and get access to curated reports without needing workspace access.

> **Reference:** [Publish an app in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-create-distribute-apps)
> **Reference:** [Apps in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-apps)

---

## App vs Direct Workspace Access

| Feature | App | Direct workspace access |
| --- | --- | --- |
| Consumer sees | Curated content only | All workspace artifacts |
| Consumer can edit | No | Depends on role |
| Navigation | Custom app navigation | Workspace list |
| Audience | Broad distribution | Team members with roles |
| Requires workspace role | No | Yes |

Use **apps** for distributing polished content to end users. Use **workspace access** for the team building the content.

---

## Creating and Publishing an App

### Step 1 — Prepare Workspace Content

Ensure all reports, dashboards, and semantic models in the workspace are ready for consumers. The app will package the selected items.

### Step 2 — Open the App Builder

1. In the workspace, click **Create app** (top-right, or **…  › Publish app**).
2. The App builder opens with four sections: Setup, Navigation, Permissions, and Review + publish.

### Step 3 — Setup

* **App name**: the name consumers see (can differ from the workspace name).
* **Description**: a brief description of the app's purpose.
* **App logo**: upload an image for visual branding.
* **App theme color**: accent color for the app's navigation.
* **Contact information**: email or URL for support.

### Step 4 — Navigation

* Choose which reports and dashboards to include in the app.
* Add **section headers** to group related items (e.g., "Financials", "Operations").
* Reorder items by dragging.
* Set a **default landing page** — the report or dashboard that opens when users launch the app.
* Optionally add **links** to external URLs or other Power BI items.

### Step 5 — Permissions

* **Entire organization** — all users in the Azure AD tenant can install the app.
* **Specific individuals or groups** — restrict to named users or AAD security groups.

Consumers with permission can find the app in **Apps › Get apps** in the Power BI Service.

### Step 6 — Review and Publish

1. Click **Review + publish**.
2. Review the summary of included content and audience.
3. Click **Publish app**.

The app is now available to the specified audience.

---

## Updating a Published App

When you update reports in the workspace and want to push the updates to app consumers:

1. Click **Update app** in the workspace.
2. Make any changes to content, navigation, or permissions.
3. Click **Update app**.

Consumers automatically see the updated content — they do not need to reinstall the app.

---

## Installing and Using an App

For consumers:

1. In the Power BI Service left navigation, click **Apps**.
2. Click **Get apps**.
3. Find the app in the AppSource-style marketplace or use the search box.
4. Click **Get it now** → **Install**.
5. The app appears in the **Apps** section.

---

## Audience Limitations

* Apps published to the **entire organisation** require the workspace to be on a Premium or Fabric capacity for consumers on Free licenses to view it.
* On Pro, both the publisher and all consumers must have Pro licenses to share content.

---

## Best Practices

* Design a clear **app navigation structure** with section headers — an app with 15 reports listed flat is confusing.
* Set a **meaningful default landing page** — most users will never navigate past it without guidance.
* Use **AAD security groups** for permissions — managing 200 individual user permissions is error-prone.
* Include **contact information** in the app setup so consumers know who to reach for questions.
* Version the app description with the last update date so consumers know when the content changed.

---

## References

* [Publish an app in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-create-distribute-apps)
* [Apps in Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/explore-reports/end-user-apps)
* [Template App Authoring Tips: Power BI – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/connect-data/service-template-apps-tips)
