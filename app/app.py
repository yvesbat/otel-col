from flask import Flask, jsonify
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import Resource
import random
import time

# Initialize OpenTelemetry metrics
metrics.set_meter_provider(
    MeterProvider(
        resource=Resource.create({"service.name": "python_app"}),
        metric_readers=[
            PeriodicExportingMetricReader(
                OTLPMetricExporter(
                    endpoint="localhost:4317",
                    insecure=True
                ),
                export_interval_millis=1000
            )
        ]
    )
)

# Get a meter
meter = metrics.get_meter(__name__)

# Create metrics
request_counter = meter.create_counter(
    name="http_requests_total",
    description="Total number of HTTP requests",
    unit="1"
)

response_time = meter.create_histogram(
    name="http_response_time_seconds",
    description="HTTP response time in seconds",
    unit="s"
)

active_users = meter.create_up_down_counter(
    name="active_users",
    description="Number of active users",
    unit="1"
)

# Create Flask app
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

@app.route('/')
def home():
    # Record request
    request_counter.add(1, {"endpoint": "/"})
    
    # Simulate some processing time
    start_time = time.time()
    time.sleep(random.uniform(0.1, 0.5))
    
    # Record response time
    response_time.record(time.time() - start_time, {"endpoint": "/"})
    
    return jsonify({"message": "Hello, World!"})

@app.route('/users')
def users():
    # Record request
    request_counter.add(1, {"endpoint": "/users"})
    
    # Simulate some processing time
    start_time = time.time()
    time.sleep(random.uniform(0.1, 0.5))
    
    # Record response time
    response_time.record(time.time() - start_time, {"endpoint": "/users"})
    
    # Simulate active users
    active_users.add(random.randint(-2, 2))
    
    return jsonify({"active_users": random.randint(10, 100)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050) 