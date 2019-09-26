Summary:            Zimbra components for apache package
Name:               zimbra-apache-components
Version:            1.0.1
Release:            alt1
License:            GPL-2
Requires:           zimbra-apache-base, zimbra-httpd, zimbra-php >= 5.6.31-alt1
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%description
Zimbra apache components pulls in all the packages used by
zimbra-apache

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.1-alt1
- Initial build for p8


%files
