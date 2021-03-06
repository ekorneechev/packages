Summary:            Zimbra's Unbound build
Name:               zimbra-unbound
Version:            VERSION
Release:            alt1
License:            BSD
Source:             %{name}-%{version}.tar.gz
Patch0:             log-facility.patch
BuildRequires:      expat-devel, zimbra-openssl-devel
Requires:           expat, zimbra-openssl-libs
Requires:           zimbra-unbound-libs = %{version}-%{release}
AutoReqProv:        no
URL:                https://www.unbound.net/
Group:              System/Servers

%description
The Zimbra Unbound build

%prep
%setup -n unbound-%{version}
%set_verify_elf_method skip
%patch0 -p1

%build
LDFLAGS="-Wl,-rpath,OZCL"; export LDFLAGS; \
CFLAGS="-O2 -g"; export CFLAGS; \
./configure --prefix=OZC \
  --with-ssl=OZC \
  --with-username=zimbra \
  --with-conf-file=/opt/zimbra/conf/unbound.conf \
  --with-pidfile=/opt/zimbra/log/unbound.pid \
  --with-chroot-dir=/opt/zimbra
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%package libs
Summary:        Unbound Libaries
Requires:       zimbra-openssl-libs, zimbra-dnscache-base
AutoReqProv:        no
Group: System/Libraries

%description libs
The zimbra-unbound-libs package contains the unbound libraries

%package devel
Summary:        Unbound Development
Requires: zimbra-unbound-libs = %{version}-%{release}
AutoReqProv:        no
Group: Development/C

%description devel
The zimbra-unbound-devel package contains the linking libraries and include files

%files
%defattr(-,root,root)
OZC/sbin
OZCS
%exclude /opt/zimbra/conf

%files libs
%defattr(-,root,root)
OZCL/*.so.*

%files devel
%defattr(-,root,root)
OZCI
OZCL/*.a
OZCL/*.la
OZCL/*.so

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1
- Initial build for p8

