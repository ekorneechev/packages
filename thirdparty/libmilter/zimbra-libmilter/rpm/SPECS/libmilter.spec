Summary:            Zimbra's libmilter build
Name:               zimbra-libmilter
Version:            VERSION
Release:            alt1.zimbra8.8.15
License:            SENDMAIL
Patch0:             ipv6.patch
Source:             %{name}-%{version}.tar.gz
URL:                https://www.sendmail.com/
Group:              System/Servers

%description
The Zimbra libmilter build

%define debug_package %{nil}

%prep
%setup -n sendmail-%{version}
%patch0 -p1

%build
LDFLAGS="-Wl,-rpath,OZCL"; export LDFLAGS; \
CFLAGS="-O2 -g"; export CFLAGS; \
cd libmilter && \
./Build -c

%install
mkdir -p ${RPM_BUILD_ROOT}OZCL
mkdir -p ${RPM_BUILD_ROOT}OZCI/libmilter
cd obj.*/libmilter && \
cp libmilter.a ${RPM_BUILD_ROOT}OZCL
cd ../../include/libmilter && \
cp -p * ${RPM_BUILD_ROOT}OZCI/libmilter

%package devel
Summary:        libmilter Development
Requires:       zimbra-base
AutoReqProv:        no
Group:              Development/Other

%description devel
The zimbra-libmilter-devel package contains the linking libraries and include files

%files devel
%defattr(-,root,root)
%dir OZCI/libmilter
OZCI/libmilter
OZCL/libmilter.a

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1.zimbra8.8.15
- Initial build for p8

