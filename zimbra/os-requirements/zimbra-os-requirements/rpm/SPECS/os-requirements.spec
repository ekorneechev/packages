Summary:            Zimbra OS Requirements
Name:               zimbra-os-requirements
Version:            1.0.0
Release:            alt1.zimbra884
License:            GPL-2
Packager:           Korneechev Evgeniy <ekorneechev@altlinux.org>
Group:              Development/Languages
Requires:           coreutils, expat, file, gmp, libaio, libidn, libstdc++, pcre
Requires:           perl, perl-core, sudo, sysstat, unzip, zimbra-base
Requires:           perl-Socket6, OSDEPS
AutoReqProv:        no

%define debug_package %{nil}

%description
Zimbra OS requirements is used as a simple method to pull in all
OS required core packages

%files
