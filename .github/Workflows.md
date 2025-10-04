# GitHub Actions Workflows

## 1. **Generate PDF from MkDocs Site**

**Workflow Name:** `Generate PDF from MkDocs Site`
**Trigger:** Manual (`workflow_dispatch`)
**Purpose:** Build the MkDocs site and generate a PDF export using `mkdocs-with-pdf`.

### Steps:

* **Checkout code:** Pulls the latest code from the repository.
* **Set up Python:** Installs Python `3.x` using `actions/setup-python@v4`.
* **Install dependencies:** Installs `mkdocs`, `mkdocs-material`, and `mkdocs-with-pdf`.
* **Build site & export PDF:**

  * Builds the MkDocs site using a custom config file: `mkdocs.withpdf.yml`.
  * Exports the site content as PDF using the `mkdocs pdf-export` plugin.
* **Upload artifact:** Stores the generated PDF in `site/pdf/` as a downloadable artifact named `site-pdf`.

**Usage:**
Manually trigger from the "Actions" tab in GitHub UI to generate and download the latest PDF documentation.

---

### 2. **Deploy MkDocs Site to GitHub Pages**

**Workflow Name:** `Deploy MkDocs site to GitHub Pages`
**Trigger:** On every push to the `main` branch
**Purpose:** Automatically deploys the MkDocs documentation to GitHub Pages.

### Steps:

* **Checkout code:** Clones the repo using a GitHub token stored in `secrets.MKDOCS_DEPLOY_TOKEN`.
* **Setup Python:** Installs Python `3.x`.
* **Install MkDocs and theme:** Installs `mkdocs` and the `mkdocs-material` theme.
* **Deploy to GitHub Pages:** Runs `mkdocs gh-deploy --force` using the configured deploy token to publish to `gh-pages` branch.
* **Cleanup (Job):**

  * Runs after the `deploy` job.
  * Deletes old GitHub Pages deployments using [`strumwolf/delete-deployment-environment`](https://github.com/marketplace/actions/delete-deployment-environment).
  * Only removes deployments from the `github-pages` environment (not the actual content).

**Secrets Required:**

* `MKDOCS_DEPLOY_TOKEN`: A GitHub token with permissions to push to the `gh-pages` branch.

---

## 3. **Check Links**

**Workflow Name:** `Check Links`
**Trigger:** On every push to the `main` branch
**Purpose:** Validates all hyperlinks in Markdown files under the `docs/` directory.

### Steps:

* **Checkout code:** Pulls the latest repository contents.
* **Install lychee:** Installs [`lychee`](https://github.com/lycheeverse/lychee), a fast and flexible link checker.
* **Run link check:** Executes `lychee` with:

  * `--verbose`: Detailed logging.
  * `--no-progress`: Disables progress spinner for CI clarity.
  * `--include-mail`: Includes mailto links in validation.
  * Target: All Markdown files under `docs/`.

**Note:** This job helps ensure external/internal links in documentation remain valid after every commit to `main`.
