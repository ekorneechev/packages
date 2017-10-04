Summary:            Zimbra's libsodium build
Name:               zimbra-libsodium
Version:            VERSION
Release:            alt1.zimbra884
License:            ISC
Source:             %{name}-%{version}.tar.gz
URL:                https://download.libsodium.org/doc/
Group: 		    System/Libraries

%description
The Zimbra libsodium build

%prep
%setup -n libsodium-%{version}
%set_verify_elf_method skip

%build
LDFLAGS="-Wl,-rpath,OZCL"; export LDFLAGS; \
CFLAGS="-O2 -g"; export CFLAGS; \
./configure --prefix=OZC \
  --enable-minimal
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%package libs
Summary:        libsodium Libaries
Requires:       zimbra-base
AutoReqProv:        no
Group:              System/Libraries

%description libs
The zimbra-libsodium-libs package contains the libsodium libraries

%package devel
Summary:        libsodium Development
Requires: zimbra-libsodium-libs = %{version}-%{release}
AutoReqProv:        no
Group:              System/Libraries

%description devel
The zimbra-libsodium-devel package contains the linking libraries and include files

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
