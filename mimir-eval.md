Report: Readiness Probe and mTLS Challenges in Mimir

Background:
We attempted to enable mTLS (client_auth_type: RequireAndVerifyClientCert) between Mimir components. However, this setup did not work as expected.

Observed Issue:
All component logs showed the following error:
"Client does not provide certificate."
Upon investigation, we determined this was due to the readiness probe: all components remained unready.

Readiness Probe Limitation:
The default readiness probe configuration does not support specifying client certificates:
(readinessProbe:
  httpGet:
    path: /ready
    port: 8080
    scheme: HTTPS)

Alternatives Explored:

1. Readiness Probe with curl:
We attempted to use an exec readiness probe with curl, which allows specifying certificates:
(readinessProbe:
  exec:
    command:
      - curl
      - -f
      - --cacert
      - /etc/ssl/certs/ca.crt
      - --cert
      - /etc/ssl/certs/client.crt
      - --key
      - /etc/ssl/private/client.key
      - https://localhost:8080/ready)
Issue: curl is not available in the Mimir container.

2. Traefik as a Sidecar Container:
Goal: Use Traefik as a sidecar to route readiness checks. The readiness probe would point to Traefik, which would then forward the request to the Mimir component, providing the necessary certificate.
Flow: ReadinessProbe (HTTP) → Traefik (HTTPS) → Mimir

Observations:
- Traefik does not allow redirection to endpoints unless they are http://localhost (limitation due to Traefik security).
- Creating a localhost certificate with Cert-Manager is not possible. 
