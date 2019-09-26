Summary:            Zimbra's memcached build
Name:               zimbra-memcached
Epoch:              1
Version:            VERSION
Release:            alt1
License:            BSD
Source:             %{name}-%{version}.tar.gz
BuildRequires:      zimbra-libevent-devel
BuildRequires:      pkgconfig
Requires:           zimbra-libevent-libs, zimbra-memcached-base
AutoReqProv:        no
URL:                http://memcached.org/
Group:              System/Servers

%description
The Zimbra memcached build

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1:VERSION-alt1
- Initial build for p8


%prep
%setup -n memcached-%{version}
%set_verify_elf_method skip

%build
LDFLAGS="-Wl,-rpath,OZCL"; export LDFLAGS; \
CFLAGS="-O2 -g"; export CFLAGS; \
PKG_CONFIG_PATH="OZCL/pkgconfig"; export PKG_CONFIG_PATH; \
./configure --prefix=OZC
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}

%package devel
Summary:        memcached Development
AutoReqProv:        no
Group: Development/C

%description devel
The zimbra-memcached-devel package contains the linking libraries and include files

%files
%defattr(-,root,root)
OZCB
OZCS

%files devel
%defattr(-,root,root)
OZCI
