Summary:            Zimbra components for proxy package
Name:               zimbra-proxy-components
Version:            1.0.3
Release:            alt1.zimbra8.8.15
License:            GPL-2
Requires:           zimbra-proxy-base, zimbra-nginx
Packager:           Korneechev Evgeniy <ekorneechev@altlinux.org>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%changelog
* Tue Feb 12 2019  Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.3
- Updated zimbra-nginx package
* Tue Sep 5 2018  Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.2
- Updated zimbra-nginx package
* Tue Jul 18 2017  Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.1
- Updated zimbra-nginx package
* Wed Sep 09 2015  Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.0
- Initial Release

%description
Zimbra proxy components pulls in all the packages used by
zimbra-proxy

%files
