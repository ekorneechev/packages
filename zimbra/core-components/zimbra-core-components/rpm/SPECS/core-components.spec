Summary:            Zimbra components for core package
Name:               zimbra-core-components
Version:            1.0.4
Release:            alt1.zimbra884
License:            GPL-2
Requires:           zimbra-base, zimbra-os-requirements, zimbra-perl, zimbra-pflogsumm
Requires:           zimbra-openssl >= 1.0.2l-alt1.zimbra884,zimbra-curl, zimbra-cyrus-sasl, zimbra-rsync
Requires:           zimbra-mariadb-libs >= 10.1.25-alt1.zimbra884, zimbra-openldap-client, zimbra-osl
Requires:           zimbra-prepflog, zimbra-tcmalloc-libs, zimbra-perl-innotop
Requires:           zimbra-openjdk >= 1.8.0u172b01-alt1.zimbra884, zimbra-openjdk-cacerts, zimbra-amavis-logwatch
Requires:           zimbra-postfix-logwatch, zimbra-rrdtool
Packager:           Korneechev Evgeniy <ekorneechev@altlinux.org>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%changelog
* Fri May 18 2018 Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.4
- Updated zimbra-openjdk package
* Fri Jul 28 2017 Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.3
- Updated zimbra-openjdk package
* Fri Jul 28 2017 Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.2
- Updated zimbra-openssl package
* Mon Jul 24 2017  Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.1
- Updated zimbra-mariadb package
* Wed Sep 09 2015  Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.0
- Initial Release

%description
Zimbra core components pulls in all the packages used by
zimbra-core

%files
