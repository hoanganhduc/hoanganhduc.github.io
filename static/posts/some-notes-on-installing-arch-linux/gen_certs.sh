#!/bin/bash

if [ "$#" != 1 ]; then
	echo "Usage: ./gen_certs.sh NAME"
	exit 1
fi 

######################
# Become a Certificate Authority
######################

if [ ! -f "myCA.key" ]; then  
	# Generate private key
	openssl genrsa -out myCA.key 4096

	# Create configuration file for generating root certificates
	>config_ssl_ca.cnf cat <<-EOF
	[ req ]
	default_bits = 4096

	prompt = no
	distinguished_name=req_distinguished_name
	req_extensions = v3_req

	[ req_distinguished_name ]
	countryName=UA
	stateOrProvinceName=root region
	localityName=root city
	organizationName=root organisation
	organizationalUnitName=roote department
	commonName=root
	emailAddress=root_email@root.localhost

	[ alternate_names ]
	DNS.1        = localhost
	DNS.2        = www.localhost
	DNS.3        = mail.localhost
	DNS.4        = ftp.localhost

	[ v3_req ]
	keyUsage=digitalSignature
	basicConstraints=CA:true
	subjectKeyIdentifier = hash
	subjectAltName = @alternate_names
	EOF

	# Generate root certificate
	openssl req -new -x509 -nodes -key myCA.key -sha256 -days 36500 -out myCA.pem -config config_ssl_ca.cnf
fi

######################
# Create CA-signed certs
######################

NAME="$1"
# Generate a private key
openssl genrsa -out $NAME.key 4096

# Create a configuration file for generating a certificate-signing request
>$NAME-config_ssl.cnf cat <<-EOF
[ req ]
default_bits = 4096

prompt = no
distinguished_name=req_distinguished_name
req_extensions = v3_req

[ req_distinguished_name ]
countryName=UA
stateOrProvinceName=root region
localityName=root city
organizationName=root organisation
organizationalUnitName=roote department
commonName=root
emailAddress=root_email@root.localhost

[ alternate_names ]
DNS.1        = $NAME
DNS.2        = www.$NAME
DNS.3        = mail.$NAME
DNS.4        = ftp.$NAME

[ v3_req ]
keyUsage=digitalSignature
basicConstraints=CA:false
subjectKeyIdentifier = hash
subjectAltName = @alternate_names
EOF

# Create a certificate-signing request
openssl req -new -sha256 -key $NAME.key -config $NAME-config_ssl.cnf -out $NAME.csr

# Create a config file for the extensions
>$NAME.ext cat <<-EOF
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names
[alt_names]
DNS.1 = $NAME # Be sure to include the domain name here
DNS.2 = www.$NAME
DNS.3 = mail.$NAME
DNS.4 = ftp.$NAME
EOF

# Create the signed certificate
openssl x509 -req -in $NAME.csr -CA myCA.pem -CAkey myCA.key -CAcreateserial \
-out $NAME.crt -days 825 -sha256 -extfile $NAME.ext

# Cleaning up
rm -rf $NAME.ext 

