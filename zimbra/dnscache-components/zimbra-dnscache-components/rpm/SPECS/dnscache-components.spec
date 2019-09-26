Summary:            Zimbra components for dnscache package
Name:               zimbra-dnscache-components
Version:            1.0.0
Release:            alt1
License:            GPL-2
Requires:           zimbra-dnscache-base, zimbra-unbound
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%description
Zimbra dnscache components pulls in all the packages used by
zimbra-dnscache

%files

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.0-alt1
- Initial build for p8

