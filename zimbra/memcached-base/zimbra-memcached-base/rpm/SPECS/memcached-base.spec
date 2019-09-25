Summary:            Zimbra memcached Base
Name:               zimbra-memcached-base
Version:            1.0.0
Release:            alt1.zimbra8.8.15
License:            GPL-2
Packager:           Korneechev Evgeniy <ekorneechev@altlinux.org>
Group:              Development/Languages
Requires:           zimbra-base
AutoReqProv:        no

%define debug_package %{nil}

%description
Zimbra memcached Base is used as a simple method to allow removing
all the zimbra-memcached specific packages

%files

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.0-alt1.zimbra8.8.15
- Initial build for p8

