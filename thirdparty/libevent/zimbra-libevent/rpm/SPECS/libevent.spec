Summary:            Zimbra's libevent build
Name:               zimbra-libevent
Version:            VERSION
Release:            alt1
License:            BSD
Source:             %{name}-%{version}-stable.tar.gz
Requires:           zimbra-libevent-libs = %{version}-%{release}
AutoReqProv:        no
URL:                http://libevent.org/
Group:  	    System/Libraries

%description
The Zimbra libevent build

%prep
%setup -n libevent-%{version}-stable
%set_verify_elf_method skip

%build
LDFLAGS="-Wl,-rpath,OZCL"; export LDFLAGS; \
CFLAGS="-O2 -g"; export CFLAGS; \
./configure --prefix=OZC
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%package libs
Summary:        libevent Libaries
Requires:       zimbra-memcached-base
AutoReqProv:        no
Group:              System/Libraries

%description libs
The zimbra-libevent-libs package contains the libevent libraries

%package devel
Summary:        libevent Development
Requires: zimbra-libevent-libs = %{version}-%{release}
AutoReqProv:        no
Group:              Development/C

%description devel
The zimbra-libevent-devel package contains the linking libraries and include files

%files libs
%defattr(-,root,root)
OZCL/*.so.*
%exclude OZCB

%files devel
%defattr(-,root,root)
OZCI
OZCL/*.a
OZCL/*.la
OZCL/*.so
OZCL/pkgconfig

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1
- Initial build for p8

