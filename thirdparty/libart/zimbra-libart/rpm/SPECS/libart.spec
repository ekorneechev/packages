Summary:            Zimbra's libart build
Name:               zimbra-libart
Version:            VERSION
Release:            alt1
License:            GPL-2.0
Source:             %{name}-%{version}.tar.bz2
URL:                http://ftp.gnome.org/pub/gnome/sources/libart_lgpl/2.3/
Group:              System/Libraries

%description
The Zimbra libart build

%prep
%setup -n libart_lgpl-%{version}
%set_verify_elf_method skip

%build
LDFLAGS="-Wl,-rpath,OZCL"; export LDFLAGS; \
CFLAGS="-O2 -g"; export CFLAGS; \
./configure --prefix=OZC
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%package libs
Summary:        libart Libaries
Requires:       zimbra-base
AutoReqProv:        no
Group:              System/Libraries

%description libs
The zimbra-libart-libs package contains the libart libraries

%package devel
Summary:        libart Development
Requires: zimbra-libart-libs = %{version}-%{release}
AutoReqProv:        no
Group:              Development/GNOME and GTK+

%description devel
The zimbra-libart-devel package contains the linking libraries and include files

%files libs
%defattr(-,root,root)
OZCL/*.so.*

%files devel
%defattr(-,root,root)
OZCB
OZCI
OZCL/pkgconfig
OZCL/*.a
OZCL/*.la
OZCL/*.so

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1
- Initial build for p8

