# Creating and Managing Relationships

## Overview

Relationships in Power BI connect tables so that filters can propagate between them. They are created in the **Model view** of Power BI Desktop and are defined by three key properties: **cardinality**, **cross-filter direction**, and **active/inactive** state.

> **Reference:** [Create and manage relationships in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships)

---

## Accessing Model View

1. In Power BI Desktop, click the **Model** view icon in the left navigation (diagram/table icon).
2. All tables loaded into the model appear as boxes with their columns listed.
3. Existing relationships are shown as lines between tables.

---

## Creating a Relationship

### Auto-Detect

When you load multiple tables that share column names, Power BI attempts to detect relationships automatically. Review auto-detected relationships in Model view before publishing — they are sometimes incorrect.

### Manual Creation — Drag and Drop

1. In **Model view**, drag a column from one table and drop it onto the matching column in another table.
2. The relationship line appears immediately.
3. Double-click the line to open **Edit relationship** and configure properties.

### Manual Creation — Manage Relationships Dialog

1. On the **Modeling** ribbon, click **Manage relationships**.
2. Click **New**.
3. Select the two tables and the key columns from the dropdowns.
4. Set cardinality and cross-filter direction.
5. Click **OK**.

---

## Cardinality

Cardinality describes the relationship multiplicity between the two tables:

| Cardinality | Description | Example |
| --- | --- | --- |
| Many-to-one (*:1) | Many rows in the fact table match one row in the dimension | Sales → Products |
| One-to-many (1:*) | Same as many-to-one, from the other direction | Products → Sales |
| One-to-one (1:1) | Each row in one table matches exactly one row in the other | Rarely used |
| Many-to-many (*:*) | Multiple rows on both sides can match | Requires bridge table or explicit M:M |

**Best practice:** Use Many-to-one relationships (fact-to-dimension). Many-to-many relationships have performance implications and should be resolved with a bridge table where possible.

> **Reference:** [Many-to-many relationship guidance – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many)

---

## Cross-Filter Direction

Cross-filter direction controls which direction filters propagate along a relationship:

| Direction | Behavior |
| --- | --- |
| Single | Filters flow from the one-side (dimension) to the many-side (fact) — standard |
| Both | Filters flow in both directions — use with caution |

**Single direction** is the default and recommended setting for star schema models. It ensures predictable filter propagation and avoids accidental circular filter paths.

**Both directions** (bidirectional) is sometimes needed for M:M relationships or role-playing scenarios, but it can cause ambiguous filter paths and unexpected results. Only use it when required.

---

## Active vs Inactive Relationships

When two tables have more than one relationship (e.g., Sales to Date via both Order Date and Ship Date), only one relationship can be **active** at a time. The active relationship is used automatically in all DAX expressions and visuals. Inactive relationships must be explicitly activated using `USERELATIONSHIP()` inside a CALCULATE expression:

```dax
Sales by Ship Date = CALCULATE(
    [Total Sales],
    USERELATIONSHIP(Sales[Ship Date], 'Date'[Date])
)
```

---

## Editing a Relationship

1. In Model view, double-click the relationship line.
2. The **Edit relationship** dialog opens.
3. Modify cardinality, cross-filter direction, or key columns.
4. Click **OK**.

---

## Deleting a Relationship

1. In Model view, click the relationship line to select it.
2. Press **Delete** or right-click → **Delete**.
3. Confirm the deletion.

---

## Viewing Relationship Properties

In the **Manage relationships** dialog (Modeling → Manage relationships), all relationships are listed in a table showing:

* From table and column.
* To table and column.
* Cardinality.
* Cross-filter direction.
* Active state.

This is the best place for a model audit — export or screenshot it for documentation.

---

## Relationship Validation

Power BI validates relationships when the model refreshes. Common issues:

| Issue | Cause | Fix |
| --- | --- | --- |
| Multiple relationships between same tables | More than one relationship creates one active and others inactive | Use `USERELATIONSHIP` for inactive ones |
| Ambiguous relationship path | Bidirectional relationships create multiple filter paths | Set to Single direction |
| Referential integrity warning | Fact table has key values not present in dimension | Clean data in Power Query or use `RELATED` with ISBLANK check |
| Circular dependency | Chain of relationships creates a loop | Restructure model to eliminate the cycle |

---

## Best Practices

* Always connect fact tables to dimension tables on the dimension's **primary key** column.
* Keep cross-filter direction **Single** unless you have a specific need for Both.
* Use **active relationships** for the primary date key (Order Date) and inactive ones for secondary date keys (Ship Date, Due Date).
* Avoid hiding relationships by using many-to-many — resolve them with a bridge table in Power Query.
* Validate all relationships in **Manage relationships** before publishing to the Service.

---

## References

* [Create and manage relationships in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships)
* [Relationships in Power BI Desktop – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-relationships-understand)
* [Many-to-many relationship guidance – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/guidance/relationships-many-to-many)
* [Bidirectional relationship guidance – Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/guidance/relationships-bidirectional-filtering)
