# OpenTelemetry Metrics Demo

## How to Run All Components

### 1. Start node-exporter

```sh
cd monitoring/node-exporter/node_exporter-1.7.0.darwin-amd64
./node_exporter --web.listen-address=:9100 
```

### 2. Start the OpenTelemetry Collector

```sh
cd monitoring/otel-collector
./otelcol-contrib --config=otel-collector-config.yaml
```

### 3. Start the Python Application

```sh
cd app
python app.py
```

---

- Make sure you have Python dependencies installed (see requirements.txt).
- The Prometheus metrics endpoint will be available at: http://localhost:8889/metrics
- The Python app will be available at: http://localhost:5050/
- The node-exporter metrics will be available at: http://localhost:9100/metrics 