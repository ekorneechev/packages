Summary:            Zimbra components for ldap package
Name:               zimbra-ldap-components
Version:            1.0.2
Release:            alt1.zimbra8.8.15
License:            GPL-2
Requires:           zimbra-ldap-base, zimbra-lmdb, zimbra-openldap-server
Packager:           Korneechev Evgeniy <ekorneechev@altlinux.org>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%description
Zimbra ldap components pulls in all the packages used by
zimbra-ldap

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.2-alt1.zimbra8.8.15
- Initial build for p8


%files
