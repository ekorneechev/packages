Summary:            Zimbra's Apache Portable Runtime build
Name:               zimbra-apr
Version:            VERSION
Release:            alt1
License:            Apache-2.0
Source:             %{name}-%{version}.tar.bz2
Requires:           zimbra-apr-libs = %{version}-%{release}
AutoReqProv:        no
URL:                https://apr.apache.org/
Group:              System/Libraries

%description
The Zimbra Apache Portable Runtime build


%prep
%setup -n apr-%{version}
%set_verify_elf_method skip

%build
LDFLAGS="-Wl,-rpath,OZCL"; export LDFLAGS; \
CFLAGS="-O2 -g"; export CFLAGS; \
./configure --prefix=OZC
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%package libs
Summary:        Apache Portable Runtime Libaries
Requires:       zimbra-apache-base
AutoReqProv:        no
Group:              System/Libraries

%description libs
The zimbra-apr-libs package contains the apr libraries

%package devel
Summary:        Apache Portable Runtime Development
Requires: zimbra-apr-libs = %{version}-%{release}
AutoReqProv:        no
Group:              Development/C

%description devel
The zimbra-apr-devel package contains the linking libraries and include files

%files libs
%defattr(-,root,root)
OZCL/*.so.*

%files devel
%defattr(-,root,root)
OZCB/apr-1-config
OZC/build-1
OZCI
OZCL/*.a
OZCL/*.la
OZCL/*.so
OZCL/apr.exp
OZCL/pkgconfig

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1
- Initial build for p8

