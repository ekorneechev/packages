Summary:            Zimbra components for snmp package
Name:               zimbra-snmp-components
Version:            1.0.0
Release:            alt1
License:            GPL-2
Requires:           zimbra-snmp-base, zimbra-net-snmp
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%description
Zimbra snmp components pulls in all the packages used by
zimbra-snmp

%files

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.0-alt1
- Initial build for p8

