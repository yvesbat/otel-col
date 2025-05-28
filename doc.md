# OTEL Collector Performance Measurement

## 1. Objectives

Objectives
To explain the differences between push and pull modes for metric collection in observability systems.
To demonstrate how OpenTelemetry Collector supports both push and pull modes for collecting metrics.
To show, through configuration and practical examples, that OpenTelemetry Collector can collect metrics from both modes simultaneously within a single instance.
To compare the advantages and use cases of each mode, highlighting scenarios where simultaneous use is beneficial.
To provide guidance for organizations seeking to unify diverse metric sources (modern and legacy) using OpenTelemetry Collector.
---

## 2. Metrics to Measure

| Metric                | Description                                                                 | How to Measure                                  |
|-----------------------|-----------------------------------------------------------------------------|-------------------------------------------------|
| **CPU Usage**         | CPU consumption of the OTEL Collector process                               | OS tools (top, htop, docker stats, etc.)        |
| **Memory Usage**      | RAM consumption of the OTEL Collector process                               | OS tools (top, htop, docker stats, etc.)        |
| **Scrape Latency**    | Time taken to scrape metrics endpoints                                      | OTEL Collector logs/metrics, Prometheus         |
| **Ingestion Latency** | Time from metric emission to ingestion by the collector                     | Timestamps in metrics, logs                     |
| **Throughput**        | Number of metrics ingested per second                                       | OTEL Collector self-metrics, Prometheus         |
| **Dropped Metrics**   | Number of metrics dropped due to overload or errors                         | OTEL Collector self-metrics, logs               |
| **Error Rate**        | Number of errors encountered during collection or export                    | OTEL Collector self-metrics, logs               |

---

## 3. Measurement Methodology

1. **Baseline Measurement**
   - Start OTEL Collector with no load.
   - Record baseline CPU and memory usage.

2. **Incremental Load Testing**
   - Gradually increase the number of scraped endpoints and push clients.
   - For each step, record:
     - CPU and memory usage
     - Scrape and ingestion latency
     - Throughput
     - Any dropped metrics or errors

3. **Peak Load Testing**
   - Simulate maximum expected load (e.g., N endpoints, M push clients).
   - Monitor for sustained performance, resource saturation, or failures.

4. **Simultaneous Collection**
   - Ensure both push and pull sources are active.
   - Observe for resource contention or metric loss.

---

## 4. Tools Used

- **System Monitoring:** `top`, `htop`, `docker stats`, or equivalent
- **OTEL Collector Self-Metrics:** Exposed at `/metrics` endpoint (Prometheus format)
- **Prometheus:** For scraping and visualizing OTEL Collector metrics
- **Grafana:** (Optional) For dashboarding and visualization
- **Custom Scripts:** For generating push metrics and simulating load

---

## 5. Example OTEL Collector Metrics

- `otelcol_process_cpu_seconds_total`
- `otelcol_process_memory_rss`
- `otelcol_receiver_accepted_metric_points`
- `otelcol_receiver_refused_metric_points`
- `otelcol_exporter_sent_metric_points`
- `otelcol_exporter_send_failed_metric_points`
- `otelcol_scraper_scraped_metric_points`
- `otelcol_scraper_errored_scrapes`

---

## 6. Results

| Test Scenario         | CPU (%) | Memory (MB) | Scrape Latency (ms) | Ingestion Latency (ms) | Throughput (metrics/sec) | Dropped Metrics | Errors |
|----------------------|---------|-------------|---------------------|------------------------|--------------------------|-----------------|--------|
| Baseline (idle)      |         |             |                     |                        |                          |                 |        |
| 5 endpoints, 2 push  |         |             |                     |                        |                          |                 |        |
| 20 endpoints, 10 push|         |             |                     |                        |                          |                 |        |
| Peak load            |         |             |                     |                        |                          |                 |        |

---

## 7. Observations

- _Note any performance bottlenecks, resource saturation, or unexpected behavior._
- _Highlight the collector’s ability to handle simultaneous push and pull loads._
- _Record any configuration changes that improved performance._

---

## 8. Recommendations

- _Summarize optimal configuration and resource requirements for your use case._
- _Suggest monitoring thresholds and scaling strategies._

OpenTelemetry Collector is a highly flexible and powerful tool for observability, capable of collecting metrics using both push and pull modes simultaneously within a single instance. By supporting multiple receivers in the same pipeline, the collector enables organizations to integrate modern, cloud-native applications that push metrics (such as via OTLP), as well as legacy or third-party systems that expose metrics endpoints for scraping (such as via Prometheus). This dual capability simplifies observability architectures, reduces operational complexity, and allows for a unified approach to monitoring diverse environments
