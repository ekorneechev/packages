Summary:            Zimbra components for store package
Name:               zimbra-store-components
Version:            1.0.1
Release:            alt1.zimbra8.8.15
License:            GPL-2
Requires:           zimbra-store-base, zimbra-mariadb >= 10.1.25-alt1.zimbra8.8.15
Packager:           Korneechev Evgeniy <ekorneechev@altlinux.org>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%description
Zimbra store components pulls in all the packages used by
zimbra-store

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.1-alt1.zimbra8.8.15
- Initial build for p8


%files
