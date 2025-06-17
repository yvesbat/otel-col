#!/bin/bash

# Create a directory for certificates
mkdir -p certs
cd certs

# Generate CA private key and certificate
openssl genrsa -out ca.key 2048
openssl req -new -x509 -days 365 -key ca.key -out ca.crt -subj "/CN=Mimir CA"

# Generate server private key
openssl genrsa -out tls.key 2048

# Generate server CSR
openssl req -new -key tls.key -out tls.csr -subj "/CN=mimir"

# Sign the server certificate with CA
openssl x509 -req -days 365 -in tls.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out tls.crt

# Clean up CSR
rm tls.csr

echo "Certificates generated successfully in the 'certs' directory" 