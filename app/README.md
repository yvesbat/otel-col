# Python OpenTelemetry Metrics Demo

This is a simple Flask application that demonstrates how to export metrics to OpenTelemetry.

## Setup

1. Create a virtual environment and install dependencies:
```bash
cd app
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Make sure the OpenTelemetry Collector is running with the updated configuration.

3. Run the application:
```bash
python app.py
```

## Available Endpoints

- `http://localhost:5000/`: Returns a hello message
- `http://localhost:5000/users`: Returns a random number of active users

## Metrics

The application exports the following metrics:

1. `http_requests_total`: Counter of total HTTP requests
2. `http_response_time_seconds`: Histogram of HTTP response times
3. `active_users`: UpDownCounter of active users

These metrics are exported to the OpenTelemetry Collector and can be viewed in your monitoring system. 