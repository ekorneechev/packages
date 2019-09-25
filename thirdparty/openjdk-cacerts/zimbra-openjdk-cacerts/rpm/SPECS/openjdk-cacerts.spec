Summary:            CA Certs keystore for OpenJDK
Name:               zimbra-openjdk-cacerts
Version:            1.0.5
Release:            alt1.zimbra8.8.15
License:            MPL-2
Requires:           zimbra-base, zimbra-openjdk
Packager:           Korneechev Evgeniy <ekorneechev@altlinux.org>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%description
CA certs keystore for use with OpenJDK

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.5-alt1.zimbra8.8.15
- Initial build for p8


%install
mkdir -p ${RPM_BUILD_ROOT}/OZCE/java
cp ../../cacerts ${RPM_BUILD_ROOT}/OZCE/java/cacerts

%files
%attr(644,zimbra,zimbra) OZCE/java/cacerts

%pre -p /bin/bash
if [ "$1" -ge "2" ]; then
  zver=$(rpm -q --queryformat='%%{version}-%%{release}' zimbra-openjdk-cacerts)
  mkdir -p /opt/zimbra/.saveconfig/zimbra-openjdk-cacerts-${zver}
  cacerts=`mktemp --tmpdir=/opt/zimbra/.saveconfig/zimbra-openjdk-cacerts-${zver} cacerts.XXXXXX`
  cp OZCE/java/cacerts $cacerts
fi

%post -p /bin/bash
/bin/chown zimbra:zimbra OZCE/java/cacerts
/bin/chmod 644 OZCE/java/cacerts
if [ "$1" -ge "2" ]; then
  if [ -x /opt/zimbra/bin/zmcertmgr ]; then
    # Run as zimbra, extract CA to /opt/zimbra/conf/ca
    /bin/su - zimbra -c '/opt/zimbra/bin/zmcertmgr createca'
    # Run as zimbra, update OpenJDK cacerts file with the CA stored in LDAP
    /bin/su - zimbra -c '/opt/zimbra/bin/zmcertmgr deployca --localonly'
  fi
fi

