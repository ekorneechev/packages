Summary:            Zimbra components for proxy package
Name:               zimbra-proxy-components
Version:            1.0.3
Release:            alt1
License:            GPL-2
Requires:           zimbra-proxy-base, zimbra-nginx
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.3-alt1
- Initial build for p8


%description
Zimbra proxy components pulls in all the packages used by
zimbra-proxy

%files
