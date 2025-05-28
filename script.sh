#!/bin/bash

URL="http://localhost:8080/metrics"  # Change this to your target URL
INTERVAL=5                           # Seconds between each curl
DURATION=600                         # Total duration in seconds (10 minutes)
END_TIME=$((SECONDS + DURATION))

while [ $SECONDS -lt $END_TIME ]; do
  echo "Curling $URL at $(date)"
  curl -s $URL > /dev/null
  sleep $INTERVAL
done

echo "Done after 10 minutes."
