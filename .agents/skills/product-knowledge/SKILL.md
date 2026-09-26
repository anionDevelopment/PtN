---
name: "product-knowledge"
description: "Contains basic knowledge about the product PtN (\"Prometheus to ntfy\"): its purpose and how it is delivered."
metadata:
  purpose: "Information about the product developed in this repository."
  tags: information, product
  version: 1.0.0
---

# PtN

## Purpose

PtN ("Prometheus to ntfy") is a bridge between the Prometheus-ecosystem and [ntfy](https://github.com/binwiederhier/ntfy)-servers.
It receives alerts from a [prometheus-alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) (via its webhook-receiver), converts them into the format expected by ntfy and forwards them to a ntfy-server.
Alertmanager and ntfy use different formats/protocols, so PtN is the small compatibility-proxy in the middle and nothing more.

## Delivery

PtN is provided as a Docker-image.
The intended usage is to run the container beside the alertmanager (for example in the same `docker-compose.yml`-file) and to configure the alertmanager to send its webhooks to PtN.

## Further information

- Usage and configuration: `PtN/ReadMe.md`
- General project-reference: `Other/Reference/Reference.md`
