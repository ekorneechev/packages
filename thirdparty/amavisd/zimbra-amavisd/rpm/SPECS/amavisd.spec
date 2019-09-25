Summary:            Zimbra's amavisd build
Name:               zimbra-amavisd
Version:            VERSION
Release:            alt1.zimbra8.8.15
License:            GPL-2
Source:             %{name}-%{version}.tar.bz2
Patch0:             amavisd.patch
Patch1:             amavis-mc.patch
Patch2:             perl-path.patch
Patch3:             socketpath.patch
Patch4:             zmq-sock.patch
Requires:           perl, zimbra-mta-base
AutoReqProv:        no
URL:                http://www.ijs.si/software/amavisd/
Group:              Networking/Mail

%description
The Zimbra amavisd build

%define debug_package %{nil}

%prep
%setup -n amavisd-new-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build

%install
mkdir -p ${RPM_BUILD_ROOT}OZC/sbin
cp amavisd ${RPM_BUILD_ROOT}OZC/sbin
cp amavisd-release ${RPM_BUILD_ROOT}OZC/sbin
cp amavis-mc ${RPM_BUILD_ROOT}OZC/sbin
cp amavis-services ${RPM_BUILD_ROOT}OZC/sbin
cp amavisd-status ${RPM_BUILD_ROOT}OZC/sbin
cp amavisd-snmp-subagent-zmq ${RPM_BUILD_ROOT}OZC/sbin

%files
%defattr(-,root,root)
OZC/sbin

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1.zimbra8.8.15
- Initial build for p8

