Summary:            Zimbra's libbsd build
Name:               zimbra-libbsd
Version:            VERSION
Release:            alt1.zimbra8.8.15
License:            BSD
Source:             %{name}-%{version}.tar.xz
URL:                http://libbsd.freedesktop.org/
Group: 		    System/Libraries

%description
The Zimbra libbsd build

%prep
%setup -n libbsd-%{version}
%set_verify_elf_method skip

%build
LDFLAGS="-Wl,-rpath,OZCL"; export LDFLAGS; \
CFLAGS="-fPIC -D_REENTRANT"; export CFLAGS; \
CXXFLAGS="-D_REENTRANT"; export CXXFLAGS;
./configure --prefix=OZC
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%package libs
Summary:        libbsd Libaries
Requires:       zimbra-base
AutoReqProv:        no
Group:              System/Libraries

%description libs
The zimbra-libbsd-libs package contains the libbsd libraries

%package devel
Summary:        libbsd Development
Requires: zimbra-libbsd-libs = %{version}-%{release}
AutoReqProv:        no
Group:              Development/Other

%description devel
The zimbra-libbsd-devel package contains the linking libraries and include files

%files libs
%defattr(-,root,root)
OZCL/*.so.*

%files devel
%defattr(-,root,root)
OZCI
OZCL/pkgconfig
OZCL/*.a
OZCL/*.la
OZCL/*.so
%exclude OZCS

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1.zimbra8.8.15
- Initial build for p8

