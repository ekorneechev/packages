Summary:            Zimbra's Secure Socket Layer build
Name:               zimbra-openssl
Version:            VERSION
Release:            alt1
License:            OpenSSL
Source:             %{name}-%{version}.tar.gz
Patch:              ipv6.patch
Requires:           zimbra-openssl-libs = %{version}-%{release}, perl
AutoReqProv:        no
URL:                https://www.openssl.org/source
Group: 		    System/Base

%description
The Zimbra OpenSSL build allows for secure communication between various processes.

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1
- Initial build for p8


%prep
%setup -n openssl-%{version}
%set_verify_elf_method skip
%patch -p1

%build
./Configure no-idea enable-ec_nistp_64_gcc_128 no-mdc2 no-rc5 no-ssl2 \
  no-hw --prefix=OZC --libdir=lib --openssldir=OZCE/ssl \
  shared linux-x86_64 -g -O2 -DOPENSSL_NO_HEARTBEATS
LD_RUN_PATH=OZCL make depend
LD_RUN_PATH=OZCL make all

%install
LD_RUN_PATH=OZCL make INSTALL_PREFIX=${RPM_BUILD_ROOT} MANDIR="OZCS/man" LIBS="" install
chmod u+w ${RPM_BUILD_ROOT}OZCL/lib* ${RPM_BUILD_ROOT}OZCL/engines/*.so

%package libs
Summary:	SSL Libaries
Requires: zimbra-base
AutoReqProv:        no
Group: System/Libraries

%description libs
The zimbra-openssl-libs package contains the openssl libraries

%package devel
Summary:	SSL Development
Requires: zimbra-openssl-libs = %{version}-%{release}
AutoReqProv:        no
Group: Development/C

%description devel
The zimbra-openssl-devel package contains the linking libraries and include files

%files
%defattr(-,root,root)
OZCB
OZCE
OZCS

%files libs
%defattr(-,root,root)
%dir /opt/zimbra
%dir OZC
%dir OZCL
%dir OZCL/engines
%attr(555,-,-) OZCL/libssl.so.*
%attr(555,-,-) OZCL/libcrypto.so.*
%attr(555,-,-) OZCL/engines/*.so

%files devel
%defattr(-,root,root)
OZCL/*.so
OZCI
OZCL/pkgconfig

%changelog
