Summary:            Initial ClamAV Databases for ClamAV
Name:               zimbra-clamav-db
Version:            1.0.0
Release:            alt1
License:            GPL-2
Requires:           zimbra-base
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%description
Initial ClamAV Databases for ClamAV

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.0-alt1
- Initial build for p8


%install
mkdir -p ${RPM_BUILD_ROOT}/opt/zimbra/data/clamav/init
cp ../../../src/bytecode.cvd ${RPM_BUILD_ROOT}/opt/zimbra/data/clamav/init/bytecode.cvd.init
cp ../../../src/daily.cvd ${RPM_BUILD_ROOT}/opt/zimbra/data/clamav/init/daily.cvd.init
cp ../../../src/main.cvd ${RPM_BUILD_ROOT}/opt/zimbra/data/clamav/init/main.cvd.init

%files
%attr(644,zimbra,zimbra) /opt/zimbra/data/clamav/init/bytecode.cvd.init
%attr(644,zimbra,zimbra) /opt/zimbra/data/clamav/init/daily.cvd.init
%attr(644,zimbra,zimbra) /opt/zimbra/data/clamav/init/main.cvd.init
