# POS Case Study Datasets

This folder contains synthetic datasets to support batch + streaming ingestion, Delta Lake transformations, and loading into Snowflake/Synapse.

## Files
- dim_stores.csv — 12 rows
- dim_products.csv — 250 rows
- dim_customers.csv — 6000 rows
- fact_orders_daily_batch.csv — 30000 rows across 139 days
- payments.csv — 30000 rows
- inventory_snapshot_daily.csv — 134400 rows
- stream_events.ndjson — 2160 events (order_created + inventory_update)
- warehouse_schema.sql — DDL for Fact/Dim tables

## Notes
- Currency in INR, dates between 2025-04-01 and 2025-08-18.
- NDJSON can be used to simulate Event Hub ingestion (each line is a JSON event).
- Orders contain occasional injected anomalies (large quantities) for fraud detection exercises.