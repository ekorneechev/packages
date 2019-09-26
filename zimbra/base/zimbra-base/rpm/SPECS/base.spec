Summary:            Zimbra Base
Name:               zimbra-base
Version:            1.0.1
Release:            alt2
License:            GPL-2
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Requires:           shadow-utils
Requires:           perl-Pod-Usage perl-Digest-SHA
Requires:           ca-certificates-java
Requires:           syslogd
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%description
Zimbra Base is used as a simple method to allow removing
all the zimbra specific third party packages.

%install
mkdir -p %buildroot/opt/zimbra/libexec
cat > %buildroot/opt/zimbra/libexec/zmjavafix << EOF
#!/bin/bash
cd /opt/zimbra/common/lib/jvm/
rm -f java
ln -s zimbra-openjdk*/jre java
EOF

%files
%attr(755,zimbra,zimbra) /opt/zimbra/libexec/zmjavafix

%changelog
* Thu Sep 26 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.1-alt2
- Added fixes for ALT

* Tue Sep 24 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.1-alt1
- Initial build for p8

%post -p /bin/bash
grp_exists() {
  if [ -x /usr/bin/getent ]
  then
    getent group $1 >/dev/null 2>&1
    FOUND=$?
  else
    egrep -q "^$1:" /etc/group
    FOUND=$?
  fi
  return $FOUND
}

acct_exists() {
  if [ -x /usr/bin/getent ]
  then
    getent passwd $1 >/dev/null 2>&1
    return $?
  else
    egrep -q "^$1:" /etc/passwd
    return $?
  fi
}

grp_exists zimbra
if [ $? != 0 ]; then
        groupadd -r zimbra
fi

acct_exists zimbra
if [ $? != 0 ]; then
        useradd -r -g zimbra -G tty -d /opt/zimbra -s /bin/bash zimbra
else
        usermod -g zimbra -d /opt/zimbra -s /bin/bash zimbra
fi

touch /var/log/zimbra-stats.log
chown zimbra:zimbra /var/log/zimbra-stats.log
control sudo public
