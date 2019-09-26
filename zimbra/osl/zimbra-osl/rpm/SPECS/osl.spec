Summary:            Opensource Licenses
Name:               zimbra-osl
Version:            1.0.9
Release:            alt1
License:            GPL-2
Requires:           zimbra-base
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%description
This file contains the licenses for the open source 3rd party
software used by Zimbra

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.9-alt1
- Initial build for p8


%install
mkdir -p ${RPM_BUILD_ROOT}/opt/zimbra/docs
cp ../../open_source_licenses.txt ${RPM_BUILD_ROOT}/opt/zimbra/docs

%files
/opt/zimbra/docs/open_source_licenses.txt
