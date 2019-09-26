Summary:            Zimbra custom dictionary
Name:               zimbra-aspell-zimbra
Version:            1.0.0
Release:            alt1
License:            GPL-2
BuildRequires:      zimbra-aspell-en
Requires:           zimbra-aspell-en
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Group:              Development/Languages
AutoReqProv:        no
Group:              Text tools

%define debug_package %{nil}

%description
This is a dictionary for aspell defining specific words
that Zimbra does not want viewed as a typo. The word Zimbra
is one example.

%install
mkdir -p ${RPM_BUILD_ROOT}/OZCL/aspell-0.60
echo -e "Zimbra\nzimlet\nzimlets\nComcast\nVMware\nSynacor\nZimbra" | /opt/zimbra/common/bin/aspell create master --lang=en ${RPM_BUILD_ROOT}/OZCL/aspell-0.60/zimbra.rws

%files
OZCL/aspell-0.60

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.0-alt1
- Initial build for p8

