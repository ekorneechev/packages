Summary:            Zimbra components for core package
Name:               zimbra-core-components
Version:            1.0.4
Release:            alt1.zimbra8.8.15
License:            GPL-2
Requires:           zimbra-base, zimbra-os-requirements, zimbra-perl, zimbra-pflogsumm
Requires:           zimbra-openssl >= 1.0.2l-alt1.zimbra8.8.15,zimbra-curl, zimbra-cyrus-sasl, zimbra-rsync
Requires:           zimbra-mariadb-libs >= 10.1.25-alt1.zimbra8.8.15, zimbra-openldap-client, zimbra-osl
Requires:           zimbra-prepflog, zimbra-tcmalloc-libs, zimbra-perl-innotop
Requires:           zimbra-openjdk >= 1.8.0u172b01-alt1.zimbra8.8.15, zimbra-openjdk-cacerts, zimbra-amavis-logwatch
Requires:           zimbra-postfix-logwatch, zimbra-rrdtool
Packager:           Korneechev Evgeniy <ekorneechev@altlinux.org>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.4-alt1.zimbra8.8.15
- Initial build for p8


%description
Zimbra core components pulls in all the packages used by
zimbra-core

%files
