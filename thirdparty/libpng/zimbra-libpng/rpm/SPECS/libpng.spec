Summary:            Zimbra's libpng build
Name:               zimbra-libpng
Version:            VERSION
Release:            alt1.zimbra884
BuildRequires:      zlib-devel
License:            MIT
Source:             %{name}-%{version}.tar.gz
URL:                http://www.libpng.org/pub/png/libpng.html
Group: 		    System/Libraries

%description
The Zimbra libpng build

%prep
%setup -n libpng-%{version}
%set_verify_elf_method skip

%build
LDFLAGS="-Wl,-rpath,OZCL"; export LDFLAGS; \
CFLAGS="-fPIC -O2 -g"; export CFLAGS; \
./configure --prefix=OZC
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%package libs
Summary:        libpng Libaries
Requires:           zlib, zimbra-base
AutoReqProv:        no
Group:              System/Libraries

%description libs
The zimbra-libpng-libs package contains the libpng libraries

%package devel
Summary:        libpng Development
Requires: zimbra-libpng-libs = %{version}-%{release}
AutoReqProv:        no
Group: 		    Development/C

%description devel
The zimbra-libpng-devel package contains the linking libraries and include files

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
%exclude OZCS
