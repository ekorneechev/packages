Summary:            Zimbra OS Requirements
Name:               zimbra-os-requirements
Version:            1.0.0
Release:            alt1
License:            GPL-2
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Group:              Development/Languages
Requires:           coreutils, expat, file, gmp, libaio, libidn, libstdc++6, pcre
Requires:           perl, sudo, sysstat, unzip, zimbra-base
Requires:           perl-Socket6
AutoReqProv:        no

%define debug_package %{nil}

%description
Zimbra OS requirements is used as a simple method to pull in all
OS required core packages

%files

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.0-alt1
- Initial build for p8

