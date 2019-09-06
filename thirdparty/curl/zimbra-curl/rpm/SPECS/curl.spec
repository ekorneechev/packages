Summary:            Zimbra's Curl build
Name:               zimbra-curl
Version:            VERSION
Release:            alt1.zimbra8.8.15
License:            MIT
Source:             %{name}-%{version}.tar.gz
BuildRequires:      glibc-devel-static groff-base libidn-devel libssh2-devel libssl-devel zlib-devel python-modules libnghttp2-devel python-modules-logging python-modules-xml
BuildRequires:      zimbra-openssl-devel
BuildRequires:      zimbra-heimdal-devel
Requires:           zlib, zimbra-curl-libs = %{version}-%{release}, zimbra-openssl-libs, zimbra-heimdal-libs
AutoReqProv:        no
URL:                http://curl.haxx.se/
Group: 		    Networking/File transfer

%description
The Zimbra Curl build

%prep
%setup -n curl-%{version}
%set_verify_elf_method skip

%build
LDFLAGS="-Wl,-rpath,OZCL"; export LDFLAGS; \
CFLAGS="-O2 -g -lpthread"; export CFLAGS; \
./configure --prefix=OZC \
  --disable-ldap --disable-ldaps \
  --with-gssapi=OZC \
  --with-ssl=OZC \
  --without-gnutls \
  --with-ca-bundle=OZCS/curl/ca-bundle.crt \
  --enable-ipv6 \
  --with-zlib \
  --without-libidn \
  --disable-static
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}
make ca-bundle
mkdir -p ${RPM_BUILD_ROOT}OZCS/curl
cp -f lib/ca-bundle.crt ${RPM_BUILD_ROOT}OZCS/curl/ca-bundle.crt

%package libs
Summary:        Curl Libaries
Requires: zlib, zimbra-openssl-libs, zimbra-heimdal-libs, zimbra-base
AutoReqProv:        no
Group: System/Libraries

%description libs
The zimbra-curl-libs package contains the curl libraries

%package devel
Summary:        Curl Development
Requires: zimbra-curl-libs = %{version}-%{release}
AutoReqProv:        no
Group: Development/C

%description devel
The zimbra-curl-devel package contains the linking libraries and include files

%files
%defattr(-,root,root)
OZCB
OZCS
%exclude OZCB/curl-config

%files libs
%defattr(-,root,root)
OZCL/*.so.*

%files devel
%defattr(-,root,root)
OZCB/curl-config
OZCL/*.la
OZCL/*.so
OZCL/pkgconfig
OZCI

